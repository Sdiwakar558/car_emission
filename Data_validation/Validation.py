import os
from idlelib.iomenu import encoding
from operator import index

import pandas as pd
# import pyspark
# from pyspark.python.pyspark.shell import spark
# from pyspark.sql import SparkSession
# from seaborn.external.docscrape import header

class File_validation:
    def __init__(self,cwd):
        self.current_working_directory = cwd
        # self.spark_instance = SparkSession.builder.appName("CSVReader").getOrCreate()
        self.final_dataset = os.path.join(cwd,"Client_merge_dataset")
        self.client_file = os.path.join(self.current_working_directory,"Client_Raw_datasets")



    def validate_file(self):
        dataframes= pd.DataFrame()
        for file in os.listdir(self.client_file):
            file_path = os.path.join(self.client_file,file)
            # file_dataframe = self.spark_instance.read.csv(file_path,header=True,inferSchema=True)
            file_dataframe = pd.read_csv(file_path,delimiter=",",encoding='Latin-1')
            dataframes = pd.concat([dataframes,file_dataframe],ignore_index=True)
        dataframes.to_csv(os.path.join(self.final_dataset,"single_target.csv"))
        return dataframes


        # if dataframes:
        #     merge_dataframe = dataframes[0]
        #     for dataframe in dataframes[1:]:
        #         merge_dataframe = merge_dataframe.union(dataframe)
        #     print(merge_dataframe.show())
        #     # merge_dataframe.show(n=merge_dataframe.count(),truncate=False)
        #     # merge_dataframe.write.csv(".//Data_validation//output.csv",header= True,mode="overwrite")







