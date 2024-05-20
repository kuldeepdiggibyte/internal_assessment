data1 = [(101, "Aravind"), (102, "John"), (103, "Sridevi")]

data2 = [("pyspark", 90, 101), ("sql", 70, 101), ("pyspark", 70, 102), ("sql", 60, 102), ("sql", 30, 103), ("pyspark", 20, 103)]

students_df = spark.createDataFrame(data1, ["student_id", "student_name"])

marks_df = spark.createDataFrame(data2, ["course_name", "marks", "student_id"])

average_marks = marks_df.groupBy("student_id").agg(avg("marks").alias("percentage"))

results_df = average_marks.withColumn("result",

    when(col("percentage") >= 70, "Distinction")

    .when((col("percentage") >= 60) & (col("percentage") < 70), "First Class")

    .when((col("percentage") >= 50) & (col("percentage") < 60), "Second Class")

    .when((col("percentage") >= 40) & (col("percentage") < 50), "Third Class")

    .otherwise("Fail")

)

result_df = results_df.join(students_df, "student_id").select("student_id", "student_name", "percentage", "result")

result_df.show()