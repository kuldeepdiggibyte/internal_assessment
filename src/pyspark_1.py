data = [("John", "Python, sql"),
        ("Aravind", "Java, SQL, HTML"),
        ("Sridevi", "Python,sql,pyspark")]

from pyspark_4.sql.functions import col, split, explode

d1 = spark.createDataFrame(data, ["name", "skill"])
explode_df = d1.withColumn("skill", explode(split(col("skill"), ",")))

explode_df.display()
