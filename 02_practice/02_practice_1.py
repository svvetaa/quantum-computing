from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer

scheme1_1 = QuantumCircuit(2, 2)

scheme1_1.x(1)

scheme1_1.measure([0, 1], [0, 1])

scheme1_1.draw(output='mpl', filename="python")

backend = Aer.get_backend('qasm_simulator')
transpiled_circuit = transpile(scheme1_1, backend)

job = backend.run(transpiled_circuit, shots=500)

result = job.result()
counts = result.get_counts(transpiled_circuit)

print("Результаты: ", counts)