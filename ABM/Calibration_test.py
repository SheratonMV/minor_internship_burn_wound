import matplotlib.pyplot as plt
from ABM import WoundModel

def run_calibration_test(step_count=120):
    print('Running the model')
    model = WoundModel(50,50,50,0.5,0.5,0.5,0.5,25,25,10,0.5)
    for i in range(step_count):
        model.step()
    cell_concentrations = model.datacollector.get_model_vars_dataframe()


    lw = 5  # Linewidth
    ls = 10 # Labelsize
    fs = 15 # Fontsize
    lfs = 15 # Fontsize legend
    ts = 15 # Title size


    n = loop_fig(1)
    plt.figure(n)
    plt.plot(cell_concentrations["Macrophages"], linewidth=lw, ls='-')
    plt.plot(cell_concentrations["Neutrophils"], linewidth=lw, ls='-')
    plt.plot(cell_concentrations["Fibroblasts"], linewidth=lw, ls='-')
    plt.xlim(0,120)
    plt.ylabel("Concentration (Arbitrary units)", fontsize=fs)
    plt.xlabel("Time (h)", fontsize=fs)

    plt.legend({ 'Fibroblasts', 'Macrophages', 'Neutrophils', }, loc='best', fontsize=lfs)
    plt.tick_params(labelsize=ls)
    plt.tight_layout()
    print('... Plotting macrophages, neutrophils and fibroblasts')
    plt.savefig('results/' + 'all.png', format='png', dpi=500, bbox_inches='tight')

    n = loop_fig(n)
    plt.figure(n)
    plt.plot(cell_concentrations["Blood_flow"], linewidth=lw, ls='-', color = 'red')
    plt.plot(cell_concentrations["Collagen"], linewidth=lw, ls='-', color = 'black')
    plt.legend({'Oxygen', 'Collagen' }, loc='best', fontsize=lfs)
    plt.xlim(0, 120)
    plt.ylabel("Concentration (Arbitrary units)", fontsize=fs)
    plt.xlabel("Time (h)", fontsize=fs)

    plt.tick_params(labelsize=ls)
    plt.tight_layout()
    print('... Plotting blood flow and oxygen content')
    plt.savefig('results/' + 'blood.png', format='png', dpi=500, bbox_inches='tight')
    #plt.plot(cell_concentrations["Collagen"], linewidth=lw, ls='-')

def loop_fig(fignum):
    return fignum + 1

run_calibration_test()