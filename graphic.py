import matplotlib.pyplot as plt
import data_file
from datetime import datetime,date,time


def convert_to_bytes(x):
    a = x.split()
    if len(a) == 1:
        return  float(a[0])
    else:
        b = float(a[0])
        if a[1] == 'G':
            return b*pow(2,30)
        if a[1] == 'M':
            return b*pow(2,20)

def graph(data):
    byte = []
    start = []
    end = []
    for row in data:
        str_byte = row[2]
        str_start_time = row[3]
        str_end_time = row[4]
        a =  str_start_time.split('.')
        b =  str_end_time.split('.')
        c =  convert_to_bytes(str_byte)
        start_time = datetime.strptime(a[0],"%Y-%m-%d %H:%M:%S")
        end_time = datetime.strptime(b[0],"%Y-%m-%d %H:%M:%S")
        start.append(start_time)
        end.append(end_time)
        byte.append(c)
    last_e = max(end)
    first_s = min(start)
    dict_data = {}
    for i in range((last_e-first_s).seconds+1):
        dict_data[i] = 0
    for i in range(len(start)):
        duration = (end[i] - start[i]).seconds + 1
        bytes_per_second = byte[i]/duration
        for j in range((start[i]-first_s).seconds,(end[i]-first_s).seconds+1):
            dict_data[j] += bytes_per_second

    y = list(dict_data.values())
    x = list(dict_data.keys())

    plt.plot(x,y)
    plt.title("Graphic of traffic data")
    plt.xlabel('Time (second)')
    plt.ylabel('Bytes')
    plt.show()

def show(ip_address):
    _,data = data_file.getdata(ip_address)
    graph(data)