# Output:
# List of participants who participated daily
# List of participants who participated only once
# List of participants who participated on the first day and never participated again.

from functools import reduce
l = [
    ['Sam', 'Emma', 'Joan', 'Krish', 'John', 'Desmond', 'Tom', 'Nicole' ],
    ['Brad', 'Walter', 'Sam', 'Krish','Desmond', 'Jennifer'],
    ['Tom', 'Krish', 'Emma', 'Mia', 'Nicole', 'Sam', 'Desmond'],
    ['Desmond', 'Sam', 'Krish', 'Mia', 'Harry'],
    ['Ron', 'Ginny', 'Ted', 'Krish', 'Mia', 'Sam', 'Sachin', 'Desmond', 'Kapil'],
    ['Krish', 'Brad', 'Walter', 'Jennifer','Desmond', 'Harry', 'Nicole', 'Sam']
    ]
ar = l
rslt = list(reduce(set.intersection, [set(item) for item in l ]))
print(rslt)
st = []
count = 0
for li in l:
    for x in li:
        st.append(x)
#print(st)        
reslt2 = []   
my_dict = {i:st.count(i) for i in st}
for key, value in my_dict.items():
   if value==1:
       reslt2.append(key)
print(reslt2)


l1 = l[0]
l3= set()
l.pop(0)
for v in l1:
    for i in l:
        l3.update(i)
l1 = set(l1)
l1.difference_update(l3)
print( l1)

    

