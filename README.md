KDD Cup 2013 - Author Paper Identification Challenge
====================================================

This repo contains a benchmark and sample code in Python for the [Author Paper Identification Challenge](https://www.kaggle.com/c/kdd-cup-2013-author-paper-identification-challenge), a machine learning challenged hosted by [Kaggle](https://www.kaggle.com) and organized by [Microsoft Research](http://research.microsoft.com/) in conjunction with the 2013 KDD Cup Committee and Kaggle.

It also contains the transformation code used to create the competition data files from the raw data in the Transform directory. This code is provided for your information only (and does not need to be looked at or run by competition participants).

This version of the repo contains the **Paper Author Set Benchmark**. Future benchmarks may be included here as well and will be marked with git tags.

Executing this benchmark requires Python 2.7 along with the following packages:

 - pandas (tested with version 10.1)
 - numpy (tested with version 1.6.2)

To run the benchmark,

1. [Download the data](https://www.kaggle.com/c/kdd-cup-2013-author-paper-identification-challenge/data)
2. Switch to the "PythonBenchmark" directory
3. Modify SETTINGS.json to point to the training and validation data on your system, as well as a place to save the trained model and a place to save the submission
4. Make predictions on the validation set by running `python predict.py`
5. [Make a submission](https://www.kaggle.com/c/kdd-cup-2013-author-paper-identification-challenge/team/select) with the output file

This benchmark took less than 5 minutes to execute on a Windows 8 laptop with 8GB of RAM and 4 cores at 2.7GHz.