import re
import collections
import time
start = time.time()


l1, l2, l3 = [], [], []
dos_c = 0


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
        #print('INSIDE edge')

        for index in l1:							# xss
            # print(index)
            pattern1 = re.compile(index)
            for match in re.finditer(pattern1, line):
                print(
                    '----------------------------------------------------------------------------')
                print('Possible Cross site scripting attempt on line ',
                      i, ' scripting query')
                # print(i,line)
                set_of_lines.append(match.group())
                print(set_of_lines)
                s = str(set_of_lines)
                with open('xss_detected', 'a+') as x1:
                    x1.write('ALERT_XSS')
                    x1.write(s)
                    x1.write('\n')
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
                    print(
                        '----------------------------------------------------------------------------')


# dos using hping
        for index in l3:
            pattern3 = re.compile(index)
            q = re.findall(pattern3, line)
            # print(q)
            if len(q) != 0:
                print('dos with hping')
                break


# dos using xerxes AND
# port scanning

        #print('about to enter in dos')
        if 'length 1: HTTP' in line:
            #print('inside dos chutiya')
            dos_c = dos_c+1

        if 'Flags [FS]' in line:
            nmap = nmap+1
            # print(nmap)

        if nmap == 1:
            print(line)

    if (dos_c > 400):
        print(line)
        print('DOS is detected')
        print('-------------------------------------------------------------------')

    if (nmap > 5):
        print('recon')
        print('--------------------------------------------------------------------')


print("end_of_execution")
end = time.time()
print(end - start)
