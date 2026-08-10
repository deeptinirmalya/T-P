data_records = {
    "1001": {"access_code": "1234", "credits": 5000},
    "1002": {"access_code": "5678", "credits": 3000}
}

def verify_session():
    user_ref = input("Enter UID: ")
    pass_key = input("Enter Key: ")
    
    if user_ref in data_records and data_records[user_ref]["access_code"] == pass_key:
        print("Access Granted")
        return user_ref
    else:
        print("Auth Failed")
        return None

def view_statement(uid):
    print("Available Credits: ", data_records[uid]["credits"])

def credit_funds(uid):
    val = float(input("Value to add: "))
    data_records[uid]["credits"] += val
    print("Transaction Completed")

def debit_funds(uid):
    val = float(input("Value to remove: "))
    if val <= data_records[uid]["credits"]:
        data_records[uid]["credits"] -= val
        print("Funds Dispatched")
    else:
        print("Limit Exceeded")

def control_panel(uid):
    while True:
        print("\n[A] Statement [B] Credit [C] Debit [D] Terminate")
        cmd = input("Command: ").upper()
        
        if cmd == "A":
            view_statement(uid)
        elif cmd == "B":
            credit_funds(uid)
        elif cmd == "C":
            debit_funds(uid)
        elif cmd == "D":
            print("Session Ended")
            break
        else:
            print("Unknown Command")

active_id = verify_session()
if active_id:
    control_panel(active_id)   