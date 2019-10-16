from batchrunner import FixedBatchRunner
from ABM import WoundModel, Blood_flow, Collagen
from agents import Neutrophil, Macrophage, Fibroblast, Endothelial


def batch_run(WoundModel):
    print('Running without AP....')
    fixed_params = {
    "Neutrophils": 80,
     "Macrophages": 50,
     "Fibroblasts": 50,
     "IL10": 0.5,
     "IL6": 0.5,
     "TNFa": 0.5,
     "TGFb": 0.5,
     "width": 25,
     "height": 25,
     "wound_radius": 10,
     "coagulation": 0.7
    }

    batch_run = FixedBatchRunner(WoundModel, fixed_parameters = fixed_params, max_steps=10, model_reporters={"Blood_flow": Blood_flow,"Collagen": Collagen,"Macrophages": lambda WoundModel: WoundModel.schedule.get_breed_count(Macrophage), "Neutrophils": lambda WoundModel: WoundModel.schedule.get_breed_count(Neutrophil), "Fibroblasts": lambda WoundModel: WoundModel.schedule.get_breed_count(Fibroblast)}
    )

    run_dataAP = batch_run.collect_model_vars(WoundModel)

    print('Running with AP....')
    fixed_params = {
        "Neutrophils": 50,
        "Macrophages": 50,
        "Fibroblasts": 50,
        "IL10": 0.5,
        "IL6": 0.5,
        "TNFa": 0.5,
        "TGFb": 0.5,
        "width": 25,
        "height": 25,
        "wound_radius": 10,
        "coagulation": 0.7
    }

    batch_run = FixedBatchRunner(
        WoundModel, variable_parameters=None,
        fixed_parameters=fixed_params, iterations= 2,
        max_steps=10,
        model_reporters={"Blood_flow": Blood_flow, "Collagen": Collagen, "Macrophages": lambda WoundModel: WoundModel.schedule.get_breed_count(Macrophage), "Neutrophils": lambda WoundModel: WoundModel.schedule.get_breed_count(Neutrophil), "Fibroblasts": lambda WoundModel: WoundModel.schedule.get_breed_count(Fibroblast)}
    )

    batch_run.run_all()
    run_data = batch_run.collect_model_vars()
    print(run_data[['Blood_flow', 'Neutrophils']])


batch_run(WoundModel)