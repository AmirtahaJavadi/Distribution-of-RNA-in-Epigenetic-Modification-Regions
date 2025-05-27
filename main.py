from Bio import SeqIO

# Path to your .fna file
file_path = "gene.fna"

for record in SeqIO.parse(file_path, "fasta"):
    print(record.id)

# Parse the FASTA file
fivemers = []
for record in SeqIO.parse(file_path, "fasta"):
    # Extract the 5-mers from the sequence
    if record.id == "NC_000006.12:35342558-35428178":
        for i in range(len(record.seq) - 5):
            fivemer = record.seq[i:i+5]
            # Add the 5-mer to the list
            fivemers.append(fivemer)

# Print the list of 5-mers
print(fivemers)

countfivemers = {}

for fivemer in fivemers:
    if fivemer in countfivemers:
        countfivemers[fivemer] += 1
    else:
        countfivemers[fivemer] = 1

# Print the count of 5-mers
print(countfivemers)