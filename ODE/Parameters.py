﻿from collections import OrderedDict

_day = 1/1440.

phi_MRA = 0.083 * _day

mu_NR = 2.77 * _day
mu_NA = 2.77 * _day
mu_NDA = 0.05 * _day
mu_NDN = 0.05 * _day
mu_APE = 0.72 * _day
mu_APSfast = 111.65 * _day
mu_APSslow = 3.94 * _day
mu_APS = (mu_APSfast + mu_APSslow)
mu_D = 0.48 * _day
mu_G = 5 * _day
mu_MA = 0.07 * _day
mu_MR = 0.0033 * _day
mu_ACH = 2.7648 * _day  # https://www.nature.com/articles/7100023/tables/1
mu_CH = 2.7648 * _day  # https://www.nature.com/articles/7100023/tables/1
mu_ITM = 0.005 * _day

lamb_DNDN = 8.4 * _day
lamb_DG = 8.4 * _day
lamb_ITMNA = 0.45 * _day
lamb_APE = 0.00000444916 * _day
lamb_APS = 0.00000301394 * _day
lamb_GA = 0.55 * _day
lamb_ITMMA = 0.8 * _day
lamb_MANDA = 2.6 * _day

lamb_MANDN = 0.001 * _day
lamb_ITMD = 0.00745733413 * _day
lamb_ITMNDN = 0.00000000157 * _day
lamb_ITMG = 0.013432 * _day

Pmax_MR = 0.1 * _day
Pmin_MR = 0.01 * _day
Pmax_NR = 11.4 * _day
Pmin_NR = 0.0001 * _day
Pmax_ITM = 100 * _day
Pmin_ITM = 10 * _day

Gmax = 5.0 * (10 ** 5)
Qmin_MR = 0 * _day
Qmax_MR = 0.5 * _day
Keq_G = 1
Mmax = 2.0 * (10 ** 2)
Nmax = 2.5 * (10 ** 3)

ACHmax = 5885266.666666666  # ref:https://link.springer.com/content/pdf/10.1007%2FBF02491513.pdf
CHmax_tissue = 288071333.33333325  # ref:https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1242452/

ITMtissue0 = 3.5e5
ITMblood0 = 3.5e7
ITMmax = ITMblood0 + ITMtissue0
supp = 100000.
APEbmax = 5300.
APElmax = 5300.
APEmax = 5300 + 5300
APSmax = supp

alpha_GNA = 200. * _day
alpha_ACHMA = 1.5 * _day

alpha_ITMNDN = 6.358*10**(-10) * _day
alpha_ITMD = 0.00745733413 * _day
beta_CHMA = 0.8 * _day

beta_CHNA = 1 * _day
beta_MANDA = 1.5 * _day

theta_ACH = 1

r_ITM = 0.5
Keq_CH = 1e6
r_AP = 0.1
r_NDN = 0.1

rinduce = 0.05
lamb_MANDN = 0.00002
mu_NDA = 7
lamb_MANDA = 0.00002

ITM_source_peak = 4 * 10 ** 6
ITM_source_width = 5 * 10 ** 2

# calibrated
beta_CHMA = 7.8e-4
beta_CHNA = 4.8e-2
theta_ACH = 1e-10
beta_MANDA = 9e1
lamb_ITMNDN = 1.e-6
alpha_ITMNDN = 1e3
Pmax_APE = 0.002
Pmin_APE = 0.0002
rdistress = 3e6  # 1e6
w_gauss_min = 8e7
rinduce_peak = 21.0
rinduce = 0.05
r_AP = 0.08
r_ITM = 0.5
r_ITMpeak = 5 * 10 ** 12
r_NDN = 0.008
lamb_MANDN = 5e-6
lamb_MANDA = 3e-5
mu_NDA = 2.5e1
Keq_CH = 2e4
r_Nhomeo = 1e-4
Pmax_NR = 6e-3

# boundary

