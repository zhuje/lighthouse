import csv
import sys

reads_dictionary = {}
coverage_list = []
read_file = "data/reads.csv"
loci_file = "data/loci.csv"
loci_header = ["position", "coverage"]




# preprocess_reads() -- takes the reads and puts them into a dictionary
# where keys are loci and values are counts of each read (aka coverage).
def preprocess_reads(file):
    with open(file) as csv_file:
        reader = csv.DictReader(csv_file)
        next(reader, None)  # skips header row
        try:
            for row in reader:
                start = row['start']
                length = row['length']
                for i in range(int(length)):
                    key = int(start) + i
                    if reads_dictionary.__contains__(key):
                        reads_dictionary[key] += 1
                    else:
                        reads_dictionary[key] = 1
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(csv_file, reader.line_num, e))
    csv_file.close()


# process_coverage() -- reads the position of interest and access the dictionary to retrieve coverage.
# This tuple is saved in an array to be written to a csv file.
def process_coverage(file):
    with open(file) as csv_file:
        reader = csv.reader(csv_file)
        next(reader, None)  # skips header row
        try:
            for row in reader:
                position = int(row[0])
                coverage = reads_dictionary.get(position)
                if coverage:
                    coverage_list.append([position, coverage])
                else:
                    coverage_list.append([position, '0'])
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(csv_file, reader.line_num, e))
    csv_file.close()


# write_coverage -- writes coverage for positions of interest to a given csv file
def write_coverage(file):
    with open(file, 'w') as csv_file:
        try:
            writer = csv.writer(csv_file)
            writer.writerow(loci_header)
            writer.writerows(coverage_list)
        except csv.Error as e:
            sys.exit('file {}, {}'.format(csv_file, e))
    csv_file.close()


def run():
    preprocess_reads(read_file)
    process_coverage(loci_file)
    write_coverage(loci_file)

