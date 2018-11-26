import os
import sys
from collections import defaultdict
directory_name='name'
years_by_names= defaultdict(list)
for filename in os.listdir(directory_name):
     if not filename.endswith('.txt'):
         continue
     year=int(filename[3:7])
     #opening 1 file for reading purposes
     #and 2 files for writing purposes
     with open(directory_name + '/' + filename) as data_file:
      #processing each line in file that i am reading
         for line in data_file:
          #Extracting the 3 fields from line
              name, gender, count=line.split(',')
              if gender == 'M':
                  break
              years_by_names[name].append(year)
     for gap,starting_year,name in sorted([(years_by_names[first_name][i+1]-years_by_names[first_name][i],
                                       #years_by_names[first_name][i],
                                       #first_name)
                                        #for first_name in years_by_names
                                        # for i in range(len(years_by_names[first_name])-1)],
                                         #reverse=True)[:10]:


       	print(f'{name} was given in {starting_year},and then {gap} years later') 