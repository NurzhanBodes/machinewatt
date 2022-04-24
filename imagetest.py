import imageio
import numpy as np
import csv
import pandas as pd


img1 = imageio.imread('landslide0.png')
y = list(img1.ravel())
z  = [y[n:n+3] for n in range(0, len(y), 3)]
mean=[0]*len(z)
"""for i in range(len(z)):
    mean[i]=np.mean(z[i])"""
#print(z)

a = np.array(z)

with open('myfile.csv', 'w', newline='') as file:
    mywriter = csv.writer(file, delimiter=',')
    mywriter.writerows(a)



df = pd.read_csv("myfile.csv", header=None)

df.to_csv("myfile.csv", header=["Red", "Green", "Blue"], index=False)
df["landslide"]=0
df.to_csv("myfile.csv",index=False)

img2 = imageio.imread('landslide1.png')
y2 = list(img2.ravel())
z2  = [y[n:n+3] for n in range(0, len(y2), 3)]


a2 = np.array(z2)

with open('myfile.csv', 'w', newline='') as file:
    mywriter = csv.writer(file, delimiter=',')
    mywriter.writerows(a2)



