from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import random
import sys

records = list(SeqIO.parse("data/covid.fasta", "fasta"))

dna_string = records[0].seq
C = 50
L = 100
G = len(dna_string)
N = C * G // L

def generate_quality(pos):
    if pos < 80:
        Q = random.randint(38, 40)
    elif pos < 90:
        Q = 32
    else:
        Q = random.randint(2, 10)
    prob = 10 ** (-Q/10)
    return Q, prob

def generate_mutation(nucleotide):
    nucleotides = ["A", "G", "C", "T"]
    nucleotides.remove(nucleotide)
    return nucleotides[random.randint(0,2)]

def main():
    sequences = []
    for i in range(N):
        k = random.randint(0, G-L)
        sequence = list(dna_string[k:k+L])
        quality_values = []
        for j in range(L):
            Q, prob = generate_quality(j)
            v = random.random()
            if v < prob:
                sequence[j] = generate_mutation(sequence[j])
                Q = 1
            quality_values.append(Q)
        record = SeqRecord(
            Seq("".join(sequence)),
            id=f"READ{i}",
            description="",
            letter_annotations={"phred_quality": quality_values},
        )
        sequences.append(record)
    SeqIO.write(sequences, "output_seqs.fastq", "fastq")

if __name__ == '__main__':
    sys.exit(main())