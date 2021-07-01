def rewriter():
    #moden schleife
    for y in range(1,19):
        #q schleife
        for z in range(-6, 7):
            #state schleife
            for a in range(1, 5):
                template= open('C:\\Users\\Jonas\\Desktop\\Ergebnisse\\Database\\pyr_s0_3_000.log') 
                zmatrix= open('C:\\Users\\Jonas\\Documents\\Orca_Computations\\Moden_inputs\\Mode'+str(y)+'_inputs\\'+str(z)+'\\_zmatrix.dat')
                energie= open('C:\\Users\\Jonas\\Desktop\\Ergebnisse\\Mode'+str(y)+'_dat\\Mode'+str(y)+'_Energien.csv')
                liste=template.readlines()
                zmatrix_liste=zmatrix.readlines()[1:-1]
                ausgabe_liste=[]
                energie_liste=energie.readlines()
                for x in range(0, 6):
                    ausgabe_liste.append(liste[x])
                for x in range(0, 8): 
                    zmatrix_zeile=zmatrix_liste[x].split()
                    zeile1= liste[x+6][0:34]+leerzeichen_macher(zmatrix_zeile[0])+leerzeichen_macher(zmatrix_zeile[1])+leerzeichen_macher(zmatrix_zeile[2])+'\n'
                    ausgabe_liste.append(zeile1)
                ausgabe_liste.append(liste[14])
                ausgabe_liste.append(liste[15])
                energie_zeile= energie_liste[-z+6].split()
                energie_zeile[a] = energie_zeile[a].replace(';', '').replace(',', '.')
                energie_zeile[a]= str(float(energie_zeile[a])/27.2113961317875)
                zeile= liste[16][0:22]+energie_zeile[a]+liste[16][36:len(liste[16])]
                ausgabe_liste.append(zeile)
                ausgabe_liste.append(liste[17])
                ausgabe_liste.append(liste[18])
                open('C:\\Users\\Jonas\\Desktop\\Ergebnisse\\Database\\propynamide_Mode'+str(y)+'_'+str(a)+'_'+str(z)+'.log', "w", newline="").writelines(ausgabe_liste)
def leerzeichen_macher(eingabestring):
    while len(eingabestring) < 12:
        eingabestring=' '+ eingabestring
    return eingabestring
rewriter()
