import matplotlib.pylot as plt

years = [1950,
         1995,1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000,
         2005, 2010,2015]

pops = [2.5, 2.7, 3, 3.3, 3.6,
        4, 4.4, 4.8, 5.3, 5.7, 6.1, 6.5, 6.9, 7.3]
death = [1.2, 1.7, 1.8, 2.2, 2.5,
         2.7, 2.9, 3, 3.1, 3.3, 3.5, 3.8, 4.0, 4.3]
'''
plt.plot(years, pops,'---', color=(255/255, 100/255, 100/255))
plt.plot(years, death, color=(.6, .6, .1))
'''
lines = plt.plot(years, pops, years, death)
plt.grid(True)

plt.setp(lines, color=(1,.4,.4), marker='o')

plt.ylabel("Population in Billions")
plt.xlabel("Population growth by Year")
plt.title("Population Growth")
plt.show()