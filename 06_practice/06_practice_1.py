from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import numpy as np

def custom_qft_circuit():
    qc = QuantumCircuit(3)

    qc.x(0)
    qc.x(1)
    qc.x(2)
    qc.h(2)
    qc.cp(np.pi / 4, 2, 0)
    qc.cp(np.pi / 2, 2, 1)
    qc.h(1)
    qc.cp(np.pi / 2, 1, 0)
    qc.h(0)
    qc.swap(0, 2)
    qc.swap(0, 2)
    qc.h(0)
    qc.cp(-np.pi / 2, 0, 1)
    qc.h(1)
    qc.cp(-np.pi / 4, 2, 0)
    qc.cp(-np.pi / 2, 2, 1)
    qc.h(2)
    qc.measure_all()

    return qc

def run_simulation():
    qc = custom_qft_circuit()
    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)
    result = simulator.run(compiled_circuit).result()
    counts = result.get_counts(qc)
    plot_histogram(counts)
    plt.show()
    return counts

counts = run_simulation()
print("Результаты симуляции:", counts)