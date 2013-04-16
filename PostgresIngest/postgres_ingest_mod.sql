CREATE TABLE Paper (
    Id BIGINT PRIMARY KEY,
    Title CHARACTER VARYING,
    Year BIGINT,
    ConferenceId BIGINT,
    JournalId BIGINT,
    Keyword CHARACTER VARYING);

COPY Paper FROM 'C:\Users\ben_000\Dropbox\Data\KDD2013AuthorPaperIdentification\Release 1\Paper.csv' DELIMITERS ',' CSV HEADER NULL AS 'NULL';

CREATE TABLE Author (
    Id BIGINT PRIMARY KEY,
    Name CHARACTER VARYING,
    Affiliation CHARACTER VARYING);

COPY Author FROM 'C:\Users\ben_000\Dropbox\Data\KDD2013AuthorPaperIdentification\Release 1\Author.csv' DELIMITERS ',' CSV HEADER NULL AS 'NULL';

CREATE TABLE Journal (
    Id BIGINT PRIMARY KEY,
    ShortName CHARACTER VARYING,
    FullName CHARACTER VARYING,
    HomePage CHARACTER VARYING);

COPY Journal FROM 'C:\Users\ben_000\Dropbox\Data\KDD2013AuthorPaperIdentification\Release 1\Journal.csv' DELIMITERS ',' CSV HEADER NULL AS 'NULL';

CREATE TABLE Conference (
    Id BIGINT PRIMARY KEY,
    ShortName CHARACTER VARYING,
    FullName CHARACTER VARYING,
    HomePage CHARACTER VARYING);

COPY Conference FROM 'C:\Users\ben_000\Dropbox\Data\KDD2013AuthorPaperIdentification\Release 1\Conference.csv' DELIMITERS ',' CSV HEADER NULL AS 'NULL';

CREATE TABLE PaperAuthor (
    PaperId BIGINT,
    AuthorId BIGINT,
    Name CHARACTER VARYING,
    Affiliation CHARACTER VARYING);

COPY PaperAuthor FROM 'C:\Users\ben_000\Dropbox\Data\KDD2013AuthorPaperIdentification\Release 1\PaperAuthor.csv' DELIMITERS ',' CSV HEADER NULL AS 'NULL';

CREATE TABLE ValidPaper (
    AuthorId BIGINT,
    PaperId BIGINT);

COPY ValidPapers FROM 'C:\Users\ben_000\Dropbox\Data\KDD2013AuthorPaperIdentification\Release 1\ValidPaper.csv' DELIMITERS ',' CSV HEADER;

CREATE TABLE TrainConfirmed (
    AuthorId BIGINT,
    PaperId BIGINT);

COPY TrainConfirmed FROM 'C:\Users\ben_000\Dropbox\Data\KDD2013AuthorPaperIdentification\Release 1\TrainConfirmed.csv' DELIMITERS ',' CSV HEADER;

CREATE TABLE TrainDeleted (
    AuthorId BIGINT,
    PaperId BIGINT);

COPY TrainDeleted FROM 'C:\Users\ben_000\Dropbox\Data\KDD2013AuthorPaperIdentification\Release 1\TrainDeleted.csv' DELIMITERS ',' CSV HEADER;