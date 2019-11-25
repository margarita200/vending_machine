from VM_1 import insert, print_matrix, can_buy, bought_products, get_change

good = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
good[0] = ["number", "name", "price", "quantity"]
good[1] = ["1", "Dr.Korner", 65, 15]
good[2] = ["2", "Oreo", 51, 15]
good[3] = ["3", "Haribo", 72, 15]
good[4] = ["4", "Tuc", 60, 15]
good[5] = ["5", "Snickers", 45, 15]
good[6] = ["6", "M&M's", 40, 15]
good[7] = ["7", "Mars", 40, 15]
good[8] = ["8", "Bounty", 50, 15]
good[9] = ["9", "Bombbar", 150, 15]
good[10] = ["10", "Bite", 150, 15]
good[11] = ["11", "Juice", 37, 15]
good[12] = ["12", "Cola", 70, 15]
good[13] = ["13", "Sprite", 70, 15]
good[14] = ["14", "Water", 50, 15]
good[15] = ["15", "Red Bull", 100, 15]
quantity_of_coins = [400, 400, 400, 400]

change = 0
check = [["number", "name", "price", "quantity"]]
length = len(good)
length2 = len(quantity_of_coins)
point1 = False

while True:
    sup = change
    if sup == 0:
        p = 1
        number = 0
        while p < length:
            number += good[p][3]
            p += 1
        if number == 0:
            print("The service is required")
            point1 = True
            sup = 1
        q = 0
        num = 0
        d = quantity_of_coins[0] * 10 + quantity_of_coins[1] * 5 + quantity_of_coins[2] * 2 + quantity_of_coins[3]
        while q < length2:
            num += quantity_of_coins[q]
            q += 1
        if num == 0 or d < 100:
            print("The service is required")
            point1 = True
            sup = 1
    menu = input("\n (1)insert a banknote\n (2)select a product\n (3)get a change\n Select option by number: ")
    if menu == '1' and not point1:
        cash = int(input("Insert a banknote: "))
        nom = cash == 50 or cash == 100 or cash == 200 or cash == 500
        if nom:
            pre_change = change + cash
            k = 1
            while k < len(good):
                if good[k][3] != 0:
                    credit = pre_change - good[k][2]
                    quantity_of_coins, count = get_change(credit, "", quantity_of_coins)
                    if count:
                        change = pre_change
                        insert(change, cash)
                        break
                k += 1
        elif not nom:
            print("Error")
    elif menu == '2' and not point1:
        stock = can_buy(change, good)
        customer_choice = str(input("Select a product by number: "))
        if int(customer_choice) in range(len(good)):
            n = 0
            while n < len(stock):
                if customer_choice == stock[n][0]:
                    pre_bought = change - stock[n][2]
                    quantity_of_coins, count = get_change(pre_bought, "", quantity_of_coins)
                    if count:
                        bought_products(stock, n, check, change)
                        change -= stock[n][2]
                n += 1
    elif menu == '3' and not point1:
        print("You've bought:")
        print_matrix(check)
        quantity_of_coins, h = get_change(change, 'YES', quantity_of_coins)
        change = 0
    if point1:
        if menu == 'srvop17':
            k = 1
            while k < length:
                good[k][3] = 15
                k += 1
            k = 0
            while k < length2:
                quantity_of_coins[k] = 400
                k += 1
            check = [["number", "name", "price", "quantity"]]
            print("All products' and coins' quantities are maximum!")
            point1 = False
            change = 0
            a = input("Please, press any key: ")
            if a != ' ':
                continue
