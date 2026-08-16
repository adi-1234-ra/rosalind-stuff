from Bio import SeqIO

for record in SeqIO.parse("rosalind_prot.fasta", "fasta"):
    protein_seq = record.seq.translate(to_stop=True)
    print(f"ID: {record.id}")
    print(f"Protein: {protein_seq}")