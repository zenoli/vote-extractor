import os

from vote_extractor.args import get_args, parse_pdf_name
from vote_extractor.extraction import extract_data


def main():
    args = get_args()

    print("Downloading pdf and extracting data...")
    df = extract_data(args.pdf_url)
    name = args.name or parse_pdf_name(args)

    if not os.path.isdir(args.directory):
        print(f"Creating directory {args.directory}")
        os.makedirs(args.directory)

    if args.csv:
        csv_file = os.path.join(args.directory, f"{name}.csv")
        print(f"Storing csv file: {csv_file}")
        df.to_csv(csv_file)
        print("DONE")
    if args.excel:
        excel_file = os.path.join(args.directory, f"{name}.xlsx")
        print(f"Storing excel_file file: {excel_file}")
        df.to_excel(excel_file)
        print("DONE")


if __name__ == "__main__":
    main()
