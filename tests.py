import APR03_eos
import matplotlib.pyplot as plt
import time
import numpy as np
import write_eos_to_file as wrt
import TOV_Rahul
import exotic_eos
import RMF_eos

testing_apr03 = False               #Check apr eos
testing_CFL = True                  #Check CFL eos and intersection with apr
testing_total_eos_B = False          #Check total eos for different values of bag constant B
testing_total_eos_Delta = False      #Check total eos for different values of pairing gap Delta
testing_total_eos_m_s = False        #Check total eos for different values strange mass m_s
testing_reading_eos_from_file = False #Check that reading and writing to file worked as it should
testing_M_R_realtions_B = False        #Test M_R_relations for the previous tests with varying B
testing_M_R_realtions_Delta = False        #Test M_R_relations for the previous tests with varying Delta
testing_M_R_realtions_m_s = False        #Test M_R_relations for the previous tests with varying m_s
testing_CFL_RMF = False
testing_CFL_RMF_MARK = False
plot_original_phases = False
testing_total_eos_B_RMF = False
testing_total_eos_Delta_RMF = False
testing_total_eos_m_s_RMF = False
#Testing
if(testing_apr03==True):

    time_0 = time.perf_counter()

    N_apr03 = 1000
    eos = APR03_eos.apr03_EoS(N_apr03)
    print("Time spent:", time.perf_counter()-time_0)

    plt.figure()
    plt.xlim(0,1)
    plt.ylim(-50,450)
    plt.xlabel("$\\rho$ [fm$^{-3}$]")
    plt.ylabel("E/A [MeV]")

    plt.plot(eos.rho_PNM_SNM_apr03_vec,eos.E_per_A_PNM_LDP_apr03_vec,label = "PNM, LDP",color="Black")
    plt.plot(eos.rho_PNM_SNM_apr03_vec,eos.E_per_A_PNM_HDP_apr03_vec,label = "PNM, HDP",color = "Red")
    plt.plot(eos.rho_PNM_SNM_apr03_vec,eos.E_per_A_SNM_LDP_apr03_vec,'--',label = "SNM, LDP", color = "Black")
    plt.plot(eos.rho_PNM_SNM_apr03_vec,eos.E_per_A_SNM_HDP_apr03_vec,'--',label = "SNM, HDP", color = "Red")
    plt.legend()
    plt.savefig("figures/tests/figures_xeos_note/E_per_A_PNM_and_SNM.pdf")

    plt.figure()
    plt.xlim(0,1)
    plt.ylim(-50,450)
    plt.xlabel("$\\rho$ [fm$^{-3}$]")
    plt.ylabel("E/A [MeV]")
    plt.plot(eos.rho_apr03_vec,eos.E_per_A_LDP_apr03_vec,label = "LDP",color = "Black")
    plt.plot(eos.rho_apr03_vec,eos.E_per_A_HDP_apr03_vec,label = "HDP",color = "Red")
    plt.legend()
    plt.savefig("figures/tests/figures_xeos_note/E_per_A_beta_equillibrium.pdf")

    plt.figure()
    plt.xlim(0,1.2)
    plt.ylim(0,0.2)
    plt.xlabel("$\\rho$ [fm$^{-3}$]")
    plt.ylabel("$x_p$")
    plt.plot(eos.rho_apr03_vec,eos.x_p_LDP_apr03_vec,'*',label = "LDP", color = "Blue")
    plt.plot(eos.rho_apr03_vec,eos.x_p_HDP_apr03_vec,'*',label = "HDP", color = "Red")
    plt.plot(eos.rho_apr03_combined_vec,eos.x_p_apr03_combined_vec,label = "APR03", color="Black")
    plt.legend()
    plt.savefig("figures/tests/figures_xeos_note/proton_fraction.pdf")

    plt.figure()
    plt.xlim(0,1)
    plt.ylim(0,600)
    plt.xlabel("$\\rho_0$[fm$^{-3}$]")
    plt.ylabel("Energy density [MeV/fm$^3$]")

    plt.plot(eos.rho_apr03_vec,eos.e_LDP_apr03_vec,'*',color = "Blue",label = "LDP")
    plt.plot(eos.rho_apr03_vec,eos.e_HDP_apr03_vec,'*',color = "Red",label = "HDP")
    plt.plot(eos.rho_apr03_combined_vec,eos.e_apr03_combined_vec,color = "Black",label = "APR03")
    plt.legend()
    plt.savefig("figures/tests/figures_xeos_note/e_of_rho.pdf")

    plt.figure()
    plt.xlim(0,100)
    plt.ylim(0,600)
    plt.xlabel("Pressure [MeV/fm$^3$]")
    plt.ylabel("Energy density [MeV/fm$^3$]")
    plt.plot(eos.P_LDP_apr03_vec,eos.e_LDP_apr03_vec,'*',label = "LDP",color = "Blue")
    plt.plot(eos.P_HDP_apr03_vec,eos.e_HDP_apr03_vec,'*',label = "HDP",color = "Red")
    plt.plot(eos.P_apr03_combined_vec,eos.e_apr03_combined_vec,label = "APR03", color = "Black")
    plt.legend()
    plt.savefig("figures/tests/figures_xeos_note/e_of_P.pdf")

    plt.figure()
    plt.xlim(0,1)
    plt.ylim(800,2100)
    plt.xlabel("$\\rho$[fm$^{-3}$]")
    plt.ylabel("$\\mu$[MeV]")
    plt.plot(eos.rho_apr03_vec,eos.mu_n_LDP_apr03_vec,'*',label = "$\\mu_n$, LDP")
    plt.plot(eos.rho_apr03_vec,eos.mu_n_HDP_apr03_vec,'*',label = "$\\mu_n$, HDP")
    plt.plot(eos.rho_apr03_vec,eos.mu_p_LDP_apr03_vec,'*',label = "$\\mu_p$, LDP")
    plt.plot(eos.rho_apr03_vec,eos.mu_p_HDP_apr03_vec,'*',label = "$\\mu_p$, HDP")
    plt.plot(eos.rho_apr03_combined_vec,eos.mu_n_apr03_combined_vec,label = "$\\mu_n$, APR03")
    plt.plot(eos.rho_apr03_combined_vec,eos.mu_p_apr03_combined_vec,label = "$\\mu_p$, APR03")
    plt.legend()
    plt.savefig("figures/tests/figures_xeos_note/mu_i_of_rho.pdf")
    plt.show()