beta_CHMA_bound = (0, 1)
beta_CHNA_bound = (0, 1)
theta_ACH_bound = (0, 1)
beta_MANDA_bound = (0, 10 ** 4)
lamb_ITMNDN_bound = (0, 1)
alpha_ITMNDN_bound = (1*10**2, 1*10**4)
Pmax_APE_bound = (0, 1)
Pmin_APE_bound = (0, 0.1)
rdistress_bound = (10**5, 10**9)
w_gauss_min_bound = (10**5, 10**9)
rinduce_peak_bound = (0, 100)
rinduce_bound = (0, 10)
r_ITM_bound = (0, 1)
r_ITMpeak_bound = (10 ** 13, 10 ** 14)
r_NDN_bound = (0, 1)
r_AP_bound = (0, 1)
lamb_MANDN_bound = (0, 1)
lamb_MANDA_bound = (0, 1)
mu_NDA_bound = (10**1, 10**4)
Keq_CH_bound = (1e4, 1e7)
r_Nhomeo_bounds = (0, 1)
pmax_nr_bounds = (0, 1)


#Wound
mu_MA_bound = (0, 1)
phi_MRA_bound = (0, 1)
theta_ACH_bound = (0, 1)
mu_TGFB_bound = (0, 1)
beta_TGFB_M_bound = (0, 1)
beta_TGFB_FIBRO_bound = (0, 1)
mu_MR_bound = (0, 1)
Pmax_MR_bound = (0, 1)
Pmin_MR_bound = (0, 1)
Keq_CH_bound = (0, 1)


beta_M_PDGF_bound = (0,1)
beta_F_PDGF_bound = (0,1)
mu_PDGF_bound = (0,1)
mu_FIBRO_bound = (0,1)
r_F_bound = (0,1)
beta_M_MMP_bound = (0,1)
k_off_bound = (0,1)
k_on_bound = (0,1)
mu_MMP_bound = (0,1)
beta_FIBRO_COLL_bound = (0,1)


#TGFB, Fibroblasts, Collagen


mu_TGFB = 9.1 *_day #decay rate TGFB
mu_FIBRO = 0.12 *_day # Fibroblast death rate (normal)
mu_COLL = 1.5e-5 *_day # Rate of collagen remodelling by fibroblasts
mu_PDGF = 2.8 * 10 ** -3
mu_MMP = 6.1 * 10 ** -4

beta_TGFB_M_A = 0.07 *_day # pg/cell
beta_M_PDGF = 0.015 *_day # pg/cell
beta_F_PDGF = 0.0015 *_day
beta_TGFB_FIBRO = 0.004 *_day
beta_FIBRO_COLL = 20 *_day # μg/cell
beta_M_MMP = 6.4 * 10 ** -4


Ti = 6
r_F = 6.4 * 10 ** -4
k_off = 2.4 * 10 ** -2
k_on = 1.9 * 10 ** -2
k_onc = 0.24

MAX_M_A = 2500
MAX_FIBRO = 1250
MAX_COLL = 3300



def fibroblast_vs_TGFB(x):
    y = 0.0492 * x**3 - 0.9868 * x**2 + 6.5408 * x +7.1092
    y = y * _day
    return y

def collagen_vs_TGFB(x):
    #y = 0.2438384 + 0.6139767*x - 0.1510895*x**2 + 0.008930976*x**3
    y = 0.2151515 + 0.6137554 * x - 0.149513 * x ** 2 + 0.008787879 * x ** 3
    return y

def collagen_vs_collagen_density(x):
    #y = -4.33e-10 * x**3 - 9e-7 * x**2 - 0.00055 * x + 0.13
    y = 0.142687 - 0.001062817 * x + 0.000002702629 * x **2 - 1.57215e-9 * x ** 3
    return y

def fibroblast_vs_PDGF(x):
    y = 5.302294 + 461.4242*x - 178.0119*x**2 + 17.17551*x**3
    y = y *_day
    return y




# beta_CHMA_bound = (0, 100)
# beta_CHNA_bound = (0, 100)
# theta_ACH_bound = (0, 100)
# beta_MANDA_bound = (0, 10 ** 5)
# lamb_ITMNDN_bound = (0, 100)
# alpha_ITMNDN_bound = (0, 1 * 10 ** 5)
# Pmin_APE_bound = (0, 10)
# Pmax_APE_bound = (0, 100)
# rdistress_bound = (0, 10**10)
# w_gauss_min_bound = (0, 10**10)
# rinduce_peak_bound = (0, 100)
# rinduce_bound = (0, 100)
# r_ITM_bound = (0, 100)
# r_ITMpeak_bound = (0, 10 ** 15)
# r_NDN_bound = (0, 100)
# r_AP_bound = (0, 100)
# lamb_MANDN_bound = (0, 100)
# lamb_MANDA_bound = (0, 100)
# mu_NDA_bound = (0, 10**5)
# Keq_CH_bound = (0, 1e8)
# r_Nhomeo_bounds = (0, 100)
# pmax_nr_bounds = (0, 100)

