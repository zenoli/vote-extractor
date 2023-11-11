import argparse
import os


def parse_pdf_name(args):
    pdf_filename = args.pdf_url.rsplit("/", 1)[-1]
    name, _ = os.path.splitext(pdf_filename)
    return name


def get_args():
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
    return parser.parse_args()
