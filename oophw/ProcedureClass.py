class Procedure:
    def __init__(self, name, date, practitioner, charges, patient_id):
        self.__name = name
        self.__date = date
        self.__practitioner = practitioner
        self.__charges = charges
        self.__patient_id = patient_id

    def get_procedure_name(self):
        return self.__name

    def get_procedure_date(self):
        return self.__date

    def get_practitioner_name(self):
        return self.__practitioner

    def get_procedure_charges(self):
        return self.__charges

    def get_patientProc_id(self):
        return self.__patient_id