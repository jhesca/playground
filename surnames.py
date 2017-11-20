import re
from collections import Counter
file=open('familytree.ged', encoding='UTF8')
names=[]
for line in file:
    if "NAME" in line:
        if not "Page" in line:
            if not "Footnote" in line and not "Bibliography" in line:
                if re.search(r"/*/", line):
                    names.append(line.split()[-1])
names_clean=[name.replace("/", "") for name in names]
names_clean=list(filter(len, names_clean))
count=Counter(names_clean)
count=(dict(count))
sorted=[(name, value) for value, name in sorted([(value, name) for name, value in count.items()], reverse=True)]
print("The total count of surnames in your family tree are: \n")
print("More than fifty:")
for name in sorted:
    if name[1]>50:
        print("%s x%s" %(name[0], name[1]))
print("\nTen to fifty:")
for name in sorted:
    if name[1]<=50 and name[1]>9:
        print("%s x%s" %(name[0], name[1]))
print("\nTwo to nine:")
for name in sorted:
    if name[1]<10 and name[1]>1:
        print("%s x%s" %(name[0], name[1]))
print("\nOne:")
for name in sorted:
    if name[1]==1:
        print("%s x%s" %(name[0], name[1]))
        