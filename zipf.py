#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import matplotlib.pyplot as plt
from nltk import FreqDist

def main():
    corpora = ['idwiki', 'kaskus', 'kompas', 'twitter']
    for corpus in corpora:
        fd = FreqDist()
        for line in codecs.open(corpus + '.1gram', 'r', 'utf-8'):
            (word, freq) = line.split('\t')
            fd[word] = int(freq.strip())

        ranks = []
        freqs = []

        for rank, word in enumerate(fd):
            ranks.append(rank + 1)
            freqs.append(fd[word])

        plt.loglog(ranks, freqs)
        plt.xlabel('frequency(f)', fontsize=14, fontweight='bold')
        plt.ylabel('rank(r)', fontsize=14, fontweight='bold')
        plt.grid(True)
        plt.savefig(corpus + '.png')

if __name__ == '__main__':
    main()