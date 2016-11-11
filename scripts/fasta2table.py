### * Description

# Convert a fasta file containing protein sequences into a tab-separated table

# Input: name of a fasta file
# Output: write the output table to stdout

# Usage: python fasta2table.py myInputFile > myOutputFile

# Depends on the Biopython package to read the fasta files

### * Import

import sys
from Bio import SeqIO

### * Functions

### * Run

# Get the input file name
inputFile = sys.argv[1]

# Load all the sequences from the fasta file
with open(inputFile, "r") as fi:
    fasta = SeqIO.parse(fi, "fasta")
    sequences = list(fasta)

# Print sequences to stdout
out = sys.stdout
out.write("species\tsequence\n")
for seq in sequences:
    out.write(str(seq.description) + "\t")
    out.write(str(seq.seq) + "\n")
