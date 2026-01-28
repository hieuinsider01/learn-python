- Code thể hiện list comprehension chứa nhiều dictionary, lấy key-value theo điều kiện

````pesticide_stock = [
    {"name": "Anvil 5SC", "stock": 75},
    {"name": "Mancozeb", "stock": 45},
    {"name": "Ridomil Gold", "stock": 102},
    {"name": "Amistar TOP", "stock": 30}
]

high_stock_pesticides = [high_stock["name"]  for high_stock in pesticide_stock if high_stock["stock"] > 50  ]

print(high_stock_pesticides) ```
````
