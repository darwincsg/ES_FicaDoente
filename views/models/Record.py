class Record:
    def __init__(self, record_id, exam, vital_signs, symptoms, diagnosis, plan):
        self.record_id = record_id
        self.exam = exam  # Instance of Exam class
        self.vital_signs = vital_signs
        self.symptoms = symptoms
        self.diagnosis = diagnosis
        self.plan = plan

    def edit_record(self, vital_signs=None, symptoms=None, diagnosis=None, plan=None):
        if vital_signs:
            self.vital_signs = vital_signs
        if symptoms:
            self.symptoms = symptoms
        if diagnosis:
            self.diagnosis = diagnosis
        if plan:
            self.plan = plan
        return "Record updated successfully"
