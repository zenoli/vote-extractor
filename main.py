import camelot
import requests
import pandas as pd
from json import loads, dumps, load
from operator import itemgetter

def extract_data(url):
    print(">>>", url)
    tables = camelot.read_pdf(url)
    votings_df = (pd.concat( map(lambda table: table.df, tables[:-1]))
        .rename(
            columns={
                0: "name",
                1: "vote",
                2: "group",
                3: "canton"
            }
        )
        .set_index("name")
    )

    print(votings_df.head())
    return votings_df

def get_url(business_reference, vote=51):
    BASE_ROUTE = f"https://www.parlament.ch/poly/Abstimmung/{vote}/out"
    return f"{BASE_ROUTE}/vote_{vote}_{business_reference}.pdf"


def get_matches(entry):
    business, recommendation = itemgetter('business', 'recommendation')(entry)
    voting_df = extract_data(get_url(business))
    return voting_df.vote == recommendation


with open("recommendations.json") as f:
    recommendations = load(f)

    result_df = pd.DataFrame(data={
        entry["business"]: get_matches(entry) for entry in recommendations
    })
    result_df["followed_recommendation"] = result_df.sum(axis=1)
    print(result_df.head())





# votings_df.to_json('out/test.json', orient="index", indent=2)
