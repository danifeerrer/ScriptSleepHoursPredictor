from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt

#DOWNLOAD AND PREPARE THE DATA

data_root = "./Sleep_health_and_lifestyle_dataset.csv"
lifesat = pd.read_csv(data_root)

#VISUALIZE THE DATA
lifesat.plot(kind='scatter', grid=True, x="Stress Level", y="Sleep Duration")
plt.axis([4, 10, 3, 9])
plt.show()

lifesat.plot(kind='scatter', grid=True, x="Physical Activity Level", y="Sleep Duration")
plt.axis([20, 100, 4, 9])
plt.show()

lifesat.plot(kind='scatter', grid=True, x="Quality of Sleep", y="Sleep Duration")
plt.axis([5, 10, 4, 9])
plt.show()

#SELECT THE INDEPENDENT VARIABLES THAT HAVE A LINEAR RELATIONSHIP WITH THE DEPENDENT VARIABLE
X = lifesat[["Quality of Sleep", "Physical Activity Level", "Stress Level"]].values
Y = lifesat["Sleep Duration"].values


#SELECT A LINEAR MODEL
model = LinearRegression()

#TRAIN THE MODEL
model.fit(X,Y)   # y =β +β1x1 +β2x2 +......βnxn +e

#MAKE A PREDICTION
stress = int(input("¿Que nivel de estres en una escala del 1-10 crees que tienes? "))
physical_level = int(input("¿Que nivel fisico en una escala del 1-100 crees que tienes? "))
quality_sleep = int(input("¿Que calidad de sueño en una escala del 1-10 crees que tienes? "))
X_new = [[quality_sleep, physical_level, stress]]
print("Tus horas de sueño estimadas son ", model.predict(X_new)[0])