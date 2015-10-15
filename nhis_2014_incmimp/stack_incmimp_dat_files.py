import os

os.chdir('/media/robbinsr/a94ffb60-544f-46c2-874c-bab46457fdb6/robbinsr_/' +
         'Projects/p_projects/nhis_exploratory/nhis_2014_incmimp')

with open('nhis_2014_incmimp1.dat', mode='r', encoding='utf8') as f_1:
    with open('nhis_2014_nhis_2014_incmimp.dat', mode='a',
              encoding='utf8') as f_out:
        for line in f_1:
            line = line.strip()
            f_out.write(line + '\n')

with open('nhis_2014_incmimp2.dat', mode='r', encoding='utf8') as f_2:
    with open('nhis_2014_nhis_2014_incmimp.dat', mode='a',
              encoding='utf8') as f_out:
        for line in f_2:
            line = line.strip()
            f_out.write(line + '\n')

with open('nhis_2014_incmimp3.dat', mode='r', encoding='utf8') as f_3:
    with open('nhis_2014_nhis_2014_incmimp.dat', mode='a',
              encoding='utf8') as f_out:
        for line in f_3:
            line = line.strip()
            f_out.write(line + '\n')

with open('nhis_2014_incmimp4.dat', mode='r', encoding='utf8') as f_4:
    with open('nhis_2014_nhis_2014_incmimp.dat', mode='a',
              encoding='utf8') as f_out:
        for line in f_4:
            line = line.strip()
            f_out.write(line + '\n')

with open('nhis_2014_incmimp5.dat', mode='r', encoding='utf8') as f_5:
    with open('nhis_2014_nhis_2014_incmimp.dat', mode='a',
              encoding='utf8') as f_out:
        for line in f_5:
            line = line.strip()
            f_out.write(line + '\n')
