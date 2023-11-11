import camelot
import pandas as pd


def extract_data(url):
    tables = camelot.read_pdf(url)
    votings_df = (
        pd.concat(map(lambda table: table.df, tables[:-1]))
        .rename(columns={0: "firstname", 1: "lastname", 2: "vote", 3: "canton"})
        .sort_values("firstname")
    )
    return votings_df
