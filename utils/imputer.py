import numpy as np
import pandas as pd
from PIL import Image
import plotly.express as px

class Imputer():
    def __init__(self):
        pass 

    def impute(self,df):
        """
        Arguments : 
            df : Pandas Dataframe with Columns [neck,sleeve,pattern].
        Returns :
            df : Imputed Dataset.
        """
        for id in df.index : 
            if np.isnan(df.loc[id,"neck"]) and (np.isnan(df.loc[id,"sleeve_length"])==False) and (np.isnan(df.loc[id,"pattern"])==False):
                vals = df.loc[(df.sleeve_length==df.loc[id,"sleeve_length"]) & (df.pattern==df.loc[id,"pattern"]),"neck"].value_counts()
                vals = vals/np.sum(vals)
                val = vals.max()
                
                if val>0.80 :
                    df.loc[(df.sleeve_length==df.loc[id,"sleeve_length"]) & (df.pattern==df.loc[id,"pattern"]),"neck"] =vals.idxmax()
                    
            if np.isnan(df.loc[id,"sleeve_length"]) and (np.isnan(df.loc[id,"neck"])==False) and (np.isnan(df.loc[id,"pattern"])==False):
                vals = df.loc[(df.neck==df.loc[id,"neck"]) & (df.pattern==df.loc[id,"pattern"]),"sleeve_length"].value_counts()
                vals = vals/np.sum(vals)
                val = vals.max()

                if val>0.80 :
                    df.loc[(df.neck==df.loc[id,"neck"]) & (df.pattern==df.loc[id,"pattern"]),"sleeve_length"] =vals.idxmax()
                    
            if np.isnan(df.loc[id,"pattern"]) and (np.isnan(df.loc[id,"neck"])==False) and (np.isnan(df.loc[id,"sleeve_length"])==False):
                vals = df.loc[(df.neck==df.loc[id,"neck"]) & (df.sleeve_length==df.loc[id,"sleeve_length"]),"pattern"].value_counts()
                vals = vals/np.sum(vals)
                val = vals.max()
                
                if val>0.80 :
                    df.loc[(df.neck==df.loc[id,"neck"]) & (df.sleeve_length==df.loc[id,"sleeve_length"]),"pattern"] =vals.idxmax()

        return df
                    