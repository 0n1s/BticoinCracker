import csv

# Function to convert TSV to CSV
def tsv_to_csv(tsv_file, csv_file):
    with open(tsv_file, 'r', newline='', encoding='utf-8') as tsv_in, \
            open(csv_file, 'w', newline='', encoding='utf-8') as csv_out:
        tsv_reader = csv.reader(tsv_in, delimiter='\t')
        csv_writer = csv.writer(csv_out)

        # Skip header
        next(tsv_reader)

        # Write modified data to CSV
        for row in tsv_reader:
            # Remove second data value
            modified_row = row[:1] + row[2:]
            csv_writer.writerow(modified_row)

# Usage
tsv_file = 'btc.tsv'
csv_file = 'output.csv'
tsv_to_csv(tsv_file, csv_file)
print("Conversion completed successfully.")
