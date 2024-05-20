data = [("Aravind", None, None),

        ("John", None, None),

        (None, "Sridevi", None)]

schema = StructType([

    StructField("Name1", StringType(), True),

    StructField("Name2", StringType(), True),

    StructField("Name3", StringType(), True)])

d2 = spark.createDataFrame(data, schema=schema)

d3 = d2.select(coalesce(col("Name1"), col("Name2"), col("Name3")).alias("Names"))

d3.show()