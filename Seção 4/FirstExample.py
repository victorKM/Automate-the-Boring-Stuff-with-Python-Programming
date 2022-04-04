def div42by(divideBy):
    return 42/divideBy

print(div42by(2))
print(div42by(12))
print(div42by(0)) #this will cause an erro, because number/0 dont exist
print(div42by(1))


#To avoid this u can do

def div42byAlternative(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError: #except "name of the error"
        print('Divisao por zero nao pode nao amigo')

print(div42byAlternative(2))
print(div42byAlternative(12))
print(div42byAlternative(0)) 
print(div42byAlternative(1))


