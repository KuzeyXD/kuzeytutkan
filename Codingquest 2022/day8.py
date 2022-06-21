#Suppose you have the following information:

#Secret key: SECRET
#Character set: ABCDEFGHIJKLMNOPQRSTUVWXYZ
#Message: WE COME IN PEACE

#To encode the message:
# Look at the first letter of the key, S. This is the 19th character of the character set.

# Look at the first letter of the message, W. Take the W and increase it 19 places through the character set. 
# The first letter of the message, W is therefore converted to P.

# For the next letter of the message, use the next letter of the secret key as well. 
# In this example, the E of the secret key indicates we will move forward 5 places.
# This will mean the E of the message will become J. (F-G-H-I-"J")

# The third character of the message is a space. This is not in the character set,
#  so use it unmodified.

secret = "Roads? Where We're Going, We Don't Need Roads."

cset="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,;:?! '()"

msg = "ftmpH.:lemGubTDmMb'YtfsublbnkKlMmOoKywmmOIpa.,3mNeEbl?(bVtkUy?xtoNtCkAg:;n)OlInqp2rjap6JwiG)9H'jHm: pjok'9njQbtOxusdql'b'VtkrBb5j!aMWGieIjOHfrw,j,ubsbm,xrufoKljGdob8q,APzqI:0fpi:.Jsipk6lueD):!wrwbd?j(LbmODCCz7:vjbANCsqp2ts);Of,?p; lulx,tXGbLmbTflKBbYlCCdle1bnYtGrCl1bnw:PrphBeYFviLoZD.7pb!)nrztr0lCvl8n'tqIHn8"

new_msg = "" #The result starts as an empty string.

secret_index = 0
for i in msg:

    index = cset.index(i) #The index of the character we are looking for.


    if secret_index > len(secret)-1:
        secret_index = 0 #If we exceed the length of our key, we set the index back to zero

    new_msg += cset[index - cset.index(secret[secret_index]) - 1]
    # "cset.index(secret[secret_index])" refers to the index of the current letter of the key in the character set.
    # For example, for the first traversal, we will look at the index of the first letter in the key, "f", in the character set. (The index of "f" is 5 in the character set)
    # We are subtracting the indexes, because we are actually decoding, not encoding.
    secret_index += 1

print(new_msg) #Works!

# Result:
#  Hello! I hope you are enjoying your trip to Ral'Malgor.
#  Don't forget to pick up some souvenirs for the family while you are there.
#  Perhaps send mom a postcard as well? Also make sure to take some great photos! 
#  See you soon!! ... by the way the answer to the question is 'codingquest2022' 
# (without the quotes).