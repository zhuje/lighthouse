import csv
import sys


class Solution:
    def __init__(self, read_file, loci_file):
        self.reads_dictionary = {}
        self.coverage_list = []
        self.read_file = read_file
        self.loci_file = loci_file
        self.loci_header = ["position", "coverage"]

    # preprocess_reads() -- takes the reads and puts them into a dictionary
    # where keys are loci and values are counts of each read (aka coverage).
    def preprocess_reads(self):
        print("preprocess_reads")
        with open(self.read_file) as csv_file:
            reader = csv.DictReader(csv_file)
            try:
                for row in reader:
                    start = row['start']
                    length = row['length']
                    for i in range(int(length)):
                        key = int(start) + i
                        if self.reads_dictionary.__contains__(key):
                            self.reads_dictionary[key] += 1
                        else:
                            self.reads_dictionary[key] = 1
            except csv.Error as e:
                sys.exit('file {}, line {}: {}'.format(csv_file, reader.line_num, e))
        csv_file.close()

    # process_coverage() -- reads the position of interest and access the dictionary to retrieve coverage.
    # This tuple is saved in an array to be written to a csv file.
    def process_coverage(self):
        print("process coverage")

        with open(self.loci_file) as csv_file:
            reader = csv.reader(csv_file)
            next(reader, None)  # skips header row
            try:
                for row in reader:
                    position = int(row[0])
                    coverage = self.reads_dictionary.get(position)
                    if coverage:
                        self.coverage_list.append([position, coverage])
                    else:
                        self.coverage_list.append([position, 0])
            except csv.Error as e:
                sys.exit('file {}, line {}: {}'.format(csv_file, reader.line_num, e))
        csv_file.close()

    # write_coverage -- writes coverage for positions of interest to a given csv file
    def write_coverage(self):
        print("write coverage")
        with open(self.loci_file, 'w') as csv_file:
            try:
                writer = csv.writer(csv_file)
                writer.writerow(self.loci_header)
                writer.writerows(self.coverage_list)
            except csv.Error as e:
                sys.exit('file {}, {}'.format(csv_file, e))
        csv_file.close()

    def run(self):
        self.preprocess_reads()
        self.process_coverage()
        self.write_coverage()

