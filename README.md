KDD Cup 2013 - Author Paper Identification Challenge
====================================================

This repo contains a benchmark and sample code in Python for the [Author Paper Identification Challenge](https://www.kaggle.com/c/kdd-cup-2013-author-paper-identification-challenge), a machine learning challenged hosted by [Kaggle](https://www.kaggle.com) and organized by [Microsoft Research](http://research.microsoft.com/) in conjunction with the 2013 KDD Cup Committee and Kaggle.

It also contains the transformation code used to create the competition data files from the raw data in the Transform directory. This code is provided for your information only (and does not need to be looked at or run by competition participants).

This version of the repo contains the **Basic Coauthor Benchmark**. It adds a coauthor-based feature to the [Basic Python Benchmark](https://github.com/benhamner/Kdd2013AuthorPaperIdentification/tree/BasicPythonBenchmark). Future benchmarks may be included here as well and will be marked with git tags.

This benchmark is intended to provide a simple example of reading the data and creating the submission file, not as a state of the art benchmark on this problem.

Executing this benchmark requires Python 2.7 along with PostgreSQL 9.2, the Python package sklearn version 0.13, and psycopg2 version 2.4.6 (other versions may work, but this has not been tested).

To run the benchmark,

1. [Download data.postgres from the competition page](https://www.kaggle.com/c/kdd-cup-2013-author-paper-identification-challenge/data). This contains the dataset as a PostgreSQL backup (as an alternative format, the data are provided as csv files as well, but these are not used in this benchmark).
2. Restore the backup to your local Postgres database. This can be done by creating a new database named Kdd2013AuthorPaperIdentification and then running the following command:

    `pg_restore -Fc -U postgres -d Kdd2013AuthorPaperIdentification data.postgres`

3. Switch to the "PythonBenchmark" directory
4. Modify SETTINGS.json to include the login information to the PostgreSQL database, as well as a place to save the trained model and a place to save the submission
5. Train the model by running `python train.py`
6. Make predictions on the validation set by running `python predict.py`
7. [Make a submission](https://www.kaggle.com/c/kdd-cup-2013-author-paper-identification-challenge/team/select) with the output file

This benchmark took less than 10 minutes to execute on a Windows 8 laptop with 8GB of RAM and 4 cores at 2.7GHz.