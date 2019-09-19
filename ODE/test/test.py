# Size of variable arrays:
sizeAlgebraic = 10
sizeStates = 7
sizeConstants = 34
from math import *
from numpy import *
import matplotlib.pyplot as plt


def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (day)"
    legend_states[0] = "phi_I in component phi_I (cells_per_mm3)"
    legend_algebraic[6] = "alpha in component model_parameters (dimensionless)"
    legend_constants[0] = "k1 in component model_parameters (dimensionless)"
    legend_constants[1] = "k2 in component model_parameters (per_day)"
    legend_constants[2] = "k3 in component model_parameters (mm3_per_cells)"
    legend_constants[3] = "k5 in component model_parameters (mm3_per_cells)"
    legend_constants[4] = "k6 in component model_parameters (mm3_per_microg)"
    legend_constants[5] = "d1 in component model_parameters (per_day)"
    legend_states[1] = "phi_R in component phi_R (cells_per_mm3)"
    legend_algebraic[0] = "K_T in component K_T (cells_per_mm3_per_day)"
    legend_states[2] = "F in component F (cells_per_mm3)"
    legend_states[3] = "C in component C (microg_per_mm3)"
    legend_states[4] = "T in component T (pg_per_mm3)"
    legend_algebraic[1] = "Apligraf in component T (pg_per_mm3_per_day)"
    legend_constants[6] = "k4 in component model_parameters (pg_per_cells_per_day)"
    legend_constants[7] = "k7 in component model_parameters (pg_per_cells_per_day)"
    legend_constants[8] = "d2 in component model_parameters (per_day)"
    legend_states[5] = "P in component P (pg_per_mm3)"
    legend_algebraic[2] = "Apligraf in component P (pg_per_mm3_per_day)"
    legend_constants[9] = "k8 in component model_parameters (pg_per_cells_per_day)"
    legend_constants[10] = "k9 in component model_parameters (pg_per_cells_per_day)"
    legend_constants[11] = "d3 in component model_parameters (per_day)"
    legend_algebraic[3] = "Apligraf in component F (cells_per_mm3_per_day)"
    legend_constants[12] = "k10 in component model_parameters (per_day)"
    legend_constants[13] = "d4 in component model_parameters (per_day)"
    legend_algebraic[7] = "M_P in component M_P (cells_per_mm3_per_day)"
    legend_algebraic[4] = "Apligraf in component C (microg_per_mm3_per_day)"
    legend_constants[14] = "k11 in component model_parameters (microg_per_cells_per_day)"
    legend_algebraic[8] = "f_T in component f_T (dimensionless)"
    legend_algebraic[9] = "g_C in component g_C (dimensionless)"
    legend_constants[15] = "d5 in component model_parameters (mm3_per_cells_per_day)"
    legend_states[6] = "H in component H (microg_per_mm3)"
    legend_algebraic[5] = "Apligraf in component H (microg_per_mm3_per_day)"
    legend_constants[16] = "k12 in component model_parameters (microg_per_cells_per_day)"
    legend_constants[17] = "d6 in component model_parameters (per_day)"
    legend_constants[18] = "tau1 in component K_T (mm6_cells_per_pg3_day)"
    legend_constants[19] = "tau2 in component K_T (mm3_cells_per_pg2_day)"
    legend_constants[20] = "tau3 in component K_T (cells_per_pg_per_day)"
    legend_constants[21] = "tau4 in component K_T (cells_per_mm3_per_day)"
    legend_constants[22] = "tau1 in component M_P (mm6_cells_per_pg3_day)"
    legend_constants[23] = "tau2 in component M_P (mm3_cells_per_pg2_day)"
    legend_constants[24] = "tau3 in component M_P (cells_per_pg_per_day)"
    legend_constants[25] = "tau4 in component M_P (cells_per_mm3_per_day)"
    legend_constants[26] = "tau1 in component f_T (mm9_per_pg3)"
    legend_constants[27] = "tau2 in component f_T (mm6_per_pg2)"
    legend_constants[28] = "tau3 in component f_T (mm3_per_pg)"
    legend_constants[29] = "tau4 in component f_T (dimensionless)"
    legend_constants[30] = "tau1 in component g_C (mm9_per_microg3)"
    legend_constants[31] = "tau2 in component g_C (mm6_per_microg2)"
    legend_constants[32] = "tau3 in component g_C (mm3_per_microg)"
    legend_constants[33] = "tau4 in component g_C (dimensionless)"
    legend_rates[0] = "d/dt phi_I in component phi_I (cells_per_mm3)"
    legend_rates[1] = "d/dt phi_R in component phi_R (cells_per_mm3)"
    legend_rates[4] = "d/dt T in component T (pg_per_mm3)"
    legend_rates[5] = "d/dt P in component P (pg_per_mm3)"
    legend_rates[2] = "d/dt F in component F (cells_per_mm3)"
    legend_rates[3] = "d/dt C in component C (microg_per_mm3)"
    legend_rates[6] = "d/dt H in component H (microg_per_mm3)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 200.0
    constants[0] = 0.05
    constants[1] = 0.693
    constants[2] = 0.002
    constants[3] = 0.0025
    constants[4] = 0.0004
    constants[5] = 0.2
    states[1] = 200.0
    states[2] = 50.0
    states[3] = 10.0
    states[4] = 6.0
    constants[6] = 0.07
    constants[7] = 0.004
    constants[8] = 9.1
    states[5] = 2.0
    constants[9] = 0.015
    constants[10] = 0.0015
    constants[11] = 4.0
    constants[12] = 0.924
    constants[13] = 2.5
    constants[14] = 5.0
    constants[15] = 1.5E-5
    states[6] = 0.01
    constants[16] = 0.001
    constants[17] = 0.7
    constants[18] = -2.47
    constants[19] = 21.94
    constants[20] = 6.41
    constants[21] = 1.75
    constants[22] = 15.333
    constants[23] = -167.21
    constants[24] = 452.38
    constants[25] = 2.6593
    constants[26] = 0.0092
    constants[27] = -0.1552
    constants[28] = 0.6279
    constants[29] = 0.2527
    constants[30] = -4.33E-10
    constants[31] = 0.0000009
    constants[32] = -0.00055
    constants[33] = 0.13
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[1] = custom_piecewise([greater_equal(voi , 0.00000) & less(voi , 28.0000), 0.00000 , greater_equal(voi , 28.0000) & less(voi , 29.0000), 0.400000 , greater_equal(voi , 29.0000) & less(voi , 35.0000), 0.00000 , greater_equal(voi , 35.0000) & less(voi , 36.0000), 0.400000 , greater_equal(voi , 36.0000) & less(voi , 42.0000), 0.00000 , greater_equal(voi , 42.0000) & less(voi , 43.0000), 0.400000 , greater_equal(voi , 43.0000) & less(voi , 49.0000), 0.00000 , greater_equal(voi , 49.0000) & less(voi , 50.0000), 0.400000 , greater_equal(voi , 50.0000) & less(voi , 56.0000), 0.00000 , greater_equal(voi , 56.0000) & less(voi , 57.0000), 0.400000 , greater_equal(voi , 57.0000) & less(voi , 63.0000), 0.00000 , greater_equal(voi , 63.0000) & less(voi , 64.0000), 0.400000 , greater_equal(voi , 64.0000) & less(voi , 70.0000), 0.00000 , greater_equal(voi , 70.0000) & less(voi , 71.0000), 0.400000 , greater_equal(voi , 71.0000) & less(voi , 77.0000), 0.00000 , greater_equal(voi , 77.0000) & less(voi , 78.0000), 0.400000 , True, 0.00000])
    rates[4] = (constants[6]*states[0]+constants[7]*states[2]+algebraic[1])-constants[8]*states[4]
    algebraic[2] = custom_piecewise([greater_equal(voi , 0.00000) & less(voi , 28.0000), 0.00000 , greater_equal(voi , 28.0000) & less(voi , 29.0000), 1.00000 , greater_equal(voi , 29.0000) & less(voi , 35.0000), 0.00000 , greater_equal(voi , 35.0000) & less(voi , 36.0000), 1.00000 , greater_equal(voi , 36.0000) & less(voi , 42.0000), 0.00000 , greater_equal(voi , 42.0000) & less(voi , 43.0000), 1.00000 , greater_equal(voi , 43.0000) & less(voi , 49.0000), 0.00000 , greater_equal(voi , 49.0000) & less(voi , 50.0000), 1.00000 , greater_equal(voi , 50.0000) & less(voi , 56.0000), 0.00000 , greater_equal(voi , 56.0000) & less(voi , 57.0000), 1.00000 , greater_equal(voi , 57.0000) & less(voi , 63.0000), 0.00000 , greater_equal(voi , 63.0000) & less(voi , 64.0000), 1.00000 , greater_equal(voi , 64.0000) & less(voi , 70.0000), 0.00000 , greater_equal(voi , 70.0000) & less(voi , 71.0000), 1.00000 , greater_equal(voi , 71.0000) & less(voi , 77.0000), 0.00000 , greater_equal(voi , 77.0000) & less(voi , 78.0000), 1.00000 , True, 0.00000])
    rates[5] = (constants[9]*(states[0]+states[1])+constants[10]*states[2]+algebraic[2])-constants[11]*states[5]
    algebraic[5] = custom_piecewise([greater_equal(voi , 0.00000) & less(voi , 28.0000), 0.00000 , greater_equal(voi , 28.0000) & less(voi , 29.0000), 80.0000 , greater_equal(voi , 29.0000) & less(voi , 35.0000), 0.00000 , greater_equal(voi , 35.0000) & less(voi , 36.0000), 80.0000 , greater_equal(voi , 36.0000) & less(voi , 42.0000), 0.00000 , greater_equal(voi , 42.0000) & less(voi , 43.0000), 80.0000 , greater_equal(voi , 43.0000) & less(voi , 49.0000), 0.00000 , greater_equal(voi , 49.0000) & less(voi , 50.0000), 80.0000 , greater_equal(voi , 50.0000) & less(voi , 56.0000), 0.00000 , greater_equal(voi , 56.0000) & less(voi , 57.0000), 80.0000 , greater_equal(voi , 57.0000) & less(voi , 63.0000), 0.00000 , greater_equal(voi , 63.0000) & less(voi , 64.0000), 80.0000 , greater_equal(voi , 64.0000) & less(voi , 70.0000), 0.00000 , greater_equal(voi , 70.0000) & less(voi , 71.0000), 80.0000 , greater_equal(voi , 71.0000) & less(voi , 77.0000), 0.00000 , greater_equal(voi , 77.0000) & less(voi , 78.0000), 80.0000 , True, 0.00000])
    rates[6] = (constants[16]*states[2]+algebraic[5])-constants[17]*states[6]
    algebraic[6] = -(0.197000*log10(states[6]))+0.440700
    algebraic[0] = constants[18]*(power(states[4], 3.00000))+constants[19]*(power(states[4], 2.00000))+constants[20]*states[4]+constants[21]
    rates[0] = (algebraic[6]*algebraic[0]+constants[0]*constants[1]*states[0]*(1.00000-(constants[2]*(states[0]+states[1])+constants[3]*states[2]+constants[4]*states[3])))-constants[5]*states[0]
    rates[1] = ((1.00000-algebraic[6])*algebraic[0]+constants[0]*constants[1]*states[1]*(1.00000-(constants[2]*(states[0]+states[1])+constants[3]*states[2]+constants[4]*states[3])))-constants[5]*states[1]
    algebraic[3] = custom_piecewise([greater_equal(voi , 0.00000) & less(voi , 28.0000), 0.00000 , greater_equal(voi , 28.0000) & less(voi , 29.0000), 8000.00 , greater_equal(voi , 29.0000) & less(voi , 35.0000), 0.00000 , greater_equal(voi , 35.0000) & less(voi , 36.0000), 8000.00 , greater_equal(voi , 36.0000) & less(voi , 42.0000), 0.00000 , greater_equal(voi , 42.0000) & less(voi , 43.0000), 8000.00 , greater_equal(voi , 43.0000) & less(voi , 49.0000), 0.00000 , greater_equal(voi , 49.0000) & less(voi , 50.0000), 8000.00 , greater_equal(voi , 50.0000) & less(voi , 56.0000), 0.00000 , greater_equal(voi , 56.0000) & less(voi , 57.0000), 8000.00 , greater_equal(voi , 57.0000) & less(voi , 63.0000), 0.00000 , greater_equal(voi , 63.0000) & less(voi , 64.0000), 8000.00 , greater_equal(voi , 64.0000) & less(voi , 70.0000), 0.00000 , greater_equal(voi , 70.0000) & less(voi , 71.0000), 8000.00 , greater_equal(voi , 71.0000) & less(voi , 77.0000), 0.00000 , greater_equal(voi , 77.0000) & less(voi , 78.0000), 8000.00 , True, 0.00000])
    algebraic[7] = constants[22]*(power(states[5], 3.00000))+constants[23]*(power(states[5], 2.00000))+constants[24]*states[5]+constants[25]
    rates[2] = (algebraic[7]+constants[12]*states[2]*(1.00000-(constants[2]*(states[0]+states[1])+constants[3]*states[2]+constants[4]*states[3]))+algebraic[3])-constants[13]*states[2]
    algebraic[4] = custom_piecewise([greater_equal(voi , 0.00000) & less(voi , 28.0000), 0.00000 , greater_equal(voi , 28.0000) & less(voi , 29.0000), 18.7500 , greater_equal(voi , 29.0000) & less(voi , 35.0000), 0.00000 , greater_equal(voi , 35.0000) & less(voi , 36.0000), 18.7500 , greater_equal(voi , 36.0000) & less(voi , 42.0000), 0.00000 , greater_equal(voi , 42.0000) & less(voi , 43.0000), 18.7500 , greater_equal(voi , 43.0000) & less(voi , 49.0000), 0.00000 , greater_equal(voi , 49.0000) & less(voi , 50.0000), 18.7500 , greater_equal(voi , 50.0000) & less(voi , 56.0000), 0.00000 , greater_equal(voi , 56.0000) & less(voi , 57.0000), 18.7500 , greater_equal(voi , 57.0000) & less(voi , 63.0000), 0.00000 , greater_equal(voi , 63.0000) & less(voi , 64.0000), 18.7500 , greater_equal(voi , 64.0000) & less(voi , 70.0000), 0.00000 , greater_equal(voi , 70.0000) & less(voi , 71.0000), 18.7500 , greater_equal(voi , 71.0000) & less(voi , 77.0000), 0.00000 , greater_equal(voi , 77.0000) & less(voi , 78.0000), 18.7500 , True, 0.00000])
    algebraic[8] = constants[26]*(power(states[4], 3.00000))+constants[27]*(power(states[4], 2.00000))+constants[28]*states[4]+constants[29]
    algebraic[9] = constants[30]*(power(states[3], 3.00000))+constants[31]*(power(states[3], 2.00000))+constants[32]*states[3]+constants[33]
    rates[3] = (constants[14]*states[2]*algebraic[8]*algebraic[9]+algebraic[4])-constants[15]*states[2]*states[3]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[1] = custom_piecewise([greater_equal(voi , 0.00000) & less(voi , 28.0000), 0.00000 , greater_equal(voi , 28.0000) & less(voi , 29.0000), 0.400000 , greater_equal(voi , 29.0000) & less(voi , 35.0000), 0.00000 , greater_equal(voi , 35.0000) & less(voi , 36.0000), 0.400000 , greater_equal(voi , 36.0000) & less(voi , 42.0000), 0.00000 , greater_equal(voi , 42.0000) & less(voi , 43.0000), 0.400000 , greater_equal(voi , 43.0000) & less(voi , 49.0000), 0.00000 , greater_equal(voi , 49.0000) & less(voi , 50.0000), 0.400000 , greater_equal(voi , 50.0000) & less(voi , 56.0000), 0.00000 , greater_equal(voi , 56.0000) & less(voi , 57.0000), 0.400000 , greater_equal(voi , 57.0000) & less(voi , 63.0000), 0.00000 , greater_equal(voi , 63.0000) & less(voi , 64.0000), 0.400000 , greater_equal(voi , 64.0000) & less(voi , 70.0000), 0.00000 , greater_equal(voi , 70.0000) & less(voi , 71.0000), 0.400000 , greater_equal(voi , 71.0000) & less(voi , 77.0000), 0.00000 , greater_equal(voi , 77.0000) & less(voi , 78.0000), 0.400000 , True, 0.00000])
    algebraic[2] = custom_piecewise([greater_equal(voi , 0.00000) & less(voi , 28.0000), 0.00000 , greater_equal(voi , 28.0000) & less(voi , 29.0000), 1.00000 , greater_equal(voi , 29.0000) & less(voi , 35.0000), 0.00000 , greater_equal(voi , 35.0000) & less(voi , 36.0000), 1.00000 , greater_equal(voi , 36.0000) & less(voi , 42.0000), 0.00000 , greater_equal(voi , 42.0000) & less(voi , 43.0000), 1.00000 , greater_equal(voi , 43.0000) & less(voi , 49.0000), 0.00000 , greater_equal(voi , 49.0000) & less(voi , 50.0000), 1.00000 , greater_equal(voi , 50.0000) & less(voi , 56.0000), 0.00000 , greater_equal(voi , 56.0000) & less(voi , 57.0000), 1.00000 , greater_equal(voi , 57.0000) & less(voi , 63.0000), 0.00000 , greater_equal(voi , 63.0000) & less(voi , 64.0000), 1.00000 , greater_equal(voi , 64.0000) & less(voi , 70.0000), 0.00000 , greater_equal(voi , 70.0000) & less(voi , 71.0000), 1.00000 , greater_equal(voi , 71.0000) & less(voi , 77.0000), 0.00000 , greater_equal(voi , 77.0000) & less(voi , 78.0000), 1.00000 , True, 0.00000])
    algebraic[5] = custom_piecewise([greater_equal(voi , 0.00000) & less(voi , 28.0000), 0.00000 , greater_equal(voi , 28.0000) & less(voi , 29.0000), 80.0000 , greater_equal(voi , 29.0000) & less(voi , 35.0000), 0.00000 , greater_equal(voi , 35.0000) & less(voi , 36.0000), 80.0000 , greater_equal(voi , 36.0000) & less(voi , 42.0000), 0.00000 , greater_equal(voi , 42.0000) & less(voi , 43.0000), 80.0000 , greater_equal(voi , 43.0000) & less(voi , 49.0000), 0.00000 , greater_equal(voi , 49.0000) & less(voi , 50.0000), 80.0000 , greater_equal(voi , 50.0000) & less(voi , 56.0000), 0.00000 , greater_equal(voi , 56.0000) & less(voi , 57.0000), 80.0000 , greater_equal(voi , 57.0000) & less(voi , 63.0000), 0.00000 , greater_equal(voi , 63.0000) & less(voi , 64.0000), 80.0000 , greater_equal(voi , 64.0000) & less(voi , 70.0000), 0.00000 , greater_equal(voi , 70.0000) & less(voi , 71.0000), 80.0000 , greater_equal(voi , 71.0000) & less(voi , 77.0000), 0.00000 , greater_equal(voi , 77.0000) & less(voi , 78.0000), 80.0000 , True, 0.00000])
    algebraic[6] = -(0.197000*log10(states[6]))+0.440700
    algebraic[0] = constants[18]*(power(states[4], 3.00000))+constants[19]*(power(states[4], 2.00000))+constants[20]*states[4]+constants[21]
    algebraic[3] = custom_piecewise([greater_equal(voi , 0.00000) & less(voi , 28.0000), 0.00000 , greater_equal(voi , 28.0000) & less(voi , 29.0000), 8000.00 , greater_equal(voi , 29.0000) & less(voi , 35.0000), 0.00000 , greater_equal(voi , 35.0000) & less(voi , 36.0000), 8000.00 , greater_equal(voi , 36.0000) & less(voi , 42.0000), 0.00000 , greater_equal(voi , 42.0000) & less(voi , 43.0000), 8000.00 , greater_equal(voi , 43.0000) & less(voi , 49.0000), 0.00000 , greater_equal(voi , 49.0000) & less(voi , 50.0000), 8000.00 , greater_equal(voi , 50.0000) & less(voi , 56.0000), 0.00000 , greater_equal(voi , 56.0000) & less(voi , 57.0000), 8000.00 , greater_equal(voi , 57.0000) & less(voi , 63.0000), 0.00000 , greater_equal(voi , 63.0000) & less(voi , 64.0000), 8000.00 , greater_equal(voi , 64.0000) & less(voi , 70.0000), 0.00000 , greater_equal(voi , 70.0000) & less(voi , 71.0000), 8000.00 , greater_equal(voi , 71.0000) & less(voi , 77.0000), 0.00000 , greater_equal(voi , 77.0000) & less(voi , 78.0000), 8000.00 , True, 0.00000])
    algebraic[7] = constants[22]*(power(states[5], 3.00000))+constants[23]*(power(states[5], 2.00000))+constants[24]*states[5]+constants[25]
    algebraic[4] = custom_piecewise([greater_equal(voi , 0.00000) & less(voi , 28.0000), 0.00000 , greater_equal(voi , 28.0000) & less(voi , 29.0000), 18.7500 , greater_equal(voi , 29.0000) & less(voi , 35.0000), 0.00000 , greater_equal(voi , 35.0000) & less(voi , 36.0000), 18.7500 , greater_equal(voi , 36.0000) & less(voi , 42.0000), 0.00000 , greater_equal(voi , 42.0000) & less(voi , 43.0000), 18.7500 , greater_equal(voi , 43.0000) & less(voi , 49.0000), 0.00000 , greater_equal(voi , 49.0000) & less(voi , 50.0000), 18.7500 , greater_equal(voi , 50.0000) & less(voi , 56.0000), 0.00000 , greater_equal(voi , 56.0000) & less(voi , 57.0000), 18.7500 , greater_equal(voi , 57.0000) & less(voi , 63.0000), 0.00000 , greater_equal(voi , 63.0000) & less(voi , 64.0000), 18.7500 , greater_equal(voi , 64.0000) & less(voi , 70.0000), 0.00000 , greater_equal(voi , 70.0000) & less(voi , 71.0000), 18.7500 , greater_equal(voi , 71.0000) & less(voi , 77.0000), 0.00000 , greater_equal(voi , 77.0000) & less(voi , 78.0000), 18.7500 , True, 0.00000])
    algebraic[8] = constants[26]*(power(states[4], 3.00000))+constants[27]*(power(states[4], 2.00000))+constants[28]*states[4]+constants[29]
    algebraic[9] = constants[30]*(power(states[3], 3.00000))+constants[31]*(power(states[3], 2.00000))+constants[32]*states[3]+constants[33]
    return algebraic

