# Vote Extractor

Simple python cli to extract voting results from PDfs published by the [swiss parliament](https://www.parlament.ch).


## Installation

### Dependencies

Make sure to have the following dependencies installed:

- Python 3.10 or later
- pip
- pipx
- Ghostscript (Windows)

## Window Setup (Tested on Windows 11)

### 1. Install python & pip

- Open the "Marketplace" and search for python. Install it.
  Alternatively, download and instal python [here](https://www.python.org/ftp/python/3.11.6/python-3.11.6-amd64.exe)
- Open a terminal: `Start > Type "cmd" > start "Command Prompt"`
- Inside the terminal, type `python --version` and press "Enter".
  If you see something like this, python was succesfully installed:

```
\> python --version
Python 3.11.6
```

- Also check if `pip` was installed by typing `pip --version`. If you see something like this you're good:

```
\> pip --version
pip 23.2.1 from C:\... (python 3..11)
```

### 2. Install pipx

Inside the terminal, first type 
```
python -m pip install --user pipx
```
Confirm with enter and wait for the command to complete. 
Then type:

```
python -m pipx ensurepath
```
Again, confirm with enter and wait for completion.
Open a new terminal (`Start > Type "cmd" > start "Command Prompt"`) and type `pipx --version` to verify if the installation was succesful:

```
\> pipx --version
1.2.1
```

### 3. Install Ghostscript

Download and install Ghostscript from [here](https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs10021/gs10021w64.exe).

Now you need to add two environment variables for Ghostscript to your PATH:

- Press START
- Type "Environment Variables" (Umgebungsvariablen?) and look for the option "Edit the system environment variables" (Umgebungsvariablen bearbeiten?)
- A dialog opens. Double click "Path" in the top panel.
- Add two new entries to the list, one for the `bin` and one for the `lib` directory of the just installed Ghostscript dependency. For the paths to the to folders looked like this (might be slightly different on your machine):

```
C:\Program Files\gs10.02.1\bin
C:\Program Files\gs10.02.1\lib
```

- Confirm and close all dialogs.

Ghostscript should be setup correctly.

### 4. Install the App!

Now that all dependencies are installed, we can install the `vote-extractor` using `pipx`:

In a new terminal, type:

```
\> pipx install vote-extractor
```

Open a new terminal and type `extract-votes --help`. If you see the following output, everything is set up correctly:

```
\> extract-votes --help
usage: extract-votes [-h] [-x] [-c] [-n NAME] [-d DIRECTORY] pdf_url

positional arguments:
  pdf_url               Url to the pdf to extract votes from.

options:
  -h, --help            show this help message and exit
  -x, --excel           Store extracted votes as excel file.
  -c, --csv             Store extracted votes CSV file.
  -n NAME, --name NAME  Name of the generated file(s). Defaults to the input PDF name.
  -d DIRECTORY, --directory DIRECTORY
                        Name of the directory where the generated PDFs are stored. Defaults to `./out.`
```

## Usage

To see an overview of what you can do, type:

```
extract-votes --help
```

To extract the votes from the following link:

https://www.parlament.ch/poly/AbstimmungSR/51/out/Abstimmung_51_6126.pdf

...and extract to both an excel file and a csv file named "my-test" inside the folder "my-output-folder", use the following command:

```shell
extract-votes --csv --excel --directory="my-output-folder" --name="my-test" https://www.parlament.ch/poly/AbstimmungSR/51/out/Abstimmung_51_6126.pdf
```

After that, you will see the following files:

```
my-output-folder
├── my-test.csv
└── my-test.xlsx
```

If you omit the `--directory` and `--name` arguments, the result would be different:

```shell
extract-votes --csv --excel  https://www.parlament.ch/poly/AbstimmungSR/51/out/Abstimmung_51_6126.pdf
```
The resulting files would be:
```
out
├── Abstimmung_51_6126.csv
└── Abstimmung_51_6126.xlsx
```