if(testing_CFL==True):
    time_0 = time.perf_counter()
    N_CFL = 100
    N_CFL_kaons = 300
    B = 190
    c = 0.
    Delta = 100
    m_s = 150
    N_apr03 = 300
    eos = exotic_eos.CFL_EoS(B,Delta,m_s,N=N_CFL,N_kaons=N_CFL_kaons,N_low_dens=N_apr03,c=c,eos_name="APR")
    print("Time spent:", time.perf_counter()-time_0)

    plt.figure()
    plt.title("APR, c="+str(np.round(c,2)))
    plt.xlim(300,530)
    plt.ylim(0,300)
    plt.xlabel("$\\mu_q$[MeV]")
    plt.ylabel("P[MeV/fm$^3$] / $\\mu[MeV]$")
    plt.plot(eos.mu_q_CFL_vec,eos.P_CFL_vec,label = "$P_{CFL}$",color = "green")
    plt.plot(eos.mu_q_CFL_with_kaons_vec,eos.P_CFL_with_kaons_vec,label = "$P_{CFL}^k$",color="orange")
    plt.plot(eos.mu_q_CFL_with_kaons_vec,eos.mu_e_CFL_with_kaons_vec,'--',label = "$\\mu_e^k$",color="black")
    plt.plot(eos.eos_low_dens.mu_n_vec/3,eos.eos_low_dens.mu_e_vec,label = "$\\mu_e$",color="black")
    plt.plot(eos.eos_low_dens.mu_n_vec/3,eos.eos_low_dens.P_vec,label = "$P_{NM}$",color="blue")
    plt.plot(eos.mu_q_vec,eos.P_vec,'--',label = "P",color="red")
    plt.legend()
    if(c!=0):
        quark_interact = "c!=0"
    else:
        quark_interact=""
    plt.savefig("figures/tests/figures_xeos_note/phases"+quark_interact+".pdf")
    plt.show()

if(testing_total_eos_B==True):

    time_0 = time.perf_counter()

    N_B = 10

    B_vec = np.linspace(175,210,N_B)
    #First create apr eos, so we dont have to call it repeatedly
    N_apr03 = 500
    eos_apr03 = APR03_eos.apr03_EoS(N_apr03,rho_min_apr03=0.1,rho_max_apr03=2)

    N_CFL = 2000
    N_CFL_kaons = 500
    Delta = 100
    m_s = 150
    c = 0.3

    plt.figure(1)
    plt.xlim(320,480)
    plt.ylim(0,400)
    plt.title("$\\Delta$ = "+str(Delta)+", $m_s$ = "+str(m_s)+", $c$ = "+str(c))
    plt.xlabel("$\\mu_q$[MeV]")
    plt.ylabel("$P$[MeV/fm$^3$]")

    plt.figure(2)
    plt.xlim(0,1000)
    plt.ylim(0,400)
    plt.title("$\\Delta$ = "+str(Delta)+", $m_s$ = "+str(m_s)+", $c$ = "+str(c))
    plt.xlabel("$\\epsilon$[MeV/fm$^3$]")
    plt.ylabel("P[MeV/fm$^3$]")

    plt.figure(3)
    plt.xlim(0,2)
    plt.ylim(0,400)
    plt.title("$\\Delta$ = "+str(Delta)+", $m_s$ = "+str(m_s)+", $c$ = "+str(c))
    plt.xlabel("$\\rho$[fm$^{-3}$]")
    plt.ylabel("P[MeV/fm$^3$]")

    parameter_file = open("figures/tests/parameter_varying/B/parameters.txt",'w')
    parameter_file.write("B, Delta, m_s \n")
    for i in range(N_B):
        B = B_vec[i]
        eos = exotic_eos.CFL_EoS(N_CFL,N_CFL_kaons,B,Delta,m_s,eos_apr03=eos_apr03,c=c)
        parameter_file.write(str(B)+" "+str(Delta)+" "+str(m_s)+"\n")

        wrt.write_EoS_to_file(eos,"figures/tests/parameter_varying/B/eos_files/"+str(i).zfill(6))


        plt.figure(1)
        plt.plot(eos.mu_q_vec,eos.P_vec,label = "B$^{1/4}$="+str(np.round(B,decimals=1))+"MeV")
        plt.legend()

        plt.figure(2)
        plt.plot(eos.e_vec,eos.P_vec,label = "B$^{1/4}$="+str(np.round(B,decimals=1))+"MeV")
        plt.legend()

        plt.figure(3)
        plt.plot(eos.rho_vec,eos.P_vec,label = "B$^{1/4}$="+str(np.round(B,decimals=1))+"MeV")
        plt.legend()

    parameter_file.close()

    plt.figure(1)
    plt.plot(eos.eos_apr03.mu_n_apr03_combined_vec/3,eos.eos_apr03.P_apr03_combined_vec,label = "NM",color = "black")
    plt.legend()

    plt.figure(2)
    plt.plot(eos.eos_apr03.e_apr03_combined_vec,eos.eos_apr03.P_apr03_combined_vec,label = "NM",color = "black")
    plt.legend()

    plt.figure(3)
    plt.plot(eos.eos_apr03.rho_apr03_combined_vec,eos.eos_apr03.P_apr03_combined_vec,label = "NM",color = "black")
    plt.legend()

    print("Time spent:", time.perf_counter()-time_0)
    plt.figure(1)
    plt.savefig("figures/tests/parameter_varying/B/P_of_mu_q.pdf")
    plt.figure(2)
    plt.savefig("figures/tests/parameter_varying/B/P_of_e.pdf")
    plt.figure(3)
    plt.savefig("figures/tests/parameter_varying/B/P_of_rho.pdf")

    plt.show()

