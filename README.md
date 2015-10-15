You are reading the README.md file in the nhis_exploratory repository 
for Russ Robbins on GitHub.

Currently this directory contains the 2014 National Health Interview Survey
data as well as a program I am finishing writing. This program in turn
writes parser programs for the following files:

1. familyxx.dat
2. fmlydisb.dat
3. funcdisb.dat, 
4. househld.dat
5. INCMIMP.dat (which contains the compilation of INCMIP1 through 5.dat)
6. injpoiep.dat
7. paradata.dat
8. personsx.dat
9. samadult.dat
10. samchild.dat. 
 
The output of any parser that is built by the program is a CSV file.

There are subdirectories for each of the types of *.dat files.

TODO:

1. Add command line functionality/arguments.
2. Identify number of lines in *.dat file and use.
3. Use try/except/else/finally for more exception handling.
4. Perform unit testing.
5. Document how to use the program.
6. Document requirements for element_names and element positions files.


