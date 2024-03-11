class Order:
    def __init__(self, product_name, count, price):
        self._product_name = product_name
        self._count = count
        self._price = price

    def get_total_price(self):
        return self._count * self._price


class Customer:
    def new_order(self, product_name, count, price):
        order = Order(product_name, count, price)
        return order


class OrderProcessor:
    def __init__(self, order):
        self._order = order

    def process_order(self):
        total_price = self._order.get_total_price()
        print(f"Загальна ціна замовлення: {total_price}")


customer = Customer()
order1 = customer.new_order("Potato", 5, 10)
order_processor = OrderProcessor(order1)
order_processor.process_order()
