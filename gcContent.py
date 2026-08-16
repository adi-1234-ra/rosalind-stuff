from pathlib import Path
from Bio import SeqIO

script_dir = Path(__file__).parent
fasta_file = script_dir / "rosalind_gc.fasta"  # Update filename if needed

highest_gc = -1
highest_id = ""

for record in SeqIO.parse(fasta_file, "fasta"):
    dna_seq = record.seq
    
    # Count Gs and Cs
    gc_count = dna_seq.count("G") + dna_seq.count("C")
    total_length = len(dna_seq)
    
    # Calculate percentage
    gc_content = (gc_count / total_length) * 100
    
    # Keep track of the highest one
    if gc_content > highest_gc:
        highest_gc = gc_content
        highest_id = record.id

# Print the ID and the GC percentage (Rosalind usually accepts 6 decimal places)
print(highest_id)
print(f"{highest_gc:.6f}")

