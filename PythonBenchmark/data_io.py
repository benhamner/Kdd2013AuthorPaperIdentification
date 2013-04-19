import csv
import json
import os
import pickle
import psycopg2

def paper_ids_to_string(ids):
    return " ".join([str(x) for x in ids])

conn_string = None

def get_db_conn():
    # Horrible coding practice. Don't use global variables. Don't follow this example.
    # Wanted to ask for a password, didn't have time to refactor to be OO.
    global conn_string
    if conn_string is None:
        conn_string = get_paths()["postgres_conn_string"]
    if "##AskForPassword##" in conn_string:
        password = raw_input("PostgreSQL Password: ")
        conn_string = conn_string.replace("##AskForPassword##", password)
    conn = psycopg2.connect(conn_string)
    return conn

def get_paths():
    paths = json.loads(open("SETTINGS.json").read())
    for key in paths:
        paths[key] = os.path.expandvars(paths[key])
    return paths

def save_model(model):
    out_path = get_paths()["model_path"]
    pickle.dump(model, open(out_path, "w"))

def load_model():
    in_path = get_paths()["model_path"]
    return pickle.load(open(in_path))

def write_submission(predictions):
    submission_path = get_paths()["submission_path"]
    rows = [(author_id, paper_ids_to_string(predictions[author_id])) for author_id in predictions]
    writer = csv.writer(open(submission_path, "w"), lineterminator="\n")
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
    query = open("feature_query.sql").read().strip()
    return query.replace("##DataTable##", table_name)
