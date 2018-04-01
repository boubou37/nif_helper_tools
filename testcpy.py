import os,re,shutil, sys


f = open(sys.argv[1], 'r')
original = open('original.obj', 'r').readlines()

for file in f.read().splitlines():
    filenameparts = os.path.splitext(file)[0].split('_')
    fout = open(file,'w')
    fout.writelines('o ' + filenameparts[len(filenameparts) - 1] + '\n')
    fout.writelines(original[9:])
    print(filenameparts[len(filenameparts) - 1])

os.system('TriCreator ' + sys.argv[1])