if(testing_total_eos_Delta==True):

    time_0 = time.perf_counter()

    N_Delta = 10

    Delta_vec = np.linspace(50,150,N_Delta)

    #First create apr eos, so we dont have to call it repeatedly
    N_apr03 = 2000
    eos_apr03 = APR03_eos.apr03_EoS(N_apr03,rho_min_apr03=0.1,rho_max_apr03=2)

    N_CFL = 2000
    N_CFL_kaons = 2000
    B = 190
    m_s = 150
    c = 0.3

    plt.figure(1)
    plt.xlim(320,480)
    plt.ylim(0,400)
    plt.title("$m_s$ = "+str(m_s)+", $B$ = "+str(B)+", $c$ = "+str(c))
    plt.xlabel("$\\mu_q$[MeV]")
    plt.ylabel("$P$[MeV/fm$^3$]")

    plt.figure(2)
    plt.xlim(0,1000)
    plt.ylim(0,400)
    plt.title("$m_s$ = "+str(m_s)+", $B$ = "+str(B)+", $c$ = "+str(c))
    plt.xlabel("$\\epsilon$[MeV/fm$^3$]")
    plt.ylabel("P[MeV/fm$^3$]")

    plt.figure(3)
    plt.xlim(0,2)
    plt.ylim(0,400)
    plt.title("$m_s$ = "+str(m_s)+", $B$ = "+str(B)+", $c$ = "+str(c))
    plt.xlabel("$\\rho$[fm$^{-3}$]")
    plt.ylabel("P[MeV/fm$^3$]")

    parameter_file = open("figures/tests/parameter_varying/Delta/parameters.txt",'w')
    parameter_file.write("B, Delta, m_s \n")
    for i in range(N_Delta):
        Delta = Delta_vec[i]
        eos = exotic_eos.CFL_EoS(N_CFL,N_CFL_kaons,B,Delta,m_s,eos_apr03=eos_apr03,c=c)
        parameter_file.write(str(B)+" "+str(Delta)+" "+str(m_s)+"\n")

        #Remove zeros from vectors
        wrt.write_EoS_to_file(eos,"figures/tests/parameter_varying/Delta/eos_files/"+str(i).zfill(6))
        mu_q_vec = eos.mu_q_vec[eos.mu_q_vec==0] = np.nan
        P_vec = eos.P_vec[eos.P_vec==0] = np.nan
        e_vec = eos.e_vec[eos.e_vec==0] = np.nan
        ##

        plt.figure(1)
        plt.plot(eos.mu_q_vec,eos.P_vec,label = "$\\Delta$="+str(np.round(Delta,decimals=1))+"MeV")
        plt.legend()

        plt.figure(2)
        plt.plot(eos.e_vec,eos.P_vec,label = "$\\Delta$="+str(np.round(Delta,decimals=1))+"MeV")
        plt.legend()

        plt.figure(3)
        plt.plot(eos.rho_vec,eos.P_vec,label = "$\\Delta$="+str(np.round(Delta,decimals=1))+"MeV")
        plt.legend()

    parameter_file.close()

    plt.figure(1)
    plt.plot(eos.eos_apr03.mu_n_apr03_combined_vec/3,eos.eos_apr03.P_apr03_combined_vec,label = "NM",color = "black")
    plt.legend()

    plt.figure(2)
    plt.plot(eos.eos_apr03.e_apr03_combined_vec,eos.eos_apr03.P_apr03_combined_vec,label = "NM",color = "black")
    plt.legend()

    plt.figure(3)
    plt.plot(eos.eos_apr03.rho_apr03_combined_vec,eos.eos_apr03.P_apr03_combined_vec,label = "NM",color = "black")
    plt.legend()

    print("Time spent:", time.perf_counter()-time_0)
    plt.figure(1)
    plt.savefig("figures/tests/parameter_varying/Delta/P_of_mu_q.pdf")
    plt.figure(2)
    plt.savefig("figures/tests/parameter_varying/Delta/P_of_e.pdf")
    plt.figure(3)
    plt.savefig("figures/tests/parameter_varying/Delta/P_of_rho.pdf")

    plt.show()

