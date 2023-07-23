# -*- coding: utf-8 -*-

"""
    Programa desarrollado por el Licenciado César Cordero Rodríguez.
    Bajo licencia GPLv3.
    Puede ser modificado, copiado y distribuido.
    Se desarrolló con fines educativos.
    Basado en el libro Quantum Development with Qiskit de O'Reilly.
"""

#Read more here: https://github.com/qiskit-community/qiskit-pocket-guide

#TO INSTALL:
#pip3 install qiskit
#pip3 install matplotlib
#pip3 install pylatexenc

from qiskit import *
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qasm_str = """
OPENQASM 2.0;
include "qelib1.inc";
qreg q[2];
creg c[2];
h q[0];
cx q[0],q[1];
measure q[0] -> c[0];
measure q[1] -> c[1];
"""
qc = QuantumCircuit.from_qasm_str(qasm_str)
qc.draw()

backend = BasicAer.get_backend('qasm_simulator')
job = execute(qc, backend)

plot_histogram(job.result().get_counts(qc), color='midnightblue', title="New Histogram (Classic computers (2). Quantum computer (various))")

plt.show()
