def supermarket():
    products = {}
    
    while True:
        entry = input()
        if entry == "stocked":
            break
        
        name, price, quantity = entry.split()
        price = float(price)
        quantity = int(quantity)
        
        if name in products:
            products[name]['quantity'] += quantity
            products[name]['price'] = price
        else:
            products[name] = {'price': price, 'quantity': quantity}
    
    grand_total = 0
    for name, data in products.items():
        total_price = data['price'] * data['quantity']
        print(f"{name}: ${data['price']:.2f} * {data['quantity']} = ${total_price:.2f}")
        grand_total += total_price
    
    print('-' * 30)
    print(f"Grand Total: ${grand_total:.2f}")

# Example usage
# supermarket()
