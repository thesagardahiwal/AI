"""
Implement any one of the following Expert System
I. Information management
II. Hospitals and medical facilities
III. Help desks management
IV. Employee performance evaluation
V. Stock market trading
VI. Airline scheduling and cargo schedules
"""


def medical_expert_system():
    symptoms = input("Enter your symptoms (comma-separated): ").lower().split(',')

    rules = {
        "fever,cough,headache": "You might have the flu.",
        "fever,cough,breathlessness": "You might have COVID-19.",
        "headache,blurred vision": "You might have a migraine.",
        "chest pain,breathlessness": "You might have a heart problem."
    }

    found = False
    user_symptoms = set(map(str.strip, symptoms))

    for condition, diagnosis in rules.items():
        condition_set = set(condition.split(','))
        if condition_set.issubset(user_symptoms):
            print("Diagnosis:", diagnosis)
            found = True
            break

    if not found:
        print("Diagnosis: Symptoms unclear, please consult a doctor.")

# Run the expert system
medical_expert_system()