# Initial Conditions
N_R0 = 2.5 * (10 ** 3)
N_A0 = 0
ND_A0 = 0
ND_N0 = 0
M_R0 = Mmax
M_A0 = 0
AP_S0 = supp
AP_Ebt0 = AP_S0 + APEbmax
AP_St0 = 0.0
AP_Eb0 = 4000.
AP_Et0 = 2500.
AP_El0 = APElmax
D0 = 0
CH0 = 0
G0 = 0
ACH0 = 0
N_B0 = 6e11/5e6  # 1 liter = 1e6 mm^3
TGFB0 = 0.21
FIBRO0 = 20
COLL0 = 10
MMP0 = 7.1
CM90 = 447
PDGF0 = 2

rinduce = 0 * _day
AP_Sinj = (1 * 5.6 * 80.) / (60. * 5)
step_max = 10 ** 100

# computed based on steady-state
r_homeo = Pmin_NR - mu_NR

time = 'min'
_stoptime = 48. * 60.
_numpoints = 10000

ITMtrans0 = 0


pred_fle = 'result/ITM0AP.txt'
cyto_fle = 'data/APPIREDII/cytokines.txt'

sample_fle = 'data/APPIREDII/sample.txt'
trt_fle = 'data/APPIREDII/segregation.txt'
AP_fle = 'data/APPIREDII/Median_AlkFosf.csv'
german_hospital_file = 'data/APPIREDII/Hospital2.txt'
dutch_hospital_file = 'data/APPIREDII/Hospital1.txt'
treatment_file = 'data/APPIREDII/segregation.txt'


