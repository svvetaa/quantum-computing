from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

scheme1_2 = QuantumCircuit(1, 1)

scheme1_2.h(0)

scheme1_2.measure(0, 0)

scheme1_2.draw(output='mpl')

shots_list = [1, 2, 8, 1024, 10000]
results = {}

backend = Aer.get_backend('qasm_simulator')

for shots in shots_list:
    transpiled_circuit = transpile(scheme1_2, backend)

    job = backend.run(transpiled_circuit, shots=shots)

    result = job.result()
    counts = result.get_counts(transpiled_circuit)

    results[shots] = counts

    print(f"Результаты для {shots} измерений: {counts}")
    plot_histogram(counts)
    plt.show()