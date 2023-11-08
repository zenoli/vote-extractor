from json import dumps, load, loads
from operator import itemgetter

import camelot
import pandas as pd
import requests


def extract_data(url):
    print(">>>", url)
    tables = camelot.read_pdf(url)
    votings_df = (
        pd.concat(map(lambda table: table.df, tables[:-1]))
        .rename(columns={0: "name", 1: "vote", 2: "group", 3: "canton"})
        .set_index("name")
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


with open("recommendations.json") as f:
    business_recommendations = load(f)
    businesses = map(lambda br: br["business"], business_recommendations)
    recommendations = list(
        map(lambda br: br["recommendation"], business_recommendations)
    )

    result_df = pd.DataFrame(
        data={business: get_matches(business, False) for business in businesses}
    )

    n_votes = len(recommendations)

    n_yes = (result_df == "+").sum(axis=1)
    n_no = (result_df == "-").sum(axis=1)
    n_abstention = (result_df == "=").sum(axis=1)
    n_attendant = n_yes + n_no + n_abstention
    n_followed_recommendation = (result_df == recommendations).sum(axis=1)
    followed_recommendation_rate = n_followed_recommendation / (n_yes + n_no)
    participation_rate = (n_yes + n_no) / n_votes

    result_df = result_df.assign(
        n_yes=n_yes,
        n_no=n_no,
        n_abstention=n_abstention,
        n_attendant=n_abstention,
        n_followed_recommendation=n_followed_recommendation,
        followed_recommendation_rate=followed_recommendation_rate,
        participation_rate=participation_rate,
    )

    result_df.to_csv("out/voting_statistics.csv")
    print(result_df)


# votings_df.to_json('out/test.json', orient="index", indent=2)
