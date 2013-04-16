import data_io
import numpy as np
import pandas as pd

def get_paper_author():
    paper_author = data_io.read_paper_author_no_duplicates()
    paper = data_io.read_meta_data("Paper")
    author = data_io.read_meta_data("Author")
    conference = data_io.read_meta_data("Conference")
    journal = data_io.read_meta_data("Journal")

    paper_author = (paper_author.join(paper, on="PaperId")
                                .join(author, on="AuthorId", rsuffix="Author_")
                                .join(conference, on="ConferenceId", rsuffix="Conference_")
                                .join(journal, on="JournalId", rsuffix="Journal_"))
    paper_author_indexed = paper_author.set_index(["PaperId", "AuthorId"], verify_integrity=True)
    return paper_author, paper_author_indexed

def get_all_computed_features(paper_author):
    return {
        "author_conference_count": paper_author.groupby(["AuthorId", "ConferenceId"]).apply(len),
        "author_journal_count": paper_author.groupby(["AuthorId", "JournalId"]).apply(len),
        "author_paper_count": paper_author.groupby("AuthorId").apply(len)
    }

def get_features(paper_id, author_id, paper_author_indexed,computed_features):
    if (paper_id, author_id) not in paper_author_indexed.index:
        return None
    conference_id = paper_author_indexed.ix[(paper_id, author_id)]["ConferenceId"]
    journal_id = paper_author_indexed.ix[(paper_id, author_id)]["JournalId"]

    features = {
        "PaperCount": computed_features["author_paper_count"][author_id],
        "AuthorSameConferenceCount": 0 if (np.isnan(conference_id) or conference_id<=0) else computed_features["author_conference_count"][(author_id, conference_id)],
        "AuthorSameJournalCount": 0 if (np.isnan(journal_id) or journal_id<=0) else computed_features["author_journal_count"][(author_id, journal_id)]
    }

    return pd.Series(features)