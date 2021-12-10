import solution

if __name__ == '__main__':
    reads_file = "data/reads.csv"
    loci_file = "data/loci.csv"
    s = solution.Solution(reads_file, loci_file)
    s.run()

