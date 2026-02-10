# Stochastic FASTQ Sequencer Simulator (SARS-CoV-2)
This Python-based tool simulates the output of a Next-Generation Sequencing (NGS) machine. It generates synthetic reads by extracting random fragments from a reference genome and modeling realistic quality degradation.
## 🧬 Key Features
* ### Genomic Fidelity:
  Extracts fragments from the SARS-CoV-2 reference genome (NC_045512.2), maintaining a validated 38.4% GC content.Dynamic Phred-Quality
* ### Modeling:
  Unlike static simulators, this tool implements a 3-tier stochastic quality profile to mimic real-world chemical decay:
  * Cycles 1-80: High stability ($Q38 - Q40$).
  * Cycles 81-90: Transition phase ($Q32$).
  * Cycles 91-100: Late-cycle noise and sensor degradation ($Q2 - Q10$).
* ### Standardized Output:
  Generates valid FASTQ files compatible with downstream bioinformatics tools (BWA, Samtools, FastQC).
## 📊 Performance & Validation
The simulator has been tested by generating 1.5 million bases with a consistent noise ratio of ~10%, accurately reflecting the expected quality drop at the end of sequencing reads.


<img width="1200" height="600" alt="graph" src="https://github.com/user-attachments/assets/13541af5-6ea7-41fe-ae48-02c80a2f40c9" />
