import argparse

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
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf_url", help="url to the pdf to extract votes from")
    parser.add_argument(
        "-x",
        "--excel",
        help="store extracted votes as excel file",
        action="store_true",
    )
    parser.add_argument(
        "-c", "--csv", help="store extracted votes CSV file", action="store_true"
    )
    parser.add_argument(
        "-n",
        "--name",
        help="name of the generated file(s). Defaults to the input PDF name",
    )
    args = parser.parse_args()
    extract_data(args.pdf_url).sort_values("firstname").head()

