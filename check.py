import sys

from Bio import SeqIO


def analyze_fastq(filename):
    records = list(SeqIO.parse(filename, "fastq"))
    n_records = len(records)
    total_bases = 0
    gc_count = 0
    low_quality_count = 0

    for record in records:
        seq = record.seq
        qualities = record.letter_annotations["phred_quality"]

        total_bases += len(seq)
        gc_count += seq.count("G") + seq.count("C")
        low_quality_count += sum(1 for q in qualities if q < 20)

    gc_content = (gc_count / total_bases) * 100
    noise_percent = (low_quality_count / total_bases) * 100

    print(f"--- Quality Report {filename} ---")
    print(f"Total analyzed sequences: {n_records}")
    print(f"Total analyzed bases: {total_bases}")
    print(f"GC Content: {gc_content}")
    print(f"Noise percent: {noise_percent}")


def main():
    analyze_fastq("output_seqs.fastq")


if __name__ == "__main__":
    sys.exit(main())
