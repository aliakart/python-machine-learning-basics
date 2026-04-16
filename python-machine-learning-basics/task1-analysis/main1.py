import pandas
import matplotlib.pyplot as plt
import numpy as np


dane = pandas.read_csv('data1.csv', header=None)

gatunek = dane.iloc[:,4].astype(int)

liczba = gatunek.count()
setosa = (gatunek == 0).sum()
versicolor = (gatunek == 1).sum()
virginica = (gatunek == 2).sum()

df1 = pandas.DataFrame({
    'Gatunek': ["Setosa","Versicolor","Virginica", "Razem"],
    'Liczebnosc': [setosa, versicolor, virginica, setosa+versicolor+virginica],
    '%': [(setosa / liczba) * 100, (versicolor / liczba) * 100, (virginica / liczba) * 100,((setosa / liczba) * 100+(versicolor / liczba) * 100+(virginica / liczba) * 100)]

    })
print(df1.round(1))

sepal_lenght = dane.iloc[:,0].astype(float)
sepal_width = dane.iloc[:,1].astype(float)
petal_lenght = dane.iloc[:,2].astype(float)
petal_width = dane.iloc[:,3].astype(float)



# pandas .std ma domyślnie ddof = 1,  ddof = 1 to odchylenie standardowe dla proby statystycznej
df2 = pandas.DataFrame({
    'Cecha': ["Długość działki kielicha(cm)","Szerokość działki kielicha(cm)","Długość płatka (cm)","Szerokość płatka (cm)"],
    'Minimum': [sepal_lenght.min(), sepal_width.min(), petal_lenght.min(), petal_width.min()],
    'Śr. arytm.':[sepal_lenght.mean(),sepal_width.mean(),petal_lenght.mean(),petal_width.mean()],
    '(±odch. stand.)':[sepal_lenght.std(),sepal_width.std(),petal_lenght.std(),petal_width.std()],
    'Mediana': [sepal_lenght.median(), sepal_width.median(),petal_lenght.median(), petal_width.median()],
    'Q1': [sepal_lenght.quantile(0.25),sepal_width.quantile(0.25),petal_lenght.quantile(0.25),petal_width.quantile(0.25)],
    'Q3':[sepal_lenght.quantile(0.75),sepal_width.quantile(0.75),petal_lenght.quantile(0.75),petal_width.quantile(0.75)],
    'Maksimum': [sepal_lenght.max(), sepal_width.max(), petal_lenght.max(), petal_width.max()],
    })
print(df2)

fig, ax = plt.subplots(figsize=(10, 6))

ax.set_yticks(np.arange(0, 40, 5))
ax.set_ylim(0, 35)
bins = np.arange(4.0, 8.5, 0.5)
ax.set_xticks(bins)

plt.hist(sepal_lenght, bins=bins, edgecolor='black',color='blue')
ax.set_xlabel('Długość(cm)', fontsize=20, labelpad=10)
ax.set_ylabel('Liczebnosc', fontsize=20, labelpad=10)
plt.title('Długość działki kielicha', fontsize=20, pad=10)
ax.tick_params(axis='both', labelsize=12, pad=5)


ax.grid(True, alpha=0.3, axis='y')
ax.set_axisbelow(True)

plt.show()

fig2, ax2 = plt.subplots(figsize=(10, 6))
setosa_sepal =  sepal_lenght[gatunek == 0]
versicolor_sepal = sepal_lenght[gatunek == 1]
virginica_sepal = sepal_lenght[gatunek == 2]

dane_do_box = [setosa_sepal, versicolor_sepal, virginica_sepal]
labele = ['setosa', 'versicolor', 'virginica']

ax2.boxplot(dane_do_box, tick_labels=labele)
ax2.set_ylabel('Długość (cm)', fontsize=20, labelpad=10)
ax2.set_xlabel('Gatunek', fontsize=20, labelpad=10)
plt.title('Długość działki kielicha', fontsize=20, pad=10)
ax2.tick_params(axis='both', labelsize=12, pad=5)
ax2.grid(True, alpha=0.3, axis='y')
ax2.set_axisbelow(True)

plt.show()

fig3, ax3 = plt.subplots(figsize=(10, 6))

ax3.set_yticks(np.arange(0, 70, 5))
ax3.set_ylim(0, 40)
bins3 = np.arange(1.8, 4.8, 0.2)
ax3.set_xticks(bins3)

plt.hist(sepal_width, bins=bins3, edgecolor='black',color='green')
ax3.set_xlabel('Szerokość(cm)', fontsize=20, labelpad=10)
ax3.set_ylabel('Liczebnosc', fontsize=20, labelpad=10)
plt.title('Szerokość działki kielicha', fontsize=20, pad=10)

ax3.tick_params(axis='both', labelsize=12, pad=5)
ax3.grid(True, alpha=0.3, axis='y')
ax3.set_axisbelow(True)

plt.show()