if(testing_total_eos_m_s==True):

    time_0 = time.perf_counter()

    N_m_s = 10

    m_s_vec = np.linspace(50,250,N_m_s)

    #First create apr eos, so we dont have to call it repeatedly
    N_apr03 = 2000
    eos_apr03 = APR_eos.apr03_EoS(N_apr03,rho_min_apr03=0.1,rho_max_apr03=2)

    N_CFL = 2000
    N_CFL_kaons = 2000
    B = 190
    Delta = 100
    c = 0.3

    plt.figure(1)
    plt.xlim(320,480)
    plt.ylim(0,400)
    plt.title("$\\Delta$ = "+str(Delta)+", $B$ = "+str(B)+", $c$ = "+str(c))
    plt.xlabel("$\\mu_q$[MeV]")
    plt.ylabel("$P$[MeV/fm$^3$]")

    plt.figure(2)
    plt.xlim(0,1000)
    plt.ylim(0,400)
    plt.title("$\\Delta$ = "+str(Delta)+", $B$ = "+str(B)+", $c$ = "+str(c))
    plt.xlabel("$\\epsilon$[MeV/fm$^3$]")
    plt.ylabel("P[MeV/fm$^3$]")

    plt.figure(3)
    plt.xlim(0,2)
    plt.ylim(0,400)
    plt.title("$\\Delta$ = "+str(Delta)+", $B$ = "+str(B)+", $c$ = "+str(c))
    plt.xlabel("$\\rho$[fm$^{-3}$]")
    plt.ylabel("P[MeV/fm$^3$]")

    parameter_file = open("figures/tests/parameter_varying/m_s/parameters.txt",'w')
    parameter_file.write("B, Delta, m_s \n")
    for i in range(N_m_s):
        m_s = m_s_vec[i]
        eos = exotic_eos.CFL_EoS(N_CFL,N_CFL_kaons,B,Delta,m_s,eos_apr03=eos_apr03,c=c)
        parameter_file.write(str(B)+" "+str(Delta)+" "+str(m_s)+"\n")

        wrt.write_EoS_to_file(eos,"figures/tests/parameter_varying/m_s/eos_files/"+str(i).zfill(6))

        #Remove zeros from vectors
        mu_q_vec = eos.mu_q_vec[eos.mu_q_vec==0] = np.nan
        P_vec = eos.P_vec[eos.P_vec==0] = np.nan
        e_vec = eos.e_vec[eos.e_vec==0] = np.nan
        ##

        plt.figure(1)
        plt.plot(eos.mu_q_vec,eos.P_vec,label = "$m_s$="+str(np.round(m_s,decimals=1))+"MeV")
        plt.legend()

        plt.figure(2)
        plt.plot(eos.e_vec,eos.P_vec,label = "$m_s$="+str(np.round(m_s,decimals=1))+"MeV")
        plt.legend()

        plt.figure(3)
        plt.plot(eos.rho_vec,eos.P_vec,label = "$m_s$="+str(np.round(m_s,decimals=1))+"MeV")
        plt.legend()

    parameter_file.close()

    plt.figure(1)
    plt.plot(eos.eos_apr03.mu_n_apr03_combined_vec/3,eos.eos_apr03.P_apr03_combined_vec,label = "NM",color = "black")
    plt.legend()

    plt.figure(2)
    plt.plot(eos.eos_apr03.e_apr03_combined_vec,eos.eos_apr03.P_apr03_combined_vec,label = "NM",color = "black")
    plt.legend()

    plt.figure(3)
    plt.plot(eos.eos_apr03.rho_apr03_combined_vec,eos.eos_apr03.P_apr03_combined_vec,label = "NM",color = "black")
    plt.legend()

    print("Time spent:", time.perf_counter()-time_0)
    plt.figure(1)
    plt.savefig("figures/tests/parameter_varying/m_s/P_of_mu_q.pdf")
    plt.figure(2)
    plt.savefig("figures/tests/parameter_varying/m_s/P_of_e.pdf")
    plt.figure(3)
    plt.savefig("figures/tests/parameter_varying/m_s/P_of_rho.pdf")

    plt.show()

if(testing_reading_eos_from_file == True):
    filename_parameters = "figures/tests/parameter_varying/Delta/parameters.txt"
    B_vec,Delta_vec,m_s_vec = wrt.read_parameters_from_file(filename_parameters)
    plt.figure()
    plt.xlabel("$\\rho$[fm$^{-3}$]")
    plt.ylabel("P[MeV/fm$^3$]")
    for i in range(10):
        P_vec,e_vec,rho_vec = wrt.read_EoS_from_file("figures/tests/parameter_varying/Delta/eos_files/"+str(i).zfill(6))
        P_conv = wrt.P_conv
        Delta = Delta_vec[i]
        plt.plot(e_vec,P_vec,label = "$\\Delta$="+str(np.round(Delta,decimals=1)))
    plt.legend()
    plt.show()


if(testing_M_R_realtions_B == True):
    time_0 = time.perf_counter()
    P_conv = wrt.P_conv

    plt.figure("B")
    plt.xlim(8,16)
    plt.ylim(0,2.2)

    filename_parameters = "figures/tests/parameter_varying/B/parameters.txt"
    B_vec,Delta_vec,m_s_vec = wrt.read_parameters_from_file(filename_parameters)
    plt.title("$m_s$ = "+str(m_s_vec[0])+"MeV,  $\\Delta$ = "+str(Delta_vec[0])+"MeV,  $c$ = "+str(0.3))
    plt.xlabel("R[km]")
    plt.ylabel("M[M$_\\odot$]")

    for i in range(len(B_vec)):
        filename_eos = "figures/tests/parameter_varying/B/eos_files/"+str(i).zfill(6)
        B = B_vec[i]
        P_vec,e_vec,rho_vec = wrt.read_EoS_from_file(filename_eos)
        v2_vec = np.gradient(P_vec,e_vec,edge_order=2)

        R_vec,M_vec,Lambda,p_c = TOV_Rahul.tov_solve(e_vec,P_vec,v2_vec)
        plt.plot(R_vec,M_vec,label ="$B^{1/4}$="+str(np.round(B,decimals=1))+"MeV")
    plt.legend()
    print("Time spent:", time.perf_counter()-time_0)
    plt.savefig("figures/tests/parameter_varying/B/MR_crurvest.pdf")
    plt.show()


