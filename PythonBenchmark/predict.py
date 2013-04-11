import data_io
import features as f
import pandas as pd

def main():
    print("Reading the test data") 
    test = data_io.read_test()

    print("Reading in the meta data")
    paper_author, paper_author_indexed = f.get_paper_author()

    print("Computing Relational Information")
    computed_features = f.get_all_computed_features(paper_author)

    print("Loading the classifier")
    classifier = data_io.load_model()

    print("Making predictions")
    predictions = []
    for author_id, row in test.iterrows():
        features = []
        paper_ids = []
        for paper_id in row["PaperIds"]:
            s = f.get_features(paper_id, author_id, paper_author_indexed,computed_features)
            if s is None:
                print("Error at Author Id %d And Paper Id %d" % (author_id, paper_id))
            else:
                features.append(s)
                paper_ids.append(paper_id)
        feature_matrix = pd.DataFrame(features)
        preds = classifier.predict_proba(feature_matrix)[:,1]
        paper_ids_sorted = sorted(zip(preds,row["PaperIds"]), reverse=True)
        print(paper_ids_sorted)
        predictions.append([x[1] for x in paper_ids_sorted])

    print("Writing predictions to file")
    data_io.write_submission(predictions)

if __name__=="__main__":
    main()