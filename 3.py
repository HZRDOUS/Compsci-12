from tabulate import tabulate

data = []

for v in range(0, 40, 5):
    for t in range(-10, 40, 5):
        w = 13.12 + (0.6215*t) - (11.37*(v**0.16)) + (0.3965*t)*(v**0.16)
        print(w)
        data.append([v, t, w])

headers = ["Wind (km/h)", "Temp (°C)", "Wind Chill"]

print(tabulate(data, headers=headers, tablefmt="grid"))