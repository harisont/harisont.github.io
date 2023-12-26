import matplotlib.pyplot as plt

langs = ["en", "es", "it", "sv", "da"]
counts = [11, 2, 17, 15, 1]

plt.pie(counts, labels = langs, startangle = 90)
plt.show()