if(testing_M_R_realtions_Delta == True):
    time_0 = time.perf_counter()
    P_conv = wrt.P_conv

    plt.figure("Delta")
    plt.xlim(8,16)
    plt.ylim(0,2.2)

    filename_parameters = "figures/tests/parameter_varying/Delta/parameters.txt"
    B_vec,Delta_vec,m_s_vec = wrt.read_parameters_from_file(filename_parameters)
    plt.title("$m_s$ = "+str(m_s_vec[0])+"MeV,  $B^{1/4}$ = "+str(B_vec[0])+"MeV,  $c$ = "+str(0.3))
    plt.xlabel("R[km]")
    plt.ylabel("M[M$_\\odot$]")

    for i in range(len(Delta_vec)):
        filename_eos = "figures/tests/parameter_varying/Delta/eos_files/"+str(i).zfill(6)
        Delta = Delta_vec[i]
        P_vec,e_vec,rho_vec = wrt.read_EoS_from_file(filename_eos)
        v2_vec = np.gradient(P_vec,e_vec,edge_order=2)

        R_vec,M_vec,Lambda,p_c = TOV_Rahul.tov_solve(e_vec,P_vec,v2_vec)
        plt.plot(R_vec,M_vec,label ="$\\Delta$="+str(np.round(Delta,decimals=1))+"MeV")
    plt.legend()
    print("Time spent:", time.perf_counter()-time_0)
    plt.savefig("figures/tests/parameter_varying/Delta/MR_crurvest.pdf")
    plt.show()



if(testing_M_R_realtions_m_s == True):
    time_0 = time.perf_counter()
    P_conv = wrt.P_conv

    plt.figure("m_s")
    plt.xlim(8,16)
    plt.ylim(0,2.2)

    filename_parameters = "figures/tests/parameter_varying/m_s/parameters.txt"
    B_vec,Delta_vec,m_s_vec = wrt.read_parameters_from_file(filename_parameters)
    plt.title("$\\Delta$ = "+str(Delta_vec[0])+"MeV,  $B^{1/4}$ = "+str(B_vec[0])+"MeV,  $c$ = "+str(0.3))
    plt.xlabel("R[km]")
    plt.ylabel("M[M$_\\odot$]")

    for i in range(len(m_s_vec)):
        filename_eos = "figures/tests/parameter_varying/m_s/eos_files/"+str(i).zfill(6)
        m_s = m_s_vec[i]
        P_vec,e_vec,rho_vec = wrt.read_EoS_from_file(filename_eos)
        v2_vec = np.gradient(P_vec,e_vec,edge_order=2)

        R_vec,M_vec,Lambda,p_c = TOV_Rahul.tov_solve(e_vec,P_vec,v2_vec)
        plt.plot(R_vec,M_vec,label ="$m_s$="+str(np.round(m_s,decimals=1))+"MeV")
    plt.legend()
    print("Time spent:", time.perf_counter()-time_0)
    plt.savefig("figures/tests/parameter_varying/m_s/MR_crurvest.pdf")
    plt.show()


if(testing_CFL_RMF==True):
    time_0 = time.perf_counter()
    N = 300
    N_CFL = 300
    N_CFL_kaons = 300
    B = 165
    c = 0.
    Delta = 100
    m_s = 150
    N_RMF = 300
    mu_q_max = 600
    eos = exotic_eos.CFL_EoS(N_CFL,N_CFL_kaons,B,Delta,m_s,N=N,N_RMF=N_RMF,c=c,eos_name="RMF",mu_q_max=mu_q_max)
    print("Time spent:", time.perf_counter()-time_0)

    plt.figure()
    plt.title("RMF, c="+str(np.round(c,2)))
    plt.xlim(300,530)
    plt.ylim(0,300)
    plt.xlabel("$\\mu_q$[MeV]")
    plt.ylabel("P[MeV/fm$^3$] / $\\mu[MeV]$")
    plt.plot(eos.mu_q_CFL_vec,eos.P_CFL_vec,label = "$P_{CFL}$",color = "green")
    plt.plot(eos.mu_q_CFL_with_kaons_vec,eos.P_CFL_with_kaons_vec,label = "$P_{CFL}^k$",color="purple")
    plt.plot(eos.mu_q_CFL_with_kaons_vec[eos.mu_e_CFL_with_kaons_vec>=0],eos.mu_e_CFL_with_kaons_vec[eos.mu_e_CFL_with_kaons_vec>=0],'--',label = "$\\mu_e^k$",color="black")
    plt.plot(eos.eos_RMF.mu_n_vec/3,eos.eos_RMF.mu_e_vec,label = "$\\mu_e$",color="black")
    plt.plot(eos.eos_RMF.mu_n_vec/3,eos.eos_RMF.P_vec,label = "$P_{NM}$",color="blue")
    plt.plot(eos.mu_q_vec,eos.P_vec,'--',label = "P",color="red")
    plt.legend()
    if(c!=0):
        quark_interact="c!=0"
    else:
        quark_interact=""
    plt.savefig("figures/tests/figures_xeos_note/phases_RMF_Waleca"+quark_interact+".pdf")
    #plt.savefig("figures/tests/figures_xeos_note/phases_RMF_Waleca_extreme_cases.pdf")
    plt.show()



