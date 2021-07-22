import csv
import time
import pprint

wallet = 500

# stock_list = [("action-1", 20, 6.5), ("action-2", 22, 12.6), ("action-3", 15, 7.0), ("action-4", 17, 5.0)]
stocks_list = []
stocks_selection_list = []

# reads csv file and creates list of stocks
with open("stocks.csv", "r") as data_file:
    data = csv.reader(data_file)
    for row in data:
        if row[1].isdigit():
            stocks_list.extend([(row[0], int(row[1]), (int(row[2]) * int(row[1])) / 100)])


def max_profit(moneymax, stocks_to_check, stocks_selection=None):
    if not stocks_selection:
        stocks_selection = []

    # s'il reste des actions dans la liste,
    if stocks_to_check:
        # 1) on n'ajoute pas l'action en privant la liste de la première action
        profit_and_stocks_1, total_invest_1 = max_profit(moneymax, stocks_to_check[1:], stocks_selection)

        # on prend la première action de la liste
        stock = stocks_to_check[0]

        #  2) si le cout de l'action < au porte-monnaie, on ajoute l'action
        if stock[1] <= moneymax:
            profit_and_stocks_2, total_invest_2 = max_profit(moneymax - stock[1], stocks_to_check[1:],
                                                             stocks_selection + [stock])

            # On garde le bénéfice le plus important
            if profit_and_stocks_1[0] < profit_and_stocks_2[0]:
                return profit_and_stocks_2, total_invest_2

        return profit_and_stocks_1, total_invest_1

    # s'il n'y a plus d'acion, la récursivité s'arrete : CAS DE BASE
    else:
        # la fonction renvoie (profit_and_stocks):
        #   1) la somme des benefs (profit) des actions selectionnees
        #   2) la liste des actions selectionnées
        profit = round(sum([i[2] for i in stocks_selection]), 2)
        profit_and_stocks = profit, stocks_selection

        # et l'investissement total (total invest)
        # calcul du cout d'achat total des actions
        total_invest = sum([i[1] for i in stocks_selection])

        return profit_and_stocks, total_invest


def display_result(stocks, invest, profit):
    print()
    print(f"Coût : {invest} euros")
    print(f"profit: {profit} euros")
    print(f"Actions : (nom, coût, bénéfice)")
    for stock in stocks:
        pprint.pprint(stock)


start = time.process_time()
result_brutef = max_profit(wallet, stocks_list)
end = time.process_time()
print(f"{end - start} s")

display_result(result_brutef[0][1], result_brutef[1], result_brutef[0][0])
