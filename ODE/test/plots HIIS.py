import matplotlib.pyplot as plt
import numpy

x = numpy.linspace(0,5,100) # 100 linearly spaced numbers
y = 5.302294 + 461.4242*x - 178.0119*x**2 + 17.17551*x**3

def loop_fig(fignum):
    return fignum + 1

# compose plot
lw = 5
ls = 15
fs = 15
lfs = 25
ts = 20

n = loop_fig(1)
plt.figure(n)
plt.plot(x,y, linewidth=lw, ls='-', color = "#377eb8" )
plt.xlim(0,5)
plt.ylim(0,400)
plt.ylabel("Recruited fibroblasts $(cells/mm^3)$", fontsize=fs)
plt.xlabel("PDGF ($pg/mm^3$)", fontsize=fs)
#plt.title("Fibroblast recruitment by PDGF per day", fontsize=ts)
plt.tick_params(labelsize=ls)
plt.tight_layout()
print('... Plotting macrophages')
plt.savefig('result/' + 'PDGF-FIBRO.png', format='png', dpi=500, bbox_inches='tight')

x = numpy.linspace(0,1400,100) # 100 linearly spaced numbers
y = 0.1378065 - 0.0005775911*x + 9.28343e-7*x**2 - 4.441029e-10*x**3

n = loop_fig(n)
plt.figure(n)
plt.plot(x,y, linewidth=lw, ls='-', color = "#377eb8" )
plt.xlim(0,1400)
plt.ylim(0,0.15)
plt.ylabel("Collagen synthesis ratio", fontsize=fs)
plt.xlabel(" Collagen $(\u03bcg/mm^3$)", fontsize=fs)
#plt.title("Collagen synthesis ratio based on the TGF-$\beta$ concentration", fontsize=ts)
plt.tick_params(labelsize=ls)
plt.tight_layout()
print('... Plotting coll-coll')
plt.savefig('result/' + 'Coll-coll.png', format='png', dpi=500, bbox_inches='tight')

x = numpy.linspace(0,9,100) # 100 linearly spaced numbers
y = 0.2151515 + 0.6137554 * x - 0.149513 * x ** 2 + 0.008787879 * x ** 3

n = loop_fig(n)
plt.figure(n)
plt.plot(x,y, linewidth=lw, ls='-', color = "#377eb8" )
plt.xlim(0,9)
plt.ylim(0,1)
plt.ylabel("Collagen synthesis ratio", fontsize=fs)
plt.xlabel(" TGFB $(\u03bcg/mm^3$)", fontsize=fs)
#plt.title("Collagen production ratio by TGFB", fontsize=ts)
plt.tick_params(labelsize=ls)
plt.tight_layout()
print('... Plotting tgfb-coll')
plt.savefig('result/' + 'tgfb-coll.png', format='png', dpi=500, bbox_inches='tight')

x = numpy.linspace(0,100,100) # 100 linearly spaced numbers
y = 0.0492 * x**3 - 0.9868 * x**2 + 6.5408 * x +7.1092


n = loop_fig(n)
plt.figure(n)
plt.plot(x,y/24, linewidth=lw, ls='-', color = "#377eb8" )
plt.xlim(0,5)
plt.ylim(0,1)
plt.ylabel("Fibroblats activation ratio", fontsize=fs)
plt.xlabel(" TGFB $(\u03bcg/mm^3$)", fontsize=fs)
#plt.title("Collagen production ratio by TGFB", fontsize=ts)
plt.tick_params(labelsize=ls)
plt.tight_layout()
print('... Plotting Fibro-tgfb')
plt.savefig('result/' + 'Fibro-tgfb.png', format='png', dpi=500, bbox_inches='tight')