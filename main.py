import camelot
import pandas as pd
from json import loads, dumps

tables = camelot.read_pdf('pdfs/test.pdf')
tables.export('foo.csv', f='csv', compress=True)
votings_df = pd.concat(map(lambda table: table.df, tables[:-1])).reset_index(drop=True)
print(votings_df)

result = votings_df.to_json(orient="index")
parsed = loads(result)
print(dumps(parsed, indent=4))
