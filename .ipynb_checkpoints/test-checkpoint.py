from Bio import SeqIO

with open("data/covid.fasta") as handle:
    for record in SeqIO.parse(handle, "fasta"):
        print(record.id)