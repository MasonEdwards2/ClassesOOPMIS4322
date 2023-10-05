class Patient:
    def __init__(self, id, name, address, phoneNum, vetstats):
        self.__id = id
        self.__name = name
        self.__address = address
        self.__phoneNum = phoneNum
        self.__vetstats = vetstats

    def get_patient_id(self):
        return self.__id 

    def get_patient_name(self):
        return self.__name
    
    def get_patient_address(self):
        return self.__address
    
    def get_patient_number(self):
        return self.__phoneNum

    def patient_veteran_status(self):
        self.vetstats = self.__vetstats == 1

    def get_patient_veteran_status(self):
        return self.__vetstats
