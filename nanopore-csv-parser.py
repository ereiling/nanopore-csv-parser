#!/bin/bash

import sys
import csv

run_id = sys.argv[2]

with open(sys.argv[1], newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    samples = {}
    linenumber = 1
    for row in reader:
        bc = row[4]
        taxon = row[6]
        if samples.get(bc) is None:
            samples[bc] = {}
        if samples[bc].get(taxon) is None:
            samples[bc][taxon] = 1
        else:
            samples[bc][taxon] += 1
        if linenumber % 10000 == 0:
            print(linenumber)
        linenumber += 1

f = open("TaxonCounts_"+run_id+".csv", "w")
for bc in samples:
    for taxon in samples[bc]:
        f.write(run_id + "_" + bc + "," + taxon + "," + str(samples[bc][taxon]) + "\n")
f.close()
