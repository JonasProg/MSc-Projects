import matplotlib.pyplot as plt
import numpy as np
def plotter():
    Anzahl_Zustaende = 4
    plot_farben_symbole=['ko', 'rs', 'g^', 'bD']
    for n in range(1,19):
        Energy_File= open('C:\\Users\\Jonas\\Desktop\\Ergebnisse\\Mode'+str(n)+'_dat\\Mode'+str(n)+'_Energien.csv')
        x_werte = []
        y_werte=[]
        for i in range(0,Anzahl_Zustaende):
            y_werte.append([])
        for zeile in Energy_File:
            zeile=zeile.replace('\n', '')
            zeile=zeile.replace(',', '.')
            zeilen_liste= zeile.split(";")
            x_werte.append(float(zeilen_liste[0]))
            for i in range(0,Anzahl_Zustaende):
                y_werte[i].append(float(zeilen_liste[i+1]))
        for i in range(0, Anzahl_Zustaende):
            plt.title('Propynamide along normal mode '+str(n))
            plt.plot(x_werte, y_werte[i], plot_farben_symbole[i])
            plt.ylabel('Energy [eV]')
            plt.xlabel('q')
        plt.savefig('C:\\Users\\Jonas\\Desktop\\Ergebnisse\\Mode'+str(n)+'_dat\\Mode'+str(n)+'_plot.png', transparent=True, dpi=450)
        plt.clf()
print(plotter())