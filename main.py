from firebase_manager import FirebaseManager

CREDENTIALS = ""
REFERENCE = ""
DATABASE_NAME = ""

def main():
    manager = FirebaseManager(cred_path=CREDENTIALS, db_url=REFERENCE, db_name=DATABASE_NAME)
    # Skriv din kod här
    print(manager.get())

if __name__ == '__main__':
    main()
