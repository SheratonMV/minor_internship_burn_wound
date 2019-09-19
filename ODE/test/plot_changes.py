import os
import matplotlib.pyplot as plt
import glob
import pandas as pd
import functools
import Parameters as prms

#create combined dataframe of all CSV files in folder
filenames = sorted(glob.glob('infection/neutrophil_change/*.csv'))
dflist = []
for file in filenames:
    data = pd.read_csv(file)
    data = data[['Time', 'N_R']]
    dflist = dflist + [data]


dataframe = functools.reduce(lambda x, y: pd.merge(x, y, on ='Time'), dflist)
dataframe.plot(x= 'Time', legend=None)
plt.xlabel("Hours After Operation")
plt.ylabel("concentration $(cells/mm^3$)")
plt.title("Resting Neutrophils using different initial Neutrophil counts")
plt.xlim((0, prms._stoptime / 60.))
plt.axhline(y = 500, color = 'b')
plt.text(20,540,'Neutropenia cut-off')
plt.savefig('infection/Resting_Neutrophils.png', format='png', dpi=500, bbox_inches='tight')
plt.show()

####################################################

filenames = sorted(glob.glob('infection/antiinflammation_change/*.csv'))
dflist = []
for file in filenames:
    data = pd.read_csv(file)
    data = data[['Time', 'N_A']]
    dflist = dflist + [data]


dataframe = functools.reduce(lambda x, y: pd.merge(x, y, on ='Time'), dflist)
dataframe.plot(x= 'Time', legend = ('label1', 'label2', 'label3'))

plt.xlabel("Hours After Operation")
plt.ylabel("concentration $(cells/mm^3$)")
plt.title("Activated Neutrophils using different vascular permeabilities")
plt.legend(fontsize=20)
plt.xlim((0, prms._stoptime / 60.))
plt.savefig('infection/Activated_Neutrophils_perm_change.png', format='png', dpi=500, bbox_inches='tight')
plt.show()

filenames = sorted(glob.glob('infection/antiinflammation_change/*.csv'))
dflist = []
for file in filenames:
    data = pd.read_csv(file)
    data = data[['Time', 'N_R']]
    dflist = dflist + [data]


dataframe = functools.reduce(lambda x, y: pd.merge(x, y, on ='Time'), dflist)
dataframe.plot(x= 'Time', legend=None)
plt.xlabel("Hours After Operation")
plt.ylabel("concentration $(cells/mm^3$)")
plt.title("Activated Neutrophils using different initial Neutrophil counts")
plt.xlim((0, prms._stoptime / 60.))
plt.savefig('infection/Resting_Neutrophils_perm_change.png', format='png', dpi=500, bbox_inches='tight')
plt.show()