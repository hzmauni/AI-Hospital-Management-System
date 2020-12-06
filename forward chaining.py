# headache, fever, runny nose ====> flu
# sneezing, runny nose ====> common cold

global facts
global is_changed
global diagnosed
is_changed = True
facts = [["Rahim","headache"],["Karim","headache"],["Hasib","headache"],
         ["Karim","fever"],["Hasib","fever"],["Hasib","sneezing"],
         ["Rahim","sneezing"],["Karim","runny nose"],["Rahim","runny nose"]]
diagnosed = [["Mauni", "flu"]]

def assert_diagnosis(diagnose):
    global diagnosed
    global is_changed
    if not diagnose in diagnosed:
        diagnosed += [diagnose]
        is_changed = True
        print("\nDiagnosis added :\n" , diagnose)

def assert_fact(fact):
    global facts
    if not fact in facts:
        facts += [fact]
        print("\nPatient and symptom added :\n" , fact)

def view():
    print("\n------Hospital Knowledgebase:------")
    print("\nAll patients and their symptoms:\n", facts)
    print("\nAll diagnosed patients:\n", diagnosed)

def diagnose():
    global is_changed
    print("\n\n------Diagnosis Activities:------\n")
    while is_changed:
        is_changed = False
        for A1 in facts:
            if A1[1] == "runny nose" and [A1[0], "sneezing"] in facts:
                assert_diagnosis([A1[0],"common cold"])
            if A1[1] == "runny nose" and [A1[0], "fever"] in facts and [A1[0], "headache"] in facts:
                assert_diagnosis([A1[0],"flu"])   

def input_p():
    input_name = input("Enter the patient's name: ")
    input_symptom_no = input("Enter the number of symptoms: ")
    i=0
    while(i<(int(input_symptom_no))):
        input_symptom = input("Enter their symptom: ")
        if input_symptom == "fever" or input_symptom == "runny nose" or input_symptom == "sneezing" or input_symptom == "headache":
            assert_fact([input_name,input_symptom])
            i=i+1
        else:
            print("Wrong symptom - enter fever or runny nose or sneezing or headache")
            
                      

exit = True
while exit:
    print("\n-----WELCOME TO THE HOSPITAL DIAGNOSIS SYSTEM-----\n")
    print("\n\t1.\tView Hospital Knowledgebase.")
    print("\t2.\tAdmit patient.")
    print("\t3.\tDiagnose patients.")
    print("\t4.\tExit.")
    print("\t5.\tSave Hospital Knowledgebase.")
    input_choice = input("\nEnter choice: ")
    if input_choice == '1':
        view()
    if input_choice == '2':
        input_p()
    if input_choice == '3':
        diagnose()
    if input_choice == '4':
        exit = False
    if input_choice == '5':
        with open('Hospital.txt', 'w') as f:
            f.write("Diagnoses:\n")
            for item in diagnosed:
                f.write("%s\n" % item)
            f.write("\nPatients and symptoms:\n")
            for item in facts:
                f.write("%s\n" % item)
    
    
            
