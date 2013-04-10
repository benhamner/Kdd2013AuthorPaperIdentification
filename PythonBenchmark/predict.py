from copy import copy
import data_io

def paper_author_set_order(row, paper_author_set):
    in_set = []
    combined = []
    for paper_id in row["PaperIds"]:
        if (paper_id, row.name) in paper_author_set:
            in_set.append(paper_id)
        else:
            combined.append(paper_id)
    combined.extend(in_set)
    return combined

def main():
    global xin
    global xout

    print("Getting the paper author set")
    paper_author_set = data_io.get_paper_author_set()

    print("Reading the test data") 
    test = data_io.read_test()

    print("Making predictions")
    predictions = test.apply(paper_author_set_order, axis=1, args=(paper_author_set, ))

    print("Writing predictions to file")
    data_io.write_submission(predictions)

if __name__=="__main__":
    main()