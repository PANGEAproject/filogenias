import sys

def get_fasta_header(fasta):
    header = []
    with open(fasta, 'r') as f:
        for line in f:
            if line.startswith('>'):
                header.append(line.strip())
    return header

def get_names_of_fasta(fasta_information):
    names = []
    with open(fasta_information,'r') as f:
        for line in f:
            names.append(line.split('\t')[4])
    names.pop(0)
    return names

def get_new_header(header,names):
    new_header = []
    for fasta, name in zip(header,names):
        tmp_header = fasta.strip().split(' ')
        tmp_header[0] = '>' + '_'.join(name.strip().split(' '))
        new_header.append(' '.join(tmp_header))
    return new_header

def change_fasta_header(fasta,new_header):
    with open(fasta) as f:
        for line in f:
            if line.startswith('>'):
                print(new_header.pop(0))
            else:
                print(line.strip())

if __name__ == '__main__':
    fasta = sys.argv[1]
    information = sys.argv[2]
    header = get_fasta_header(fasta)
    names = get_names_of_fasta(information)
    new_header = get_new_header(header,names)
    change_fasta_header(fasta,new_header)