def custom_piecewise(cases):
    """Compute result of a piecewise function"""
    return select(cases[0::2],cases[1::2])

def solve_model():
    """Solve model with ODE solver"""
    from scipy.integrate import ode
    # Initialise constants and state variables
    (init_states, constants) = initConsts()

    # Set timespan to solve over
    voi = linspace(0, 10, 500)

    # Construct ODE object to solve
    r = ode(computeRates)
    r.set_integrator('vode', method='bdf', atol=1e-06, rtol=1e-06, max_step=1)
    r.set_initial_value(init_states, voi[0])
    r.set_f_params(constants)

    # Solve model
    states = array([[0.0] * len(voi)] * sizeStates)
    states[:,0] = init_states
    for (i,t) in enumerate(voi[1:]):
        if r.successful():
            r.integrate(t)
            states[:,i+1] = r.y
        else:
            break

    # Compute algebraic variables
    algebraic = computeAlgebraic(constants, states, voi)
    return (voi, states, algebraic)

def plot_model(voi, states, algebraic):
    """Plot variables against variable of integration"""
    import pylab
    (legend_states, legend_algebraic, legend_voi, legend_constants) = createLegends()
    pylab.figure(1)
    pylab.plot(voi,vstack((states,algebraic)).T)
    pylab.xlabel(legend_voi)
    pylab.legend(legend_states + legend_algebraic, loc='best')
    pylab.show()


