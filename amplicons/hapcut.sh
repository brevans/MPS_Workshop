#!/bin/bash

for b in *_de_duped.bam
do
    sampl=${b/_de_duped.bam/}
    samtools mpileup -DISuf ../ref/tort_sptree_ref.fasta $b | bcftools view -vg - > ${sampl}.vcf
    extractHAIRS --bam $b --VCF ${sampl}.vcf --ref ../ref/tort_sptree_ref.fasta > ${sampl}.fragments
    HAPCUT --VCF ${sampl}.vcf --fragments ${sampl}.fragments --output ${sampl}_phased.txt > ${sampl}_hapcut.log
done
