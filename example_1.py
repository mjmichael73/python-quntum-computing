from qiskit import QuantumCircuit, Aer, execute

# Create a Quantum Circuit With 2 Qubits
qc = QuantumCircuit(2)

# Applying a Hadamard gate to the first qubit
qc.h(0)

# Apply a CX gate between the first and second qubits
qc.cx(0, 1)

# Measuring both qubits
qc.measure_all()


# Using the QisKit Simulator to run the circuit
simulator = Aer.get_backend('qasm_simulator')

# Printing the measurement outcome for 100 runs
for i in range(0, 100):
    result = execute(qc, simulator, shots=1024).result()
    result_counts = result.get_counts(qc)
    if result_counts['11'] == result_counts['00']:
        print(result.get_counts(qc))


