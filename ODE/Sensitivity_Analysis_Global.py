import _pickle as pickle
import pandas as pd
import seaborn as sns
import ast
import os
import matplotlib.pyplot as plt
from collections import OrderedDict

from tqdm import tqdm

from SALib.sample import saltelli, fast_sampler
from SALib.analyze import sobol, fast

import numpy as np

import Parameters as par
import APSim_Model as innate


def get_label_dictionary():
    params = OrderedDict()
    params['mu_TGFB'] = r'$\mu_{TGFB}$'
    params['beta_TGFB_M_A'] = r'$\beta_{TGFB|MA}$'
    params['beta_TGFB_FIBRO'] = r'$\beta_{TGFB|FIBRO}$'
    params['mu_MA'] = r'$\mu_{MA}$'
    params['phi_MRA'] = r'$\phi_{MRA}$'
    params['theta_ACH'] = r'$\theta_{ACH}$'
    params['mu_MR'] = r'$\mu_{MR}$'
    params['Pmax_MR'] = r'$P^{max}_{MR}$'
    params['Pmin_MR'] = r'$P^{min}_{MR}$'
    params['Keq_CH'] = r'$K^{eq}_{CH}$'

    return params

def get_problem():
    problem = {
        'num_vars': 10,
        'names': list(par.get_boundaries().keys()),
        'bounds': list(par.get_boundaries().values())
    }
    return problem


def generate_samples(problem, params, project_dir, method):
    """
    The Saltelli sampler generated 8000 samples. The Saltelli sampler generates N*(2D+2) samples, where in this
    example N is 1000 (the argument we supplied) and D is 3 (the number of model inputs).
    """

    if method == 'Saltelli':
        param_values = saltelli.sample(problem, params['samples'])
    elif method == 'FAST':
        param_values = fast_sampler.sample(problem, params['samples'])

    count = 0

    for i, X in enumerate(param_values):
        count += 1
        p, w, pred_fle = par.get_params(innate, X)
        _numpoints = 70
        t = [par._stoptime * float(i) / (_numpoints - 1) for i in range(_numpoints)]
        w0 = innate.get_init(w, params)
        t, wsol = innate.solve(p, w0, t, params)

        TGFB = []


        for t1, w1 in zip(t, wsol):
            TGFB.append(w1[15])
        # Y_list.append(APE_blood)
        write_file(project_dir, method, TGFB, 'TGFB')
        print(count, ' of ', len(param_values))


def write_file(project_dir, method, blood_parameter, param_name):
    with open(project_dir + '/' + method + '_' + param_name + '.txt', 'a') as file:
        file.write(str(blood_parameter) + '\n')
    file.close()


def read_file(project_dir, param_name, method):
    with open(project_dir + '/' + method + '_' + param_name + '.txt') as file:
        content = file.readlines()
    content = [ast.literal_eval(x.replace("\n", "")) for x in content]
    file.close()
    return content


def pickle_it(unpickled, project_dir, pickle_file):
    print("Pickling it...")
    pickle_out = open(project_dir + '/' + pickle_file, "wb")
    pickle.dump(unpickled, pickle_out)
    pickle_out.close()


def read_pickle(project_dir, pickle_file):
    pickle_in = open(project_dir + '/' + pickle_file, 'rb')
    pickle_out = pickle.load(pickle_in)
    return pickle_out


def perform_analysis(problem, Y_list, method):
    S1_dic = OrderedDict()
    S1_dic['mu_TGFB'] = []
    S1_dic['beta_TGFB_M_A'] = []
    S1_dic['beta_TGFB_FIBRO'] = []
    S1_dic['mu_MA'] = []
    S1_dic['phi_MRA'] = []
    S1_dic['theta_ACH'] = []
    S1_dic['mu_MR'] = []
    S1_dic['Pmax_MR'] = []
    S1_dic['Pmin_MR'] = []
    S1_dic['Keq_CH'] = []

    Y_list = np.array(Y_list)
    print (Y_list.shape)
    print('hi')


    Y_list_trans = Y_list.transpose()


    total = len(Y_list_trans)
    count = 0

    for Y in Y_list_trans:

        count += 1
        if method == 'FAST':
            Si = fast.analyze(problem, Y, print_to_console=True)
        elif method == 'Saltelli':
            Si = sobol.analyze(problem, Y)

        mu_TGFB,beta_TGFB_M_A, beta_TGFB_FIBRO, mu_MA,phi_MRA, theta_ACH, mu_MR,Pmax_MR,Pmin_MR,Keq_CH = Si['S1'] #Si['ST']# = Si['S1']


        S1_dic['mu_TGFB'].append(mu_TGFB)
        S1_dic['beta_TGFB_M_A'].append(beta_TGFB_M_A)
        S1_dic['beta_TGFB_FIBRO'].append(beta_TGFB_FIBRO)
        S1_dic['mu_MA'].append(mu_MA)
        S1_dic['phi_MRA'].append(phi_MRA)
        S1_dic['theta_ACH'].append(theta_ACH)
        S1_dic['mu_MR'].append(mu_MR)
        S1_dic['Pmax_MR'].append(Pmax_MR)
        S1_dic['Pmin_MR'].append(Pmin_MR)
        S1_dic['Keq_CH'].append(Keq_CH)

        print(total, count)
    return pd.DataFrame(S1_dic)


