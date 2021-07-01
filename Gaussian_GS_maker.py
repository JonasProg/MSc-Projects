def gaussian_gs_maker():
    #modenschleife
    for n in range(1,19):
        file = open('C:\\Users\\Jonas\\Documents\\Orca_Computations\\Moden_Gaussian_GS\\Mode'+str(n)+'_inputs\\Mode'+str(n)+'_GS\\Mode'+str(n)+'_GS.dat', "w", newline="")
        file.write("   DDNC (   9)         ENERGY   0   \n")
        #file schleife
        for z in [6,5,4,3,2,1]:
            Mode = open('C:\\Users\\Jonas\\Documents\\Orca_Computations\\Moden_Gaussian_GS\\Mode'+str(n)+'_inputs\\Mode'+str(n)+'_GS\\propynamide_Mode_'+str(n)+'_0'+str(z)+'l.log')
            liste = Mode.readlines()
            liste2=[]
            liste3=[]
            liste4=[]
            for x in range(0,len(liste)):
                if "MP2=" in liste[x]:
                    liste2.append(liste[x])
                    index_value=liste2[0].rfind("MP2=")
                    liste3.append(liste2[0][index_value+4:index_value+15])
                    liste4=['-'+str(z), liste3[0]] 
                    file.write(" ".join(liste4)+"\n")
        for z in range(0,1):
            Mode = open('C:\\Users\\Jonas\\Documents\\Orca_Computations\\Moden_Gaussian_GS\\Mode'+str(n)+'_inputs\\Mode'+str(n)+'_GS\\propynamide_Mode_'+str(n)+'_000.log')
            liste = Mode.readlines()
            liste2=[]
            liste3=[]
            liste4=[]
            for x in range(0,len(liste)):
                if "MP2=" in liste[x]:
                    liste2.append(liste[x])
                    index_value=liste2[0].rfind("MP2=")
                    liste3.append(liste2[0][index_value+4:index_value+15])
                    liste4=[str(z), liste3[0]] 
                    file.write(" ".join(liste4)+"\n")
        for z in range(1,7):
            Mode = open('C:\\Users\\Jonas\\Documents\\Orca_Computations\\Moden_Gaussian_GS\\Mode'+str(n)+'_inputs\\Mode'+str(n)+'_GS\\propynamide_Mode_'+str(n)+'_0'+str(z)+'r.log')
            liste = Mode.readlines()
            liste2=[]
            liste3=[]
            liste4=[]
            for x in range(0,len(liste)):
                if "MP2=" in liste[x]:
                    liste2.append(liste[x])
                    index_value=liste2[0].rfind("MP2=")
                    liste3.append(liste2[0][index_value+4:index_value+15])
                    liste4=[str(z), liste3[0]] 
                    file.write(" ".join(liste4)+"\n")
print(gaussian_gs_maker())