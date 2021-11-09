# Quiz-competition-daily

## Problem: 

Clark is conducting an online Quiz competition daily where daily participation for contestants is optional. 
Clark want to send specific notifications to following group of participants
Participants who participated everyday
Participants who participated only once
Participants who participated on the first day and never participated again.

Help Clark to write functions in python to get the above information.
Input:
List of every day participant list

# Output:
List of participants who participated daily
List of participants who participated only once
List of participants who participated on the first day and never participated again.
# Sample input
[
[‘Sam’, ‘Emma’, ‘Joan’, ‘Krish’, ‘John’, ‘Desmond’, ‘Tom’, ‘Nicole’ ],
[‘Brad’, ‘Walter’, ‘Sam’, ‘Krish’,’Desmond’, ‘Jennifer’],
[‘Tom’, ‘Krish’, ‘Emma’, ‘Mia’, ‘Nicole’, ‘Sam’, ‘Desmond’],
[‘Desmond’, ‘Sam’, ‘Krish’, ‘Mia’, ‘Harry’],
[‘Ron’, ‘Ginny’, ‘Ted’, ‘Krish’, ‘Mia’, ‘Sam’, ‘Sachin’, ‘Desmond’, ‘Kapil’],
[‘Krish’, ‘Brad’, ‘Walter’, ‘Jennifer’,’Desmond’, ‘Harry’, ‘Nicole’, ‘Sam’]
] 

# Sample output
[‘Desmond’, ‘Krish’, ‘Sam’]
[‘Kapil’, ‘Ron’, ‘Ginny’, ‘Ted’, ‘Sachin’, ‘John’, ‘Joan’]
[‘John’, ‘Joan’]

