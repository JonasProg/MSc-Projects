import os
import shutil
def _zmatrix_maker():
    for n in range(6,24):
        Mode = open(
            'C:\\Users\\Jonas\\Documents\\Orca_Computations\\propynamid_traj_alleModen\\Mode'+str(n)+'\\propyn_normal_mode.m' + str(n) + '.xyz')
        liste = Mode.readlines()
        liste2 = []
        liste3 = []
        liste4 = []
        liste5 = []
        zmatrix = []
        outputdirectory= ('C:\\Users\\Jonas\\Documents\\Orca_Computations\\propynamid_traj_alleModen\\Mode'+ str(n))
        for x in range(0,len(liste)):
            if "*" in liste[x]:
                dir1 = 'C:\\Users\\Jonas\\Documents\\Orca_Computations\\Input_Files'
                liste2 = [liste[x+1],liste[x+2], liste[x+3], liste[x+4], liste[x+5], liste[x+6], liste[x+7], liste[x+8]]
                if os.path.exists(outputdirectory+"\\"+liste[x][36:-6].strip()) == False:
                    os.mkdir(outputdirectory+"\\"+liste[x][36:-6].strip())
                dir1 = ('C:\\Users\\Jonas\\Documents\\Orca_Computations\\Input_Files\\')
                dir2 = (outputdirectory + "\\" + liste[x][36:-6].strip() + "\\")
                for files in os.listdir(dir1):
                    shutil.copy2(dir1 + files, dir2 + files)

                file = open("{0}\\{1}\\_zmatrix.dat".format(outputdirectory, liste[x][36:-6].strip()), "w", newline="")
                file.write("geometry angstroms\n")

                for y in range(0, len(liste2)):
                    liste3 = liste2[y].split()
                    liste4.append(liste3)
                for z in liste4:
                    liste5 = [z[1],z[2],z[3], ladungszuordnung(z[0]),z[0]]
                    file.write(" ".join(liste5)+"\n")
                    zmatrix.append(liste5)
                liste4.clear()
                file.write("end\n")
                zmatrix.clear()

def ladungszuordnung(symbol):
    if symbol == "O":
        return "8.0"
    if symbol == "N":
        return "7.0"
    if symbol == "C":
        return "6.0"
    if symbol == "H":
        return "1.0"


print(_zmatrix_maker())