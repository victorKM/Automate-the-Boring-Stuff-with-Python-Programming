print('How many cats do you have?')
numCats = input()
try: 
    if int(numCats) >= 4:
        print('That is a lot of cats.')
    else:
        print('That is not that many cats.')
except ValueError:
    print('You did not enter a number.')

#The problem here is that the user can put not only number
#so put the except ValueErro to avoid an erro message