if(testing_CFL_RMF_MARK==True):
    time_0 = time.perf_counter()
    N = 300
    N_CFL = 300
    N_CFL_kaons = 300
    B = 190.
    c = 0.
    Delta = 100
    m_s = 150
    N_RMF = 300
    mu_q_max = 600
    eos = exotic_eos.CFL_EoS(N_CFL,N_CFL_kaons,B,Delta,m_s,N=N,N_RMF=N_RMF,c=c,eos_name="RMF",mu_q_max=mu_q_max,FSUGold_filename="FSUGold_MARK.inp")
    print("Time spent:", time.perf_counter()-time_0)

    plt.figure()
    plt.title("RMF, c="+str(np.round(c,2)))
    plt.xlim(300,530)
    plt.ylim(0,300)
    plt.xlabel("$\\mu_q$[MeV]")
    plt.ylabel("P[MeV/fm$^3$] / $\\mu[MeV]$")
    plt.plot(eos.mu_q_CFL_vec,eos.P_CFL_vec,label = "$P_{CFL}$",color = "green")
    plt.plot(eos.mu_q_CFL_with_kaons_vec,eos.P_CFL_with_kaons_vec,label = "$P_{CFL}^k$",color="purple")
    plt.plot(eos.mu_q_CFL_with_kaons_vec[eos.mu_e_CFL_with_kaons_vec>=0],eos.mu_e_CFL_with_kaons_vec[eos.mu_e_CFL_with_kaons_vec>=0],'--',label = "$\\mu_e^k$",color="black")
    plt.plot(eos.eos_RMF.mu_n_vec/3,eos.eos_RMF.mu_e_vec,label = "$\\mu_e$",color="black")
    plt.plot(eos.eos_RMF.mu_n_vec/3,eos.eos_RMF.P_vec,label = "$P_{NM}$",color="blue")
    plt.plot(eos.mu_q_vec,eos.P_vec,'--',label = "P",color="red")
    if(plot_original_phases==True):
        textfile = open('pmqk.dat')
        textfile_0 = open('pmqk_c=0.dat')
        mu_q_0 = []
        mu_e_k_0 = []
        p_0 = []

        mu_q = []
        mu_e_k = []
        p = []


        for line in textfile_0:
            data = line.split()
            if(len(data)>0):
                mu_q_0.append(float(data[0]))
                mu_e_k_0.append(float(data[1]))
                p_0.append(float(data[2]))

        for line in textfile:
            data = line.split()
            if(len(data)>0):
                mu_q.append(float(data[0]))
                mu_e_k.append(float(data[1]))
                p.append(float(data[2]))

        textfile.close()
        textfile_0.close()
        n_stop = 2100
        plt.plot(mu_q[:n_stop],p[:n_stop],"Magenta",label = "P Walec")
        plt.plot(mu_q,mu_e_k,label = "$\\mu_e$ Walec")
        plt.plot(mu_q_0,mu_e_k_0,label = "$\\mu_e$ Walec c=0")
        #for line in textfile:
        #    data = np.array([float(v) for v in line.strip().split(" ")])
        #data = list([list(map(float, line.split())) for line in open('pmqk.dat')])
        #print(data)
        #plt.plot(data[0],data[1])
    plt.legend()
    if(c!=0):
        quark_interact="c!=0"
    else:
        quark_interact=""
    plt.savefig("figures/tests/figures_xeos_note/phases_RMF_Waleca"+quark_interact+"_Mark.pdf")
    #plt.savefig("figures/tests/figures_xeos_note/phases_RMF_Waleca_extreme_cases.pdf")
    plt.show()


