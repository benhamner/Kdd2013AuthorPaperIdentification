import csv
import json
import os
import pandas as pd
import pickle
import psycopg2

def get_db_conn():
    conn_string = get_paths()["postgres_conn_string"]
    conn = psycopg2.connect(conn_string)
    return conn

def get_paths():
    paths = json.loads(open("Settings.json").read())
    for key in paths:
        paths[key] = os.path.expandvars(paths[key])
    return paths

def parse_paper_ids(id_string):
    if id_string:
        return [int(x) for x in id_string.split(" ")]
    return []

def paper_ids_to_string(ids):
    return " ".join([str(x) for x in ids])

def parse_row(row, column_name):
    return parse_paper_ids(row[column_name])

def read_train():
    train_path = get_paths()["train_path"]
    converters = {
        "ConfirmedPaperIds": lambda x: x,
        "DeletedPaperIds": lambda x: x
    }
    train = pd.read_csv(train_path, index_col="AuthorId", converters=converters)
    train["ConfirmedPaperIds"] = train.apply(parse_row, axis=1, args=("ConfirmedPaperIds",))
    train["DeletedPaperIds"] = train.apply(parse_row, axis=1, args=("DeletedPaperIds",))
    return train

def read_test():
    test_path = get_paths()["test_path"]
    test = pd.read_csv(test_path, index_col="AuthorId")
    test["PaperIds"] = test.apply(parse_row, axis=1, args=("PaperIds",))
    return test

def read_meta_data(meta_data_file):
    meta_data_path = os.path.join(get_paths()["meta_data_path"], meta_data_file + ".csv")
    meta_data = pd.read_csv(meta_data_path)
    if "Id" in meta_data:
        meta_data = meta_data.set_index("Id")
    return meta_data

def read_paper_author_no_duplicates():
    paper_author = read_meta_data("PaperAuthor")
    previously_seen=set()
    mask = []
    for i, row in paper_author.iterrows():
        if (row["PaperId"], row["AuthorId"]) in previously_seen:
            mask.append(False)
        else:
            previously_seen.add((row["PaperId"], row["AuthorId"]))
            mask.append(True)
    return paper_author[mask]

def read_paper_no_duplicates():
    paper = read_meta_data("Paper")

def get_paper_author_set():
    paper_author_df = read_meta_data("PaperAuthor")
    paper_author_set = set()
    for i, row in paper_author_df.iterrows():
        paper_author_set.add((row["PaperId"], row["AuthorId"]))
    return paper_author_set

def save_model(model):
    out_path = get_paths()["model_path"]
    pickle.dump(model, open(out_path, "w"))

def load_model():
    in_path = get_paths()["model_path"]
    return pickle.load(open(in_path))

def write_submission(predictions):
    predictions = [paper_ids_to_string(x) for x in predictions]
    submission_path = get_paths()["submission_path"]
    writer = csv.writer(open(submission_path, "w"), lineterminator="\n")
    test = read_test()
    rows = [x for x in zip(test.index, predictions)]
    writer.writerow(("AuthorId", "PaperIds"))
    writer.writerows(rows)

def get_features_db(table_name):
    conn = get_db_conn()
    query = get_features_query(table_name)
    cursor = conn.cursor()
    cursor.execute(query)
    res = cursor.fetchall()
    return res

def get_features_query(table_name):
    query = """
    WITH AuthorJournalCounts AS (
        SELECT AuthorId, JournalId, Count(*) AS Count
        FROM PaperAuthor pa
        LEFT OUTER JOIN Paper p on pa.PaperId=p.Id
        GROUP BY AuthorId, JournalId),
    AuthorConferenceCounts AS (
        SELECT AuthorId, ConferenceId, Count(*) AS Count
        FROM PaperAuthor pa
        LEFT OUTER JOIN Paper p on pa.PaperId=p.Id
        GROUP BY AuthorId, ConferenceId),
    AuthorPaperCounts AS (
        SELECT AuthorId, Count(*) AS Count
        FROM PaperAuthor
        GROUP BY AuthorId),
    PaperAuthorCounts AS (
        SELECT PaperId, Count(*) AS Count
        FROM PaperAuthor
        GROUP BY PaperId)
    SELECT t.AuthorId, t.PaperId, ajc.Count As NumSameJournal, acc.Count AS NumSameConference, apc.Count AS NumPapersWithAuthorm, pac.Count AS NumAuthorsWithPaper
    FROM %s t
    LEFT OUTER JOIN Paper p ON t.PaperId=p.Id
    LEFT OUTER JOIN AuthorJournalCounts ajc
        ON ajc.AuthorId=t.AuthorId
           AND ajc.JournalId = p.JournalId
    LEFT OUTER JOIN AuthorConferenceCounts acc
        ON acc.AuthorId=t.AuthorId
           AND acc.ConferenceId = p.ConferenceId
    LEFT OUTER JOIN AuthorPaperCounts apc
        ON apc.AuthorId=t.AuthorId
    LEFT OUTER JOIN PaperAuthorCounts pac
        ON pac.PaperId=t.PaperId
    """ % table_name
    return query