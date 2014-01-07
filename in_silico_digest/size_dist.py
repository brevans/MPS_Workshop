#!/usr/bin/env python
import sys
import matplotlib.pyplot as plt
import numpy as np

fi=open(sys.argv[1])
enz1 = sys.argv[2]
enz2 = sys.argv[3]

c_contig = None
all_sizes = []
dd_sizes = []
enz_sizes = {enz1:[], enz2:[]}

#Start/End/Strand/Enzyme_name/Restriction_site/5prime/3prime/5primerev/3primerev
for line in fi:
    if (line.startswith('# Sequence:')):
        p_contig = c_contig
        c_contig = line.split()[2]
        p_site = None
        c_site = None
        last_enz = {enz1:None, enz2:None}
        continue

    elif(line.startswith('#') or line.startswith('  Start') or len(line)==1):
        continue

    else:
        p_site = c_site
        c_site = line.split()

        if p_site is None:
            all_sizes.append(int(c_site[0]))
            enz_sizes[c_site[3]].append(int(c_site[0]))

        elif(p_site[3] != c_site[3]):
            dd_sizes.append( int(c_site[0]) - int(p_site[0]) )
            all_sizes.append( int(c_site[0]) - int(p_site[0]) )
            if last_enz[c_site[3]] is not None:
                enz_sizes[c_site[3]].append( int(c_site[0]) - int(last_enz[c_site[3]][0]) )
            last_enz[c_site[3]] = c_site

        elif(p_site[3] == c_site[3]):
            all_sizes.append( int(c_site[0]) - int(p_site[0]) )
            enz_sizes[c_site[3]].append( int(c_site[0]) - int(p_site[0]) )

print "Average distances:"
for e in enz_sizes:
    print '%s:%.02f' % (e, np.average(enz_sizes[e]))

fig = plt.figure(1)
ax = fig.add_subplot(221)
al_n, bins, patches = ax.hist(all_sizes, 120, facecolor='green', alpha=0.75, range=(0,1200))
plt.ylim(0,3000000)
ax.set_xlabel('Size')
ax.set_ylabel('Number of Fragments')
ax.set_title('Double Digestion')
ax.grid(True)

ax = fig.add_subplot(222)
se_n, bins, patches = ax.hist(dd_sizes, 120, facecolor='green', alpha=0.75, range=(0,1200))
plt.ylim(0,3000000)
ax.set_xlabel('Size')
ax.set_ylabel('Number of Fragments')
ax.set_title('Number of Sequenceable Fragments')
ax.grid(True)

ax = fig.add_subplot(223)
e1_n, bins, patches = ax.hist(enz_sizes[enz1], 120, facecolor='green', alpha=0.75, range=(0,1200))
plt.ylim(0,3000000)
ax.set_xlabel('Size')
ax.set_ylabel('Number of Fragments')
ax.set_title(enz1+' Digestion')
ax.grid(True)

ax = fig.add_subplot(224)
e2_n, bins, patches = ax.hist(enz_sizes[enz2], 120, facecolor='green', alpha=0.75, range=(0,1200))
plt.ylim(0,3000000)
ax.set_xlabel('Size')
ax.set_ylabel('Number of Fragments')
ax.set_title(enz2+' Digestion')
ax.grid(True)

out = open('size_dists.csv', 'w')
out.write('%s,%s,%s,%s_digest,%s_digest\n' % ('bin_start', 
          'all_fragments', 'Sequenceable_Fragments', enz1, enz2))
for tup in zip(bins, al_n, se_n, e1_n, e2_n):
    out.write('%i,%i,%i,%i,%i\n' % (tup))

plt.show()
