CREATE TABLE LabeledSetConfirmed (
    AuthorId BIGINT,
    PaperId BIGINT);

COPY LabeledSetConfirmed FROM 'C:\Users\ben_000\Dropbox\Data\KDD2013AuthorPaperIdentification\LabeledTransformed\LabeledSetConfirmed.csv' DELIMITERS ',' CSV HEADER;

CREATE TABLE LabeledSetDeleted (
    AuthorId BIGINT,
    PaperId BIGINT);

COPY LabeledSetDeleted FROM 'C:\Users\ben_000\Dropbox\Data\KDD2013AuthorPaperIdentification\LabeledTransformed\LabeledSetDeleted.csv' DELIMITERS ',' CSV HEADER;