import camelot
import pandas as pd
import requests


def extract_data(url):
    print(">>>", url)
    tables = camelot.read_pdf(url)
    votings_df = pd.concat(map(lambda table: table.df, tables[:-1])).rename(
        columns={0: "firstname", 1: "lastname", 2: "vote", 3: "canton"}
    )

    print(votings_df.head())
    return votings_df


def get_url(business_reference, remote, vote=51):
    REMOTE_ROUTE = f"https://www.parlament.ch/poly/Abstimmung/{vote}/out"
    LOCAL_ROUTE = "pdfs"
    LOCATION = REMOTE_ROUTE if remote else LOCAL_ROUTE
    return f"{LOCATION}/vote_{vote}_{business_reference}.pdf"


def get_matches(business, remote=True):
    voting_df = extract_data(get_url(business, remote))
    return voting_df.vote


if __name__ == "__main__":
    extract_data(
        "https://www.parlament.ch/poly/AbstimmungSR/51/out/Abstimmung_51_6126.pdf"
    ).sort_values("firstname").to_csv("out/out.csv")
