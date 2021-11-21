import sqlite3
import pandas as pd
'''import matplotlib.pyplot as plt
from io import StringIO'''

'''
conn = sqlite3.connect('db.sqlite3', check_same_thread=False)
df=pd.read_sql_query("SELECT * FROM dadosOKatual",conn)

def gerargrafico():
    print(df.groupby('year'))
    return

gerargrafico()
'''
'''def return_graph():

    

    fig = plt.figure()
    
    plt.plot(x,y)

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data
'''