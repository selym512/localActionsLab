import sys
import os
import snowflake.connector

def get_connector():
    # Connects using standard env vars, but purely for Admin tasks
    return snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse="COMPUTE_WH",
        role="SYSADMIN" # We need extra rights to Clone/Drop
    )

def create_clone(clone_name, source_db):
    print(f"OPS: Attempting to clone {source_db} to {clone_name}...")
    conn = get_connector()
    conn.cursor().execute(f'CREATE OR REPLACE DATABASE "{clone_name}" CLONE "{source_db}"')
    print(f"OPS: Success! Zero-Copy Clone created: {clone_name}")
    conn.close()

def drop_clone(clone_name):
    print(f"OPS: Teardown initiated for {clone_name}...")
    conn = get_connector()
    conn.cursor().execute(f'DROP DATABASE IF EXISTS "{clone_name}"')
    print(f"OPS: Success! Database dropped.")
    conn.close()

if __name__ == "__main__":
    # Usage: python ops_db_manager.py [create|drop] [DB_NAME]
    if len(sys.argv) < 3:
        print("Error: Missing arguments. Usage: python ops_db_manager.py [create|drop] [DB_NAME]")
        sys.exit(1)

    action = sys.argv[1]
    db_name = sys.argv[2]

    if action == "create":
        # We clone FROM 'CICD_DEMO' (Your Prod DB) TO the new name
        create_clone(db_name, "CICD_DEMO") 
    elif action == "drop":
        drop_clone(db_name)
    else:
        print(f"Error: Unknown action '{action}'")
