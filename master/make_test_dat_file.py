import os
from itertools import islice

os.chdir('/media/robbinsr/a94ffb60-544f-46c2-874c-bab46457fdb6/robbinsr_/Projects/p_projects/nhis_exploratory/nhis_2014_samadult')

N = 20

with open('nhis_2014_samadult.dat', mode='r', encoding='utf8') as f_in:
    with open('../test.dat', mode='w', encoding='utf8') as f_out:
        head = list(islice(f_in, N))
        for line in head:
            temp = line.strip()
            f_out.write(temp + '\n')