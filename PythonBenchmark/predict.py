from collections import defaultdict
import data_io

def main():
    print("Getting features for valid papers from the database")
    data = data_io.get_features_db("ValidPaper")
    author_paper_ids = [x[:2] for x in data]
    features = [x[2:] for x in data]

    print("Loading the classifier")
    classifier = data_io.load_model()

    print("Making predictions")
    predictions = classifier.predict_proba(features)[:,1]
    predictions = list(predictions)

    author_predictions = defaultdict(list)
    paper_predictions = {}

    for (a_id, p_id), pred in zip(author_paper_ids, predictions):
        author_predictions[a_id].append((pred, p_id))

    for author_id in sorted(author_predictions):
        paper_ids_sorted = sorted(author_predictions[author_id], reverse=True)
        paper_predictions[author_id] = [x[1] for x in paper_ids_sorted]

    print("Writing predictions to file")
    data_io.write_submission(paper_predictions)

if __name__=="__main__":
    main()