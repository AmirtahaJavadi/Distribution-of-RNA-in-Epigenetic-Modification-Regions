from Bio import SeqIO

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
            

count_fivemers("gene.fna" ,"NC_000006.12:35342558-35428178")

def bedtocsv(file_path):
    return