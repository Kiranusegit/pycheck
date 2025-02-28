



jdbc_url = "jdbc:postgresql://<hostname>:<port>/<database>"
properties = {
    "user": "<your_username>",
    "password": "<your_password>",
    "driver": "org.postgresql.Driver"
}

# Step 2: Load data from a table in the database
query = "(SELECT * FROM your_table) AS your_query"
df = spark.read.jdbc(url=jdbc_url, table=query, properties=properties)


df.show(5)



df_transformed = df.filter(df['column_name'] > 100) \
                   .withColumn('new_column', df['column_name'] * 2) \
                   .select('column_name', 'new_column', 'another_column')

# Show the transformed data
df_transformed.show(5)



target_jdbc_url = "jdbc:postgresql://<hostname>:<port>/<target_database>"
target_properties = {
    "user": "<your_username>",
    "password": "<your_password>",
    "driver": "org.postgresql.Driver"
}


df_transformed.write.jdbc(url=target_jdbc_url, table="target_table", mode="overwrite", properties=target_properties)





output_path = "/mnt/data/transformed_data.parquet"
df_transformed.write.parquet(output_path, mode="overwrite")


print(f"Data written to {output_path}")