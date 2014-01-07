#!/usr/bin/env python
import sys
from Bio import SeqIO

fi = open(sys.argv[1])
enz1 = sys.argv[2]
enz2 = sys.argv[3]
ref_fn = sys.argv[4]

c_contig = None
rad_tags = []

ref = SeqIO.to_dict(SeqIO.parse(open(ref_fn), "fasta"))

#Start/End/Strand/Enzyme_name/Restriction_site/5prime/3prime/5primerev/3primerev
for line in fi:
    if (line.startswith('# Sequence:')):
        p_contig = c_contig
        c_contig = line.split()[2]
        p_site = None
        c_site = None
        continue

    elif(line.startswith('#') or line.startswith('  Start') or len(line)==1):
        continue

    else:
        p_site = c_site
        c_site = line.split()

        if(p_site != None and p_site[3] != c_site[3]):
            start = int(p_site[0])
            stop = int(c_site[1])
            frag_len = stop - start
            if frag_len >= 200 and frag_len <= 5000:
                rad_tags.append( (c_contig, start, stop, str(ref[c_contig].seq[start-1:stop])) )

single_rads = open('single_rads.bed', 'w')
merged_rads = open('merged_rads.bed', 'w')
merged_seqs = open('merged_rads.fa', 'w')

merge_dist = 5000
prev_rt = None
merged_rt = None

for rt in rad_tags:
    single_rads.write('\t'.join([str(x) for x in rt])+'\n')
        
    if merged_rt is None:
        merged_rt = rt
    elif prev_rt is None:
        prev_rt = merged_rt
        merged_rt = rt
    elif prev_rt[0] == rt[0] and (rt[1] - prev_rt[2]) <= merge_dist:
        merged_rt=(prev_rt[0], prev_rt[1], rt[2], str(ref[prev_rt[0]].seq[prev_rt[1]-1:rt[2]]))
    else:
        merged_rads.write('\t'.join([str(x) for x in prev_rt])+'\n')
        merged_seqs.write('>'+'_'.join([str(x) for x in prev_rt[:3]])+"\n"+prev_rt[3]+"\n")
        prev_rt = rt

merged_rads.write('\t'.join([str(x) for x in prev_rt])+'\n')
merged_seqs.write('>'+'_'.join([str(x) for x in prev_rt[:3]])+"\n"+prev_rt[3]+"\n")



