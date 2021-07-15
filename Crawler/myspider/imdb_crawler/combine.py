"""combine movie details"""

# filenames
file1 = 'Details1.txt'
file2 = 'Details2.txt'

# open file
f1 = open(file1)
f2 = open(file2)
fo = open('Details.txt', 'a+')

# insert movies
movies = set()
# map name and year to movie details
name2detail = {}

# insert movie names from file1
for line in f1:
    name = line.split('|')[0] + line.split('|')[1]
    name2detail[name] = line
    movies.add(name)

# insert movie names from file2
for line in f2:
    name = line.split('|')[0] + line.split('|')[1]
    name2detail[name] = line
    movies.add(name)

# write file
for name in movies:
    fo.write(name2detail[name])

# close
f1.close()
f2.close()
fo.close()
