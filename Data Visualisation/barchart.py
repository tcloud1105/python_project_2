import matplotlib.pyplot as plt
import numpy as np

col_count = 3
bar_width = .2

korea_scores = (554, 536, 538)
canada_scores = (518, 523, 525)
china_scores = (613, 570,580)
france_scores = (495, 505, 499)

def CreateLabels(data):
    for item in data:
        height = item.get_height()
        plt.text(item.get_x() + item.get_width()/2., height*1.05, '%d'% int(height), ha="center", va="bottom")

index = np.arange(col_count)

k1 = plt.bar(index, korea_scores, bar_width, alpha=.4, label="Korea")
c1 = plt.bar(index + 0.2, canada_scores, bar_width, alpha=.4, label="Canada")
ch1 = plt.bar(index + 0.4, china_scores, bar_width,alpha=.3, label="China")
f1 = plt.bar(index + 0.6, france_scores, bar_width, alpha=.4, label="France")

CreateLabels(k1)
CreateLabels(c1)
CreateLabels(ch1)
CreateLabels(f1)


plt.ylabel("Mean score in PISA 2012")
plt.xlabel("Subjects")
plt.title("Test Score by Country")

plt.xticks(index + .3/2, ("Mathematics", "Reading", "Science"))
plt.legend(edgecolor=None,shadow=None, facecolor=(1, .4, .4), frameon=False, loc=2, bbox_to_anchor=(1,1))
plt.grid(True)

for item in k1:
    print(item.get_height())
    print(item.get_width())
    print(item.get_x())

plt.show()
