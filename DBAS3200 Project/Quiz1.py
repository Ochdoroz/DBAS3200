def calculate_order_totals(price_list, orders):
    final_total = []

    for order in orders:
        final_order = {}
        grand_total = 0
        item = order.get('items')
        final_order['order_id'] = order.get('order_id')
        for different_items in item:
            if price_list.get(different_items) is not None:
                grand_total += price_list.get(different_items) * item.get(different_items)
        final_order['total'] = grand_total
        final_total.append(final_order)
    return final_total


if __name__ == '__main__':
    price_list = {
        "apple": 0.5,
        "banana": 0.3,
        "cherry": 1.2
    }
    orders = [
        {"order_id": 1, "items": {"apple": 3, "banana": 4}},
        {"order_id": 2, "items": {"cherry": 2, "apple": 1}},
        {"order_id": 3, "items": {"banana": 5}}
    ]
    invoices = calculate_order_totals(price_list, orders)
    print(f'here is your invoices for the first batch {invoices}')
