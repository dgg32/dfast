#embl to json

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation
import json
import sys
import os

folder = sys.argv[1]



input_embl = os.path.join(folder, "genome.embl")
input_rrna = os.path.join(folder, "rna.fna")


if folder.endswith("/"):
    folder = folder[:-1]

bin_name = os.path.basename(folder).replace("_dfast", "")
#print (os.path.basename(folder))
#output_json = sys.argv[2]

#{"id":"0","type":"relationship","label":"KNOWS","properties":{"since":1993,"bffSince":"P5M1DT12H"},"start":{"id":"0","labels":["User"]},"end":{"id":"1","labels":["User"]}}

rid = 0

content = ""

desired_products = ["DNA-directed RNA polymerase subunit beta"]

for seq_record in SeqIO.parse(input_embl, "embl"):
   
    
    for index, f in enumerate(seq_record.features):
        
        #print (f)
        q = {k[0]: k[1] for k in list(f.qualifiers.items())}
        

        if "product" in q:
            if q["product"][0] in desired_products:

                content += f'>{bin_name}_{q["locus_tag"][0]}_{q["gene"][0]}\n{q["translation"][0]}\n'


for seq_record in SeqIO.parse(input_rrna, "fasta"):

    if "16S ribosomal RNA" in seq_record.description:
        content += f'>{bin_name}_{seq_record.description}\n{seq_record.seq}\n'


print (content)



