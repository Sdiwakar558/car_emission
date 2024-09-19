


class DataPreprocessing:
    def __init__(self,raw_dataframe):
        self.raw_dataframe = raw_dataframe

    def preprocessing(self):
        print(self.raw_dataframe)



    def encode_data(self):
        self.raw_dataframe.iloc[:,1:]
