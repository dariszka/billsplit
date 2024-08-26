
total_bill = 100

persons = {
    'm': 1/2,
    'd': 1/3,
    'j': 1/2,
    'a': 2/3
}
denom = sum(persons.values())

persons_equalized = persons.copy()
for key in persons_equalized:
    persons_equalized[key] /= denom

to_pay = persons_equalized.copy()

for key in to_pay:
    to_pay[key] *= total_bill

print(to_pay)

