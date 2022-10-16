salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
a = 0
need_money = 0  # количество денег, чтобы прожить 10 месяцев
while True:
    months -= 1
    a = spend - salary
    need_money += a
    spend = spend + spend * increase
    if months == 0:
        break
# TODO Оформить решение

print(round(need_money))
