import pandas as pd



class Encode:
    def __init__(self):
        pass

    def encode_data(self,dataframes):
        dataframes = dataframes.iloc[:,1:]
        for column in dataframes.columns:
            dataframes[column]= dataframes[column].factorize()[0]
        return  dataframes


