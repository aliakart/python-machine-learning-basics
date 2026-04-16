import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score


def main():
    train_df = pd.read_csv('data3_train.csv', header=None)
    test_df = pd.read_csv('data3_test.csv', header=None)

    # kolumny 0-3 to cechy, kolumna 4 to etykieta
    cechy_train_pelne = train_df.iloc[:, :4].values
    etykiety_train = train_df.iloc[:, 4].values
    cechy_test_pelne = test_df.iloc[:, :4].values
    etykiety_test = test_df.iloc[:, 4].values

    nazwy = ['setosa', 'versicolor', 'virginica']

    def analiza(indeks_cech, tytul):
        print(f"\n--- {tytul} ---")
        cechy_train = cechy_train_pelne[:, indeks_cech]
        cechy_test = cechy_test_pelne[:, indeks_cech]

        # normalizacja danych
        # fitujemy scaler na zbiorze treningowym, transformujemy oba
        scaler = StandardScaler()
        cechy_train_znormalizowane = scaler.fit_transform(cechy_train)
        cechy_test_znormalizowane = scaler.transform(cechy_test)

        dokladnosci = []
        najlepsze_k = -1
        max_dokladnosc = -1.0
        najlepsza_predykcja = None
        k_wartosci = range(1, 13)
        for k in k_wartosci:
            knn = KNeighborsClassifier(n_neighbors=k)
            knn.fit(cechy_train_znormalizowane, etykiety_train)
            etykiety_predykcja = knn.predict(cechy_test_znormalizowane)

            dokladnosc = accuracy_score(etykiety_test, etykiety_predykcja)
            dokladnosci.append(dokladnosc)

            # szukanie najlepszego k (jeśli remis, zostaje mniejsze - bo > a nie >=)
            if dokladnosc > max_dokladnosc:
                max_dokladnosc = dokladnosc
                najlepsze_k = k
                najlepsza_predykcja = etykiety_predykcja

        plt.figure(figsize=(12, 8))
        plt.bar(k_wartosci, dokladnosci, color='green', edgecolor='black')
        plt.title(f'Dokładność klasyfikacji \n({tytul})', fontsize=22, pad=10)
        plt.xlabel('Wartość k', fontsize=20, labelpad=10)
        plt.ylabel('Dokładność', fontsize=20, labelpad=10)
        plt.tick_params(axis='x', labelsize=14)
        plt.tick_params(axis='y', labelsize=14)
        plt.xticks(k_wartosci)
        plt.ylim(0,1.1)
        plt.grid(axis='y', linestyle='--', alpha=0.5)
        plt.savefig(f'dokladnosc_{tytul}')
        plt.show()

        #macierz pomylek
        macierz_pomylek = confusion_matrix(etykiety_test, najlepsza_predykcja)

        df = pd.DataFrame(macierz_pomylek, index=[['Faktyczna klasa']*3, nazwy], columns=[['Wynik rozpoznania']*3, nazwy])
        print(df)

    # wszystkie indeksy: 0, 1, 2, 3
    analiza([0, 1, 2, 3], "Przestrzeń 4-wymiarowa")

    # indeksy działek kielicha: 0 (sepal_length), 1 (sepal_width)
    analiza([0, 1], "Przestrzeń 2-wymiarowa (działka kielicha)")

    # indeksy płatków: 2 (petal_length), 3 (petal_width)
    analiza([2, 3], "Przestrzeń 2-wymiarowa (płatek)")

main()