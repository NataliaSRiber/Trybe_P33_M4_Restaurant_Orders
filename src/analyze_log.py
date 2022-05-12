import csv
from collections import Counter


def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            file_reader = csv.reader(file, delimiter=",")
            data = list(file_reader)
            return data
    except FileNotFoundError:
        if not file_path.endswith("csv"):
            raise FileNotFoundError(f"Extensão inválida: '{file_path}'")
        raise FileNotFoundError(f"Arquivo inexistente: '{file_path}'")


# requisito 1.1
def most_ordered_dish(customer, data):
    all_orders = []
    for order in data:
        if order[0] == customer:
            all_orders.append(order[1])
    most_ordered = Counter(all_orders).most_common(1)[0][0]
    return most_ordered


# requisito 1.2
def had_ordered_hamburguer(customer, data):
    all_orders = []
    for order in data:
        if order[0] == customer and order[1] == "hamburguer":
            all_orders.append(order[1])
    most_ordered = len(all_orders)
    return most_ordered


# requisito 1.3
def never_ordered_dishes(customer, data):
    all_dishes_types = set()
    customer_dishes = set()
    for order in data:
        all_dishes_types.add(order[1])
        if order[0] == customer:
            customer_dishes.add(order[1])
    return all_dishes_types.difference(customer_dishes)


# requisito 1.4
def days_customer_not_eat_out(customer, data):
    all_open_days = set()
    customer_eat_out_days = set()
    for order in data:
        all_open_days.add(order[2])
        if order[0] == customer:
            customer_eat_out_days.add(order[2])
    return all_open_days.difference(customer_eat_out_days)


def analyze_log(path_to_file):
    data = read_file(path_to_file)
    result_1 = most_ordered_dish("maria", data)
    result_2 = had_ordered_hamburguer("arnaldo", data)
    result_3 = never_ordered_dishes("joao", data)
    result_4 = days_customer_not_eat_out("joao", data)
    with open("data/mkt_campaign.txt", "w") as file:
        file.write(f"{result_1}\n")
        file.write(f"{result_2}\n")
        file.write(f"{result_3}\n")
        file.write(f"{result_4}\n")
    file.close()
