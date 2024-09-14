#MY WAY

total_bill = 135.6

persons = {
    'Markijan': 1/2,
    'Darina': 1/3,
    'Julian': 1/2,
    'Adam': 2/3
}
denom = sum(persons.values())

persons_equalized = persons.copy()
for key in persons_equalized:
    persons_equalized[key] /= denom

to_pay = persons_equalized.copy()

for key in to_pay:
    to_pay[key] *= total_bill

print(sum(to_pay.values()))

print(f'Płatności typu: \n')
for key in to_pay:
    print(key, ':  ', f'{to_pay[key]:0.2f}')


################################
#HIGHWAY

total_bill = 135.6

x = total_bill
persons = {
    'Markijan': x/4,
    'Darina': 17*x/36,
    'Julian': 7*x/12,
    'Adam': x
}
denom = sum(persons.values())

persons_equalized = persons.copy()
for key in persons_equalized:
    persons_equalized[key] /= denom

to_pay = persons_equalized.copy()

for key in to_pay:
    to_pay[key] *= total_bill

print(sum(to_pay.values()))

print(f'Płatności typu: \n')
for key in to_pay:
    print(key, ':  ', f'{to_pay[key]:0.2f}')
