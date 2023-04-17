from firebase_manager import FirebaseManager

CREDENTIALS = ""
REFERENCE = ""
DATABASE_NAME = ""

def main():
    manager = FirebaseManager(cred_path=CREDENTIALS, db_url=REFERENCE, db_name=DATABASE_NAME)
    # Skriv din kod här
    # Använd manager.push(data) för att lägga in ny data i din databas
    # Använd manager.get()
    data = 5
    manager.push(data)

    get_data = manager.get()
    print(get_data)

if __name__ == '__main__':
    main()