fig4, ax4 = plt.subplots(figsize=(10, 6))
setosa_sepal_w =  sepal_width[gatunek == 0]
versicolor_sepal_w = sepal_width[gatunek == 1]
virginica_sepal_w = sepal_width[gatunek == 2]

dane_do_box2 = [setosa_sepal_w, versicolor_sepal_w, virginica_sepal_w]
labele2 = ['setosa', 'versicolor', 'virginica']
ax4.boxplot(dane_do_box2, tick_labels=labele2)
ax4.set_ylabel('Szerokość (cm)', fontsize=20, labelpad=10)
ax4.set_xlabel('Gatunek', fontsize=20, labelpad=10)
plt.title('Szerokość działki kielicha', fontsize=20, pad=10)
ax4.grid(True, alpha=0.3, axis='y')

ax4.tick_params(axis='both', labelsize=12, pad=5)
ax4.set_axisbelow(True)

plt.show()

fig5, ax5 = plt.subplots(figsize=(10, 6))

ax5.set_yticks(np.arange(0, 40, 5))
ax5.set_ylim(0, 40)
bins5 = np.arange(0.6, 7.8, 0.4)
ax5.set_xticks(bins5)

plt.hist(petal_lenght, bins=bins5, edgecolor='black',color='red')
ax5.set_xlabel('Długość(cm)', fontsize=20, labelpad=10)
ax5.set_ylabel('Liczebnosc', fontsize=20, labelpad=10)
plt.title('Długość płatka', fontsize=20, pad=10)

ax5.tick_params(axis='both', labelsize=12, pad=5)
ax5.grid(True, alpha=0.3, axis='y')
ax5.set_axisbelow(True)

plt.show()

fig6, ax6 = plt.subplots(figsize=(10, 6))
setosa_petal =  petal_lenght[gatunek == 0]
versicolor_petal = petal_lenght[gatunek == 1]
virginica_petal = petal_lenght[gatunek == 2]

dane_do_box3 = [setosa_petal, versicolor_petal, virginica_petal]
labele3 = ['setosa', 'versicolor', 'virginica']
ax6.boxplot(dane_do_box3, tick_labels=labele3)
ax6.set_ylabel('Długość (cm)', fontsize=20, labelpad=10)
ax6.set_xlabel('Gatunek', fontsize=20, labelpad=10)
plt.title('Długość płatka', fontsize=20, pad=10)
ax6.grid(True, alpha=0.3, axis='y')

ax6.tick_params(axis='both', labelsize=12, pad=5)
ax6.set_axisbelow(True)

plt.show()

fig7, ax7 = plt.subplots(figsize=(10, 6))

ax7.set_yticks(np.arange(0, 50, 5))
ax7.set_ylim(0, 50)
bins7 = np.arange(0, 2.9, 0.2)
ax7.set_xticks(bins7)
ax7.set_xlim(0, 2.9)

plt.hist(petal_width, bins=bins7, edgecolor='black',color='purple')
ax7.set_xlabel('Szerokość(cm)', fontsize=20, labelpad=10)
ax7.set_ylabel('Liczebnosc', fontsize=20, labelpad=10)
plt.title('Szerokość płatka', fontsize=20, pad=10)

ax7.tick_params(axis='both', labelsize=12, pad=5)
ax7.grid(True, alpha=0.3, axis='y')
ax7.set_axisbelow(True)

plt.show()

fig8, ax8 = plt.subplots(figsize=(10, 6))
setosa_petal_w =  petal_width[gatunek == 0]
versicolor_petal_w = petal_width[gatunek == 1]
virginica_petal_w = petal_width[gatunek == 2]

dane_do_box4 = [setosa_petal_w, versicolor_petal_w, virginica_petal_w]
labele4 = ['setosa', 'versicolor', 'virginica']
ax8.boxplot(dane_do_box4, tick_labels=labele4)
ax8.set_ylabel('Szerokość (cm)', fontsize=20, labelpad=10)
ax8.set_xlabel('Gatunek', fontsize=20, labelpad=10)
plt.title('Szerokość płatka', fontsize=20, pad=10)
ax8.grid(True, alpha=0.3, axis='y')

ax8.tick_params(axis='both', labelsize=12, pad=5)
ax8.set_axisbelow(True)

plt.show()

fig9, ax9 = plt.subplots(figsize=(10, 6))
cr1 = np.corrcoef(sepal_lenght, sepal_width)[0, 1]
a1, b1 = np.polyfit(sepal_lenght, sepal_width, 1)

ax9.scatter(sepal_lenght, sepal_width, color='red')
ax9.plot(sepal_lenght, a1*sepal_lenght+b1, color='blue')
plt.title(f'r = {cr1:.2f}; y = {a1:.1f}x + {b1:.1f}', fontsize=20, pad=10)
ax9.set_ylabel('Szerokość działki kielicha (cm)', fontsize=20, labelpad=10)
ax9.set_xlabel('Długość działki kielicha (cm)', fontsize=20, labelpad=10)
ax9.grid(True, alpha=0.3, axis='y')
ax9.grid(True, alpha=0.3, axis='x')

