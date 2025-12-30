import sys

def calculate_patient_risk(age, heart_rate):
    # Simple logic: Risk = Age + (Heart Rate / 2)
    if heart_rate < 0:
        raise ValueError("Heart rate cannot be negative")
    
    # RISK CALCULATOR LOGIC
    risk_score = age + (heart_rate / 2)
    return risk_score

if __name__ == "__main__":
    # This block prevents the code below from running when we import the file for testing
    print("----------------------------------------")
    print("APP STARTING: Risk Calculator")
    score = calculate_patient_risk(50, 80)
    print(f"Test Patient Score: {score}")
    print("----------------------------------------")
