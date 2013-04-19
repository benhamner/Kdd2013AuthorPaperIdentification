CREATE TABLE Paper (
    Id BIGINT PRIMARY KEY,
    Title CHARACTER VARYING,
    Year BIGINT,
    ConferenceId BIGINT,
    JournalId BIGINT,
    Keyword CHARACTER VARYING);

COPY Paper FROM '##DataPath##\KDD2013AuthorPaperIdentification\Release 2\Paper.csv' DELIMITERS ',' CSV HEADER NULL AS 'NULL';

CREATE TABLE Author (
    Id BIGINT PRIMARY KEY,
    Name CHARACTER VARYING,
    Affiliation CHARACTER VARYING);

COPY Author FROM '##DataPath##\KDD2013AuthorPaperIdentification\Release 2\Author.csv' DELIMITERS ',' CSV HEADER NULL AS 'NULL';

CREATE TABLE Journal (
    Id BIGINT PRIMARY KEY,
    ShortName CHARACTER VARYING,
    FullName CHARACTER VARYING,
    HomePage CHARACTER VARYING);

COPY Journal FROM '##DataPath##\KDD2013AuthorPaperIdentification\Release 2\Journal.csv' DELIMITERS ',' CSV HEADER NULL AS 'NULL';

CREATE TABLE Conference (
    Id BIGINT PRIMARY KEY,
    ShortName CHARACTER VARYING,
    FullName CHARACTER VARYING,
    HomePage CHARACTER VARYING);

COPY Conference FROM '##DataPath##\KDD2013AuthorPaperIdentification\Release 2\Conference.csv' DELIMITERS ',' CSV HEADER NULL AS 'NULL';

CREATE TABLE PaperAuthor (
    PaperId BIGINT,
    AuthorId BIGINT,
    Name CHARACTER VARYING,
    Affiliation CHARACTER VARYING);

COPY PaperAuthor FROM '##DataPath##\KDD2013AuthorPaperIdentification\Release 2\PaperAuthor.csv' DELIMITERS ',' CSV HEADER NULL AS 'NULL';

CREATE TABLE ValidPaper (
    AuthorId BIGINT,
    PaperId BIGINT);

COPY ValidPaper FROM '##DataPath##\KDD2013AuthorPaperIdentification\Release 2\ValidPaper.csv' DELIMITERS ',' CSV HEADER;

CREATE TABLE TrainConfirmed (
    AuthorId BIGINT,
    PaperId BIGINT);

COPY TrainConfirmed FROM '##DataPath##\KDD2013AuthorPaperIdentification\Release 2\TrainConfirmed.csv' DELIMITERS ',' CSV HEADER;

CREATE TABLE TrainDeleted (
    AuthorId BIGINT,
    PaperId BIGINT);

COPY TrainDeleted FROM '##DataPath##\KDD2013AuthorPaperIdentification\Release 2\TrainDeleted.csv' DELIMITERS ',' CSV HEADER;