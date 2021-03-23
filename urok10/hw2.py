#full_price = price_of_one * qty * margin * tax



full_price = 2500000
qty = 50
margin = 0.3
tax = 0.12


price_of_one = full_price / (qty * margin * tax)
print(price_of_one)