if(testing_total_eos_B_RMF==True):
    plot_CFL = False

    time_0 = time.perf_counter()

    N_B = 3

    B_vec = np.linspace(150,220,N_B)
    N = 300
    N_RMF = 300
    N_CFL = 300

    N_CFL_kaons = 300
    Delta = 100
    m_s = 150
    c = 0.3

    mu_q_max = 700

    plt.figure(1)
    plt.xlim(320,700)
    plt.ylim(0,2000)
    plt.title("$\\Delta$ = "+str(Delta)+", $m_s$ = "+str(m_s)+", $c$ = "+str(c))
    plt.xlabel("$\\mu_q$[MeV]")
    plt.ylabel("$P$[MeV/fm$^3$]")

    plt.figure(2)
    plt.xlim(0,4500)
    plt.ylim(0,1500)
    plt.title("$\\Delta$ = "+str(Delta)+", $m_s$ = "+str(m_s)+", $c$ = "+str(c))
    plt.xlabel("$\\epsilon$[MeV/fm$^3$]")
    plt.ylabel("P[MeV/fm$^3$]")

    plt.figure(3)
    plt.xlim(0,5)
    plt.ylim(0,2000)
    plt.title("$\\Delta$ = "+str(Delta)+", $m_s$ = "+str(m_s)+", $c$ = "+str(c))
    plt.xlabel("$\\rho$[fm$^{-3}$]")
    plt.ylabel("P[MeV/fm$^3$]")

    plt.figure(4)
    plt.xlim(8,15)
    plt.ylim(0,2.5)
    plt.xlabel("R[km]")
    plt.ylabel("M[$M_\\odot$]")

    plt.figure(5)
    plt.xlim(0,3)
    plt.ylim(0,1.5)
    plt.xlabel("$\\rho$[fm$^{-3}$]")
    plt.ylabel("v$^2$[1]")

    parameter_file = open("figures/tests/parameter_varying/B/parameters_RMF.txt",'w')
    parameter_file.write("B, Delta, m_s \n")
    for i in range(N_B):
        B = B_vec[i]
        print(B)
        eos = exotic_eos.CFL_EoS(N_CFL,N_CFL_kaons,B,Delta,m_s,N=N,eos_name="RMF",c=c,N_RMF=N_RMF,mu_q_max=mu_q_max,TOV=True,FSUGold_filename="FSUGoldgarnet.inp")
        parameter_file.write(str(B)+" "+str(Delta)+" "+str(m_s)+"\n")

        wrt.write_EoS_to_file(eos,"figures/tests/parameter_varying/B/eos_files_RMF/"+str(i).zfill(6),crust=True)


        plt.figure(1)
        plt.plot(eos.mu_q_vec,eos.P_vec,label = "B$^{1/4}$="+str(np.round(B,decimals=1))+"MeV")
        if(plot_CFL==True):
            plt.plot(eos.mu_q_CFL_vec,eos.P_CFL_vec,label="CFL")
        plt.legend()

        #print(eos.e_vec)
        #print(eos.P_vec)
        plt.figure(2)
        plt.plot(eos.e_vec,eos.P_vec,label = "B$^{1/4}$="+str(np.round(B,decimals=1))+"MeV")
        if(plot_CFL==True):
            plt.plot(eos.e_CFL_vec,eos.P_CFL_vec,label="CFL")
        plt.legend()

        plt.figure(3)
        plt.plot(eos.rho_vec,eos.P_vec,label = "B$^{1/4}$="+str(np.round(B,decimals=1))+"MeV")
        if(plot_CFL==True):
            plt.plot(eos.rho_CFL_vec,eos.P_CFL_vec,label="CFL")
        plt.legend()

        plt.figure(4)
        plt.plot(eos.R_vec,eos.M_vec,label = "B$^{1/4}$="+str(np.round(B,decimals=1))+"MeV")

        plt.figure(5)
        plt.plot(eos.rho_vec,np.gradient(eos.P_vec,eos.e_vec,edge_order=2),label = "B$^{1/4}$="+str(np.round(B,decimals=1))+"MeV")

    parameter_file.close()

    plt.figure(1)
    plt.plot(eos.eos_RMF.mu_n_vec/3,eos.eos_RMF.P_vec,'--',label = "NM",color = "black")
    plt.legend()

    plt.figure(2)
    plt.plot(eos.eos_RMF.e_vec,eos.eos_RMF.P_vec,'--',label = "NM",color = "black")
    plt.legend()

    plt.figure(3)
    plt.plot(eos.eos_RMF.rho_vec,eos.eos_RMF.P_vec,'--',label = "NM",color = "black")
    plt.legend()

    plt.figure(4)
    plt.legend()

    plt.figure(5)
    plt.legend()

    print("Time spent:", time.perf_counter()-time_0)
    plt.figure(1)
    plt.savefig("figures/tests/parameter_varying/B/P_of_mu_q_RMF.pdf")
    plt.figure(2)
    plt.savefig("figures/tests/parameter_varying/B/P_of_e_RMF.pdf")
    plt.figure(3)
    plt.savefig("figures/tests/parameter_varying/B/P_of_rho_RMF.pdf")
    plt.figure(4)
    plt.savefig("figures/tests/parameter_varying/B/MR_RMF.pdf")
    plt.figure(5)
    plt.savefig("figures/tests/parameter_varying/B/v2_RMF.pdf")
    plt.show()

if(testing_total_eos_Delta_RMF==True):

    time_0 = time.perf_counter()

    N_Delta = 10

    Delta_vec = np.linspace(50,150,N_Delta)

    #First create apr eos, so we dont have to call it repeatedly
    N_apr03 = 2000
    eos_apr03 = APR_eos.apr03_EoS(N_apr03,rho_min_apr03=0.1,rho_max_apr03=2)

    N_CFL = 2000
    N_CFL_kaons = 2000
    B = 190
    m_s = 150
    c = 0.3

    plt.figure(1)
    plt.xlim(320,480)
    plt.ylim(0,400)
    plt.title("$m_s$ = "+str(m_s)+", $B$ = "+str(B)+", $c$ = "+str(c))
    plt.xlabel("$\\mu_q$[MeV]")
    plt.ylabel("$P$[MeV/fm$^3$]")

    plt.figure(2)
    plt.xlim(0,1000)
    plt.ylim(0,400)
    plt.title("$m_s$ = "+str(m_s)+", $B$ = "+str(B)+", $c$ = "+str(c))
    plt.xlabel("$\\epsilon$[MeV/fm$^3$]")
    plt.ylabel("P[MeV/fm$^3$]")

    plt.figure(3)
    plt.xlim(0,2)
    plt.ylim(0,400)
    plt.title("$m_s$ = "+str(m_s)+", $B$ = "+str(B)+", $c$ = "+str(c))
    plt.xlabel("$\\rho$[fm$^{-3}$]")
    plt.ylabel("P[MeV/fm$^3$]")

    parameter_file = open("figures/tests/parameter_varying/Delta/parameters_RMF.txt",'w')
    parameter_file.write("B, Delta, m_s \n")
    for i in range(N_Delta):
        Delta = Delta_vec[i]
        eos = exotic_eos.CFL_EoS(N_CFL,N_CFL_kaons,B,Delta,m_s,eos_apr03=eos_apr03,c=c)
        parameter_file.write(str(B)+" "+str(Delta)+" "+str(m_s)+"\n")

        #Remove zeros from vectors
        wrt.write_EoS_to_file(eos,"figures/tests/parameter_varying/Delta/eos_files_RMF/"+str(i).zfill(6),crust=False)
        mu_q_vec = eos.mu_q_vec[eos.mu_q_vec==0] = np.nan
        P_vec = eos.P_vec[eos.P_vec==0] = np.nan
        e_vec = eos.e_vec[eos.e_vec==0] = np.nan
        ##

        plt.figure(1)
        plt.plot(eos.mu_q_vec,eos.P_vec,label = "$\\Delta$="+str(np.round(Delta,decimals=1))+"MeV")
        plt.legend()

        plt.figure(2)
        plt.plot(eos.e_vec,eos.P_vec,label = "$\\Delta$="+str(np.round(Delta,decimals=1))+"MeV")
        plt.legend()

        plt.figure(3)
        plt.plot(eos.rho_vec,eos.P_vec,label = "$\\Delta$="+str(np.round(Delta,decimals=1))+"MeV")
        plt.legend()

    parameter_file.close()

    plt.figure(1)
    plt.plot(eos.eos_apr03.mu_n_apr03_combined_vec/3,eos.eos_apr03.P_apr03_combined_vec,label = "NM",color = "black")
    plt.legend()

    plt.figure(2)
    plt.plot(eos.eos_apr03.e_apr03_combined_vec,eos.eos_apr03.P_apr03_combined_vec,label = "NM",color = "black")
    plt.legend()

    plt.figure(3)
    plt.plot(eos.eos_apr03.rho_apr03_combined_vec,eos.eos_apr03.P_apr03_combined_vec,label = "NM",color = "black")
    plt.legend()

    print("Time spent:", time.perf_counter()-time_0)
    plt.figure(1)
    plt.savefig("figures/tests/parameter_varying/Delta/P_of_mu_q_RMF.pdf")
    plt.figure(2)
    plt.savefig("figures/tests/parameter_varying/Delta/P_of_e_RMF.pdf")
    plt.figure(3)
    plt.savefig("figures/tests/parameter_varying/Delta/P_of_rho_RMF.pdf")

    plt.show()

