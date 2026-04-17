import pandas

sales = {
    "Bananas" : 12,
    "Apples": 14,
    "Oranges": 18
}

df = pandas.DataFrame(sales, index=["weight"])

print(df)