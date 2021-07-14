import csv
import time


stocks_cost = [20, 22, 15, 17]
stocks_profit = [6.5, 12.6, 7.0, 5.0]
stocks_name = ["a1", "a2", "a3", "a4"]
# stocks_cost = []
# stocks_profit = []
# stocks_name = []

wallet = 60

# stock_list = [("action-1", 20, 6.5), ("action-2", 22, 12.6), ("action-3", 15, 7.0), ("action-4", 17, 5.0)]

# creates list of stocks
# with open("actions.csv", "r") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         if row[1].isdigit():
#             stocks_cost.append(int(row[1]))
#             stocks_profit.append((int(row[2]) * int(row[1])) / 100)
#             stocks_name.append(row[0])

print(stocks_cost)
print(stocks_profit)
stock_index = len(stocks_cost) - 1


# n = index
def max_profit(money, cost, profit, n, stocks_selection=None):
    if stocks_selection is None:
        stocks_selection = []
    if n < 0 or money <= 0:
        profit_max = 0
    # si le cout de la derniere action > money alors on ne l'ajoute pas et on verifie la précédente
    elif cost[n] > money:
        profit_max = max_profit(money, cost, profit, n - 1, stocks_selection)

    else:
        not_added = max_profit(money, cost, profit, n - 1, stocks_selection)
        # print(f"not added: {not_added}")
        added = profit[n] + max_profit(money - cost[n], cost, profit, n - 1, stocks_selection + [stocks_name[n]])
        # print(f"added: {added}, {profit[n]}, {stocks_selection}")
        # stocks_selection.append(stocks_name[n])
        profit_max = max(not_added, added)

    return profit_max


start = time.process_time()
print(max_profit(wallet, stocks_cost, stocks_profit, stock_index))
end = time.process_time()
print(f"Actions: ")
print(f"{end - start} s")
