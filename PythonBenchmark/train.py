import data_io
from sklearn.ensemble import RandomForestClassifier

def main():
    print("Getting features for confirmed papers from the database")
    features_conf = data_io.get_features_db("TrainConfirmed")

    print("Getting features for deleted papers from the database")
    features_deleted = data_io.get_features_db("TrainDeleted")

    features = [x[2:] for x in features_conf + features_deleted]
    target = [0 for x in range(len(features_conf))] + [1 for x in range(len(features_deleted))]

    print("Training the Classifier")
    classifier = RandomForestClassifier(n_estimators=50, 
                                        verbose=2,
                                        n_jobs=1,
                                        min_samples_split=10,
                                        random_state=1)
    classifier.fit(features, target)
    
    print("Saving the classifier")
    data_io.save_model(classifier)
    
if __name__=="__main__":
    main()