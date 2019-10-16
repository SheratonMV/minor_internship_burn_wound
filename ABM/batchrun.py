from mesa.batchrunner import BatchRunner


def batch_run(WoundModel):

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

    batch_run = BatchRunner(
    WoundModel,variable_parameters=None,
    fixed_parameters = fixed_params,
    max_steps=10,
    model_reporters={"Blood_flow": Blood_flow,"Collagen": Collagen,"Macrophages": lambda WoundModel: WoundModel.schedule.get_breed_count(Macrophage), "Neutrophils": lambda WoundModel: WoundModel.schedule.get_breed_count(Neutrophil), "Fibroblasts": lambda WoundModel: WoundModel.schedule.get_breed_count(Fibroblast)}
    )

    batch_run.run_all()
    run_dataAP = batch_run.get_model_vars_dataframe()

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

    batch_run = BatchRunner(
        WoundModel, variable_parameters=None,
        fixed_parameters=fixed_params, iterations= 5,
        max_steps=10,
        model_reporters={"Blood_flow": Blood_flow, "Collagen": Collagen, "Macrophages": lambda WoundModel: WoundModel.schedule.get_breed_count(Macrophage), "Neutrophils": lambda WoundModel: WoundModel.schedule.get_breed_count(Neutrophil), "Fibroblasts": lambda WoundModel: WoundModel.schedule.get_breed_count(Fibroblast)}
    )

    batch_run.run_all()
    run_data = batch_run.get_model_vars_dataframe()
    print(run_data[['Blood_flow', 'Neutrophils']])


batch_run(WoundModel)