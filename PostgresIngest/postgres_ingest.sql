CREATE TABLE Paper (
    Id BIGINT,
    Title CHARACTER VARYING,
    Year BIGINT,
    ConferenceId BIGINT,
    JournalId BIGINT,
    Keyword CHARACTER VARYING);

COPY Paper FROM '##DataPath##\KDD2013AuthorPaperIdentification\Release 1\Paper.csv' DELIMITERS ',' CSV HEADER;

CREATE TABLE Author (
    Id BIGINT,
    Name CHARACTER VARYING,
    Affiliation CHARACTER VARYING);

COPY Author FROM '##DataPath##\KDD2013AuthorPaperIdentification\Release 1\Author.csv' DELIMITERS ',' CSV HEADER;

CREATE TABLE Journal (
    Id BIGINT,
    ShortName CHARACTER VARYING,
    FullName CHARACTER VARYING,
    HomePage CHARACTER VARYING);

COPY Journal FROM '##DataPath##\KDD2013AuthorPaperIdentification\Release 1\Journal.csv' DELIMITERS ',' CSV HEADER;

CREATE TABLE Conference (
    Id BIGINT,
    ShortName CHARACTER VARYING,
    FullName CHARACTER VARYING,
    HomePage CHARACTER VARYING);

COPY Conference FROM '##DataPath##\KDD2013AuthorPaperIdentification\Release 1\Conference.csv' DELIMITERS ',' CSV HEADER;

CREATE TABLE PaperAuthor (
    PaperId BIGINT,
    AuthorId BIGINT,
    Name CHARACTER VARYING,
    Affiliation CHARACTER VARYING);

COPY PaperAuthor FROM '##DataPath##\KDD2013AuthorPaperIdentification\Release 1\PaperAuthor.csv' DELIMITERS ',' CSV HEADER;

CREATE TABLE Train (
    AuthorId BIGINT,
    DeletedPaperIds CHARACTER VARYING,
    ConfirmedPaperIds CHARACTER VARYING);

COPY Train FROM '##DataPath##\KDD2013AuthorPaperIdentification\Release 1\Train.csv' DELIMITERS ',' CSV HEADER;

CREATE TABLE Valid (
    AuthorId BIGINT,
    PaperIds CHARACTER VARYING);

COPY Valid FROM '##DataPath##\KDD2013AuthorPaperIdentification\Release 1\Valid.csv' DELIMITERS ',' CSV HEADER;

CREATE TABLE ValidPapers (
    AuthorId BIGINT,
    PaperId BIGINT);

COPY ValidPapers FROM '##DataPath##\KDD2013AuthorPaperIdentification\Release 1\ValidPapers.csv' DELIMITERS ',' CSV HEADER;

CREATE TABLE TrainConfirmed (
    AuthorId BIGINT,
    PaperId BIGINT);

COPY TrainConfirmed FROM '##DataPath##\KDD2013AuthorPaperIdentification\Release 1\TrainConfirmed.csv' DELIMITERS ',' CSV HEADER;

CREATE TABLE TrainDeleted (
    AuthorId BIGINT,
    PaperId BIGINT);

COPY TrainDeleted FROM '##DataPath##\KDD2013AuthorPaperIdentification\Release 1\TrainDeleted.csv' DELIMITERS ',' CSV HEADER;