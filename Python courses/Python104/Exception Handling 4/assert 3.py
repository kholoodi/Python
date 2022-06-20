# assert keyword التأكيد
# assert if the condition does not work write the assert then the condition we want to achieve
try:
    num = int(input('Plase Enter the number: '))
    assert num % 2 == 0 # num must be even number if not do except code

except:
    print('Not even number')
else:
    evennumber = num / 2
    print(evennumber)