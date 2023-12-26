import matplotlib.pyplot as plt

langs = ["en", "es", "it", "sv", "da"]
counts = [11, 2, 17, 15, 1]

fig = plt.figure()
plt.pie(counts, labels = langs, startangle = 90, labeldistance=0.82)
fig.savefig('2023.png', transparent=True)