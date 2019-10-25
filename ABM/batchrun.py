from batchrunner import FixedBatchRunner
from ABM import WoundModel, Blood_flow, Collagen
from agents import Neutrophil, Macrophage, Fibroblast, Endothelial
import matplotlib.pyplot as plt
import pandas as pd

def batch_run(WoundModel):
    # Batch run with AP
    print('Running with AP....')
    fixed_paramsAP = {"Neutrophils": 80,
     "Macrophages": 50,
     "Fibroblasts": 50,
     "IL10": 7,
     "IL6": 0.0,
     "TNFa": 0.5,
     "TGFb": 0.5,
     "width": 25,
     "height": 25,
     "wound_radius": 10,
     "coagulation": 0.7}
    batch_run = FixedBatchRunner(WoundModel, iterations= 5, fixed_parameters = fixed_paramsAP, max_steps=10, model_reporters={"Blood_flow": Blood_flow,"Collagen": Collagen,"Macrophages": lambda WoundModel: WoundModel.schedule.get_breed_count(Macrophage), "Neutrophils": lambda WoundModel: WoundModel.schedule.get_breed_count(Neutrophil), "Fibroblasts": lambda WoundModel: WoundModel.schedule.get_breed_count(Fibroblast)})
    batch_run.run_all()
    run_dataAP = batch_run.get_model_vars_dataframe()
    run_dataAP['Treatment'] = 'AP'

    # Batch run without AP
    print('Running without AP....')
    fixed_params = {"Neutrophils": 50,
        "Macrophages": 50,
        "Fibroblasts": 50,
        "IL10": 0.5,
        "IL6": 0.5,
        "TNFa": 0.5,
        "TGFb": 0.5,
        "width": 25,
        "height": 25,
        "wound_radius": 10,
        "coagulation": 0.7}
    batch_run = FixedBatchRunner(WoundModel, fixed_parameters=fixed_params, iterations= 5, max_steps=10, model_reporters={"Blood_flow": Blood_flow, "Collagen": Collagen, "Macrophages": lambda WoundModel: WoundModel.schedule.get_breed_count(Macrophage), "Neutrophils": lambda WoundModel: WoundModel.schedule.get_breed_count(Neutrophil), "Fibroblasts": lambda WoundModel: WoundModel.schedule.get_breed_count(Fibroblast)})
    batch_run.run_all()
    run_data = batch_run.get_model_vars_dataframe()
    run_data['Treatment'] ='NON-AP'

    # Boxplots of combined data
    boxplotdata = pd.concat([run_dataAP, run_data])

    fs = 25  # Fontsize axes
    ts = 30  # Title size
    ls = 20  # Labelsize

    n = loop_fig(1)
    plt.figure(n)
    boxplotdata.boxplot(column=["Collagen"], by = 'Treatment')
    plt.ylabel('Concentration (Arbitrary units)', fontsize=fs)
    plt.xlabel("Treatment", fontsize=fs)
    plt.title("Collagen", fontsize=ts)
    plt.ylim(0,100)
    plt.tick_params(labelsize=ls)
    plt.savefig('results/' + 'Boxplot_collagen.png', format='png', dpi=500, bbox_inches='tight')

    n = loop_fig(n)
    plt.figure(n)
    boxplotdata.boxplot(column=["Blood_flow"], by='Treatment')
    plt.ylabel('Concentration (Arbitrary units)', fontsize=fs)
    plt.xlabel("Treatment", fontsize=fs)
    plt.title("Collagen", fontsize=ts)
    plt.ylim(0,100)
    plt.tick_params(labelsize=ls)
    plt.savefig('results/' + 'Boxplot_bloodflow.png', format='png', dpi=500, bbox_inches='tight')

