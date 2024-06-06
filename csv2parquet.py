import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

#Use pandas to read the CSV file into a DataFrame.
csv_file_path = "./path/to/file" 
df = pd.read_csv(csv_file_path)

#Convert the DataFrame to a Parquet format using pyarrow

table = pa.Table.from_pandas(df)

#Save the Parquet file.

parquet_file_path = "./path/to/destination/folder"
pq.write_table(table, parquet_file_path)
