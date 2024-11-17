def grocery_store(**products):
    products_sorted = sorted(products.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    result = []

    for product, quantity in products_sorted:
        result.append(f"{product}: {quantity}")

    return "\n".join(result)