def ugly_batch_run(step_count):
    """ The batch run presented by the mesa framework only measured data at the end of a run, so we built an 'ugly' coded batchrun which does work."""

    # Running multiple models with AP
    print('Running with AP....')
    AP1 = run_model("AP",step_count)
    AP2 = run_model("AP",step_count)
    AP3 = run_model("AP",step_count)
    AP4 = run_model("AP",step_count)
    AP5 = run_model("AP",step_count)

    # Running multiple models without AP
    print('Running without AP....')
    NON_AP1 = run_model("NON-AP",step_count)
    NON_AP2 = run_model("NON-AP",step_count)
    NON_AP3 = run_model("NON-AP",step_count)
    NON_AP4 = run_model("NON-AP",step_count)
    NON_AP5 = run_model("NON-AP",step_count)

    # Text setup in plots
    lw = 2  # Linewidth
    ls = 20  # Labelsize
    fs = 25  # Fontsize
    lfs = 10  # Fontsize legend
    ts = 30  # Title size

    # Plotting batch run results
    n = loop_fig(1)
    plt.figure(n)
    color = ['cyan', 'lightblue', 'steelblue', 'midnightblue', 'blue', 'limegreen', 'darkgreen', 'lime', 'lawngreen', 'lightgreen']
    colorcount = 0
    for frame in [AP1,AP2,AP3,AP4,AP5]:
        plt.plot(frame["Blood_flow"], linewidth=lw, ls='-', label = "AP", color= color[colorcount])
        colorcount +=1
    for frame in [NON_AP1, NON_AP2, NON_AP3, NON_AP4, NON_AP5]:
        plt.plot(frame["Blood_flow"], linewidth=lw, ls='-', label="NON AP", color= color[colorcount])
        colorcount += 1
    plt.ylabel("Oxygen (Arbitrary units)", fontsize=fs)
    plt.xlabel("Time (h)", fontsize=fs)
    plt.title("Blood flow", fontsize=ts)
    plt.ylim(0, 100)
    plt.xlim(0, 120)
    plt.legend(loc='best', fontsize=lfs)
    plt.tick_params(labelsize=ls)
    print('... Plotting blood flow')
    plt.savefig('results/' + 'Bloodflow_batchrun.png', format='png', dpi=500, bbox_inches='tight')
    plt.show()

    n = loop_fig(1)
    plt.figure(n)
    color = ['cyan', 'lightblue', 'steelblue', 'midnightblue', 'blue', 'limegreen', 'darkgreen', 'lime', 'lawngreen',
             'lightgreen']
    colorcount = 0
    for frame in [AP1, AP2, AP3, AP4, AP5]:
        plt.plot(frame["Collagen"], linewidth=lw, ls='-', label="AP", color=color[colorcount])
        colorcount += 1
    for frame in [NON_AP1, NON_AP2, NON_AP3, NON_AP4, NON_AP5]:
        plt.plot(frame["Collagen"], linewidth=lw, ls='-', label="NON AP", color=color[colorcount])
        colorcount += 1
    plt.ylabel("Collagen (Arbitrary units)", fontsize=fs)
    plt.xlabel("Time (h)", fontsize=fs)
    plt.title("Collagen", fontsize=ts)
    plt.ylim(0, 100)
    plt.xlim(0, 120)
    plt.legend(loc='best', fontsize=lfs)
    plt.tick_params(labelsize=ls)
    print('... Plotting Collagen')
    plt.savefig('results/' + 'Collagen_batchrun.png', format='png', dpi=500, bbox_inches='tight')
    plt.show()

def run_model(treatment,step_count):
    if treatment == "NON-AP":
        model = WoundModel(50, 50, 50, 0.5, 0.5, 0.5, 0.5, 25, 25, 10, 0.7)
        for j in range(step_count):
            model.step()
        return model.datacollector.get_model_vars_dataframe()
    elif treatment == "AP":
        model = WoundModel(80, 50, 50, 10, 0, 0.5, 0.5, 25, 25, 10, 0.7)
        for j in range(step_count):
            model.step()
        return model.datacollector.get_model_vars_dataframe()

