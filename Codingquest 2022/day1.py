# Your supervisor has granted your request for shore leave once you complete a couple of important safety checks on the ship. 
# The first is an engine diagnostics report.
# The FTL (faster than light) engines are tricky and complicated technology, 
# however like most engine systems, the most important reading to monitor 
# is engine temperature. The normal safe operating temperature for 
# the engine is within 1500 and 1600 degrees Kelvin.
# Your task is to check the temperature log files for the previous day
# and determine how many seconds the 60 second rolling average
# was either less than 1500 or greater than 1600 degrees. 
# The log file records the temperature once per second.

# To clarify: The 60 second rolling average requirement is 
# referring to calculating an average for each block of 60 seconds. 
# For instance, you would start with timestamps 0 to 59, then 1 to 60, 
# then 2 to 61, then 3 to 62, and so forth; until you have found the average 
# for every 60 second block in the dataset.

testfile=open("puzzledata.txt", "r") #Opening the file 
words=testfile.read().splitlines() #Placing all the words into an array

length = len(words) 

initial=0
result=0

while initial != length-60: #Until the last 60 elements in the dataset
    sum=0 # Resetting the sum at every travsersal
    for i in range(initial, initial+60): # start-end indexes.
        sum+= int(words[i]) 

    initial+=1
    average=sum/60 #Finding the average

    if average < 1500 or average > 1600: #Comparison
        result+=1

print(result)