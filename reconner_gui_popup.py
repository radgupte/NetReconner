import re
import collections
import time
import os
from tkinter import *


'''while True:

    os.system("sudo tcpdump -c 1000 -nnvvSs 1564 -A > packet_capture.txt &")
    time.sleep(3)
    os.system("pgrep -f tcpdump > pid.txt")
    with open("pid.txt","r") as f:
        pids = list(f.read())

    for i in pids[0:2]:
        try:
            os.kill(int(i), signal.SIGSTOP)
        except:
            pass
            
print('abc') '''
start = time.time()


l1, l2, l3 = [], [], []
c = 0
with open('regex-database/xss_regex.txt', 'r+') as s1:
    with open('regex-database/temp_xss_regex.txt', 'r') as d1:
        for line in s1:
            # print(line)
            if line.strip():
                l1.append(line)
                c = len(l1)-1
        for line in d1:
            if(line != l1[c]):
                s1.write('\n')
                s1.write(line)


c = 0
with open('regex-database/sqli_regex.txt', 'r+') as s2:
    with open('regex-database/temp_sqli_regex.txt', 'r') as d2:
        for line in s2:
            # print(line)
            if line.strip():
                l2.append(line)
                c = len(l2)-1
        for line in d2:
            if(line != l2[c]):
                s2.write('\n')
                s2.write(line)


c = 0
with open('regex-database/dos_regex.txt', 'r+') as s3:
    with open('regex-database/temp_dos_regex.txt', 'r') as d3:
        for line in s3:
            # print(line)
            if line.strip():
                l3.append(line)
                c = len(l3)-1
        for line in d3:
            if(line != l3[c]):
                s3.write('\n')
                s3.write(line)

flagnmap = 0
nmap = 0
set_of_lines = collections.deque(maxlen=20)
with open('packet_capture.txt') as f:
    for i, line in enumerate(f):
        set_of_lines.append(line)
        for index in l1:							# xss
            # print(index)
            pattern1 = re.compile(index)
            for match in re.finditer(pattern1, line):
                # print('----------------------------------------------------------------------------')
                print('Possible Cross site scripting attempt on line ',
                      i, ' scripting query')
            # print(i,line)
                set_of_lines.append(match.group())
                print(set_of_lines)
                s = str(set_of_lines)
                with open('xss_detected.txt', 'a+') as x1:
                    x1.write('ALERT_XSS')
                    x1.write(s)
                    x1.write('\n')
                with open('xss_detected.txt', 'r') as r:

                    screen = Tk()  # to initialize a screen
                    screen.geometry("500x500")
                    # specific_line=21
                    # r.seek(3,0)
                    # print(r.tell())
                    # data_1=r.read()
                    # print(data_1)
                   # data=r.readlines()
                    # yo=data[specific_line-1]

                    label = Label(
                        screen, text="cross site scripting attack detected", height=300)
            # this creates a new label to the GUI
                    label.pack()

                    screen.mainloop()
                    print(
                        '----------------------------------------------------------------------------')
        for index in l2:								# sql injection
            pattern2 = re.compile(index)
            for match in re.finditer(pattern2, line):
                print(
                    '----------------------------------------------------------------------------')
                print('sql injection on line ', i)
            # print(i,line)
                set_of_lines.append(match.group())
                print(set_of_lines)
                s = str(set_of_lines)
                with open('sql_detected', 'a+') as sq1:
                    sq1.write('ALERT_SQLi')
                    sq1.write(s)
                    sq1.write('\n')
                with open('sql_detected', 'r') as r:
                    screen = Tk()  # to initialize a screen
                    screen.geometry("500x500")
                    label = Label(
                        screen, text="Sql injection attack detected", height=300)
            # this creates a new label to the GUI
                    label.pack()

                    screen.mainloop()
                    print(
                        '----------------------------------------------------------------------------')
# port scanning

        if 'Flags [FS]' in line:
            nmap = nmap+1
            # print(nmap)

        if nmap == 1:
            print(line)
    if (nmap > 5):
        print('recon')

# dos using xerxes
        c = 0
        if 'length 1: HTTP' in line:
            c = c+1

        # print(c)
    if (c > 1000):
        print(line)
        print('dos is detected')

# dos using hping
        for index in l3:
            pattern3 = re.compile(index)
            q = re.findall(pattern3, line)
            # print(q)
            if len(q) != 0:
                print('dos with hping')
                break

print("end_of_execution")
end = time.time()
print(end - start)
