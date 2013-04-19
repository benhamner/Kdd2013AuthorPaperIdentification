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
    data_path = os.path.join(os.environ["DataPath"], "KDD2013AuthorPaperIdentification", "Raw")
    labeled_path = os.path.join(data_path, "Task1LabeledDataSet.csv")
    labeled_transformed_path = os.path.join(os.environ["DataPath"], "KDD2013AuthorPaperIdentification", "LabeledTransformed")

    labeled_data = [row for row in csv.reader(open(labeled_path))]
    
    labeled_confirmed = [(row[0], row[1]) for row in labeled_data[1:]]
    labeled_deleted = [(row[0], row[2]) for row in labeled_data[1:]]

    write_data(labeled_transformed_path, "LabeledSetConfirmed.csv", ["AuthorId", "PaperId"], labeled_confirmed)
    write_data(labeled_transformed_path, "LabeledSetDeleted.csv", ["AuthorId", "PaperId"], labeled_deleted)

if __name__=="__main__":
    main()