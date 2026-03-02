"""
Context:
Hospitals store large amounts of data keyed by patient ID. A hash map (dictionary)
allows quick lookups by ID.

Exercise:
1) Create a dictionary patient_records mapping IDs to short info strings.
2) Add a few records, retrieve one by its key, and demonstrate key checking.
"""


def demo_hash_map():
    patient_records = {}

    # TODO: Add patient records to the dictionary using patient IDs as keys.
    # Patients to add:
    # - Patient "1001", with value "Patient A: Diagnosed with flu"
    # - Patient "1002", with value "Patient B: Chest X-Ray pending"
    # - Patient "1003", with value "Patient C: Discharged"
    patient_records = { 1001: "Diagnosed with flu",
    1002: "Chest X-Ray pending",
    1003: "Patient C: Discharged"}
    patient_records[1004] = "Blood test results ready"
    patient_records[1005] = "Diagnosed with "

    # Retrieving
    pid_to_lookup = 1002
    if pid_to_lookup in patient_records:
        print(f"Record for {pid_to_lookup}:", patient_records[pid_to_lookup])
    else:
        print(f"No record found for {pid_to_lookup}")

    # Checking keys
    print("All patient IDs:", patient_records.keys())


if __name__ == "__main__":
    demo_hash_map()
