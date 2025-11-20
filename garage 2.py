print('Hrs' ,'fee')#heading
#repitition structure
for hours in range(1,9):
    hours = float(input('Enter how many hours the user park there: '))
    
    #processing
    charge = 5 + 2.5 * hours
    if charge > 10:
        chareg = 10.0
    elif charge > 20:
        charge = 20.0
    print(hours, format(charge, '6.2f'))