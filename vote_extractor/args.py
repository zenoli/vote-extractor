import argparse
import os


def parse_pdf_name(args):
    pdf_filename = args.pdf_url.rsplit("/", 1)[-1]
    name, _ = os.path.splitext(pdf_filename)
    return name


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument()
    parser.add_argument(
        "pdf_url",
        help="Url to the pdf to extract votes from."
    )  # fmt: skip
    parser.add_argument(
        "-x",
        "--excel",
        help="Store extracted votes as excel file.",
        action="store_true",
    )
    parser.add_argument(
        "-c",
        "--csv",
        help="Store extracted votes CSV file.",
        action="store_true"
    )  # fmt: skip
    parser.add_argument(
        "-n",
        "--name",
        help="Name of the generated file(s). Defaults to the input PDF name.",
    )
    parser.add_argument(
        "-d",
        "--directory",
        help="""
            Name of the directory where the generated PDFs are stored.
            Defaults to `./out.`
        """,
        default="out",
    )
    return parser.parse_args()
