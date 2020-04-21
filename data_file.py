import csv

input = 'datafile.txt'

def getdata(ip_address):

    get_data = []
    lines = []

    with open(input,'r') as f:
        data_reader = csv.reader(f)
        get_data = data_reader.__next__()
        for row in data_reader:
            lines.append(row)

    res = []
    for row in lines:
        string = row[0].split()[0]
        if string == ip_address:
            res.append(row)

    return get_data,res