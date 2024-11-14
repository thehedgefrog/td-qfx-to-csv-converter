import csv
import sys
import argparse
from datetime import datetime
from ofxparse import OfxParser

# Set up argument parser for the input file
parser = argparse.ArgumentParser(description="Convert OFX file to CSV.")
parser.add_argument("input_file", help="The OFX file to convert")
args = parser.parse_args()

# Open and parse the OFX file specified in the command line
with open(args.input_file) as fileobj:
    ofx = OfxParser.parse(fileobj)

# Generate a timestamped filename for the CSV export
timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
output_filename = f"export-{timestamp}.csv"

# Open the CSV file for writing
with open(output_filename, mode='w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Iterate over each account and write transaction details
    for account in ofx.accounts:
        account_id = account.account_id
        statement = account.statement

        # Iterate over transactions within the account's statement
        for transaction in statement.transactions:
            writer.writerow([
                account_id,
                transaction.date,
                transaction.payee,
                transaction.type,
                transaction.amount
            ])

print(f"CSV file '{output_filename}' has been created successfully.")