if(testing_total_eos_m_s==True):

    time_0 = time.perf_counter()

    N_m_s = 10

    m_s_vec = np.linspace(50,250,N_m_s)

    #First create apr eos, so we dont have to call it repeatedly
    N_apr03 = 2000
    eos_apr03 = APR03_eos.apr03_EoS(N_apr03,rho_min_apr03=0.1,rho_max_apr03=2)

    N_CFL = 2000
    N_CFL_kaons = 2000
    B = 190
    Delta = 100
    c = 0.3

    plt.figure(1)
    plt.xlim(320,480)
    plt.ylim(0,400)
    plt.title("$\\Delta$ = "+str(Delta)+", $B$ = "+str(B)+", $c$ = "+str(c))
    plt.xlabel("$\\mu_q$[MeV]")
    plt.ylabel("$P$[MeV/fm$^3$]")

    plt.figure(2)
    plt.xlim(0,1000)
    plt.ylim(0,400)
    plt.title("$\\Delta$ = "+str(Delta)+", $B$ = "+str(B)+", $c$ = "+str(c))
    plt.xlabel("$\\epsilon$[MeV/fm$^3$]")
    plt.ylabel("P[MeV/fm$^3$]")

    plt.figure(3)
    plt.xlim(0,2)
    plt.ylim(0,400)
    plt.title("$\\Delta$ = "+str(Delta)+", $B$ = "+str(B)+", $c$ = "+str(c))
    plt.xlabel("$\\rho$[fm$^{-3}$]")
    plt.ylabel("P[MeV/fm$^3$]")

    parameter_file = open("figures/tests/parameter_varying/m_s/parameters_RMF.txt",'w')
    parameter_file.write("B, Delta, m_s \n")
    for i in range(N_m_s):
        m_s = m_s_vec[i]
        eos = exotic_eos.CFL_EoS(N_CFL,N_CFL_kaons,B,Delta,m_s,eos_apr03=eos_apr03,c=c)
        parameter_file.write(str(B)+" "+str(Delta)+" "+str(m_s)+"\n")

        wrt.write_EoS_to_file(eos,"figures/tests/parameter_varying/m_s/eos_files_RMF/"+str(i).zfill(6),crust=False)

        #Remove zeros from vectors
        mu_q_vec = eos.mu_q_vec[eos.mu_q_vec==0] = np.nan
        P_vec = eos.P_vec[eos.P_vec==0] = np.nan
        e_vec = eos.e_vec[eos.e_vec==0] = np.nan
        ##

        plt.figure(1)
        plt.plot(eos.mu_q_vec,eos.P_vec,label = "$m_s$="+str(np.round(m_s,decimals=1))+"MeV")
        plt.legend()

        plt.figure(2)
        plt.plot(eos.e_vec,eos.P_vec,label = "$m_s$="+str(np.round(m_s,decimals=1))+"MeV")
        plt.legend()

        plt.figure(3)
        plt.plot(eos.rho_vec,eos.P_vec,label = "$m_s$="+str(np.round(m_s,decimals=1))+"MeV")
        plt.legend()

    parameter_file.close()

    plt.figure(1)
    plt.plot(eos.eos_apr03.mu_n_apr03_combined_vec/3,eos.eos_apr03.P_apr03_combined_vec,label = "NM",color = "black")
    plt.legend()

    plt.figure(2)
    plt.plot(eos.eos_apr03.e_apr03_combined_vec,eos.eos_apr03.P_apr03_combined_vec,label = "NM",color = "black")
    plt.legend()

    plt.figure(3)
    plt.plot(eos.eos_apr03.rho_apr03_combined_vec,eos.eos_apr03.P_apr03_combined_vec,label = "NM",color = "black")
    plt.legend()

    print("Time spent:", time.perf_counter()-time_0)
    plt.figure(1)
    plt.savefig("figures/tests/parameter_varying/m_s/P_of_mu_q_RMF.pdf")
    plt.figure(2)
    plt.savefig("figures/tests/parameter_varying/m_s/P_of_e_RMF.pdf")
    plt.figure(3)
    plt.savefig("figures/tests/parameter_varying/m_s/P_of_rho_RMF.pdf")

    plt.show()