def custom_piecewise(cases):
    """Compute result of a piecewise function"""
    return select(cases[0::2],cases[1::2])

if __name__ == "__main__":
    (voi, states, algebraic) = solve_model()
    plot_model(voi, states, algebraic)

    hoi = custom_piecewise(
        [greater_equal(voi, 0.00000) & less(voi, 28.0000), 1.00000, greater_equal(voi, 28.0000) & less(voi, 29.0000),
         0.400000, greater_equal(voi, 29.0000) & less(voi, 35.0000), 0.00000,
         greater_equal(voi, 35.0000) & less(voi, 36.0000), 0.400000, greater_equal(voi, 36.0000) & less(voi, 42.0000),
         0.00000, greater_equal(voi, 42.0000) & less(voi, 43.0000), 0.400000,
         greater_equal(voi, 43.0000) & less(voi, 49.0000), 0.00000, greater_equal(voi, 49.0000) & less(voi, 50.0000),
         0.400000, greater_equal(voi, 50.0000) & less(voi, 56.0000), 0.00000,
         greater_equal(voi, 56.0000) & less(voi, 57.0000), 0.400000, greater_equal(voi, 57.0000) & less(voi, 63.0000),
         0.00000, greater_equal(voi, 63.0000) & less(voi, 64.0000), 0.400000,
         greater_equal(voi, 64.0000) & less(voi, 70.0000), 0.00000, greater_equal(voi, 70.0000) & less(voi, 71.0000),
         0.400000, greater_equal(voi, 71.0000) & less(voi, 77.0000), 0.00000,
         greater_equal(voi, 77.0000) & less(voi, 78.0000), 0.400000, True, 0.00000])
    plt.plot(hoi)
    plt.show()


