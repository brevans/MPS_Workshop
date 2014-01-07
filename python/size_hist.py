#!/usr/bin/env python
import sys
from Bio import SeqIO
from matplotlib import pyplot as plt

#get the size of each sequence in the file passed as argument 1
sizes = [len(rec) for rec in SeqIO.parse(sys.argv[1], "fasta")]

#make a new histogram with the sequence sizes
plt.hist(sizes, bins=50)

#add labels
plt.title("{} sequences\nLengths {} to {}".format(
            len(sizes), min(sizes), max(sizes)))
plt.xlabel("Sequence length (bp)")
plt.ylabel("Count")

#show me!
plt.show()
