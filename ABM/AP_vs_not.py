import matplotlib.pyplot as plt
import numpy as np
from ABM import WoundModel

def AP_vs_not_model(step_count=120):
    model = WoundModel(50,50,50,0.5,0.5,0.5,0.5,25,25,10,0.7)
    for i in range(step_count):
        model.step()
    cell_concentrations = model.datacollector.get_model_vars_dataframe()
    print('NON-AP run finished....')

    modelAP = WoundModel(80, 50, 50, 7, 0.0, 0.5, 0.5, 25, 25, 10, 0.7)
    for i in range(step_count):
        modelAP.step()
    cell_concentrationsAP = modelAP.datacollector.get_model_vars_dataframe()
    print('AP run finished....')

    lw = 5 #Linewidth
    ls = 20 #Labelsize
    fs = 25 #Fontsize
    lfs = 25 #Fontsize legend
    ts = 30 #Title size

    n = loop_fig(1)
    plt.figure(n)
    plt.plot(cell_concentrations["Macrophages"], linewidth=lw, ls='-', color = "#377eb8" )
    plt.plot(cell_concentrationsAP["Macrophages"], linewidth=lw, ls='-', color = "#4daf4a")
    plt.ylabel("Concentration (Arbitrary units)", fontsize=fs)
    plt.xlabel("Time (h)", fontsize=fs)
    plt.title("Macrophages", fontsize=ts)
    plt.ylim(0,100)
    plt.xlim(0,120)
    plt.legend({ 'bIAP', 'Placebo'}, loc='best', fontsize=lfs)
    plt.tick_params(labelsize=ls)
    plt.tight_layout()
    print('... Plotting macrophages')
    plt.savefig('results/' + 'Macrophages.png', format='png', dpi=500, bbox_inches='tight')

    n = loop_fig(n)
    plt.figure(n)
    plt.plot(cell_concentrations["Neutrophils"], linewidth=lw, ls='-', color = "#377eb8" )
    plt.plot(cell_concentrationsAP["Neutrophils"], linewidth=lw, ls='-', color = "#4daf4a")
    plt.ylabel("Concentration (Arbitrary units)", fontsize=fs)
    plt.xlabel("Time (h)", fontsize=fs)
    plt.ylim(0, 100)
    plt.xlim(0, 120)
    plt.legend({ 'bIAP', 'Placebo'}, loc='best', fontsize=lfs)
    plt.title("Neutrophils", fontsize=ts)
    plt.tick_params(labelsize=ls)
    plt.tight_layout()
    print('... Plotting neutrophils')
    plt.savefig('results/' + 'Neutrophils.png', format='png', dpi=500, bbox_inches='tight')

    n = loop_fig(n)
    plt.figure(n)
    plt.plot(cell_concentrations["Fibroblasts"], linewidth=lw, ls='-', color = "#377eb8")
    plt.plot(cell_concentrationsAP["Fibroblasts"], linewidth=lw, ls='-', color = "#4daf4a" )
    plt.ylabel("Concentration (Arbitrary units)", fontsize=fs)
    plt.xlabel("Time (h)", fontsize=fs)
    plt.ylim(0, 100)
    plt.xlim(0, 120)
    plt.legend({ 'bIAP', 'Placebo'}, loc='best', fontsize=lfs)
    plt.title("Fibroblasts", fontsize=ts)
    plt.tick_params(labelsize=ls)
    plt.tight_layout()
    print('... Plotting fibroblasts')
    plt.savefig('results/' + 'Fibroblasts.png', format='png', dpi=500, bbox_inches='tight')

    n = loop_fig(n)
    plt.figure(n)

    plt.plot(cell_concentrations["Blood_flow"], linewidth=lw, ls='-', color = "#377eb8" )
    plt.plot(cell_concentrationsAP["Blood_flow"], linewidth=lw, ls='-', color="#4daf4a")
    plt.ylabel("Concentration (Arbitrary units)", fontsize=fs)
    plt.xlabel("Time (h)", fontsize=fs)
    plt.ylim(0, 100)
    plt.xlim(0, 120)
    plt.legend({ 'bIAP', 'Placebo'}, loc='best', fontsize=lfs)
    plt.title("Oxygen", fontsize=ts)
    plt.tick_params(labelsize=ls)
    plt.tight_layout()
    print('... Plotting Oxygen')
    plt.savefig('results/' + 'oxygen.png', format='png', dpi=500, bbox_inches='tight')

    n = loop_fig(n)
    plt.figure(n)

    plt.plot(cell_concentrations["Collagen"], linewidth=lw, ls='-', color = "#377eb8" )
    plt.plot(cell_concentrationsAP["Collagen"], linewidth=lw, ls='-', color="#4daf4a")
    plt.ylabel("Concentration (Arbitrary units)", fontsize=fs)
    plt.xlabel("Time (h)", fontsize=fs)
    plt.ylim(0, 100)
    plt.xlim(0, 120)
    plt.legend({ 'bIAP', 'Placebo'}, loc='best', fontsize=lfs)
    plt.title("Collagen ", fontsize=ts)
    plt.tick_params(labelsize=ls)
    plt.tight_layout()
    print('... Plotting collagen')
    plt.savefig('results/' + 'Collagen.png', format='png', dpi=500, bbox_inches='tight')

    n = loop_fig(n)
    plt.figure(n)
    TG_map = cell_concentrations["TGFb"][119]
    Tmap = np.zeros((25, 25))
    for x in TG_map:
        a, b = x[0][0], x[0][1]
        Tmap[a, b] = x[1]
    # plt.show()
    plt.imshow(Tmap, cmap="hot")
    plt.title("TGFb", fontsize=ts)
    plt.savefig('results/' + 'tgfb.png', format='png', dpi=500, bbox_inches='tight')

    n = loop_fig(n)
    plt.figure(n)
    TG_map = cell_concentrationsAP["TGFb"][119]
    Tmap = np.zeros((25, 25))
    for x in TG_map:
        a, b = x[0][0], x[0][1]
        Tmap[a, b] = x[1]
    # plt.show()
    plt.imshow(Tmap, cmap="hot")
    plt.title("TGFb", fontsize=ts)
    plt.savefig('results/' + 'tgfbAP.png', format='png', dpi=500, bbox_inches='tight')

    n = loop_fig(n)
    plt.figure(n)
    TG_map = cell_concentrations["IL6"][119]
    Tmap = np.zeros((25, 25))
    for x in TG_map:
        a, b = x[0][0], x[0][1]
        Tmap[a, b] = x[1]
    # plt.show()
    plt.imshow(Tmap, cmap="hot")
    plt.title("IL-6", fontsize=ts)
    plt.savefig('results/' + 'IL6.png', format='png', dpi=500, bbox_inches='tight')

    n = loop_fig(n)
    plt.figure(n)
    TG_map = cell_concentrationsAP["IL6"][119]
    Tmap = np.zeros((25, 25))
    for x in TG_map:
        a, b = x[0][0], x[0][1]
        Tmap[a, b] = x[1]
    # plt.show()
    plt.imshow(Tmap, cmap="hot")
    plt.title("IL-6", fontsize=ts)
    plt.savefig('results/' + 'IL10AP.png', format='png', dpi=500, bbox_inches='tight')

    n = loop_fig(n)
    plt.figure(n)
    TG_map = cell_concentrations["IL10"][119]
    Tmap = np.zeros((25, 25))
    for x in TG_map:
        a, b = x[0][0], x[0][1]
        Tmap[a, b] = x[1]
    # plt.show()
    plt.imshow(Tmap, cmap="hot")
    plt.title("IL-10", fontsize=ts)
    plt.savefig('results/' + 'IL10.png', format='png', dpi=500, bbox_inches='tight')

    n = loop_fig(n)
    plt.figure(n)
    TG_map = cell_concentrationsAP["IL10"][119]
    Tmap = np.zeros((25, 25))
    for x in TG_map:
        a, b = x[0][0], x[0][1]
        Tmap[a, b] = x[1]
    # plt.show()
    plt.imshow(Tmap, cmap="hot")
    plt.title("IL-10", fontsize=ts)
    plt.savefig('results/' + 'IL-10AP.png', format='png', dpi=500, bbox_inches='tight')

    n = loop_fig(n)
    plt.figure(n)
    TG_map = cell_concentrations["TNFa"][119]
    Tmap = np.zeros((25, 25))
    for x in TG_map:
        a, b = x[0][0], x[0][1]
        Tmap[a, b] = x[1]
    # plt.show()
    plt.imshow(Tmap, cmap="hot")
    plt.title("TNFa", fontsize=ts)
    plt.savefig('results/' + 'TNFa.png', format='png', dpi=500, bbox_inches='tight')

    n = loop_fig(n)
    plt.figure(n)
    TG_map = cell_concentrationsAP["TNFa"][119]
    Tmap = np.zeros((25, 25))
    for x in TG_map:
        a, b = x[0][0], x[0][1]
        Tmap[a, b] = x[1]
    # plt.show()
    plt.imshow(Tmap, cmap="hot")
    plt.title("TNFa", fontsize=ts)
    plt.savefig('results/' + 'TNFaAP.png', format='png', dpi=500, bbox_inches='tight')

def loop_fig(fignum):
    return fignum + 1

AP_vs_not_model()