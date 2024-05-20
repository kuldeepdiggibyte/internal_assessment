data = [
    ("John", "Apple", 10),
    ("Alice", "Apple", 20),
    ("John", "Banana", 12),
    ("Alice", "Banana", 14),
    ("Mike", "Apple", 15),
    ("Mike", "Banana", 17)
]
schema = ["salesperson","product","quantity"]
df = spark.createDataFrame(data, schema=schema)
df = df.groupBy("product").pivot("salesperson").sum("quantity")
df = df.orderBy("product")
df.display()