# Databricks notebook source
# MAGIC %md
# MAGIC Hello World!

# COMMAND ----------

#Databricks notebook source
df = spark.read.format("csv") \
    .option("inferSchema","true") \
    .option("header", "true") \
    .option("sep",",") \
    .load("/FileStore/tables/ind.csv")

display(df)
