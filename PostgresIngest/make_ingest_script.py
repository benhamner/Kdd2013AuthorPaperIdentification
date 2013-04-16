from csvjazz import csv_to_postgres
import os

def get_sql(data_path, table_name):
    csv_path = os.path.join(data_path, table_name + ".csv")
    schema = csv_to_postgres.make_postgres_schema(csv_path, table_name)
    ingest = csv_to_postgres.make_postgres_ingest(csv_path, table_name)
    return schema + "\n\n" + ingest

def main():
    data_path = os.path.join(os.environ["DataPath"], "KDD2013AuthorPaperIdentification", "Release 1")
    tables = ["Paper", "Author", "Journal", "Conference", "PaperAuthor", "ValidPapers", "TrainConfirmed", "TrainDeleted"]
    scripts = [get_sql(data_path, table) for table in tables]
    sql_script = "\n\n".join(scripts)
    f = open("postgres_ingest.sql", "w")
    f.write(sql_script)
    f.close()

if __name__=="__main__":
    main()