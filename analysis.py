import pandas as pd
import os
import numpy as np
import seaborn as sns
from scipy import stats
from matplotlib import pylab as plt
from statsmodels.graphics.gofplots import qqplot
from IPython.core.interactiveshell import InteractiveShell

def truc_quan_hoa_tuong_quan(data):
    numeric_data = data.select_dtypes(include=[np.number])
    sns.set_style("whitegrid")
    fig = plt.figure(dpi=100, figsize=(14, 8))
    sns.heatmap(numeric_data.corr(), annot=True, cmap="Blues")
    plt.title("COP (Customer, Order, Product) Data Correlation", weight="bold", fontsize=30, fontname="fantasy", pad=10)
    plt.xticks(weight="bold", fontsize=15, rotation=45, ha="right")
    plt.yticks(weight="bold", fontsize=15, rotation=360, ha="right")
    plt.show()

def phan_tich_don_bien(data, color, title1, title2):    
    fig, (ax1, ax2) = plt.subplots(
        ncols=2,
        nrows=1,
        figsize=(20, 6)
    )

    sns.distplot(
        data,
        ax=ax1,
        kde=True,
        color=color
    )
    
    ax1.set_title(
        title1, 
        weight="bold",
        fontname="monospace",
        fontsize=15,
        pad=10
    )
    
    qqplot(
        data,
        ax=ax2,
        line='s'
    )
    
    ax2.set_title(
        title2, 
        weight="bold",
        fontname="monospace",
        fontsize=15,
        pad=10
    )

    range_from = round(data.mean() - 2 * data.std())
    range_to = round(data.mean() + 2 * data.std())
    plt.suptitle(f"Giá trị {data.name} nằm trong khoang {range_from} - {range_to}", weight="bold",
        fontname="monospace",
        fontsize=20)

    plt.show()