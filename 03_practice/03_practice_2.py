from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer, AerSimulator
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit.quantum_info import Statevector
import math
import matplotlib.pyplot as plt

simulator = AerSimulator()

qc1 = QuantumCircuit(1, 1)
qc1.h(0)
qc1.reset(0)
qc1.measure(0, 0)

qc2 = QuantumCircuit(1, 1)
qc2.reset(0)
qc2.x(0)
qc2.measure(0, 0)

qc3 = QuantumCircuit(1, 1)
qc3.h(0)
qc3.measure(0, 0)

qc4 = QuantumCircuit(1, 1)
qc4.x(0)
qc4.h(0)
qc4.measure(0, 0)

qc5 = QuantumCircuit(1, 1)
qc5.rx(math.pi / 5, 0)

qc6 = QuantumCircuit(1, 1)
qc6.rx(math.pi / 5, 0)
qc6.x(0)

schemes = [qc1, qc2, qc3, qc4, qc5, qc6]
results = []

for i, qc in enumerate(schemes):
    print(f"Scheme1_5_{i + 1}:")

    if i < 4:
        compiled_circuit = transpile(qc, simulator)
        job = simulator.run(compiled_circuit, shots=1000)
        result = job.result()
        counts = result.get_counts(compiled_circuit)
        results.append(counts)

        print(f"Результаты scheme1_5_{i + 1}: {counts}")
        plot_histogram(counts)
        qc.draw(output='mpl', filename=f"результат_scheme1_5_{i + 1}.png")
        plt.show()

state_5 = Statevector.from_instruction(qc5)
plot_bloch_multivector(state_5.data)
plt.title("Состояние кубита для scheme1_5_5 на сфере Блоха\n")
plt.show()

state_6 = Statevector.from_instruction(qc6)
plot_bloch_multivector(state_6.data)
plt.title("Состояние кубита для scheme1_5_6 на сфере Блоха\n")
plt.show()
