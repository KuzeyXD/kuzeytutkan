# As you are approaching the main entrance of the markets, 
# one hawker in particular convinces you to purchase some lottery tickets 
# for a draw that is just about to start. 
# You stay to watch the draw on his TV with interest 
# as the numbers are called. You decide you want to calculate your winnings
# immediately so you can spend the proceeds while souvenir shopping!

# The winnings work like this:
# A ticket with 3 of the winning numbers wins $1,
# A ticket with 4 of the winning numbers wins $10,
# A ticket with 5 of the winning numbers wins $100, and
# A ticket with 6 of the winning numbers wins $1000.


array = [[46, 46, 5, 87, 92, 73],[95, 73, 30, 12, 97, 27],
[34, 49, 42, 41, 58, 16],[33, 5, 91, 60, 40, 88],[74, 52, 63, 74, 19, 31],
[13, 31, 13, 6, 68, 4],[57, 36, 41, 17, 40, 15],[29, 59, 20, 85, 73, 42],
[31, 67, 82, 51, 44, 80],[48, 41, 55, 12, 15, 30]] #For testing

win = [12, 48, 30, 95, 15, 55, 97] #The winning numbers
dollar=0
for i in range(len(array)): #Repeating for every ticket
    result=0
    for j in range(len(array[i])):
        if array[i][j] in win: #If the number is a winning number
            result+=1
    
    if result == 3: #Calculating how much we won from a ticket
        dollar += 1
    elif result == 4:
        dollar += 10
    elif result == 5:
        dollar += 100
    elif result == 6:
        dollar += 1000
    elif result == 7:
        dollar += 10000

print(dollar)
