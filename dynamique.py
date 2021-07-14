import csv
import time
import pprint

wallet = 10
stocks_list = [("action-1", 2, 0.5), ("action-2", 3, 0.1), ("action-3", 5, 1.3), ("action-4", 4, 0.9),
               ("action-5", 1, 0.3)]
# stocks_list = []
#
# # reads csv file and creates list of stocks
# with open("actions.csv", "r") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         if row[1].isdigit():
#             stocks_list.extend([(row[0], int(row[1]), (int(row[2]) * int(row[1])) / 100)])


def max_profit(moneymax, stocks):
    # crée un tableau à double entrées (lignes: moneymax et colonnes: stocks) initialisé à 0
    matrice = [[0 for x in range(moneymax + 1)] for x in range(len(stocks) + 1)]

    for i in range(1, len(stocks) + 1):
        for w in range(1, moneymax + 1):
            # vérifie le cout de l'action
            if stocks[i-1][1] <= w:
                matrice[i][w] = max(stocks[i-1][2] + matrice[i-1][w-stocks[i-1][1]], matrice[i-1][w])
            else:
                matrice[i][w] = matrice[i-1][w]

    # retrouver les actions selectionnées
    # dernière case de la matrice
    m = moneymax  # index derniere colonne
    n = len(stocks)  # index derniere ligne

    stocks_selection = []

    # on parcourt le tableau en partant de la dernière case
    while m >= 0 and n >= 0:
        s = stocks[n-1]  # dernière action de la liste d'action
        # si la valeur de la case = à la valeur de l'action + valeur case ligne précedente
        # et de la colonne actuelle - le cout de l'action
        if matrice[n][m] == matrice[n-1][m-s[1]] + s[2]:
            stocks_selection.append(s)
            m -= s[1]

        n -= 1

    # print(matrice)
    return matrice[-1][-1], stocks_selection


def show_result(profit, stocks, cost):
    print(f"Coût: {cost} euros")
    print(f"Bénéfice: {round(profit, 2)} euros")
    print(f"Actions: ")
    for i in stocks:
        pprint.pprint(i)


start = time.time()
result = max_profit(wallet, stocks_list)
end = time.time()

print()
print(f"temps exec: {end-start} sec\n")

invest = sum(i[1] for i in result[1])

show_result(result[0], result[1], invest)
