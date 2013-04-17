import csv
from itertools import chain
import os
import re

class CsvDialect(csv.Dialect):
    def __init__(self):
        self.delimiter = ','
        self.doublequote = True
        self.escapechar = None
        self.lineterminator = "\n"
        self.quotechar = '"'
        self.quoting = csv.QUOTE_MINIMAL
        self.skipinitialspace = False
        self.strict = False

def to_relational(data):
    data = [[(row[0], paper_id) for paper_id in re.sub(r"\s+", " ",row[1].strip()).split(" ")] for row in data]
    return list(chain.from_iterable(data))

def write_data(data_path, file_name, header, data):
    writer = csv.writer(open(os.path.join(data_path, file_name), "w"), dialect=CsvDialect())
    writer.writerow(header)
    writer.writerows(to_relational(data))    

def main():
    data_path = os.path.join(os.environ["DataPath"], "KDD2013AuthorPaperIdentification", "Release 1")
    train_path = os.path.join(data_path, "Train.csv")
    valid_path = os.path.join(data_path, "Valid.csv")

    train_data = [row for row in csv.reader(open(train_path))]
    valid_data = [row for row in csv.reader(open(train_path))]

    train_deleted = [(row[0], row[1]) for row in train_data[1:]]
    train_confirmed = [(row[0], row[2]) for row in train_data[1:]]
    valid_papers = valid_data[1:]

    write_data(data_path, "TrainDeleted.csv", ["AuthorId", "PaperId"], train_deleted)
    write_data(data_path, "TrainConfirmed.csv", ["AuthorId", "PaperId"], train_confirmed)
    write_data(data_path, "ValidPapers.csv", ["AuthorId", "PaperId"], valid_papers)


if __name__=="__main__":
    main()