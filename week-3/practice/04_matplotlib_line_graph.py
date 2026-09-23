import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]
temperatures = [30, 32, 31, 35, 34, 33, 36]

plt.plot(days, temperatures, marker="o")

plt.title("Temperature During the Week")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.xticks(days)
plt.grid(True)

plt.show()
