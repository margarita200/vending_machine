def insert(money, new):
    hand5 = money // 500
    hand2 = money % 500 // 200
    hand1 = (money - hand5 * 500 - hand2 * 200) // 100
    print(f"Inserted cash: {new}")
    print(f"Your credit is 500 x {hand5}; 200 x {hand2}; 100 x {hand1}; 50 x {money % 100 // 50}; coins {money % 50}")
    return money


def print_matrix(matrix):
    for row in range(len(matrix)):
        print('| ', end='')
        for column in range(len(matrix[row])):
            print(f"{matrix[row][column]:9}", end='')
        print(' |')
    return matrix


def can_buy(money, products):
    i = 1
    available_products = []
    while i < len(products):
        if products[i][2] <= money and products[i][3] > 0:
            available_products.append(products[i])
        i += 1
    available_products.insert(0, ["number", "name", "price", "quantity"])
    print_matrix(available_products)
    return available_products


def bought_products(prod, i, bought, change):
    chosen_products = prod[i]
    bought_goods = bought
    bought_goods.append(chosen_products)
    prod[i][3] -= 1
    spent_money = chosen_products[2]
    print("You've bought")
    print_matrix(bought_goods)
    credit = change - spent_money
    hand5 = credit // 500
    hand2 = credit % 500 // 200
    hand1 = (credit - hand5 * 500 - hand2 * 200) // 100
    print(f"Your credit is 500 x {hand5}; 200 x {hand2}; 100 x {hand1}; 50 x {credit % 100 // 50}; coins {credit % 50}")
    return bought_goods, prod


def get_change(money, option, quantity):
    coins = [0, 0, 0, 0]
    c10 = int(quantity[0])
    c5 = int(quantity[1])
    c2 = int(quantity[2])
    count = True
    if money > c10 * 10 + c5 * 5 + c2 * 2 + int(quantity[3]):
        print("Error")
        count = False
    while count and 0 < money <= c10 * 10 + c5 * 5 + c2 * 2 + int(quantity[3]) and quantity[0] > 0:
        money -= 10
        coins[0] += 1
        quantity[0] -= 1
    while 0 < money <= c5 * 5 + c2 * 2 + int(quantity[3]) and quantity[1] > 0:
        coins[1] += 1
        money -= 5
        quantity[1] -= 1
    while 0 < money <= c2 * 2 + int(quantity[3]) and quantity[2] > 0:
        coins[2] += 1
        money -= 2
        quantity[2] -= 1
    while money % 2 <= int(quantity[3]) and quantity[3] > 0 and money > 0:
        coins[3] += 1
        money -= 1
        quantity[3] -= 1
    if money == 0:
        if option == "YES":
            if coins[0] == coins[1] == coins[2] == coins[3] == 0:
                print("You've spent all money:(((")
            else:
                print(f"Your change is 10 x {coins[0]}; 5 x {coins[1]}; 2 x {coins[2]}; 1 x {coins[3]}")
            print("Enjoy your meal!")
        if option != "YES":
            k = 0
            while k < len(quantity):
                quantity[k] += coins[k]
                k += 1
    return quantity, count
