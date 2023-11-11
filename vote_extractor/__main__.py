import os

from vote_extractor.args import get_args, parse_pdf_name
from vote_extractor.extraction import extract_data


def main():
    args = get_args()
    df = extract_data(args.pdf_url).sort_values("firstname").head()
    name = args.name or parse_pdf_name(args)

    if args.csv:
        df.to_csv(os.path.join("out", f"{name}.csv"))
    if args.excel:
        df.to_csv(os.path.join("out", f"{name}.xlsx"))


if __name__ == "__main__":
    main()
