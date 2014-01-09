#!/bin/bash

for s in *.sam
do
    samtools view -Shbu $s | samtools sort -m 6442450944 - ${s/.sam/} 2> /dev/null
    java -jar /home/be59/bin/picard-tools-1.98/MarkDuplicates.jar \
	 INPUT=${s/.sam/.bam} \
	 OUTPUT=${s/.sam/_de_duped.bam} \
	 METRICS_FILE=${s/.sam/_dupe_mets.txt} \
	 ASSUME_SORTED=true
    samtools index ${s/.sam/_de_duped.bam}
done
