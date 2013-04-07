from copy import copy
import data_io
import numpy as np

def shuffle(row):
    paper_ids = copy(row["PaperIds"])
    np.random.shuffle(paper_ids)
    return paper_ids

def main():
    print("Reading the test data") 
    test = data_io.read_test()

    print("Making predictions")
    np.random.seed(12341234) 
    predictions = test.apply(shuffle, axis=1)

    print("Writing predictions to file")
    data_io.write_submission(predictions)

if __name__=="__main__":
    main()