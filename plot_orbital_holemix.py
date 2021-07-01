import matplotlib.pyplot as plt
import numpy as np
def plotter():
    Anzahl_Zustaende = 13
    plot_farben_symbole=['ko', 'ro', 'go', 'bo', 'mo', 'yo', 'ko', 'ro', 'go', 'bo', 'mo', 'yo', 'co']
    for x in range(0,4):
        for n in range(1,19):
            Energy_File= open('C:\\Users\\Jonas\\Desktop\\Ergebnisse\\Mode'+str(n)+'_dat\\Mode'+str(n)+'_orbitale'+str(x+1)+'.csv')
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
                plt.title('Hole-mixing along normal mode '+str(n)+' for state '+str(x+1))
                plt.plot(x_werte, y_werte[i], plot_farben_symbole[i])
                axes = plt.gca()
                axes.set_ylim([0, 1])
                plt.ylabel('Hole-mixing weights')
                plt.xlabel('q')
            plt.savefig('C:\\Users\\Jonas\\Desktop\\Ergebnisse\\Mode'+str(n)+'_dat\\Mode'+str(n)+'_orb'+str(x+1)+'.png', transparent=True, dpi=450)
            plt.clf()
print(plotter())