def pick(result):
    pick_result = []
    for i in range(len(result)):
        if i % 5 == 0 or i == 0:
            pick_result.append(result[i])
    print (pick_result)
    return pick_result


def get_order_params(df):
    sensitive = []
    not_sensitive =[]
    for column in df:
        result = (df[column])
        if max(result) >= 0.05:
            sensitive.append(column)
        else:
            not_sensitive.append(column)
    return sensitive+not_sensitive


def plot(df, project_dir, method, param_name, label_dic, title_dic):
    sns.set_style("ticks")
    sns.set_style({"xtick.direction": "in", "ytick.direction": "in", "axes.linewidth": 2.5})

    lw = 3
    ls = 20
    fs = 20
    line_styles = ['-', '--', '-.', ':']
    count = 0
    count_important = 0
    sns.set(style="white")
    df.fillna(0, inplace=True)
    increment = 0
    columns = get_order_params(df)
    for column in columns:
        result = (df[column])
        time = [(i/len(result))*48. for i in range(len(result))]
        if max(result) >= 0.2:
            line_style = line_styles[count_important % len(line_styles)]
            color = '#e41a1c'
            plt.plot(time, result, label=label_dic[column], ls=line_style, linewidth=lw, color=color, alpha=1-increment)
            increment += 0.1
            count_important += 1
        else:
            color = '#999999'
            if count == 5:
                plt.plot(time, result, ls='-', label='Others', linewidth=lw, color=color, alpha=0.4)
            else:
                plt.plot(time, result, ls='-', linewidth=lw, color=color, alpha=0.4, label='')
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., prop={'size': ls}, frameon=True)
        plt.plot(time, [0.05]*len(time), ls='-', linewidth=lw, color='black')
        plt.xlabel("Hours After Operation", fontsize=fs)
        plt.ylabel('Sensitivity Index', fontsize=fs)
        plt.title(title_dic[param_name], fontsize=fs)
        plt.xlim((0, 48))
        plt.tick_params(labelsize=ls)
        plt.savefig(project_dir + '/' + method + '_' + param_name + '_SA.png', dpi=500, bbox_inches='tight')
        count += 1


def do_analysis(params, project_dir, pickle_file, method):
    for param_name in params['param_names']:
        problem = read_pickle(project_dir, pickle_file)
        Y_list = read_file(project_dir, param_name, method)
        df = perform_analysis(problem, Y_list, method)
        df_file = 'df_' + param_name + '_' + method + '.pickle'
        pickle_it(df, project_dir, df_file)


def main():
    project_dir = 'C:/Users/mark_/Documents/minor stage/brandwonden_git/sensitivity'
    params = {'h': 'h4',
              'restrict': False,
              'case': 6,
              'method': ['FAST'],
              'samples': 70,
              'param_names': ['TGFB']
              }

    if not os.path.exists(project_dir):
        os.makedirs(project_dir)

    label_dic = get_label_dictionary()
    title_dic = {'TGFB': 'TGFB'
                 }
    for method in params['method']:
        pickle_file = method + '_Problem.pickle'
        problem = get_problem()
        pickle_it(problem, project_dir, pickle_file)
        generate_samples(problem, params, project_dir, method)

        do_analysis(params, project_dir, pickle_file, method)

        param_name = 'TGFB'
        df_file = 'df_' + param_name + '_' + method + '.pickle'
        df = read_pickle(project_dir, df_file)
        plot(df, project_dir, method, param_name, label_dic, title_dic)

if __name__ == '__main__':
    main()