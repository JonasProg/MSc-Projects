import re
list=[]
with open('C:\\Users\\Jonas\\Documents\\Orca_Computations\\Reader\\cyclopropan_ffopt.txt') as f:
    for line in f:
        if re.match('Total Enthalpy', line):
            list.append(line)
print(list)
