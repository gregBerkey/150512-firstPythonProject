__author__ = 'greg.berkey'

globalVar = 'This is global'

def myfunction():
    localVar = 'This is local'
    print('myFunction - localVar:  ' + localVar)
    print('myFunction - globalVar: ' + globalVar)


myfunction()
print()
print('global - globalVar: ' + globalVar)