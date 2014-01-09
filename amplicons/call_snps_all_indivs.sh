samtools mpileup -DISuf ../ref/tort_sptree_ref.fasta ../sams/*_de_duped.bam | bcftools view -vg - > raw_calls.vcf
