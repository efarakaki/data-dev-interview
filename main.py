import gzip
import csv

def main():
    print('Welcome to data tech interview 1')
    with open('dataset/basics.tsv', 'r') as file:
        readf = csv.DictReader(file, dialect='excel-tab')
        contador = 0
        for reg in readf:
            if contador < 10:
                print(reg[0])
            else:
                break
            contador = contador +1



if __name__ == "__main__":
    main()
