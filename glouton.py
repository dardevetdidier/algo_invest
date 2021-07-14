import csv

stocks_list = []
wallet = 500
stocks_selection = []
# stocks_name_list = []


with open("actions.csv", "r") as csv_file:
    data = csv.reader(csv_file)
    for row in data:
        if row[1].isdigit():
            profit_cost_ratio = float(row[2]) / 100
            stocks_list.extend([(row[0], int(row[1]), profit_cost_ratio)])
            stocks_list.sort(key=lambda x: x[2], reverse=True)


def max_profit_glouton(stocks, moneymax):
    cost = 0
    profit = 0
    for i in range(len(stocks)):
        if int(stocks[i][1]) <= moneymax:
            stocks_selection.append(stocks[i])
            moneymax -= stocks[i][1]
            cost += stocks[i][1]
            profit += stocks[i][2] * stocks[i][1]
            # stocks_name_list.append(stocks[i][0])

    print(stocks_list)
    print()
    print(f"prix d'achat total: {cost} euros")
    print(f"Bénéfice: {round(profit, 2)} euros")
    print(f"actions: {stocks_selection}")


max_profit_glouton(stocks_list, wallet)
