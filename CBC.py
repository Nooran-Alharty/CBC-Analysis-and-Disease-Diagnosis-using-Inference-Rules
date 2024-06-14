def analyze_cbc(rbc, wbc, hemoglobin, platelets):
    average_intervals = {
        'rbc': (4.2, 5.8),
        'wbc': (4000, 11000),
        'hemoglobin': (13, 17),
        'platelets': (150000, 450000)
    }

    result = ""

    if rbc < average_intervals['rbc'][0]:
        result += "p: rbc count is lower than average\n"
    elif rbc > average_intervals['rbc'][1]:
        result += "p: rbc count is higher than average\n"

    if wbc < average_intervals['wbc'][0]:
        result += "r: wbc count is lower than average\n"
    elif wbc > average_intervals['wbc'][1]:
        result += "r: wbc count is higher than average\n"

    if hemoglobin < average_intervals['hemoglobin'][0]:
        result += "s: hemoglobin levels are lower than average\n"
    elif hemoglobin > average_intervals['hemoglobin'][1]:
        result += "s: hemoglobin levels are higher than average\n"

    if platelets < average_intervals['platelets'][0]:
        result += "t: platelet count is lower than average\n"
    elif platelets > average_intervals['platelets'][1]:
        result += "t: platelet count is higher than average\n"

    return result.strip()

def disease_diagnosis_modus_pones(rbc, wbc, hemoglobin, platelets):
    cbc_analysis = analyze_cbc(rbc, wbc, hemoglobin, platelets)
    print(cbc_analysis)

    if "p: rbc count is lower than average" in cbc_analysis and \
       "r: wbc count is higher than average" in cbc_analysis and \
       "t: platelet count is lower than average" in cbc_analysis:
        print("\nq: The patient might have Thrombocytopenia, please consult with a doctor")
        print("(p ∧ r ∧ t) -> q")
        print("p ∧ r ∧ t ")
        print("--------------------")
        print("q")

def disease_diagnosis_modus_tollens(rbc, wbc, hemoglobin, platelets):
    cbc_analysis = analyze_cbc(rbc, wbc, hemoglobin, platelets)

    if not "r: wbc count is higher than average" in cbc_analysis:
        print("\ni: patient is sick")
        print("v: wbc count is higher than average")
        print("since r, then ¬v ")
        print("i -> v")
        print("¬v")
        print("--------------------")
        print("¬i")






rbc = float(input("Enter RBC count: "))
wbc = float(input("Enter WBC count: "))
hemoglobin = float(input("Enter hemoglobin level: "))
platelets = float(input("Enter platelet count: "))

disease_diagnosis_modus_pones(rbc, wbc, hemoglobin, platelets)
disease_diagnosis_modus_tollens(rbc, wbc, hemoglobin, platelets)
