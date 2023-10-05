import PatientClass as pat
import ProcedureClass as pro

def main():
    # PATIENT OBJ
    patient1 = pat.Patient(1, "Matt Jones", "123 Main st, Waco TX 76706", "254-555-7415", 1)
    
    # PROCEDURE OBJ
    procedure1 = pro.Procedure("Physical Exam", "2/15/2022", "Dr. Irvine", 250, 1)
    procedure2 = pro.Procedure("MRI", "2/15/2022", "Dr. Hamilton", 1500, 1)
    procedure3 = pro.Procedure("CT Scan", "2/17/2022", "Dr. Drey", 1200, 2)
    
    # Initialize total charges
    total_original_charges = 0
    total_discounted_charges = 0
    
    # Print Patient information
    print(f"*** Patient Bill ***")
    print(f"Name: {patient1.get_patient_name()}")
    print(f"Address: {patient1.get_patient_address()}")
    print(f"Phone: {patient1.get_patient_number()}\n")

    # Loop through procedures and print patient information and charges
    for procedure in [procedure1, procedure2, procedure3]:
        if procedure.get_patientProc_id() == patient1.get_patient_id():
            print(f"Procedure: {procedure.get_procedure_name()}")
            print(f"Date: {procedure.get_procedure_date()}")
            print(f"Practitioner: {procedure.get_practitioner_name()}")
            charge = procedure.get_procedure_charges()

            # Check if the patient is a veteran and eligible for a discount
            if patient1.get_patient_id() == 1 and patient1.get_patient_veteran_status():
                discount = 0.4  # 40% discount for veterans
                discounted_charge = charge * (1 - discount)
                print(f"Original Charge: ${charge:.2f}")
                print(f"Charge (with 40% Veteran Discount): ${discounted_charge:.2f}\n")
                total_original_charges += charge
                total_discounted_charges += discounted_charge
            else:
                print(f"Charge: ${charge:.2f}\n")
                total_original_charges += charge
                total_discounted_charges += charge

    # Print total charges based on whether the patient is a veteran
    if patient1.get_patient_id() == 1 and patient1.get_patient_veteran_status():
        discount = 0.4
        total_charges_with_discount = total_discounted_charges
        print(f"Total Charges (with 40% Veteran Discount): ${total_charges_with_discount:.2f}")
    else:
        total_charges_without_discount = total_original_charges
        print(f"Total Charges: ${total_charges_without_discount:.2f}")

main()
