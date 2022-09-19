from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_ibm_runtime.accounts.exceptions import AccountNotFoundError
from qiskit_ibm_runtime.api.exceptions import RequestsApiError


if __name__ == "__main__":
    channel = "ibm_quantum"
    try:
        service = QiskitRuntimeService(channel="ibm_quantum")
    except AccountNotFoundError:
        token = input("Please provide your IBM Quantum token: ").strip()
        try:
            service = QiskitRuntimeService(channel="ibm_quantum", token=token)
        except RequestsApiError as ex:
            if "Error code: 3446" in ex.message:
                raise ValueError("Authentication failed. Make sure the "
                                 "token you passed in is correct.") from None
            raise

    print("Doing quantum magic, please wait...")
    options = {"backend_name": "ibmq_qasm_simulator"}
    job = service.run(program_id="hello-world", inputs={}, options=options)
    print(job.result())
