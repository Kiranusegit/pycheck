# MAGIC # Databricks Notebook: Connecting to Database, Transforming Data, and Writing to Target
# MAGIC This notebook demonstrates how to:
# MAGIC 1. Connect to a database (PostgreSQL in this example)
# MAGIC 2. Perform data transformations
# MAGIC 3. Write the transformed data to a target (another database or file system)

# COMMAND ----------

# Step 1: Set up database connection properties

jdbc_url = "jdbc:postgresql://<hostname>:<port>/<database>"
properties = {
    "user": "<your_username>",
    "password": "<your_password>",
    "driver": "org.postgresql.Driver"
}

# Step 2: Load data from a table in the database
query = "(SELECT * FROM your_table) AS your_query"
df = spark.read.jdbc(url=jdbc_url, table=query, properties=properties)

# Display the first few rows to confirm connection
df.show(5)

# COMMAND ----------

# Step 3: Data Transformation
# Example: Filter rows and add a new column based on a condition

df_transformed = df.filter(df['column_name'] > 100) \
                   .withColumn('new_column', df['column_name'] * 2) \
                   .select('column_name', 'new_column', 'another_column')

# Show the transformed data
df_transformed.show(5)

# COMMAND ----------

# Step 4: Writing transformed data to another table in the database
# Target database connection properties

target_jdbc_url = "jdbc:postgresql://<hostname>:<port>/<target_database>"
target_properties = {
    "user": "<your_username>",
    "password": "<your_password>",
    "driver": "org.postgresql.Driver"
}

# Write data to a new table in the target database
df_transformed.write.jdbc(url=target_jdbc_url, table="target_table", mode="overwrite", properties=target_properties)

# COMMAND ----------

# OR Write to DBFS (Databricks File System) as Parquet

output_path = "/mnt/data/transformed_data.parquet"
df_transformed.write.parquet(output_path, mode="overwrite")

# Show file path for confirmation
print(f"Data written to {output_path}")