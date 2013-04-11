import os
import numpy as np
import pandas as pd
import re

def split_data(data, train_frac, valid_frac):
    index = np.arange(len(data))
    np.random.seed(135633)
    np.random.shuffle(index)
    train_end = int(train_frac*len(data))
    valid_end = int((train_frac+valid_frac)*len(data))
    train = data.ix[index[:train_end]]
    valid = data.ix[index[train_end:valid_end]]
    test = data.ix[index[valid_end:]]
    return train, valid, test

def parse_paper_ids(id_string):
    id_string = id_string.strip()
    id_string = re.sub(r"\s+", " ", id_string)
    if id_string:
        return [int(x) for x in id_string.split(" ")]
    return []

def paper_ids_to_string(ids):
    return " ".join([str(x) for x in ids])

def sort_ids(row, column_name):
    ids = parse_paper_ids(row[column_name])
    ids = sorted(ids)
    return paper_ids_to_string(ids)

def convert_to_train_format(train):
    train["ConfirmedPaperIds"] = train.apply(sort_ids, axis=1, args=("ConfirmedPaperId",))
    train["DeletedPaperIds"] = train.apply(sort_ids, axis=1, args=("DeletedPaperId",))
    train = train[["AuthorId", "DeletedPaperIds", "ConfirmedPaperIds"]]
    train = train.sort("AuthorId")
    return train

def combine_id_columns(row):
    return row["DeletedPaperId"] + " " + row["ConfirmedPaperId"]

def convert_to_test_format(test, usage="PrivateTest"):
    test["PaperIds"] = test.apply(combine_id_columns, axis=1)
    test["PaperIds"] = test.apply(sort_ids, axis=1, args=("PaperIds",))
    test["DeletedPaperIds"] = test.apply(sort_ids, axis=1, args=("DeletedPaperId",))
    test_set = test[["AuthorId", "PaperIds"]]
    test_set = test_set.sort("AuthorId")
    solution = test[["AuthorId", "DeletedPaperIds"]]
    solution = solution.rename(columns={"DeletedPaperIds": "PaperIds"})
    solution = solution.sort("AuthorId")
    solution["Usage"]=usage
    return test_set, solution

def create_competition_data():
    data_path = os.path.join(os.environ["DataPath"],
                             "Kdd2013AuthorPaperIdentification")
    raw_path = os.path.join(data_path, "Raw")
    labels_path = os.path.join(raw_path, "Task1LabeledDataSet.csv")
    out_path = os.path.join(data_path, "Release 1")

    converters = {
        "ConfirmedPaperId": lambda x: x,
        "DeletedPaperId": lambda x: x
    }

    data = pd.read_csv(labels_path, converters=converters)

    train, valid, test = split_data(data, 0.5, 0.2)
    train = convert_to_train_format(train)
    valid, valid_solution = convert_to_test_format(valid, "PublicTest")
    test, test_solution = convert_to_test_format(test, "PrivateTest")

    train.to_csv(os.path.join(out_path, "Train.csv"), index=False)
    valid.to_csv(os.path.join(out_path, "Valid.csv"), index=False)
    valid_solution.to_csv(os.path.join(out_path, "ValidSolution.csv"), index=False)
    test.to_csv(os.path.join(out_path, "Test.csv"), index=False)
    test_solution.to_csv(os.path.join(out_path, "TestSolution.csv"), index=False)

if __name__=="__main__":
    create_competition_data()