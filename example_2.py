from qiskit import QuantumCircuit, Aer, execute

# Defining the number of qubits and the number of marked elements
n = 3
marked = [4]

# Defining the Grover's algorithm circuit
qc = QuantumCircuit(n, n)

# Apply a Hadamard gate to all qubits
qc.h(range(n))

# Apply the oracle to mark the target element
for i in marked:
    qc.barrier()
    b = "{0:b}".format(i).zfill(n)
    for j in range(n):
        if b[j] == "0":
            qc.x(j)
    qc.cz(0, 1)
    for j in range(n):
        if b[j] == "0":
            qc.x(j)
    qc.barrier()

# Applying the diffuser
qc.h(range(n))
qc.x(range(n))
qc.h(n-1)
qc.mct(list(range(n-1)), n - 1)
qc.h(n - 1)
qc.x(range(n))
qc.h(range(n))


# Measure the qubits
qc.measure(range(n), range(n))

# Running the circuit on the simulator
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, simulator).result()

# Print the measurement outcome
print(result.get_counts(qc))