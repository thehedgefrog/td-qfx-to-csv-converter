# TD QFX to CSV Converter
I am using [Lunch Money](https://lunchmoney.app/?refer=i7ge2gmq) *(this is an affiliate link, if you like this, please use it to sign up!)* and for now, TD Canada Trust does not support OAuth integration with Plaid.

Since I would rather not give Plaid my credentials, I have to resort to importing CSV files.  With TD, you can get a multi-account QFX (Quicken) file from the main accounts page, but not a CSV.

This script converts your multi-account QFX to a CSV that you can import as is in Lunch Money, and match the accounts from the first column into your existing Lunch Money configuration.

## Requirements
Any computer with Python with version 3.6 or later installed.

## Usage
First, install prerequisites:
```
pip install -r requirements.txt
```

Then, you can use it by running
```
python3 converter.py your_qfx_file.qfx
```
where you specify your own QFX file.  The output file name will be diplayed and will be `export` followed by a timestamp.