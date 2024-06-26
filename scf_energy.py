import numpy as np
import matplotlib.pyplot as plt

def plot_scf_energy(filename):
    with open(filename) as f:
        lines = f.readlines()
        
    energy = []

    num_lines = len(lines) - 1
    for i in range(num_lines):
        line = lines[i]
        if "FINAL SINGLE POINT ENERGY" in line:
            scf_energy = float(line.split()[4])
            print(scf_energy)
            energy.append(scf_energy)        
            
    #print(energy)

    plt.plot(energy)
    plt.title(filename)
    plt.show()
    
output_files = [
    "opt-pro1-M062X-cc-pVTZ.log",
    "opt-pro1-M062X-cc-pVTZ.log",
    "opt-pro1-M062X-cc-pVTZ.log",
    "opt-pro1-M062X-cc-pVTZ.log",
]


for f in output_files:
    plot_scf_energy(f)