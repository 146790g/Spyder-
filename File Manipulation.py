# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 14:04:54 2019

@author: 146790
"""


import os
path="D:\Python"
files=os.listdir(path)

import glob

print(glob.glob('D:/Python/file sousa/*'))

import os
os.chdir('D:/Python')
os.rename('./file sousa/a.docx', './file sousa/a_000.docx')

print('{0:03d}, {1:04d},{2:05d}'.format(4, 6,9))


# 

import os
import glob

files = glob.glob('D:/Python/dir/*')

for f in files:
    print(os.path.basename(f))
    
for f in files:
    print(os.path.join(path, 'img_' + os.path.basename(f)))
    

for f in files:
    os.rename(f, os.path.join(path, 'img_' + os.path.basename(f)))


os.getcwd()
dirpath_without_sep = './dir/d.docx'

print(os.path.splitext(dirpath_without_sep))

type(os.path.splitext(dirpath_without_sep))

import os
os.getcwd()
path = 'dir/f.docx'

f = open(path)

print(type(f))
# <class '_io.TextIOWrapper'>

with open(path) as f:
    s = f.read()
    print(type(s))
    print(s)
    

f.close()


path_w = 'dir/test_w.txt'

s = 'New file'

with open(path_w, mode='w') as f:
    f.write(s)

with open(path_w) as f:
    print(f.read())
    
with open(path_w, mode='a') as f:
    f.write('\nFour')


with open(path_w) as f:
    print(f.read())
    
    
path = 'dir/test_w.txt'


with open(path) as f:
    lines = f.readlines()

print(lines)
# ['XXX YYY ZZZ\n', 'YYY\n', 'aaa\n', 'XXX\n', 'ZZZ XXX\n', 'xxx']

print(type(lines))

lines_strip = [line.strip() for line in lines]
print(lines_strip)

l_XXX_start = [line for line in lines_strip if line.startswith('XXX')]
print(l_XXX_start)

