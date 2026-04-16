import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

dane = pd.read_csv("data2.csv", header=None)
sepal_lenght = dane.iloc[:,0].astype(float)
sepal_width = dane.iloc[:,1].astype(float)
petal_lenght = dane.iloc[:,2].astype(float)
petal_width = dane.iloc[:,3].astype(float)
# StandardScaler standaryzuje dane do średniej 0 i odchylenia standardowego 1.
scaler = StandardScaler()
daneZnormalizowane = scaler.fit_transform(dane)

# WCSS zawsze maleje wraz ze wzrostem k, ponieważ klastry stają się mniejsze, a punkty są bliżej swoich centroidów.
# Liczba iteracji potrzebnych do zbieżności jest różna, co jest typowe, ponieważ algorytm zaczyna od losowych punktów i znajduję lokalne minimum.

k_range = range(2, 11)
wyniki_lista = []
for k in k_range:
    kmeans = KMeans(n_clusters=k, init='k-means++', n_init='auto', random_state=42)
    kmeans.fit(daneZnormalizowane)
    iteracje = kmeans.n_iter_
    wcss = kmeans.inertia_ # wcss = inercja
    wyniki_lista.append({"Liczba klastrów": k, "Iteracje": iteracje, "WCSS": wcss})

k_3 = KMeans(n_clusters=3, init='k-means++', n_init='auto', random_state=42)
k_3.fit(daneZnormalizowane)
centroidy = k_3.cluster_centers_
centroidy_oryginalne = scaler.inverse_transform(centroidy)
centroidy_df = pd.DataFrame(centroidy_oryginalne)
centroidy_color = centroidy_df.index.values
df = pd.DataFrame(wyniki_lista)
df['WCSS'] = df['WCSS'].round(2)
print(df)

fig, ax = plt.subplots(figsize=(12, 8))
ax.plot(k_range, df['WCSS'], marker='o')
ax.set_xlabel('Liczba klastrów', fontsize=22, labelpad=10)
ax.set_ylabel('WCSS', fontsize=22, labelpad=10)
ax.set_title('WCSS dla każdej wartości k', fontsize=24, pad=10)
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)
ax.set_xticks(k_range)
ax.set_ylim(0, 230)
ax.set_yticks(np.arange(0, 250, 25))
ax.grid(visible=True, linestyle='-', alpha=0.5, axis='x')
ax.set_axisbelow(True)
plt.savefig('wykres1')
plt.close(fig)

fig2, ax2 = plt.subplots(figsize=(12, 8))
ax2.scatter(sepal_lenght, sepal_width, c=k_3.labels_, cmap='viridis', s=50)
ax2.scatter(centroidy_df.iloc[:, 0], centroidy_df.iloc[:, 1], marker='D', s=200,cmap='viridis', c=centroidy_color, linewidths=1.5, edgecolor='black')
ax2.set_xlabel('Długość działki kielicha (cm)', fontsize=22, labelpad=10)
ax2.set_ylabel('Szerokość działki kielicha (cm)', fontsize=22, labelpad=10)
ax2.tick_params(axis='x', labelsize=20)
ax2.tick_params(axis='y', labelsize=20)
plt.savefig('sl_sw.png')
plt.close(fig2)


fig3, ax3 = plt.subplots(figsize=(12, 8))
ax3.scatter(sepal_lenght, petal_lenght, c=k_3.labels_, cmap='viridis', s=50)
ax3.scatter(centroidy_df.iloc[:, 0], centroidy_df.iloc[:, 2], marker='D', s=200,cmap='viridis', c=centroidy_color, linewidths=1.5, edgecolor='black')
ax3.set_xlabel('Długość działki kielicha (cm)', fontsize=22, labelpad=10)
ax3.set_ylabel('Długość płatka (cm)', fontsize=22, labelpad=10)
ax3.tick_params(axis='x', labelsize=20)
ax3.tick_params(axis='y', labelsize=20)
plt.savefig('sl_pl.png')
plt.close(fig3)

fig4, ax4 = plt.subplots(figsize=(12, 8))
ax4.scatter(sepal_lenght, petal_width, c=k_3.labels_, cmap='viridis', s=50)
ax4.scatter(centroidy_df.iloc[:, 0], centroidy_df.iloc[:, 3], marker='D', s=200,cmap='viridis', c=centroidy_color, linewidths=1.5, edgecolor='black')
ax4.set_xlabel('Długość działki kielicha (cm)', fontsize=22, labelpad=10)
ax4.set_ylabel('Szerokość płatka (cm)', fontsize=22, labelpad=10)
ax4.tick_params(axis='x', labelsize=20)
ax4.tick_params(axis='y', labelsize=20)
plt.savefig('sl_pw.png')
plt.close(fig4)

fig5, ax5 = plt.subplots(figsize=(12, 8))
ax5.scatter(sepal_width, petal_lenght, c=k_3.labels_, cmap='viridis', s=50)
ax5.scatter(centroidy_df.iloc[:, 1], centroidy_df.iloc[:, 2], marker='D', s=200,cmap='viridis', c=centroidy_color, linewidths=1.5, edgecolor='black')
ax5.set_xlabel('Szerokość działki kielicha (cm)', fontsize=22, labelpad=10)
ax5.set_ylabel('Długość płatka (cm)', fontsize=22, labelpad=10)
ax5.tick_params(axis='x', labelsize=20)
ax5.tick_params(axis='y', labelsize=20)
plt.savefig('sw_pl.png')
plt.close(fig5)

fig6, ax6 = plt.subplots(figsize=(12, 8))
ax6.scatter(sepal_width, petal_width, c=k_3.labels_, cmap='viridis', s=50)
ax6.scatter(centroidy_df.iloc[:, 1], centroidy_df.iloc[:, 3], marker='D', s=200,cmap='viridis', c=centroidy_color, linewidths=1.5, edgecolor='black')
ax6.set_xlabel('Szerokość działki kielicha (cm)', fontsize=22, labelpad=10)
ax6.set_ylabel('Szerokość płatka (cm)', fontsize=22, labelpad=10)
ax6.tick_params(axis='x', labelsize=20)
ax6.tick_params(axis='y', labelsize=20)
plt.savefig('sw_pw.png')
plt.close(fig6)

fig7, ax7 = plt.subplots(figsize=(12, 8))
ax7.scatter(petal_lenght, petal_width, c=k_3.labels_, cmap='viridis', s=50)
ax7.scatter(centroidy_df.iloc[:, 2], centroidy_df.iloc[:, 3], marker='D', s=200,cmap='viridis', c=centroidy_color, linewidths=1.5, edgecolor='black')
ax7.set_xlabel('Długość płatka (cm)', fontsize=22, labelpad=10)
ax7.set_ylabel('Szerokość płatka (cm)', fontsize=22, labelpad=10)
ax7.tick_params(axis='x', labelsize=20)
ax7.tick_params(axis='y', labelsize=20)
plt.savefig('pl_pw.png')
plt.close(fig7)