from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

scheme1_3 = QuantumCircuit(2, 2)

scheme1_3.h(0)

scheme1_3.x(1)

scheme1_3.cx(0, 1)

scheme1_3.measure([0, 1], [0, 1])

scheme1_3.draw(output='mpl')

backend = Aer.get_backend('qasm_simulator')
transpiled_circuit = transpile(scheme1_3, backend)

job = backend.run(transpiled_circuit, shots=1000)

result = job.result()
counts = result.get_counts(transpiled_circuit)

print("Результаты: ", counts)
plot_histogram(counts)
plt.show()