def ugly_batch_run2(step_count):
    """ The batch run presented by the mesa framework only measured data at the end of a run, so we built an 'ugly' coded batchrun which does work."""

    # Running multiple models with AP
    print('Running with AP....')
    AP0 = run_model_IL10(0,step_count)
    AP1 = run_model_IL10(1,step_count)
    AP2 = run_model_IL10(2,step_count)
    AP3 = run_model_IL10(3,step_count)
    AP4 = run_model_IL10(4,step_count)
    print('halfway')
    AP5 = run_model_IL10(5, step_count)
    AP6 = run_model_IL10(6, step_count)
    AP7 = run_model_IL10(7, step_count)
    AP8 = run_model_IL10(8, step_count)
    AP9 = run_model_IL10(9, step_count)
    AP10 = run_model_IL10(10, step_count)

    # Text setup in plots
    lw = 2  # Linewidth
    ls = 20  # Labelsize
    fs = 25  # Fontsize
    lfs = 15  # Fontsize legend
    ts = 30  # Title size

    # Plotting batch run results
    n = loop_fig(1)
    plt.figure(n)
    color = ['cyan', 'lightblue', 'steelblue', 'midnightblue', 'blue', 'limegreen', 'darkgreen', 'lime', 'lawngreen', 'lightgreen', 'green']
    IL10label = ['0','1','2','3','4','5','6','7','8','9','10']
    colorcount = 0
    for frame in [AP0,AP1,AP2,AP3,AP4,AP5,AP6,AP7,AP8,AP9,AP10]:
        plt.plot(frame["Blood_flow"], linewidth=lw, ls='-', label = IL10label[colorcount] , color= color[colorcount])
        colorcount +=1
    plt.ylabel("Concentration (Arbitrary units)", fontsize=fs)
    plt.xlabel("Time (h)", fontsize=fs)
    plt.title("Blood flow", fontsize=ts)
    plt.ylim(0, 100)
    plt.xlim(0, 120)
    plt.legend(title = 'IL-10 Concentration', ncol = 2, fontsize=lfs, loc='center left', bbox_to_anchor=(1, 0.5))
    plt.tick_params(labelsize=ls)
    print('... Plotting blood flow')
    plt.savefig('results/' + 'Bloodflow_IL10.png', format='png', dpi=500, bbox_inches='tight')
    plt.show()

    # Plotting batch run results
    n = loop_fig(n)
    plt.figure(n)
    colorcount = 0
    for frame in [AP0, AP1, AP2, AP3, AP4, AP5, AP6, AP7, AP8, AP9, AP10]:
        plt.plot(frame["Collagen"], linewidth=lw, ls='-', label=IL10label[colorcount], color=color[colorcount])
        colorcount += 1
    plt.ylabel("Concentration (Arbitrary units)", fontsize=fs)
    plt.xlabel("Time (h)", fontsize=fs)
    plt.title("Collagen", fontsize=ts)
    plt.ylim(0, 100)
    plt.xlim(0, 120)
    plt.legend(title = 'IL-10 Concentration', ncol = 2, fontsize=lfs,  loc='center left', bbox_to_anchor=(1, 0.5))
    plt.tick_params(labelsize=ls)
    print('... Plotting blood flow')
    plt.savefig('results/' + 'Collagen_IL10.png', format='png', dpi=500, bbox_inches='tight')
    plt.show()

    n = loop_fig(n)
    plt.figure(n)
    colorcount = 0
    for frame in [AP0, AP1, AP2, AP3, AP4, AP5, AP6, AP7, AP8, AP9, AP10]:
        plt.plot(frame["Neutrophils"], linewidth=lw, ls='-', label=IL10label[colorcount], color=color[colorcount])
        colorcount += 1
    plt.ylabel("Concentration (Arbitrary units)", fontsize=fs)
    plt.xlabel("Time (h)", fontsize=fs)
    plt.title("Neutrophils", fontsize=ts)
    plt.ylim(0, 100)
    plt.xlim(0, 120)
    plt.legend(title='IL-10 Concentration', ncol=2, fontsize=lfs, loc='center left', bbox_to_anchor=(1, 0.5))
    plt.tick_params(labelsize=ls)
    print('... Plotting neutrophils')
    plt.savefig('results/' + 'Neutrophils.png', format='png', dpi=500, bbox_inches='tight')
    plt.show()


    n = loop_fig(n)
    plt.figure(n)
    colorcount = 0
    for frame in [AP0, AP1, AP2, AP3, AP4, AP5, AP6, AP7, AP8, AP9, AP10]:
        plt.plot(frame["Fibroblasts"], linewidth=lw, ls='-', label=IL10label[colorcount], color=color[colorcount])
        colorcount += 1
    plt.ylabel("Concentration (Arbitrary units)", fontsize=fs)
    plt.xlabel("Time (h)", fontsize=fs)
    plt.title("Fibroblasts", fontsize=ts)
    plt.ylim(0, 100)
    plt.xlim(0, 120)
    plt.legend(title = 'IL-10 Concentration', ncol = 2, fontsize=lfs,  loc='center left', bbox_to_anchor=(1, 0.5))
    plt.tick_params(labelsize=ls)
    print('... Plotting fibroblasts')
    plt.savefig('results/' + 'fibroblasts_IL10.png', format='png', dpi=500, bbox_inches='tight')
    plt.show()

    n = loop_fig(n)
    plt.figure(n)
    colorcount = 0
    for frame in [AP0, AP1, AP2, AP3, AP4, AP5, AP6, AP7, AP8, AP9, AP10]:
        mac_phen = frame["Mac_phen"]
        mac_2 = []
        for x in mac_phen:
            mac_2.append(x[1])
        plt.plot(mac_2, linewidth=lw, ls='-', label=IL10label[colorcount], color=color[colorcount])
        colorcount += 1
    plt.ylabel("Concentration (Arbitrary units)", fontsize=fs)
    plt.xlabel("Time (h)", fontsize=fs)
    plt.title("M2 macrophages", fontsize=ts)
    plt.ylim(0, 100)
    plt.xlim(0, 120)
    plt.legend(title = 'IL-10 Concentration', ncol = 2, fontsize=lfs,  loc='center left', bbox_to_anchor=(1, 0.5))
    plt.tick_params(labelsize=ls)
    print('... Plotting m2 macrophages')
    plt.savefig('results/' + 'M2_IL10.png', format='png', dpi=500, bbox_inches='tight')
    plt.show()

    n = loop_fig(n)
    plt.figure(n)
    colorcount = 0
    for frame in [AP0, AP1, AP2, AP3, AP4, AP5, AP6, AP7, AP8, AP9, AP10]:
        mac_phen = frame["Mac_phen"]
        mac_1 = []
        for x in mac_phen:
            mac_1.append(x[0])
        plt.plot(mac_1, linewidth=lw, ls='-', label=IL10label[colorcount], color=color[colorcount])
        colorcount += 1
    plt.ylabel("Concentration (Arbitrary units)", fontsize=fs)
    plt.xlabel("Time (h)", fontsize=fs)
    plt.title("M1 macrophages", fontsize=ts)
    plt.ylim(0, 100)
    plt.xlim(0, 120)
    plt.legend(title='IL-10 Concentration', ncol=2, fontsize=lfs, loc='center left', bbox_to_anchor=(1, 0.5))
    plt.tick_params(labelsize=ls)
    print('... Plotting M1 macrophages')
    plt.savefig('results/' + 'M1_IL10.png', format='png', dpi=500, bbox_inches='tight')
    plt.show()




def run_model_IL10(value,step_count):
    model = WoundModel(50, 50, 50, value, 0.5,0.5, 0.5, 25, 25, 10, 0.7)
    for j in range(step_count):
        model.step()
    return model.datacollector.get_model_vars_dataframe()




def loop_fig(fignum):
    return fignum + 1

ugly_batch_run2(120)
#batch_run(WoundModel)