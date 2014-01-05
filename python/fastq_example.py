#!/usr/bin/env python
from Bio import SeqIO
#quality filter a fastq file, print results to screen

#set an average quality score cutoff
qual_cutoff = 25

#initialize fastq file parser
fastq_file = SeqIO.parse(open("fastqs/fastq1.fastq", "r"), "fastq")

for record in fastq_file:
    #sum of quality scores divided by the length
    avg_qual = sum(record.letter_annotations["phred_quality"]) / len(record)

    #if the read is of sufficient average quality
    if avg_qual > qual_cutoff:
        #print it in fastq format
        print(record.format("fastq"))
