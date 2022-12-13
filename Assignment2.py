# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 13:03:16 2022

@author: Aswathi
"""

#importing requiredpackages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def read_file(file_name):
    """
        This function takes name of the file and reads the file and loads it into a dataframe.
        Then transposes the dataframe and returns both the first and transposed dataframes
    """

    df = pd.read_csv(file_name)
    df_transpose = pd.DataFrame.transpose(df)
    return(df, df_transpose)

#Reads the files
df_Forest_total,df_forest_countries = read_file("Forest_Area.csv")
