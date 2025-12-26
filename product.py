def product_details(prod_id, name, quantity, price):
    result = (
        f"product ID:{prod_id}\n"
        f"product Name:{name}\n"
        f"Quantity:{quantity}\n"
        f"Price:{price}\n"
    )
    return result


if __name__ == "__main__":
    print(product_details(107, "iphone", 2, 70000))
