import csv
import time
import pprint


def choose_data():
    dataset = ""
    solution_txt = ""
    dataset_choice = ""
    while not dataset_choice.isdigit() or not 0 <= int(dataset_choice) <= 2:
        dataset_choice = input("Choose the dataset: 0, 1 or 2 ? ")
    if dataset_choice == "0":
        dataset = "dataset0.csv"
        solution_txt = "solution_dataset0.txt"
    elif dataset_choice == "1":
        dataset = "dataset1.csv"
        solution_txt = "solution_dataset1.txt"
    elif dataset_choice == "2":
        dataset = "dataset2.csv"
        solution_txt = "solution_dataset2.txt"

    return dataset, solution_txt


user_choice = choose_data()
data_to_analyse = user_choice[0]
solution_file = user_choice[1]


wallet = 50000
# stocks_list = [("action-1", 2, 0.5), ("action-2", 3, 0.1), ("action-3", 5, 1.3), ("action-4", 4, 0.9),
#                ("action-5", 1, 0.3)]
stocks_list = []

# reads csv file and creates list of stocks
with open(data_to_analyse, "r") as data_file:
    data = csv.reader(data_file)
    for row in data:
        if not row[1].isalpha():
            cost = int(float(row[1])*100)
            stocks_list.extend([(row[0], cost, round((cost * float(row[2])) / 100, 2))])


def max_profit(moneymax, stocks):
    # crée un tableau à double entrées (lignes: actions et colonnes: moneymax) initialisé à 0
    matrice = [[0 for x in range(moneymax + 1)] for x in range(len(stocks) + 1)]

    for i in range(1, len(stocks) + 1):  # iteration actions (lignes)
        for w in range(1, moneymax + 1):  # w --> iteration pour chaque colonne (portefeuille: 0, 1, 2, ..., 500)
            # vérifie le cout de l'action
            if w >= stocks[i - 1][1] > 0:
                # inscrit dans la matrice le max entre valeur totale case ligne precedente et val action + val case
                matrice[i][w] = max(stocks[i - 1][2] + matrice[i - 1][w - stocks[i - 1][1]], matrice[i - 1][w])
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
        # si la valeur de la case = à la valeur de l'action +
        # (valeur case ligne précedente / colonne actuelle - le cout de l'action) alors on ajoute l'action à la liste
        if matrice[n][m] == matrice[n-1][m-s[1]] + s[2] and s[1] != 0:
            stocks_selection.append(s)
            m -= s[1]

        n -= 1

    return matrice[-1][-1], stocks_selection


def write_data(profit, stocks, price):
    """Writes stocks bought, cost and profit in text file"""
    with open(solution_file, "w", encoding='utf-8') as file:
        file.write("Actions:\n")
        for i in range(len(stocks)):
            file.write(f"{stocks[i][0]} {stocks[i][1]}\n")
        file.write(f"\nCoût: {price} euros\nBénéfice: {round(profit / 100, 2)} euros")


def show_write_result(profit, stocks, price):
    """Prints result and writes it in a file"""
    print(f"Coût: {price} euros")
    print(f"Bénéfice: {round(profit / 100, 2)} euros")
    print(f"Actions: ")
    for i in stocks:
        pprint.pprint(i)

    write_data(profit, stocks, price)


start = time.time()
print()
print("Processing...")
result = max_profit(wallet, stocks_list)
end = time.time()

print()
print(f"temps exec: {end-start} sec\n")

total_profit = sum(i[2] for i in result[1])
invest = sum(i[1] for i in result[1]) / 100
show_write_result(total_profit, result[1], invest)


