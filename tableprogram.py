#this program display table values
import sys
print("welcome") 

maxtable = sys.argv[1]
print(maxtable)
for i in list(range(1,int(maxtable))):
    for j in list(range(1,11)):
        k=i*j;
        print(k, end = ' ')
    print()