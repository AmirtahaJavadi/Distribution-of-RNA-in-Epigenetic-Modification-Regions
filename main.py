from Bio import Entrez, SeqIO
import pandas as pd
import time

Entrez.email = "adelganeh@gmail.com"  # Use a real email
Entrez.tool = "fetch_sequence_script"


def fetch_sequence(row):
    chrom = row['chr']
    start = int(row['epigenetic_start'])
    end = int(row['epigenetic_end'])
    strand = 1 if row['strand'] == '+' else 2
    accession = chrom_to_accession.get(chrom)

    handle = Entrez.efetch(
        db="nucleotide",
        id=accession,
        rettype="fasta",
        retmode="text",
        seq_start=start,
        seq_stop=end,
        strand=strand
    )
    record = SeqIO.read(handle, "fasta")
    handle.close()
    return str(record.seq)

# Fetch sequences
df['sequence'] = df.apply(fetch_sequence, axis=1)


def count_fivemers(file_path , gene_id):
    file_path = file_path
    countfivemers = {}

    for record in SeqIO.parse(file_path, "fasta"):
        print(record.id)

    # Parse the FASTA file
    fivemers = []
    for record in SeqIO.parse(file_path, "fasta"):
        # Extract the 5-mers from the sequence
        if record.id == gene_id:
            for i in range(len(record.seq) - 5):
                fivemer = record.seq[i:i+5]
                # Add the 5-mer to the list
                fivemers.append(fivemer)



    for fivemer in fivemers:
        if fivemer in countfivemers:
            countfivemers[fivemer] += 1
        else:
            countfivemers[fivemer] = 1

    # Print the count of 5-mers
    primary_fivemers = countfivemers
    print(countfivemers)
    for key, value in countfivemers.items():
        if value <= 1 :
            primary_fivemers.pop(key)
            

# count_fivemers("gene.fna" ,"NC_000006.12:35342558-35428178")

def bedtocsv(file_path):
    file_path = file_path
    csv_file_path = file_path.replace(".bed", ".csv")
    df = pd.read_csv(file_path, sep="\t")
    df.to_csv(csv_file_path, index=False)


bedtocsv("H2AZ.bed")