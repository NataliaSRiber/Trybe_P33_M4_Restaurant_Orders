from collections import Counter


class TrackOrders:
    # aqui deve expor a quantidade de estoque
    # requisito 2.1
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    # requisito 2.2
    def add_new_order(self, customer, order, day):
        new_order = [customer, order, day]
        self.data.append(new_order)

    # requisito 2.3
    def get_most_ordered_dish_per_customer(self, customer):
        all_orders = []
        for order in self.data:
            if order[0] == customer:
                all_orders.append(order[1])
        most_ordered = Counter(all_orders).most_common(1)[0][0]
        return most_ordered

    # requisito 2.4
    def get_never_ordered_per_customer(self, customer):
        all_dishes_types = set()
        customer_dishes = set()
        for order in self.data:
            all_dishes_types.add(order[1])
            if order[0] == customer:
                customer_dishes.add(order[1])
        return all_dishes_types.difference(customer_dishes)

    # requisito 2.5
    def get_days_never_visited_per_customer(self, customer):
        all_open_days = set()
        customer_eat_out_days = set()
        for order in self.data:
            all_open_days.add(order[2])
            if order[0] == customer:
                customer_eat_out_days.add(order[2])
        return all_open_days.difference(customer_eat_out_days)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
