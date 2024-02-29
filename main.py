p_conv = 8.96057e-7 #Convert between MeV/fm^3 to M_sol/km^3

def write_crust_to_file(filename,filename_crust):
    file = open(filename,'w')
    file_crust = open(filename_crust,'r')
    

    for line in file_crust:
        file.write(line)
    file.close()
    file_crust.close()
        
        
def write_EoS_to_file(eos,filename,crust=True,filename_crust="nveos.in"):
    file = open(filename,'w')
    e_vec = eos.e_vec*p_conv
    P_vec = eos.P_vec*p_conv
    rho_vec = eos.rho_vec
    for i in range(len(e_vec)):
        P = P_vec[i]
        e = e_vec[i]
        rho = rho_vec[i]

        file.write(str(P)+" "+str(e)+" " +str(rho)+"\n")
    if(crust==True):
        write_crust_to_file(filename,filename_crust)
    file.close()
    



#write_crust_to_file("test","nveos.in")




#write_EoS_to_file(None,"test2")

#def write_EoS_to_file()