def get_params(innate, p0):

    mu_nr = mu_NR
    mu_na = mu_NA
    mu_ndn = mu_NDN
    mu_ape = mu_APE
    mu_aps_fast = mu_APSfast
    mu_aps_slow = mu_APSslow
    mu_aps = mu_APS


    mu_ach = mu_ACH
    mu_ch = mu_CH
    mu_itm = mu_ITM

    lamb_itmna = lamb_ITMNA
    lamb_ape = lamb_APE
    lamb_aps = lamb_APS
    lamb_itmma = lamb_ITMMA

    alpha_achma = alpha_ACHMA



    pmin_nr = Pmin_NR
    pmax_itm = Pmax_ITM
    pmin_itm = Pmin_ITM

    mmax = Mmax
    nmax = Nmax
    achmax = ACHmax
    chmax_tissue = CHmax_tissue

    itmmax = ITMmax

    apebmax = innate.convert_AP(APEbmax, 'endo', 'tissue')
    apelmax = innate.convert_AP(APElmax, 'endo', 'tissue')
    apemax = innate.convert_AP(APEmax, 'endo', 'tissue')
    apsmax = innate.convert_AP(APSmax, 'supp', 'blood')

    # Initial Conditions
    n_r0 = N_R0
    n_a0 = N_A0
    nd_a0 = ND_A0
    nd_n0 = ND_N0
    m_r0 = M_R0
    m_a0 = M_A0
    ap_s0 = innate.convert_AP(AP_S0, 'supp', 'blood')
    ap_st0 = AP_St0
    ap_et0 = innate.convert_AP(AP_Et0, 'endo', 'tissue')
    ap_el0 = innate.convert_AP(AP_El0, 'endo', 'blood')
    ap_eb0 = innate.convert_AP(AP_Eb0, 'endo', 'blood') + ap_el0
    ch0 = CH0
    ach0 = ACH0
    tgfb0 = TGFB0
    fibro0 = FIBRO0
    coll0 = COLL0
    mmp0 = MMP0
    cm90 = CM90
    pdgf0 = PDGF0


    ap_sinj = innate.convert_AP(AP_Sinj, 'supp', 'blood')
    stepmax = step_max

    t = [_stoptime * float(i) / (_numpoints - 1) for i in range(_numpoints)]

    itmblood0 = ITMblood0
    itmtissue0 = ITMtissue0
    predfle = pred_fle

    itm_source_peak = ITM_source_peak
    itm_source_width = ITM_source_width

    mu_TGFB,beta_TGFB_M_A,beta_TGFB_FIBRO,mu_MA, phi_MRA, theta_ACH, mu_MR,Pmax_MR,Pmin_MR,Keq_CH = abs(p0[0]), abs(p0[1]), abs(p0[2]) , abs(p0[3]), abs(p0[4]), abs(p0[5]), \
                                                                                                          abs(p0[6]) , abs(p0[7]), abs(p0[8]), abs(p0[9]), \




    beta_CHMA = 7.8e-4
    beta_CHNA = 4.8e-2

    beta_MANDA = 9e1
    lamb_ITMNDN = 1.e-6
    alpha_ITMNDN = 1e3
    Pmax_APE = 0.002
    Pmin_APE = 0.0002
    rdistress = 3e6  # 1e6
    w_gauss_min = 8e7
    rinduce_peak = 21.0
    rinduce = 0.05
    r_AP = 0.08
    r_ITM = 0.5
    r_ITMpeak = 5 * 10 ** 12
    r_NDN = 0.008
    lamb_MANDN = 5e-6
    lamb_MANDA = 3e-5
    mu_NDA = 2.5e1

    r_Nhomeo = 1e-4
    Pmax_NR = 6e-3

    r_APhomeo = Pmin_APE + mu_APE

    p = [mu_ACH , mu_APE, mu_APS, mu_APSfast, mu_APSslow, mu_CH, mu_MA, mu_MR, mu_NA, mu_NDA, mu_NDN,
         mu_NR, mu_ITM, Pmin_MR, Pmin_NR, ACHmax, CHmax_tissue, Mmax, Nmax, Pmax_MR, Pmax_NR, Keq_CH, phi_MRA,
         theta_ACH, lamb_APE, lamb_ITMNA, lamb_ITMMA, lamb_MANDA, lamb_MANDN, lamb_APS, alpha_ACHMA, beta_CHMA,
         beta_CHNA, beta_MANDA, APEmax, APEbmax, APElmax, APSmax, rdistress, lamb_ITMNDN, alpha_ITMNDN, Pmax_APE,
         Pmin_APE, rinduce_peak, AP_Sinj, w_gauss_min, r_Nhomeo, r_APhomeo, Pmax_ITM, Pmin_ITM, ITMmax, step_max,
         r_NDN, r_ITM, r_ITMpeak, r_AP, rinduce, ITM_source_peak, ITM_source_width, mu_TGFB, beta_TGFB_M_A,
         beta_TGFB_FIBRO, beta_M_PDGF, beta_F_PDGF, mu_PDGF, mu_FIBRO, r_F, beta_M_MMP, Ti,
         k_off, k_on, mu_MMP, k_onc, mu_COLL, beta_FIBRO_COLL, MAX_FIBRO, MAX_COLL, MAX_M_A]

    w = [n_r0, ap_eb0, ap_et0, ap_el0, ap_s0, ap_st0, itmblood0, itmtissue0, m_r0, m_a0, ch0, n_a0, nd_a0, ach0, nd_n0, tgfb0, fibro0, coll0, mmp0, cm90, pdgf0]
    return p, w, predfle


