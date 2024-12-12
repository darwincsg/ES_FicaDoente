class Exam:
    def __init__(self, exam_id, exam_type, results):
        self.exam_id = exam_id
        self.exam_type = exam_type  # e.g., Blood Test, MRI
        self.results = results  # Could be a string or a file link

    def download_results(self):
        return f"Downloading results for {self.exam_type}: {self.results}"

    def mail_to_patient(self, patient_email):
        return f"Results emailed to {patient_email}"


