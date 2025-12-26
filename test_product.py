from products import product_details

def test_products_details():
    expected_output = (
        "product ID:107\n"
        "product Name:iphone\n"
        "Quantity:2\n"
        "Price:70000\n"
    )
    assert product_details(107, "iphone", 2, 70000) == expected_output
