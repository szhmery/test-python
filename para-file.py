# coding=utf8

file="./rtt-file/rtt-2.out"
result_file="./rtt-file/rtt-2.txt"
fp = open(file,'r+')
fp2 = open(result_file,'r+')
string =''
try:

    for line in fp.read().splitlines():
        print(line)
        string = string + line[1:11] +'\n'
finally:
     fp2.write(string)
     print(string)
     fp.close()
     fp2.close()