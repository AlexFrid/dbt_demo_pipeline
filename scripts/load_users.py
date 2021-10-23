import pandas as pd
import snowflake.connector as snow
from snowflake.connector.pandas_tools import write_pandas


# Get the data in a pandas dataframe
file_path = '../dbt/data/users_extract.csv'

df = pd.read_csv(file_path, sep = ",")

# Rename the columns in the dataframe to match the table definition in snowflake
df.rename(columns={
    "id": "ID",
    "postcode": "POSTCODE"
    }, inplace=True)

# Open a connection to snowflake, would be put in environment variables if running in production / not a demo exercise
connection = snow.connect(user="AFRIDRIKSSON",
    password="Datastorydesign#1",
    account="checkoutdatatechtests.eu-west-1",
    warehouse="DEMO_WH",
    database="AFRIDRIKSSON",
    schema="DEV")

# Write the dataframe to snowflake
write_pandas(connection, df, "USERS_EXTRACT")

# Close snowflake connection
connection.close()