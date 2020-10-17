import matplotlib.pylot as plt
inport pandas as pd

raw_data={'name': ['Nick','Cedric','Jules', 'Donald'],
          'jan_ir': [124, 112, 110, 180],
          'feb_ir': [122, 132, 144, 98],
          'march_ir': [65, 88, 12, 32]}

df = pd.DataFrame(raw_data, columns=['name','jan_ir', 'feb_ir', 'march_ir'])

df['total_ir'] = df['jan_ir'] + df['feb_ir'] + df['march_ir']

color = [(1, .4, .4), (1, .6, 1), (.5, .3, 1), (.3, 1, .5)]

plt.pie(df['total_ir'], labels=df['names'], colors=color, autopct='%1.1f%%')
plt.show()

print(df)