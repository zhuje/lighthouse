import csv
import sys
import unittest

from solution import Solution

read_file = "tests/test_data/read_test.csv"
loci_file = "tests/test_data/loci_test.csv"


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.solution = Solution(read_file, loci_file)
        self.solution.preprocess_reads()
        self.solution.process_coverage()

    def test_preprocess_reads(self):
        dictionary_result = {
            1: 1,
            2: 2,
            3: 3,
            4: 3,
            5: 3,
            6: 2,
            7: 2,
            8: 1,
            9: 1,
            40: 1
        }
        self.assertEqual(self.solution.reads_dictionary, dictionary_result)

    def test_process_coverage(self):
        coverage_results = [
            [1, 1],
            [5, 3],
            [6, 2],
            [7, 2],
            [8, 1],
            [40, 1],
            [100000000, 0],
        ]
        self.assertEqual(self.solution.coverage_list, coverage_results)

    def test_write_coverage(self):
        loci_results = [
            ["1", "1"],
            ["5", "3"],
            ["6", "2"],
            ["7", "2"],
            ["8", "1"],
            ["40", "1"],
            ["100000000", "0"],
        ]
        self.solution.write_coverage()
        with open(loci_file, 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader, None)  # skips header row
            try:
                i = 0
                for row in reader:
                    self.assertEqual(row, loci_results[i])
                    i += 1
            except csv.Error as e:
                sys.exit('file {}, {}'.format(csv_file, e))
        csv_file.close()


if __name__ == '__main__':
    unittest.main()
