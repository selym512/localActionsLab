import sys
import os
import snowflake.connector

def calculate_patient_risk(age, heart_rate):
    if heart_rate < 0:
        raise ValueError("Heart rate cannot be negative")
    risk_score = age + (heart_rate / 2)
    return risk_score

def save_to_db(score):
    # 1. Get credentials from Environment Variables (injected by Docker)
    user = os.getenv("SNOWFLAKE_USER")
    password = os.getenv("SNOWFLAKE_PASSWORD")
    account = os.getenv("SNOWFLAKE_ACCOUNT")
    target_db = os.getenv("SNOWFLAKE_DATABASE", "CICD_DEMO")
    
    # 2. Connect to Snowflake
    print("Connecting to Snowflake...")
    conn = snowflake.connector.connect(
        user=user,
        password=password,
        account=account,
        warehouse="COMPUTE_WH",
        database=target_db,
        schema="PUBLIC",
        role="SYSADMIN"
    )
    
    # 3. Insert Data
    cursor = conn.cursor()
    query = f"INSERT INTO {target_db}.PUBLIC.PATIENT_RISKS (PATIENT_ID, RISK_SCORE) VALUES (101, {score})"
    cursor.execute(query)
    print(f"SUCCESS: Saved Risk Score {score} to the Cloud!")
    conn.close()

if __name__ == "__main__":
    print("----------------------------------------")
    print("APP STARTING: Risk Calculator")
    
    # 1. Calculate
    final_score = calculate_patient_risk(50, 80)
    print(f"Calculated Score: {final_score}")
    
    # 2. Save (Only if we have the password)
    if os.getenv("SNOWFLAKE_PASSWORD"):
        save_to_db(final_score)
    else:
        print("SKIPPING DB SAVE: No credentials found (Running locally?)")
        
    print("----------------------------------------")
