# Uses National Data on the relative frequency of given names in the population of U.S. births,
# stored in a directory "names", in files named "yobxxxx.txt with xxxx being the year of birth.
#
# Prompts the user for a first name, and finds out the first year
# when this name was most popular in terms of frequency of names being given,
# as a female name and as a male name.
#
# Written by *** and Eric Martin for COMP9021


import os
import sys
from collections import defaultdict

first_name = input('Enter a first name: ')
directory = 'names'
min_male_frequency = 0
male_first_year = None
min_female_frequency = 0
female_first_year = None

counts_by_mnames = []
counts_by_fnames = []
years_by_mnames= []
years_by_fnames=[]
year_ftotal={}
year_mtotal={}
feyear=[]
mayear=[]
dict1={}
dict2={}
for filename in os.listdir(directory):
    if not filename.endswith('.txt'):
         continue
    year = int(filename[3:7])
    with open(directory + '/' + filename) as data_file:
        ftotal = 0
        mtotal = 0
        for line in data_file:
            name, gender, count = line.split(',')
            if gender=='M':
                mtotal+=int(count)
            else:
                ftotal+=int(count)
            if name==first_name and gender == 'M':
                #counts_by_mnames.append([year,count])
                dict1[year]=count
                mayear.append(year)
            if name == first_name and gender == 'F':
                #counts_by_fnames.append([year,count])
                dict2[year]=count
                feyear.append(year)
        year_ftotal[year]=ftotal
        year_mtotal[year] = mtotal
temp=0
if dict1!={}:
    for i in mayear:
       temp=int(dict1[i])/year_mtotal[i]*100
       counts_by_mnames.append((i,temp))
       temp = 0
    years_by_mnames=sorted(counts_by_mnames, key=lambda x: x[1], reverse=True)
    min_male_frequency=years_by_mnames[0][1]
    male_first_year=years_by_mnames[0][0]
print(min_male_frequency,male_first_year)
if dict2!={}:
    for i in feyear:
        temp=int(dict2[i])/year_ftotal[i]*100
        counts_by_fnames.append((i,temp))
        temp = 0
    years_by_fnames=sorted(counts_by_fnames, key=lambda x: x[1], reverse=True)
    min_female_frequency=years_by_fnames[0][1]
    female_first_year=years_by_fnames[0][0]

if not female_first_year:
    print(f'In all years, {first_name} was never given as a female name.')
else:
    print(f'In terms of frequency, {first_name} was the most popular '
          f'as a female name first in the year {female_first_year}.\n'
          f'  It then accounted for {min_female_frequency:.2f}% of all female names.'
         )
if not male_first_year:
    print(f'In all years, {first_name} was never given as a male name.')
else:
    print(f'In terms of frequency, {first_name} was the most popular '
          f'as a male name first in the year {male_first_year}.\n'
          f'  It then accounted for {min_male_frequency:.2f}% of all male names.'
         )
