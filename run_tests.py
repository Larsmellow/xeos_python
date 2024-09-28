import tests_new as tst

'''
Uncomment any line to run a specific test
'''

'''
Nomenclature:
    LDP: Low density phase
    HDP: High density phase
    SNM: Symmetric nuclear matter
    PNM: Pure neutron matter
'''

'''
Testing aspects of apr03

Input parameters:
    N:          number of points used
    figsize:    figure size

Plots:
    1) Energy per nucleon E/A as a function of density rho for SNM and PNM
        in the LDP and HDP

    2) Energy per nucleon E/A as a function of density rho for matter in beta equilbrium
        in the LDP and HDP

    3) Proton fraction as a function of density rho

    4) Energy density as a function of density rho

    5) Energy density as a function of pressure

    6) Neutron and proton chemical potentials mun and mup, as a function of density rho
        in the LDP and HDP
'''
#tst.testing_apr03(N=1000)


'''
Testing the CFL phases by plotting chemical potentials and pressures

Input parameters:
    B:                      Fourth root of the Bag constant
    Delta:                  Pairing gap in MeV
    m_s:                    Strange quark mass in MeV
    c:                      Phenomenological quark coupling constant, dimensionless
    N:                      Number of points used in the CFL phase
    N_kaons:                Number of points used in the mixed phase
    N_low_dens:             number of points used in the low density phase
    eos_name:               Name of the low density phase used. So far only 'APR' and 'RMF' are supported
    mix_phase:              If set to False, we do not compute the mixed phase, but insted go from
                            neutron matter to pure CFL
    RMF_filename:           Filename used for parameters in RMF model
    plot_original_phases:   If set to True, show comparison to a simple Waleca model. Also,
                            use parameters that are more similar to this Waleca model
'''
#tst.testing_CFL(B=190,Delta=100,m_s=150,c=0.0,N=100,N_kaons=300,N_low_dens=300,eos_name="APR")
#tst.testing_CFL(B=190,Delta=100,m_s=150,c=0.0,N=100,N_kaons=300,N_low_dens=300,eos_name="RMF")
#tst.testing_CFL(B=190,Delta=100,m_s=150,c=0.0,N=100,N_kaons=300,N_low_dens=300,eos_name="RMF",mix_phase=False)
#tst.testing_CFL(B=190,Delta=100,m_s=150,c=0.3,N=100,N_kaons=300,N_low_dens=300,eos_name="RMF",mix_phase=False)
#tst.testing_CFL(B=190,Delta=100,m_s=150,c=0.0,N=100,N_kaons=300,N_low_dens=300,eos_name="RMF",plot_original_phases=True)
#tst.testing_CFL(B=190,Delta=100,m_s=150,c=0.3,N=300,N_kaons=300,N_low_dens=300,eos_name="RMF",plot_original_phases=True)


'''
Test full eos including mass-radius relations

Input parameters:
    variable:               Either "B", "Delta", "m_s" or "c". Sets the parameter we vary in the test
    variable_range:         The range we vary the parameter over
    N_variables:            The number of different variables we choose
    TOV:                    Set to True if we compute the Mass, Radius and deformability
    B:                      Fourth root of the Bag constant
    Delta:                  Pairing gap in MeV
    m_s:                    Strange quark mass in MeV
    c:                      Phenomenological quark coupling constant, dimensionless
    N:                      Number of points used in the CFL phase
    N_kaons:                Number of points used in the mixed phase
    N_low_dens:             number of points used in the low density phase
    eos_name:               Name of the low density phase used. So far only 'APR' and 'RMF' are supported
    mix_phase:              If set to False, we do not compute the mixed phase, but insted go from
                            neutron matter to pure CFL
    RMF_filename:           Filename used for parameters in RMF model
    plot_original_phases:   If set to True, show comparison to a simple Waleca model. Also,
                            use parameters that are more similar to this Waleca model

'''
#tst.testing_total_eos(variable="B",variable_range=[175,220],N_variable=5,N=300,N_kaons=300,N_low_dens=300,eos_name="RMF",TOV=True)
#tst.testing_total_eos(variable="Delta",variable_range=[60,140],N_variable=5,N=300,N_kaons=300,N_low_dens=300,eos_name="RMF",TOV=True)
#tst.testing_total_eos(variable="m_s",variable_range=[130,180],N_variable=5,N=300,N_kaons=300,N_low_dens=300,eos_name="RMF",TOV=True)
#tst.testing_total_eos(variable="c",variable_range=[0,0.4],N_variable=5,N=300,N_kaons=300,N_low_dens=300,eos_name="RMF",TOV=True)

'''
Test that creating parameter sets works

Input parameters:
    filename:           Filename we write the parameters to
    N:                  Number of parameter sets generated
    parameter_ranges:   List of lists with the ranges of each parameter
    distributions:      List containing the names of distributions used
                        for each paramerer. So far uniform and gauss
                        is supported
'''
#filename="runs/tests/parameters.txt"
#tst.test_writing_parameter_sets(filename,N=10000,parameter_ranges=[[175,220],[40,160],[100,200],[0,0.6]],distributions=["uniform","uniform","uniform","uniform"])
#tst.test_writing_parameter_sets(filename,N=10000,parameter_ranges=[[175,220],[40,160],[100,200],[0,0.6]],distributions=["gauss","gauss","gauss","gauss"])


'''
Test that writing eos to file works

Input parameters:
    filename:   Filename we write eos to
'''
#tst.test_write_and_read_eos_to_file(filename="runs/tests/EoS_files/test.txt")

'''
Test if MR write to file works

Input parameters:
    filenmae:   Filename we write MR to
'''
#tst.test_write_and_read_MR_to_file(filename="runs/tests/MR_files/test.txt")


