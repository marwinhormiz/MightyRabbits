from firebase_manager import FirebaseManager

CREDENTIALS = "solar-team-development-firebase-adminsdk-ryi02-02010eb561.json"
REFERENCE = "https://solar-team-development-default-rtdb.europe-west1.firebasedatabase.app"
DATABASE_NAME = "data"

def main():
    manager = FirebaseManager(cred_path=CREDENTIALS, db_url=REFERENCE, db_name=DATABASE_NAME)
    # Skriv din kod här
    print(manager.get())

if __name__ == '__main__':
    main()
