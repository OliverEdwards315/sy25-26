print("/n---Py-Fest 2026 stage Manager ---")
print("1. View Lineup & total time")
print("2. Add a new band")
print("3. Move first Band to End (late arival)")
print("4. Remove a band by name")
print("5. Move band by name to specific position")
print("6. Exit")


lineup = [
    {"name": "band name", "duration": 10},
    {"name": "band name", "duration": 10},
    {"name": "band name", "duration": 10},
    {"name": "band name", "duration": 10},
    ]


while True:
    
    choice = input("enter your choice (1-6): ")
    

    if choice == "1":
        print("\n--- Current Lineup ---")
        print(lineup)



    elif choice == "2":
        new_band = input("Enter the name of the new band: ")
        print(f"{new_band} has been added to the lineup.")

    elif choice == "3":
        band_name = int(input("Enter the name of the band to move from front to end: "))
        print(f"{band_name} has been moved to the end of the lineup.")
