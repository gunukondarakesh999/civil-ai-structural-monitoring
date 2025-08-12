import pandas as pd 
data ={
    "Day":[1,2,3,4,5,6,7],
    "Sensor_A":[0.5,0.3,0.25,0.28,0.35,0.4,0.25],
    "Sensor_B":[0.5,0.3,0.25,0.28,0.35,0.4,0.25],
    "Sensor_C":[0.5,0.3,0.25,0.28,0.35,0.4,0.25]
}
df =pd.DataFrame(data)
print(df)
print(df.mean(numeric_only=True))
print(df.max(numeric_only=True))
print(df.min(numeric_only=True))


limit = 0.3 
dangerous = df[(df["Sensor_A"]>limit) | (df["Sensor_B"] >limit)| (df["Sensor_C"]>limit)]
print(dangerous)
dangerous = df[(df["Sensor_A"] > limit) | (df["Sensor_B"] > limit) | (df["Sensor_C"] > limit)]
print("\nDays with dangerous cracks:\n", dangerous)

df.to_excel("crack.xlsx",index=False)
