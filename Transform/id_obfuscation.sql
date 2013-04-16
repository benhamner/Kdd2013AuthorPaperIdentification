-- Id Obfuscation Maps

CREATE TABLE AuthorIdObfuscationMap (
    NewAuthorId SERIAL PRIMARY KEY,
    OldAuthorId BIGINT NOT NULL
);

CREATE TABLE PaperIdObfuscationMap (
    NewPaperId SERIAL PRIMARY KEY,
    OldPaperId BIGINT NOT NULL
);

-- Obfuscated Tables

CREATE TABLE AuthorObfuscated (
    Id BIGINT PRIMARY KEY,
    Name CHARACTER VARYING,
    Affiliation CHARACTER VARYING);

CREATE TABLE PaperObfuscated (
    Id BIGINT PRIMARY KEY,
    Title CHARACTER VARYING,
    Year BIGINT,
    ConferenceId BIGINT,
    JournalId BIGINT,
    Keyword CHARACTER VARYING);

CREATE TABLE PaperAuthorObfuscated (
    PaperId BIGINT,
    AuthorId BIGINT,
    Name CHARACTER VARYING,
    Affiliation CHARACTER VARYING);

CREATE TABLE LabeledSetConfirmedObfuscated (
    AuthorId BIGINT,
    PaperId BIGINT);

CREATE TABLE LabelSetDeletedObfuscated (
    AuthorId BIGINT,
    PaperId BIGINT);

-- Filling out Id Obfuscation Maps

INSERT INTO AuthorIdObfuscationMap (OldAuthorId)
    WITH AuthorIds AS (
        SELECT Id
        FROM Author
      UNION
        SELECT AuthorId
        FROM PaperAuthor),
    DistinctAuthorIds AS (
        SELECT DISTINCT Id AS AuthorId
        FROM AuthorIds
    )
    SELECT AuthorId AS OldAuthorId
    FROM DistinctAuthorIds
    ORDER BY RANDOM();

INSERT INTO PaperIdObfuscationMap (OldPaperId)
    WITH PaperIds AS (
        SELECT Id
        FROM Paper
      UNION
        SELECT PaperId
        FROM PaperAuthor),
    DistinctPaperIds AS (
        SELECT DISTINCT Id AS PaperId
        FROM PaperIds
    )
    SELECT PaperId AS OldPaperId
    FROM DistinctPaperIds
    ORDER BY RANDOM();

-- Filling out Obfuscated Tables

INSERT INTO AuthorObfuscated
    SELECT m.NewAuthorId, a.Name, a.Affiliation
    FROM Author a
    INNER JOIN AuthorIdObfuscationMap m ON m.OldAuthorId=a.Id
    ORDER BY m.NewAuthorId;

INSERT INTO PaperObfuscated
    SELECT m.NewPaperId, p.Title, p.Year, p.ConferenceId, p.JournalId, p.Keyword
    FROM Paper p
    INNER JOIN PaperIdObfuscationMap m ON m.OldPaperId=p.Id
    ORDER BY m.NewPaperId;

INSERT INTO PaperAuthorObfuscated
    SELECT mp.NewPaperId, ma.NewauthorId, pa.Name, pa.Affiliation
    FROM PaperAuthor pa
    INNER JOIN PaperIdObfuscationMap mp ON mp.OldPaperId=pa.PaperId
    INNER JOIN AuthorIdObfuscationMap ma ON ma.OldAuthorId=pa.AuthorId
    ORDER BY mp.NewPaperId, ma.NewAuthorId;

-- Saving the obfuscated data files

COPY (
    SELECT * FROM AuthorObfuscated)
TO  'C:\Users\ben_000\Dropbox\Data\KDD2013AuthorPaperIdentification\Release 1\Author.csv'
WITH CSV HEADER;

COPY (
    SELECT * FROM PaperObfuscated)
TO  'C:\Users\ben_000\Dropbox\Data\KDD2013AuthorPaperIdentification\Release 1\Paper.csv'
WITH CSV HEADER;

COPY (
    SELECT * FROM PaperAuthorObfuscated)
TO  'C:\Users\ben_000\Dropbox\Data\KDD2013AuthorPaperIdentification\Release 1\PaperAuthor.csv'
WITH CSV HEADER;

-- Saving the obfuscated id maps

COPY (
    SELECT * FROM AuthorIdObfuscationMap)
TO  'C:\Users\ben_000\Dropbox\Data\KDD2013AuthorPaperIdentification\IdObfuscationMaps\AuthorIdObfuscationMap.csv'
WITH CSV HEADER;

COPY (
    SELECT * FROM PaperIdObfuscationMap)
TO  'C:\Users\ben_000\Dropbox\Data\KDD2013AuthorPaperIdentification\IdObfuscationMaps\PaperIdObfuscationMap.csv'
WITH CSV HEADER;
