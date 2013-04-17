CREATE TABLE LabeledSetConfirmed (
    AuthorId BIGINT,
    PaperId BIGINT);

COPY LabeledSetConfirmed FROM '##DataPath##\KDD2013AuthorPaperIdentification\LabeledTransformed\LabeledSetConfirmed.csv' DELIMITERS ',' CSV HEADER;

CREATE TABLE LabeledSetDeleted (
    AuthorId BIGINT,
    PaperId BIGINT);

COPY LabeledSetDeleted FROM '##DataPath##\KDD2013AuthorPaperIdentification\LabeledTransformed\LabeledSetDeleted.csv' DELIMITERS ',' CSV HEADER;