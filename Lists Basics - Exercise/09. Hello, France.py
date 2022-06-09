list_of_items = input().split('|')
budget = float(input())
ticket = 150
bought_items = []
total_profit = 0
new_budget = 0
for item in list_of_items:
    item_kind = item.split('->')
    type_of_item = item_kind[0]
    price_of_item = float(item_kind[1])
    if type_of_item == 'Clothes' and price_of_item <= 50.00 and budget >= price_of_item:
        budget -= price_of_item
        new_price = price_of_item * 1.4
        profit = new_price - price_of_item
        total_profit += profit
        new_budget += new_price
        new_price = f'{price_of_item * 1.4:.2f}'
        bought_items.append(new_price)
    elif type_of_item == 'Shoes' and price_of_item <= 35.00 and budget >= price_of_item:
        budget -= price_of_item
        new_price = price_of_item * 1.4
        profit = new_price - price_of_item
        total_profit += profit
        new_budget += new_price
        new_price = f'{price_of_item * 1.4:.2f}'
        bought_items.append(new_price)
    elif type_of_item == 'Accessories' and price_of_item <= 20.50 and budget >= price_of_item:
        budget -= price_of_item
        new_price = price_of_item * 1.4
        profit = new_price - price_of_item
        total_profit += profit
        new_budget += new_price
        new_price = f'{price_of_item * 1.4:.2f}'
        bought_items.append(new_price)
print(' '.join(bought_items))
print(f'Profit: {total_profit:.2f}')
if (new_budget + budget) >= ticket:
    print('Hello, France!')
else:
    print('Not enough money.')