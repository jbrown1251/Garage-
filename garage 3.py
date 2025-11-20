#heading
print('hrs' , 'Fee')
startHours = 1.0
incrhours = 1.0
endhours = 6.0

#Repitition
hours =startHours
while hours<=endhours:
    charge = 5 + 2.5 * hours
    if charge > 10:
        chareg = 10.0
    elif charge > 20:
        charge = 20.0
    print(hours, '$' format(charge, '5.2f'))
    Hours += incrHours