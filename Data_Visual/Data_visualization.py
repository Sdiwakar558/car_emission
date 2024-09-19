import matplotlib.pyplot as plt
import seaborn as sns
import streamlit


class Data_visual:
    def __init__(self):
        pass
    def data_visual(self,encoaded_data):
        corr_graph = encoaded_data.corr()
        plt.figure(figsize=(10,10))
        sns.heatmap(encoaded_data,annot=True,cmap='coolwarm')
        plt.show()

