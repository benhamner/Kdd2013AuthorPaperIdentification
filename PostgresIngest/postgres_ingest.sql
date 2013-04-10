CREATE TABLE Paper (
    Id BIGINT,
    Title CHARACTER VARYING,
    Year BIGINT,
    ConferenceId BIGINT,
    JournalId BIGINT,
    Keyword CHARACTER VARYING);

COPY Paper FROM 'C:\Users\ben_000\Dropbox\Data\KDD2013AuthorPaperIdentification\Release 1\Paper.csv' DELIMITERS ',' CSV HEADER;

CREATE TABLE Author (
    Id BIGINT,
    Name CHARACTER VARYING,
    Affiliation CHARACTER VARYING);

COPY Author FROM 'C:\Users\ben_000\Dropbox\Data\KDD2013AuthorPaperIdentification\Release 1\Author.csv' DELIMITERS ',' CSV HEADER;

CREATE TABLE Journal (
    Id BIGINT,
    ShortName CHARACTER VARYING,
    FullName CHARACTER VARYING,
    HomePage CHARACTER VARYING);

COPY Journal FROM 'C:\Users\ben_000\Dropbox\Data\KDD2013AuthorPaperIdentification\Release 1\Journal.csv' DELIMITERS ',' CSV HEADER;

CREATE TABLE Conference (
    Id BIGINT,
    ShortName CHARACTER VARYING,
    FullName CHARACTER VARYING,
    HomePage CHARACTER VARYING);

COPY Conference FROM 'C:\Users\ben_000\Dropbox\Data\KDD2013AuthorPaperIdentification\Release 1\Conference.csv' DELIMITERS ',' CSV HEADER;

CREATE TABLE PaperAuthor (
    PaperId BIGINT,
    AuthorId BIGINT,
    Name CHARACTER VARYING,
    Affiliation CHARACTER VARYING);

COPY PaperAuthor FROM 'C:\Users\ben_000\Dropbox\Data\KDD2013AuthorPaperIdentification\Release 1\PaperAuthor.csv' DELIMITERS ',' CSV HEADER;

CREATE TABLE Train (
    AuthorId BIGINT,
    DeletedPaperIds CHARACTER VARYING,
    ConfirmedPaperIds CHARACTER VARYING);

COPY Train FROM 'C:\Users\ben_000\Dropbox\Data\KDD2013AuthorPaperIdentification\Release 1\Train.csv' DELIMITERS ',' CSV HEADER;

CREATE TABLE Valid (
    AuthorId BIGINT,
    PaperIds CHARACTER VARYING);

COPY Valid FROM 'C:\Users\ben_000\Dropbox\Data\KDD2013AuthorPaperIdentification\Release 1\Valid.csv' DELIMITERS ',' CSV HEADER;