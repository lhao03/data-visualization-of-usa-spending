import sys
from pyspark.sql import SparkSession
import pandas as pd
from pyspark.sql.types import StructType, StructField, FloatType, StringType, IntegerType
import pyspark.sql.functions as F
from states import states_names, state_codes, get_state_code

# read in the data
filename = "states_spending.xls"
xl_file = pd.read_excel(
    filename,
    sheet_name=[0,1,2,3,4,5,6,7,8,9,10,11,12,13], 
    skiprows=9, 
    skipfooter=5,
    names=["region", "total_total", "inter_governmental", "total", "elementary_and_secondary_edu", "higher_edu", "public_welfare", "health_and_hospitals", "highways", "police", "all_other", "population_thousands"],)

# dict mapping from index to df 
df_pd = xl_file.copy()    

# list of years 
years = list(range(2004, 2018))
years.reverse()

# list of datasts
datasets = list(df_pd.values())
datasets = [df.dropna() for df in datasets]

# dict of year: df
year_df = dict(zip(years,datasets))

# creating schema
schema = StructType([
    StructField("region", StringType(), True),
    StructField("total_total", FloatType(), True),
    StructField("inter_governmental", FloatType(), True),
    StructField("total",FloatType(), True),
    StructField("elementary_and_secondary_edu", FloatType(), True),
    StructField("higher_edu", FloatType(), True),
    StructField("public_welfare", FloatType(), True),
    StructField("health_and_hospitals", FloatType(), True),
    StructField("highways", FloatType(), True),
    StructField("police", FloatType(), True),
    StructField("all_other", FloatType(), True),
    StructField("population_thousands", FloatType(), True),
    StructField("year", IntegerType(), True),
    StructField("status_code", StringType(), True),
])

# func to add year col to each dataset then concat them togehter 
def concat_df(year_df):
    # add year col to each df
    for year, df in year_df.items():
        df["year"] = [year for num in range(0,len(df))]
        df['status_code'] = df.apply(get_state_code, axis=1)
    
    # convert to spark df 
    df = year_df.values()
    
     # # creating SparkSession instance 
    spark = SparkSession.builder.getOrCreate()

    df_sp = [spark.createDataFrame(df_pd, schema=schema) for df_pd in df]

    # concat to each other  
    drop_list = ['total_total', 'inter_governmental']
    final_df = df_sp[0].select([col for col in df_sp[0].columns if col not in drop_list])

    for df_raw in df_sp[1:-1]:
        final_df = final_df.union(df_raw.select([col for col in df_sp[0].columns if col not in drop_list]))

    final_df = final_df.filter("region != 'District of Columbia'").collect()
    final_df_pd = pd.DataFrame(final_df)
    final_df_pd.to_csv('2004-2017_usa_spending.csv')
    return final_df

final_sp_df = concat_df(year_df=year_df)
