import numpy as np 
import matplotlib.pyplot as plt

# # arr1 = np.array([1,2,3,4,5])
# # # print(arr1)
# # # print(arr1.ndim)

# arr = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
# # # print(arr)
# # # print(arr.ndim)
# # new = arr.reshape(-1)
# # print(new)
# # for i in np.nditer(arr):
# #     print(i)
# for i, x in np.ndenumerate(arr):
#   print(i, x)

# # print(arr1[2])
# # print(arr[0, 1, 1])
# # print(arr.dtype)
# # arr2 =np.array([1,"Apple","Banana"])
# # print(arr2.dtype)

# # arr = np.array([1.2,3.2])
# # arr = arr.astype('i4')
# # print(arr)

# # Copy -will not effect the original one
# # arr =np.array([1,2,3])
# # arr2 =arr.copy()
# # arr2[2] =5 
# # print(arr)
# # print(arr2)



# # View -will  effect the original one

# # arr =np.array([1,2,3])
# # arr2 =arr.view()
# # arr2[2] =5 
# # print(arr)
# # print(arr2)


# # arr = np.array([1,2,3,4,5],ndmin=4)
# # print(arr.shape)


# # arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# # print(arr.reshape(4,3))

# # arr = np.array([[1,2,3,4],[5,6,7,8]])
# # new = arr.reshape(-1)
# # print(new)


# ............


# Simulated strain readings (microstrain) for 7 days from 3 sensors

data = np.array([[150,152,155],
                [150,152,154],
                [152,160,153],
                [162, 168, 164],
                [165, 170, 166],
                [170, 172, 169],
                [172, 175, 171]])

# Mean strain per day

daily_avg = np.mean(data ,axis=1)
print(daily_avg)
# Mean strain per sensor

sensor_avg = np.mean(data ,axis =0)
print(sensor_avg)

# Detect readings exceeding 170 microstrain

high_strain = data >170
print(high_strain)

strain_values = data/1_000_000
print(strain_values)

#...........Visualization.............

days = np.arange(1,8)   #7 days will be cvered 1,2,3,4,5,6,7

# Plot readings for each sensor

plt.plot(days, data[:, 0], marker='o', label='Sensor 1')

plt.plot(days ,data[:, 1],marker ='s',label="Sensor 2")

plt.plot(days ,data[:, 2],marker ='^',label="Sensor 3")

# Plot daily average
plt.plot(days, daily_avg, marker ="D",linestyle ="--",color="black",label="Daily Average")
plt.show()

# Highlight points exceeding 170 microstrain
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        if data[i, j] > 170:
            plt.scatter(days[i], data[i, j], color='red', s=100, edgecolor='black', zorder=5)

# Labels and title
plt.xlabel("Day")
plt.ylabel("Strain (µε)")
plt.title("Daily Strain Readings from Sensors")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()