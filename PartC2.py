# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 12:44:27 2025

@author: Harley
"""
import numpy as np
import pandas as pd
data0 = pd.read_excel('C:/Users/Harley/OneDrive/LSE/MACRO/pwt100.xlsx', sheet_name = 'Data', header = 0)
alpha = 0.3
data2 = data0.loc[data0['country'] == "India", ["country", "year", "rgdpna", "emp", "rnna", "hc"]]
data2 = data2.reset_index(drop = True) 
# Y = (K**alpha)*(AL)**(1-alpha) Eq. 1
# Y: real GDP (rgdpna)
# A: TFP 
# L: the number of employed workers (emp)
# K: the capital stock at constant 2017 national prices (rnna)

Y=data2['rgdpna']
data2['TFP (alpha)'] = (data2['rgdpna'] / (data2['rnna']**(alpha) * data2['emp']**(1-alpha)))**(1/(1-alpha))
A=data2['TFP (alpha)']
L=data2['emp']
K=data2['rnna']

print(Y)
gY =np.empty(len(Y)-1)
for n in range(len(Y)-1):
    gY[n]=np.log(Y[n+1]/Y[n])
gA =np.empty(len(A)-1)
for n in range(len(A)-1):
        gA[n]=np.log(A[n+1]/A[n])
gK =np.empty(len(K)-1)
for n in range(len(K)-1):
    gK[n]=np.log(K[n+1]/K[n])
gL =np.empty(len(L)-1)
for n in range(len(L)-1):
    gL[n]=np.log(L[n+1]/L[n])
print(gL)
#def compute_growth_rate(X):
#    gX = np.empty(len(X)-1)
#    for n in range(len(X)-1):
#       gX[n]=np.log(X[n+1]/X[n])

#growth rate= ln(Xt/Xt-
#gY = compute_growth_rate(Y)
#print(gY)
#gA = compute_growth_rate(A)
#gK = compute_growth_rate(K)
#gL = compute_growth_rate(L)

for y1, y2, growth in zip(data2['year'][:-1], data2['year'][1:], gY):
    print(f"\t {y1:.0f}-{y2:.0f} \t {growth:.4f}")
#growth accounting:
contrib_gK = alpha * gK / gY
contrib_gL = (1 - alpha) * gL / gY
contrib_gA = (1 - alpha) * gA / gY
intvls = np.array([f"{y1}-{y2}" for y1, y2 in zip(data2['year'][:-1], data2['year'][1:])])

df_contribs = pd.DataFrame(
    data=np.column_stack((intvls, contrib_gK, contrib_gL, contrib_gA)),
    columns=["year", "K contribution", "L contribution", "A contribution"],
)

df_contribs = df_contribs.astype(
    {
        "year": "object",
        "K contribution": "float64",
        "L contribution": "float64",
        "A contribution": "float64",
    }
)

# Set index
df_contribs = df_contribs.set_index("year")

# Set display options
pd.set_option("display.float_format", "{:.4f}".format)


print("\n\t == year by year contributions ==\n")
print(df_contribs)
print("\n")








print("year \t \t K contrib \t L contrib \t A contrib \t Y growth")
print("------- \t --------- \t --------- \t --------- \t --------")
print(
    f"1950-2019 \t {alpha * np.log(K[69]/K[0]) / np.log(Y[69]/Y[0]):.4f}",
    f"\t {(1-alpha) * np.log(L[69]/L[0]) / np.log(Y[69]/Y[0]):.4f}",
    f"\t {(1-alpha) * np.log(A[69]/A[0]) / np.log(Y[69]/Y[0]):.4f}",
    f"\t {np.log(Y[69] / Y[0]):.4f}",)

