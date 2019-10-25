import matplotlib.pyplot as plt
import numpy as np
from ABM import WoundModel

def AP_vs_not_model(step_count=120):
    print('Running without AP....')
    model = WoundModel(50,50,50,0.5,0.5,0.5,0.5,25,25,10,0.7)
    for i in range(step_count):
        model.step()
    cell_concentrations = model.datacollector.get_model_vars_dataframe()

    print('Running with AP....')
    modelAP = WoundModel(80, 50, 50, 6, 0.0, 0.5, 0.5, 25, 25, 10, 0.7)
    for i in range(step_count):
        modelAP.step()
    cell_concentrationsAP = modelAP.datacollector.get_model_vars_dataframe()

    lw = 5 #Linewidth
    ls = 20 #Labelsize
    fs = 25 #Fontsize
    lfs = 25 #Fontsize legend
    ts = 30 #Title size

    n = loop_fig(1)
    plt.figure(n)
    plt.plot(cell_concentrations["Macrophages"], linewidth=lw, ls='-', color = "#377eb8", label='NON-AP')
    plt.plot(cell_concentrationsAP["Macrophages"], linewidth=lw, ls='-', color = "#4daf4a", label='AP')
    plt.ylabel("Concentration (Arbitrary units)", fontsize=fs)
    plt.xlabel("Time (h)", fontsize=fs)
    plt.title("Macrophages", fontsize=ts)
    plt.ylim(0,100)
    plt.xlim(0,120)
    plt.legend(loc='best', fontsize=lfs)
    plt.tick_params(labelsize=ls)
    plt.tight_layout()
    print('... Plotting macrophages')
    plt.savefig('results/' + 'Macrophages.png', format='png', dpi=500, bbox_inches='tight')

    n = loop_fig(n)
    plt.figure(n)
    plt.plot(cell_concentrations["Neutrophils"], linewidth=lw, ls='-', color = "#377eb8", label='NON-AP')
    plt.plot(cell_concentrationsAP["Neutrophils"], linewidth=lw, ls='-', color = "#4daf4a", label='AP')
    plt.ylabel("Concentration (Arbitrary units)", fontsize=fs)
    plt.xlabel("Time (h)", fontsize=fs)
    plt.ylim(0, 100)
    plt.xlim(0, 120)
    plt.legend(loc='best', fontsize=lfs)
    plt.title("Neutrophils", fontsize=ts)
    plt.tick_params(labelsize=ls)
    plt.tight_layout()
    print('... Plotting neutrophils')
    plt.savefig('results/' + 'Neutrophils.png', format='png', dpi=500, bbox_inches='tight')

    n = loop_fig(n)
    plt.figure(n)
    plt.plot(cell_concentrations["Fibroblasts"], linewidth=lw, ls='-', color = "#377eb8", label='NON-AP')
    plt.plot(cell_concentrationsAP["Fibroblasts"], linewidth=lw, ls='-', color = "#4daf4a", label='AP')
    plt.ylabel("Concentration (Arbitrary units)", fontsize=fs)
    plt.xlabel("Time (h)", fontsize=fs)
    plt.ylim(0, 100)
    plt.xlim(0, 120)
    plt.legend(loc='best', fontsize=lfs)
    plt.title("Fibroblasts", fontsize=ts)
    plt.tick_params(labelsize=ls)
    plt.tight_layout()
    print('... Plotting fibroblasts')
    plt.savefig('results/' + 'Fibroblasts.png', format='png', dpi=500, bbox_inches='tight')

    n = loop_fig(n)
    plt.figure(n)

    plt.plot(cell_concentrations["Blood_flow"], linewidth=lw, ls='-', color = "#377eb8", label='NON-AP')
    plt.plot(cell_concentrationsAP["Blood_flow"], linewidth=lw, ls='-', color="#4daf4a", label='AP')
    plt.ylabel("Concentration (Arbitrary units)", fontsize=fs)
    plt.xlabel("Time (h)", fontsize=fs)
    plt.ylim(0, 100)
    plt.xlim(0, 120)
    plt.legend(loc='best', fontsize=lfs)
    plt.title("Oxygen", fontsize=ts)
    plt.tick_params(labelsize=ls)
    plt.tight_layout()
    print('... Plotting Oxygen')
    plt.savefig('results/' + 'oxygen.png', format='png', dpi=500, bbox_inches='tight')

    n = loop_fig(n)
    plt.figure(n)

    plt.plot(cell_concentrations["Collagen"], linewidth=lw, ls='-', color = "#377eb8", label='NON-AP')
    plt.plot(cell_concentrationsAP["Collagen"], linewidth=lw, ls='-', color="#4daf4a", label='AP')
    plt.ylabel("Concentration (Arbitrary units)", fontsize=fs)
    plt.xlabel("Time (h)", fontsize=fs)
    plt.ylim(0, 100)
    plt.xlim(0, 120)
    plt.legend(loc='best', fontsize=lfs)
    plt.title("Collagen ", fontsize=ts)
    plt.tick_params(labelsize=ls)
    plt.tight_layout()
    print('... Plotting collagen')
    plt.savefig('results/' + 'Collagen.png', format='png', dpi=500, bbox_inches='tight')

    print('... Plotting TGFb heatmaps')
    n = loop_fig(n)
    plt.figure(n)
    TG_map = cell_concentrations["TGFb"][119]
    Tmap = np.zeros((25, 25))
    for x in TG_map:
        a, b = x[0][0], x[0][1]
        Tmap[a, b] = x[1]
    # plt.show()
    plt.imshow(Tmap, cmap="hot", vmin=0, vmax=10)
    cbar = plt.colorbar()
    cbar.set_label('Concentration (Arbitrary units)', rotation=90, fontsize=15)
    plt.xlabel("X coordinate", fontsize=15)
    plt.ylabel("Y coordinate", fontsize=15)
    plt.title("TGFB without AP", fontsize=ts)
    plt.savefig('results/' + 'tgfb.png', format='png', dpi=500, bbox_inches='tight')

    n = loop_fig(n)
    plt.figure(n)
    TG_map = cell_concentrationsAP["TGFb"][119]
    Tmap = np.zeros((25, 25))
    for x in TG_map:
        a, b = x[0][0], x[0][1]
        Tmap[a, b] = x[1]
    # plt.show()
    plt.imshow(Tmap, cmap="hot", vmin=0, vmax=10)
    cbar = plt.colorbar()
    cbar.set_label('Concentration (Arbitrary units)', rotation=90, fontsize=15)
    plt.xlabel("X coordinate", fontsize=15)
    plt.ylabel("Y coordinate", fontsize=15)
    plt.title("TGFB with AP", fontsize=ts)
    plt.savefig('results/' + 'tgfbAP.png', format='png', dpi=500, bbox_inches='tight')

    print('... Plotting IL6 heatmaps')
    n = loop_fig(n)
    plt.figure(n)
    TG_map = cell_concentrations["IL6"][119]
    Tmap = np.zeros((25, 25))
    for x in TG_map:
        a, b = x[0][0], x[0][1]
        Tmap[a, b] = x[1]
    # plt.show()
    plt.imshow(Tmap, cmap="hot", vmin=0, vmax=10)
    cbar = plt.colorbar()
    cbar.set_label('Concentration (Arbitrary units)', rotation=90, fontsize=15)
    plt.xlabel("X coordinate", fontsize=15)
    plt.ylabel("Y coordinate", fontsize=15)
    plt.title("IL-6 without AP", fontsize=ts)
    plt.savefig('results/' + 'IL6.png', format='png', dpi=500, bbox_inches='tight')

    n = loop_fig(n)
    plt.figure(n)
    TG_map = cell_concentrationsAP["IL6"][119]
    Tmap = np.zeros((25, 25))
    for x in TG_map:
        a, b = x[0][0], x[0][1]
        Tmap[a, b] = x[1]
    # plt.show()
    plt.imshow(Tmap, cmap="hot", vmin=0, vmax=10)
    cbar = plt.colorbar()
    cbar.set_label('Concentration (Arbitrary units)', rotation=90, fontsize=15)
    plt.xlabel("X coordinate", fontsize=15)
    plt.ylabel("Y coordinate", fontsize=15)
    plt.title("IL-6 with AP", fontsize=ts)
    plt.savefig('results/' + 'IL6AP.png', format='png', dpi=500, bbox_inches='tight')

    print('... Plotting Il10 heatmaps')
    n = loop_fig(n)
    plt.figure(n)
    TG_map = cell_concentrations["IL10"][119]
    Tmap = np.zeros((25, 25))
    for x in TG_map:
        a, b = x[0][0], x[0][1]
        Tmap[a, b] = x[1]
    # plt.show()
    plt.imshow(Tmap, cmap="hot", vmin=0, vmax=10)
    cbar = plt.colorbar()
    cbar.set_label('Concentration (Arbitrary units)', rotation=90, fontsize=15)
    plt.xlabel("X coordinate", fontsize=15)
    plt.ylabel("Y coordinate", fontsize=15)
    plt.title("IL-10 without AP", fontsize=ts)
    plt.savefig('results/' + 'IL10.png', format='png', dpi=500, bbox_inches='tight')

    n = loop_fig(n)
    plt.figure(n)
    TG_map = cell_concentrationsAP["IL10"][119]
    Tmap = np.zeros((25, 25))
    for x in TG_map:
        a, b = x[0][0], x[0][1]
        Tmap[a, b] = x[1]
    # plt.show()
    plt.imshow(Tmap, cmap="hot", vmin=0, vmax=10)
    cbar = plt.colorbar()
    cbar.set_label('Concentration (Arbitrary units)', rotation=90, fontsize=15)
    plt.xlabel("X coordinate", fontsize=15)
    plt.ylabel("Y coordinate", fontsize=15)
    plt.title("IL-10 with AP", fontsize=ts)
    plt.savefig('results/' + 'IL10AP.png', format='png', dpi=500, bbox_inches='tight')

    print('... Plotting TNFa heatmaps')
    n = loop_fig(n)
    plt.figure(n)
    TG_map = cell_concentrations["TNFa"][119]
    Tmap = np.zeros((25, 25))
    for x in TG_map:
        a, b = x[0][0], x[0][1]
        Tmap[a, b] = x[1]
    # plt.show()
    plt.imshow(Tmap, cmap="hot", vmin=0, vmax=10)
    cbar = plt.colorbar()
    cbar.set_label('Concentration (Arbitrary units)', rotation=90, fontsize=15)
    plt.xlabel("X coordinate", fontsize=15)
    plt.ylabel("Y coordinate", fontsize=15)
    plt.title("TNFa without AP", fontsize=ts)
    plt.savefig('results/' + 'TNFa.png', format='png', dpi=500, bbox_inches='tight')

    n = loop_fig(n)
    plt.figure(n)
    TG_map = cell_concentrationsAP["TNFa"][119]
    Tmap = np.zeros((25, 25))
    for x in TG_map:
        a, b = x[0][0], x[0][1]
        Tmap[a, b] = x[1]
    # plt.show()
    plt.imshow(Tmap, cmap="hot", vmin=0, vmax=10)
    cbar = plt.colorbar()
    cbar.set_label('Concentration (Arbitrary units)', rotation=90, fontsize=15)
    plt.xlabel("X coordinate", fontsize=15)
    plt.ylabel("Y coordinate", fontsize=15)
    plt.title("TNFa with AP", fontsize=ts)
    plt.savefig('results/' + 'TNFaAP.png', format='png', dpi=500, bbox_inches='tight')

    n = loop_fig(n)
    plt.figure(n)
    mac_phen = cell_concentrations["Mac_phen"]
    mac_phen_AP = cell_concentrationsAP["Mac_phen"]
    mac_1,mac_2,mac_1_AP,mac_2_AP =[],[],[],[]
    for x in mac_phen:
        mac_1.append(x[0])
        mac_2.append(x[1])
    for y in mac_phen_AP:
        mac_1_AP.append(y[0])
        mac_2_AP.append(y[1])
    plt.plot(mac_1, linewidth=lw, ls='-',label='NON-AP M1', color = "#377eb8")
    plt.plot(mac_2, linewidth=lw, ls='-',label='NON-AP M2', color = '#0b1924')
    plt.plot(mac_1_AP, linewidth=lw, ls='-',label='AP M1', color="#4daf4a")
    plt.plot(mac_2_AP, linewidth=lw, ls='-', label='AP M2', color = '#a6d7a4' )
    plt.ylabel('Concentration (Arbitrary units)', fontsize=fs)
    plt.xlabel("Time (h)", fontsize=fs)
    plt.ylim(0, 100)
    plt.xlim(0, 120)
    plt.legend(loc='best',fontsize = 20)
    plt.title("Macrophage Phenotypes", fontsize=ts)
    plt.tick_params(labelsize=ls)
    plt.tight_layout()
    print('... Plotting macrophage phenotypes')
    plt.savefig('results/' + 'macrophage_phenotypes.png', format='png', dpi=500, bbox_inches='tight')

    n = loop_fig(n)
    plt.figure(n)
    cytokines = cell_concentrations["Cytokines"]
    cytokines_AP = cell_concentrationsAP["Cytokines"]
    IL6, IL10, TNFa, TGFb, IL6_AP, IL10_AP, TNFa_AP, TGFb_AP = [], [], [], [], [], [], [], []
    for x in cytokines:
        IL6.append(x[0])
        IL10.append(x[1])
        TNFa.append(x[2])
        TGFb.append(x[3])
    for y in cytokines_AP:
        IL6_AP.append(y[0])
        IL10_AP.append(y[1])
        TNFa_AP.append(y[2])
        TGFb_AP.append(y[3])
    plt.plot(TNFa, linewidth=lw, ls='-', label='NON-AP TNFa')
    plt.plot(TNFa_AP, linewidth=lw, ls='-', label='AP TNFa')
    plt.plot(TGFb, linewidth=lw, ls='-', label='NON-AP TGFb')
    plt.plot(TGFb_AP, linewidth=lw, ls='-', label='AP TGFb')
    plt.ylabel("Total Cytokine Levels", fontsize=20)
    plt.xlabel("Time (h)", fontsize=20)
    plt.xlim(0, 120)
    plt.legend(loc='best', fontsize=15)
    plt.title("Cytokine Levels", fontsize=20)
    plt.tick_params(labelsize=15)
    plt.tight_layout()
    print('... Plotting cytokine levels')
    plt.savefig('results/' + 'cytokines.png', format='png', dpi=500, bbox_inches='tight')

    n = loop_fig(n)
    plt.figure(n)
    plt.plot(IL6, linewidth=lw, ls='-', label='NON-AP IL-6')
    plt.plot(IL6_AP, linewidth=lw, ls='-', label='AP IL-6')
    plt.plot(IL10, linewidth=lw, ls='-', label='NON-AP IL-10')
    plt.plot(IL10_AP, linewidth=lw, ls='-', label='AP IL-10')
    plt.ylabel("Concentration (Arbitrary units)", fontsize=20)
    plt.xlabel("Time (h)", fontsize=20)
    plt.xlim(0, 120)
    plt.legend(loc='best', fontsize=15)
    plt.title("Cytokine Levels", fontsize=20)
    plt.tick_params(labelsize=15)
    plt.tight_layout()
    print('... Plotting cytokine levels')
    plt.savefig('results/' + 'IL6_IL_10.png', format='png', dpi=500, bbox_inches='tight')


    n = loop_fig(n)
    plt.figure(n)
    plt.plot(cell_concentrations["Neutrophils"], color='red', linewidth=lw, ls='-', label="Active neutrophils")
    plt.plot(cell_concentrations["Phagocytized_neutrophils"], color='blue', linewidth=lw, ls='-', label="Phagocytized neutrophils")
    plt.plot(cell_concentrations["Apoptised_neutrophils"], color='yellow', linewidth=lw, ls='-', label="Apoptotic neutrophils")
    plt.plot(cell_concentrations["Necrotic_neutrophils"], color='green', linewidth=lw, ls='-', label="Necrotic neutrophils")
    plt.ylabel("Number of Neutrophils", fontsize=fs)
    plt.xlabel("Time (h)", fontsize=fs)
    plt.ylim(0, 100)
    plt.xlim(0, 120)
    plt.legend(loc='best', fontsize=15)
    plt.title("Neutrophil stages", fontsize=ts)
    plt.tick_params(labelsize=ls)
    plt.tight_layout()
    print('... Plotting neutrophil types')
    plt.savefig('results/' + 'neutrophils_stages.png', format='png', dpi=500, bbox_inches='tight')


def loop_fig(fignum):
    return fignum + 1

AP_vs_not_model()