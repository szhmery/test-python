import random

string=''
for i in range(1,11):
    for num in range(0,222):
        value = random.uniform(0.02,0.06)
        string = string+str(value)[0:8]+"000\n"
        print(string)
    filename = "rtt-file/disable-dps-rtt-"+str(i)+".out"
    fp = open(filename,"w")
    fp.write(string)
    fp.write("END")
    fp.close()
    string=''

string=''
for i in range(1,11):
    for num in range(0,222):
        value = random.uniform(0.02,0.06)
        string = string+str(value)[0:8]+"000\n"
        print(string)
    filename = "rtt-file/en-dps-rtt-"+str(i)+".out"
    fp = open(filename,"w")
    fp.write(string)
    fp.write("END")
    fp.close()
    string=''