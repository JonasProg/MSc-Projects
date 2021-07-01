import pandas
def Ergebnisse_in_Tabelle():
    liste3 = []
    final_liste=[]
    for n in range(1,19):
        summierer_liste= calc_ground_state(n)
        File2 = open('C:\\Users\\Jonas\\Desktop\\Ergebnisse\\Mode'+str(n)+'_dat\\Mode'+str(n)+'_Energien.csv', "w", newline="")
        orb_file_liste= []
        for a in range(0,4):
            orb_file_liste.append(open('C:\\Users\\Jonas\\Desktop\\Ergebnisse\\Mode'+str(n)+'_dat\\Mode'+str(n)+'_orbitale'+str(a+1)+'.csv', "w", newline=""))
        for x in range(-6,7):
            File = open('C:\\Users\\Jonas\\Desktop\\Ergebnisse\\Mode'+str(n)+'_dat\\Mode'+str(n)+'_inputs_'+str(x)+'.dat')
            liste = File.readlines()
            for y in range(0 ,16):
                checkliste= liste[y].split()
                if pandas.to_numeric(checkliste[2]) >= 0.5:
                    liste3.append(float(checkliste[1])+summierer_liste[x+6])
                    if len(liste3) == 1:
                        orb_file_liste[0].write("{0}; {1}; {2}; {3}; {4}; {5}; {6}; {7}; {8}; {9}; {10}; {11}; {12}; {13}\n".format(str(-x),float(checkliste[3])**2,float(checkliste[4])**2,float(checkliste[5])**2,float(checkliste[6])**2,float(checkliste[7])**2,float(checkliste[8])**2,float(checkliste[9])**2,float(checkliste[10])**2, float(checkliste[11])**2, float(checkliste[12])**2, float(checkliste[13])**2, float(checkliste[14])**2, float(checkliste[15])**2).replace(".", ","))
                    if len(liste3) == 2:
                        orb_file_liste[1].write("{0}; {1}; {2}; {3}; {4}; {5}; {6}; {7}; {8}; {9}; {10}; {11}; {12}; {13}\n".format(str(-x),float(checkliste[3])**2,float(checkliste[4])**2,float(checkliste[5])**2,float(checkliste[6])**2,float(checkliste[7])**2,float(checkliste[8])**2,float(checkliste[9])**2,float(checkliste[10])**2, float(checkliste[11])**2, float(checkliste[12])**2, float(checkliste[13])**2, float(checkliste[14])**2, float(checkliste[15])**2).replace(".", ","))
                    if len(liste3) == 3:
                        orb_file_liste[2].write("{0}; {1}; {2}; {3}; {4}; {5}; {6}; {7}; {8}; {9}; {10}; {11}; {12}; {13}\n".format(str(-x),float(checkliste[3])**2,float(checkliste[4])**2,float(checkliste[5])**2,float(checkliste[6])**2,float(checkliste[7])**2,float(checkliste[8])**2,float(checkliste[9])**2,float(checkliste[10])**2, float(checkliste[11])**2, float(checkliste[12])**2, float(checkliste[13])**2, float(checkliste[14])**2, float(checkliste[15])**2).replace(".", ","))
                    if len(liste3) == 4:
                        orb_file_liste[3].write("{0}; {1}; {2}; {3}; {4}; {5}; {6}; {7}; {8}; {9}; {10}; {11}; {12}; {13}\n".format(str(-x),float(checkliste[3])**2,float(checkliste[4])**2,float(checkliste[5])**2,float(checkliste[6])**2,float(checkliste[7])**2,float(checkliste[8])**2,float(checkliste[9])**2,float(checkliste[10])**2, float(checkliste[11])**2, float(checkliste[12])**2, float(checkliste[13])**2, float(checkliste[14])**2, float(checkliste[15])**2).replace(".", ","))
                if len(liste3) == 4:
                    break
            final_liste.append(liste3)
            File2.write("{0}; {1}; {2}; {3}; {4}\n".format(str(-x), liste3[0], liste3[1], liste3[2], liste3[3]).replace(".", ","))
            liste3 = []

def calc_ground_state(n):
    mp2_energies_liste= open('C:\\Users\\Jonas\\Documents\\Orca_Computations\\Moden_Gaussian_GS\\Mode'+str(n)+'_inputs\\Mode'+str(n)+'_GS\\Mode'+str(n)+'_GS.dat')
    liste = mp2_energies_liste.readlines()
    for y in range(1,14):
        liste2 = liste[y].split()
        if float(liste2[0]) == 0:
            null_value= liste2[1]
            break
    summierer_liste = []
    for y in range(1,14):
        liste2 = liste[y].split()
        Summierer=(float(liste2[1])-float(null_value))*27.2113961317875
        summierer_liste.append(Summierer)
    return summierer_liste
print(Ergebnisse_in_Tabelle())
