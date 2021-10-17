# while True:
#     proceeds = input('введите сумму выручки фирмы: ')
#     if proceeds.isdigit():
#         proceeds = int(proceeds)
#         break
#
# while True:
#     costs = input('введите сумму издержек фирмы: ')
#     if costs.isdigit():
#         costs = int(costs)
#         break

proceeds = int('1000')
costs = int('800')

result = proceeds - costs

if result >= 0:
    print(f'выручка фирмы за текущий период составляет {result}.')
else:
    loss = result * -1
    print(f'убыток фирмы за текущий период составляет {loss}.')

if result > 0:
    profitability = result / proceeds
    print(f'рентабельность выручки составляет {profitability:.2f}')
    # while True:
    #     persons = input('введите количество сотрудников фирмы: ')
    #     if persons.isdigit() and int(persons) > 0:
    #         persons = int(persons)
    #         break
    persons = 5
    proceeds_for_person = result / persons
    print(f'прибыль фирмы в расчете на одного сотрудника составляет {proceeds_for_person:.2f}.')
