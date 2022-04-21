# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from datetime import datetime
from datetime import timedelta
url = "C:/Users/usuario/Downloads/ford.xlsx"
ford = pd.read_excel(url,  sheet_name="sin", header=3)
ford.drop(ford.columns[[9,10,11,12,13]], axis=1)

now = datetime.now()
test_date = ford['Fecha Venta']
#parsed_test = datetime.strptime(test_date['Fecha Venta'], '%Y-%m-%d')
ford['date'] = pd.to_datetime(ford['Fecha Venta'], format='%Y-%m-%d')

def operacion_six(df):
    nowtime = 4
    factor = 6
    factor2 = 12
    if df[1]<factor:
        return (factor - df[1] + nowtime )
    elif df[1] > factor:
        return (factor2 - df[1]) + nowtime
    else:
        return nowtime

def operacion_nine(df):
    nowtime = 4
    factor = 9
    factor2 = 12
    if df[1]<factor:
        return (factor - df[1] + nowtime )
    elif df[1] > factor:
        return (factor2 - df[1]) + nowtime
    else:
        return nowtime

def filter_date(df,dg):
    factor = 2019
    if df < factor:
        return "es de 6 meses"
    else:
        return "es de 9 meses"

ford = ford.assign(
elapsed_months=((12*(now.year - ford["date"].map(lambda x: x.year))) 
+(now.month - ford["date"].map(lambda x: x.month))))

ford = ford.assign(exactime=(ford["elapsed_months"].map(lambda x: divmod(x,12))))
#ford = ford.assign(appointment=ford["exactime"].apply(operacion_six))
#ford = ford.assign(tempo=ford["date"].apply(filter_date(ford["date"], ford["exactime"])))
nowtime =  now.month
factorsix = 6
factornine = 9
factor2 = 12 
nueva = []
for date, em in zip(ford["date"],ford["elapsed_months"]):
    if date.year < 2019:
        if em < factorsix:
            resta = em - factorsix
            nueva.append(resta + nowtime)
        elif em==factorsix:
            nueva.append(nowtime)
        else:
            mod = em % factorsix
            nueva.append((factorsix-mod) + nowtime)
    else:
        if em < factornine:
            resta = factornine - em
            nueva.append(resta + nowtime)
        elif em % factornine == 0:
            nueva.append(nowtime)
        else:
            mod = em % factornine
            nueva.append((factornine-mod) + nowtime)
            
ford["nueva"] = nueva