import camelot
import pandas as pd


def extract_data(url):
    tables = camelot.read_pdf(url, backend="ghostscript")
    df = pd.concat(map(lambda table: table.df, tables[:-1])).rename(
        columns={
            0: "firstname",
            1: "lastname",
            2: "vote",
            3: "canton"
        }
    )  # fmt: skip
    df["firstname"] = df["firstname"].map(lambda name: name.replace("\n", ""))
    df = df.sort_values("firstname")
    df = df[df["vote"] != ""]
    return df
