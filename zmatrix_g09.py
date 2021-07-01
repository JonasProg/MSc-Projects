import os
import shutil
def _zmatrix_maker():
    for n in range(1,19):
        for z in range(1, 7):
            Mode = open(
                'C:\\Users\\Jonas\\Documents\\Orca_Computations\\Moden_inputs\\Mode'+str(n)+'_inputs\\propynamide_Mode_'+str(n)+'_0'+str(z)+'l.com')
            liste = Mode.readlines()
            liste2 = []
            liste3 = []
            liste4 = []
            liste5 = []
            zmatrix = []
            outputdirectory= ('C:\\Users\\Jonas\\Documents\\Orca_Computations\\Moden_inputs\\Mode'+str(n)+'_inputs')
            for x in range(0,len(liste)):
                if "0 1" in liste[x]:
                    dir1 = 'C:\\Users\\Jonas\\Documents\\Orca_Computations\\Input_Files\\'
                    liste2 = [liste[x+1],liste[x+2], liste[x+3], liste[x+4], liste[x+5], liste[x+6], liste[x+7], liste[x+8]]
                    if os.path.exists(outputdirectory+"\\"+'-'+str(z)+'\\') == False:
                        os.mkdir(outputdirectory+"\\"+'-'+str(z)+'\\')
                    dir2 = (outputdirectory + "\\" + "-"+str(z) + "\\")
                    for files in os.listdir(dir1):
                        shutil.copy2(dir1 + files, dir2 + files)
                    file = open('C:\\Users\\Jonas\\Documents\\Orca_Computations\\Moden_inputs\\Mode'+str(n)+'_inputs\\-'+str(z)+'\\_zmatrix.dat', "w", newline="")
                    file.write("geometry angstroms\n")
                    for y in range(0, len(liste2)):
                        liste3 = liste2[y].split()
                        liste4.append(liste3)
                    for m in liste4:
                        liste5 = [m[1],m[2],m[3], ladungszuordnung(m[0]),m[0]]
                        file.write(" ".join(liste5)+"\n")
                        zmatrix.append(liste5)
                    liste4.clear()
                    file.write("end\n")
                    zmatrix.clear()
                    break
        for z in range(1, 7):
            Mode = open(
                'C:\\Users\\Jonas\\Documents\\Orca_Computations\\Moden_inputs\\Mode'+str(n)+'_inputs\\propynamide_Mode_'+str(n)+'_0'+str(z)+'r.com')
            liste = Mode.readlines()
            liste2 = []
            liste3 = []
            liste4 = []
            liste5 = []
            zmatrix = []
            outputdirectory= ('C:\\Users\\Jonas\\Documents\\Orca_Computations\\Moden_inputs\\Mode'+str(n)+'_inputs')
            for x in range(0,len(liste)):
                if "0 1" in liste[x]:
                    dir1 = 'C:\\Users\\Jonas\\Documents\\Orca_Computations\\Input_Files\\'
                    liste2 = [liste[x+1],liste[x+2], liste[x+3], liste[x+4], liste[x+5], liste[x+6], liste[x+7], liste[x+8]]
                    if os.path.exists(outputdirectory+"\\"+str(z)+'\\') == False:
                        os.mkdir(outputdirectory+"\\"+str(z)+'\\')
                    dir2 = (outputdirectory + "\\" +str(z) + "\\")
                    for files in os.listdir(dir1):
                        shutil.copy2(dir1 + files, dir2 + files)
                    file = open('C:\\Users\\Jonas\\Documents\\Orca_Computations\\Moden_inputs\\Mode'+str(n)+'_inputs\\'+str(z)+'\\_zmatrix.dat', "w", newline="")
                    file.write("geometry angstroms\n")
                    for y in range(0, len(liste2)):
                        liste3 = liste2[y].split()
                        liste4.append(liste3)
                    for m in liste4:
                        liste5 = [m[1],m[2],m[3], ladungszuordnung(m[0]),m[0]]
                        file.write(" ".join(liste5)+"\n")
                        zmatrix.append(liste5)
                    liste4.clear()
                    file.write("end\n")
                    zmatrix.clear()
                    break
        for z in range(0,1):
            Mode = open(
                'C:\\Users\\Jonas\\Documents\\Orca_Computations\\Moden_inputs\\Mode'+str(n)+'_inputs\\propynamide_Mode_'+str(n)+'_000.com')
            liste = Mode.readlines()
            liste2 = []
            liste3 = []
            liste4 = []
            liste5 = []
            zmatrix = []
            outputdirectory= ('C:\\Users\\Jonas\\Documents\\Orca_Computations\\Moden_inputs\\Mode'+str(n)+'_inputs')
            for x in range(0,len(liste)):
                if "0 1" in liste[x]:
                    dir1 = 'C:\\Users\\Jonas\\Documents\\Orca_Computations\\Input_Files\\'
                    liste2 = [liste[x+1],liste[x+2], liste[x+3], liste[x+4], liste[x+5], liste[x+6], liste[x+7], liste[x+8]]
                    if os.path.exists(outputdirectory+"\\"+str(z)+'\\') == False:
                        os.mkdir(outputdirectory+"\\"+str(z)+'\\')
                    dir2 = (outputdirectory + "\\" +str(z) + "\\")
                    for files in os.listdir(dir1):
                        shutil.copy2(dir1 + files, dir2 + files)
                    file = open('C:\\Users\\Jonas\\Documents\\Orca_Computations\\Moden_inputs\\Mode'+str(n)+'_inputs\\'+str(z)+'\\_zmatrix.dat', "w", newline="")
                    file.write("geometry angstroms\n")
                    for y in range(0, len(liste2)):
                        liste3 = liste2[y].split()
                        liste4.append(liste3)
                    for m in liste4:
                        liste5 = [m[1],m[2],m[3], ladungszuordnung(m[0]),m[0]]
                        file.write(" ".join(liste5)+"\n")
                        zmatrix.append(liste5)
                    liste4.clear()
                    file.write("end\n")
                    zmatrix.clear()
                    break
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