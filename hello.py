from prefect import flow, task
from pydicom import dcmread


@task(log_prints=True)
def read_content(filepath: str):
    """Read the content of a DICOM file."""
    try:
        dicom_data = dcmread(filepath)
        return dicom_data
    except Exception as e:
        print(f"Error reading DICOM file: {e}")
        return {"error": str(e)}


@task(log_prints=True)
def information(patient_info: dict):
    """Print the patient information."""
    return patient_info.PatientName


@flow(name="DICOM Processing Flow")
def main_flow(filepath: str):
    """Main flow to process a DICOM file."""
    contents = read_content(filepath)
    patient_info = information(contents)
    return print(patient_info)