def get_params_to_pass(innate, p0_to_pass):

    # Initial Conditions
    n_r0 = N_R0
    n_a0 = N_A0
    nd_a0 = ND_A0
    nd_n0 = ND_N0
    m_r0 = M_R0
    m_a0 = M_A0
    ap_s0 = innate.convert_AP(AP_S0, 'supp', 'blood')
    ap_st0 = AP_St0
    ap_et0 = innate.convert_AP(AP_Et0, 'endo', 'tissue')
    ap_el0 = innate.convert_AP(AP_El0, 'endo', 'blood')
    ap_eb0 = innate.convert_AP(AP_Eb0, 'endo', 'blood') + ap_el0
    ch0 = CH0
    ach0 = ACH0
    tgfb0 = TGFB0
    fibro0 = FIBRO0
    coll0 = COLL0
    mmp0 = MMP0
    cm90 = CM90
    pdgf0 = PDGF0

    ap_sinj = innate.convert_AP(AP_Sinj, 'supp', 'blood')
    stepmax = step_max

    t = [_stoptime * float(i) / (_numpoints - 1) for i in range(_numpoints)]

    itmblood0 = ITMblood0
    itmtissue0 = ITMtissue0
    predfle = pred_fle

    p = OrderedDict()
    p['mu_ACH'] = mu_ACH
    p['mu_APE'] = mu_APE
    p['mu_APS'] = mu_APS
    p['mu_APSfast'] = mu_APSfast
    p['mu_APSslow'] = mu_APSslow
    p['mu_CH'] = mu_CH
    p['mu_MA'] = mu_MA
    p['mu_MR'] = mu_MR
    p['mu_NA'] = mu_NA
    p['mu_NDA'] = mu_NDA
    p['mu_NDN'] = mu_NDN
    p['mu_NR'] = mu_NR
    p['mu_ITM'] = mu_ITM
    p['Pmin_MR'] = Pmin_MR
    p['Pmin_NR'] = Pmin_NR
    p['ACHmax'] = ACHmax
    p['CHmax_tissue'] = CHmax_tissue
    p['Mmax'] = Mmax
    p['Nmax'] = Nmax
    p['Pmax_MR'] = Pmax_MR
    p['Pmax_NR'] = Pmax_NR
    p['Keq_CH'] = Keq_CH
    p['phi_MRA'] = phi_MRA
    p['theta_ACH'] = theta_ACH
    p['lamb_APE'] = lamb_APE
    p['lamb_ITMNA'] = lamb_ITMNA
    p['lamb_ITMMA'] = lamb_ITMMA
    p['lamb_MANDA'] = lamb_MANDA
    p['lamb_MANDN'] = lamb_MANDN
    p['lamb_APS'] = lamb_APS
    p['alpha_ACHMA'] = alpha_ACHMA
    p['beta_CHMA'] = beta_CHMA
    p['beta_CHNA'] = beta_CHNA
    p['beta_MANDA'] = beta_MANDA
    p['APEmax'] = innate.convert_AP(APEmax, 'endo', 'tissue')
    p['APEbmax'] = innate.convert_AP(APEbmax, 'endo', 'tissue')
    p['APElmax'] = innate.convert_AP(APElmax, 'endo', 'tissue')
    p['APSmax'] = innate.convert_AP(APSmax, 'supp', 'blood')
    p['rdistress'] = rdistress
    p['lamb_ITMNDN'] = lamb_ITMNDN
    p['alpha_ITMNDN'] = alpha_ITMNDN
    p['Pmax_APE'] = Pmax_APE
    p['Pmin_APE'] = Pmin_APE
    p['rinduce_peak'] = rinduce_peak
    p['AP_Sinj'] = AP_Sinj
    p['w_gauss_min'] = w_gauss_min
    p['r_Nhomeo'] = r_Nhomeo
    p['r_APhomeo'] = 0
    p['Pmax_ITM'] = Pmax_ITM
    p['Pmin_ITM'] = Pmin_ITM
    p['ITMmax'] = ITMmax
    p['step_max'] = step_max
    p['r_NDN'] = r_NDN
    p['r_ITM'] = r_ITM
    p['r_ITMpeak'] = r_ITMpeak
    p['r_AP'] = r_AP
    p['rinduce'] = rinduce
    p['ITM_source_peak'] = ITM_source_peak
    p['ITM_source_width'] = ITM_source_width

    for key, value in p0_to_pass.items():
        p[key] = value
    p['r_APhomeo'] = p['Pmin_APE'] + p['mu_APE']
    w = [n_r0, ap_eb0, ap_et0, ap_el0, ap_s0, ap_st0, itmblood0, itmtissue0, m_r0, m_a0, ch0, n_a0, nd_a0, ach0, nd_n0, tgfb0, fibro0, coll0, mmp0, cm90, pdgf0 ]
    return p.values(), w, predfle


def get_boundaries():
    boundaries = OrderedDict()

    boundaries['mu_TGFB'] = mu_TGFB_bound
    boundaries['beta_TGFB_M_A'] = beta_TGFB_M_bound
    boundaries['beta_TGFB_FIBRO'] = beta_TGFB_FIBRO_bound
    boundaries['mu_MA'] = mu_MA_bound
    boundaries['phi_MRA'] = phi_MRA_bound
    boundaries['theta_ACH'] = theta_ACH_bound
    boundaries['mu_MR'] = mu_MR_bound
    boundaries['Pmax_MR'] = Pmax_MR_bound
    boundaries['Pmin_MR'] = Pmin_MR_bound
    boundaries['Keq_CH'] = Keq_CH_bound

    return boundaries


def get_t(innate, numpoints):
    stoptime = innate.convert_to_day(_stoptime, time)
    t = [stoptime * float(i) / (numpoints - 1) for i in range(numpoints)]
    return t


def stoptime():
    return _stoptime