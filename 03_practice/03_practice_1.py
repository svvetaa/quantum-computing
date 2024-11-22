from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram
from qiskit_aer import Aer, AerSimulator
import matplotlib.pyplot as plt

simulator = AerSimulator()

qc1 = QuantumCircuit(2, 2)

qc1.x(0)
qc1.h(0)
qc1.h(1)
qc1.cx(1, 0)
qc1.measure(0, 0)

compiled_qc1 = transpile(qc1, simulator)

result1 = simulator.run(compiled_qc1, shots=1000).result()

counts1 = result1.get_counts()

qc2 = QuantumCircuit(2, 2)

qc2.x(0)
qc2.h(0)
qc2.h(1)
qc2.cx(1, 0)

qc2.measure(0, 0)
qc2.measure(1, 1)

compiled_qc2 = transpile(qc2, simulator)

result2 = simulator.run(compiled_qc2, shots=1000).result()

counts2 = result2.get_counts()

print("Гистограмма для scheme1_4_1:")
plot_histogram(counts1, filename="scheme1_4_1")
plt.show()

print("Гистограмма для scheme1_4_2:")
plot_histogram(counts2, filename="scheme1_4_2")
plt.show()