ax9.tick_params(axis='both', labelsize=12, pad=5)
ax9.set_axisbelow(True)

plt.show()

fig10, ax10 = plt.subplots(figsize=(10, 6))
cr2 = np.corrcoef(sepal_lenght, petal_lenght)[0, 1]
a2, b2 = np.polyfit(sepal_lenght, petal_lenght, 1)

ax10.scatter(sepal_lenght, petal_lenght, color='green')
ax10.plot(sepal_lenght, a2*sepal_lenght+b2, color='blue')
plt.title(f'r = {cr2:.2f}; y = {a2:.1f}x + {b2:.1f}', fontsize=20, pad=10)
ax10.set_ylabel('Długość płatka (cm)', fontsize=20, labelpad=10)
ax10.set_xlabel('Długość działki kielicha (cm)', fontsize=20, labelpad=10)
ax10.grid(True, alpha=0.3, axis='y')
ax10.grid(True, alpha=0.3, axis='x')

ax10.tick_params(axis='both', labelsize=12, pad=5)
ax10.set_axisbelow(True)

plt.show()

fig11, ax11 = plt.subplots(figsize=(10, 6))
cr3 = np.corrcoef(sepal_lenght, petal_width)[0, 1]
a3, b3 = np.polyfit(sepal_lenght, petal_width, 1)

ax11.scatter(sepal_lenght, petal_width, color='brown')
ax11.plot(sepal_lenght, a3*sepal_lenght+b3, color='blue')
plt.title(f'r = {cr3:.2f}; y = {a3:.1f}x + {b3:.1f}', fontsize=20, pad=10)
ax11.set_ylabel('Szerokość płatka (cm)', fontsize=20, labelpad=10)
ax11.set_xlabel('Długość działki kielicha (cm)', fontsize=20, labelpad=10)
ax11.grid(True, alpha=0.3, axis='y')
ax11.grid(True, alpha=0.3, axis='x')

ax11.tick_params(axis='both', labelsize=12, pad=5)
ax11.set_axisbelow(True)

plt.show()

fig12, ax12 = plt.subplots(figsize=(10, 6))
cr4 = np.corrcoef(sepal_width, petal_lenght)[0, 1]
a4, b4 = np.polyfit(sepal_width, petal_lenght, 1)

ax12.scatter(sepal_width, petal_lenght, color='orange')
ax12.plot(sepal_width, a4*sepal_width+b4, color='blue')
plt.title(f'r = {cr4:.2f}; y = {a4:.1f}x + {b4:.1f}', fontsize=20, pad=10)
ax12.set_ylabel('Długość płatka (cm)', fontsize=20, labelpad=10)
ax12.set_xlabel('Szerokość działki kielicha (cm)', fontsize=20, labelpad=10)
ax12.grid(True, alpha=0.3, axis='y')
ax12.grid(True, alpha=0.3, axis='x')

ax12.tick_params(axis='both', labelsize=12, pad=5)
ax12.set_axisbelow(True)

plt.show()

fig13, ax13 = plt.subplots(figsize=(10, 6))
cr5 = np.corrcoef(sepal_width, petal_width)[0, 1]
a5, b5 = np.polyfit(sepal_width, petal_width, 1)

ax13.scatter(sepal_width, petal_width, color='black')
ax13.plot(sepal_width, a5*sepal_width+b5, color='blue')
plt.title(f'r = {cr5:.2f}; y = {a5:.1f}x + {b5:.1f}', fontsize=20, pad=10)
ax13.set_ylabel('Szerokość płatka (cm)', fontsize=20, labelpad=10)
ax13.set_xlabel('Szerokość działki kielicha (cm)', fontsize=20, labelpad=10)
ax13.grid(True, alpha=0.3, axis='y')
ax13.grid(True, alpha=0.3, axis='x')

ax13.tick_params(axis='both', labelsize=12, pad=5)
ax13.set_axisbelow(True)

plt.show()

fig14, ax14 = plt.subplots(figsize=(10, 6))
cr6 = np.corrcoef(petal_lenght, petal_width)[0, 1]
a6, b6 = np.polyfit(petal_lenght, petal_width, 1)

ax14.scatter(petal_lenght, petal_width, color='darkgoldenrod')
ax14.plot(petal_lenght, a6*petal_lenght+b6, color='blue')
plt.title(f'r = {cr6:.2f}; y = {a6:.1f}x + {b6:.1f}', fontsize=20, pad=10)
ax14.set_ylabel('Szerokość płatka (cm)', fontsize=20, labelpad=10)
ax14.set_xlabel('Długość płatka (cm)', fontsize=20, labelpad=10)
ax14.grid(True, alpha=0.3, axis='y')
ax14.grid(True, alpha=0.3, axis='x')

ax14.tick_params(axis='both', labelsize=12, pad=5)
ax14.set_axisbelow(True)

plt.show()