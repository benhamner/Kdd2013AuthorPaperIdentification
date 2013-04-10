import csv
import json
import os
import pandas as pd

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
    train = pd.read_csv(train_path, index_col="AuthorId")
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
    return meta_data

def get_paper_author_set():
    paper_author_df = read_meta_data("PaperAuthor")
    paper_author_set = set()
    for i, row in paper_author_df.iterrows():
        paper_author_set.add((row["PaperId"], row["AuthorId"]))
    return paper_author_set

def write_submission(predictions):
    predictions = [paper_ids_to_string(x) for x in predictions]
    submission_path = get_paths()["submission_path"]
    writer = csv.writer(open(submission_path, "w"), lineterminator="\n")
    test = read_test()
    rows = [x for x in zip(test.index, predictions)]
    writer.writerow(("AuthorId", "PaperIds"))
    writer.writerows(rows)