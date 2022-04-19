per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
your_input = input('Введите сумму: ')
money = float(your_input)
for i in per_cent:
    deposit.append(money * per_cent[i] / 100)
    print(i, "Проценты по депозитам =", deposit[-1])
print("Максимальный депозит =", max(deposit))
