import data_io
import features as f
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def main():
    print("Reading in the training data")
    train = data_io.read_train()

    print("Reading in the meta data")
    paper_author, paper_author_indexed = f.get_paper_author()

    print("Computing Relational Information")
    computed_features = f.get_all_computed_features(paper_author)

    print("Extracting features")
    features = []
    target = []
    for author_id, row in train.iterrows():
        for paper_id in row["DeletedPaperIds"]:
            s = f.get_features(paper_id, author_id, paper_author_indexed,computed_features)
            if s is None:
                print("Error at Author Id %d And Paper Id %d" % (author_id, paper_id))
            else:
                target.append(1)
                features.append(s)
        for paper_id in row["ConfirmedPaperIds"]:
            s = f.get_features(paper_id, author_id, paper_author_indexed,computed_features)
            if s is None:
                print("Error at Author Id %d And Paper Id %d" % (author_id, paper_id))
            else:
                target.append(0)
                features.append(s)

    print("Target Length: %d" % len(target))
    print("Feature Length: %d" % len(features))

    feature_matrix = pd.DataFrame(features)

    print("Training the Classifier")
    classifier = RandomForestClassifier(n_estimators=50, 
                                        verbose=2,
                                        n_jobs=1,
                                        min_samples_split=10,
                                        random_state=1)
    try:
        classifier.fit(feature_matrix, target)
    except:
        import pdb;pdb.set_trace()

    print("Saving the classifier")
    data_io.save_model(classifier)
    
if __name__=="__main__":
    import profile
    profile.run('main()')