from batchrunner import FixedBatchRunner
from ABM import WoundModel, Blood_flow, Collagen
from agents import Neutrophil, Macrophage, Fibroblast, Endothelial
import matplotlib.pyplot as plt
import pandas as pd

def batch_run(WoundModel):
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
    batch_run = FixedBatchRunner(WoundModel, iterations= 20, fixed_parameters = fixed_paramsAP, max_steps=30, model_reporters={"Blood_flow": Blood_flow,"Collagen": Collagen,"Macrophages": lambda WoundModel: WoundModel.schedule.get_breed_count(Macrophage), "Neutrophils": lambda WoundModel: WoundModel.schedule.get_breed_count(Neutrophil), "Fibroblasts": lambda WoundModel: WoundModel.schedule.get_breed_count(Fibroblast)})
    batch_run.run_all()
    run_dataAP = batch_run.get_model_vars_dataframe()
    run_dataAP['Treatment'] = 'AP'

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
    batch_run = FixedBatchRunner(WoundModel, fixed_parameters=fixed_params, iterations= 20, max_steps=30, model_reporters={"Blood_flow": Blood_flow, "Collagen": Collagen, "Macrophages": lambda WoundModel: WoundModel.schedule.get_breed_count(Macrophage), "Neutrophils": lambda WoundModel: WoundModel.schedule.get_breed_count(Neutrophil), "Fibroblasts": lambda WoundModel: WoundModel.schedule.get_breed_count(Fibroblast)})
    batch_run.run_all()
    run_data = batch_run.get_model_vars_dataframe()
    run_data['Treatment'] = 'NON-AP'

    #Boxplots
    boxplotdata = pd.concat([run_dataAP, run_data])

    n = loop_fig(1)
    plt.figure(n)
    boxplotdata.boxplot(column=["Collagen"], by = 'Treatment')
    plt.ylim(0,20)
    plt.savefig('results/' + 'Boxplot_collagen.png', format='png', dpi=500, bbox_inches='tight')

    n = loop_fig(n)
    plt.figure(n)
    boxplotdata.boxplot(column=["Blood_flow"], by='Treatment')
    plt.ylim(70, 100)
    plt.savefig('results/' + 'Boxplot_bloodflow.png', format='png', dpi=500, bbox_inches='tight')

def ugly_batch_run(step_count):
    print('Running with AP....')
    AP1 = run_model("AP",step_count)
    AP2 = run_model("AP",step_count)
    AP3 = run_model("AP",step_count)
    AP4 = run_model("AP",step_count)
    AP5 = run_model("AP",step_count)

    print('Running without AP....')
    NON_AP1 = run_model("NON-AP",step_count)
    NON_AP2 = run_model("NON-AP",step_count)
    NON_AP3 = run_model("NON-AP",step_count)
    NON_AP4 = run_model("NON-AP",step_count)
    NON_AP5 = run_model("NON-AP",step_count)

    lw = 2  # Linewidth
    ls = 20  # Labelsize
    fs = 25  # Fontsize
    lfs = 10  # Fontsize legend
    ts = 30  # Title size

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

def run_model(treatment,step_count):
    if treatment == "NON-AP":
        model = WoundModel(50, 50, 50, 0.5, 0.5, 0.5, 0.5, 25, 25, 10, 0.7)
        for j in range(step_count):
            model.step()
        return model.datacollector.get_model_vars_dataframe()
    if treatment == "AP":
        model = WoundModel(80, 50, 50, 10, 0, 0.5, 0.5, 25, 25, 10, 0.7)
        for j in range(step_count):
            model.step()
        return model.datacollector.get_model_vars_dataframe()


def loop_fig(fignum):
    return fignum + 1

ugly_batch_run(120)
#batch_run(WoundModel)