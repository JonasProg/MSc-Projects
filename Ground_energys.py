def calc_ground_state():
    for n in range(6,7):
        mp2_energies_liste= open('C:\\Users\\Jonas\\Documents\\Orca_Computations\\propynamid_traj_alleModen\\Mode'+str(n)+'\\propyn_normal_mode'+str(n)+'.mtr.emp2.m'+str(n)+'.dat')
        liste = mp2_energies_liste.readlines()
        for y in range(1,14):
            liste2 = liste[y].split()
            if float(liste2[0]) == 0:
                null_value= liste2[1]
                break
        for y in range(1,14):
            liste2 = liste[y].split()
            Summierer=(float(liste2[1])-float(null_value))*27.2113961317875
        print(Summierer)
print(calc_ground_state())