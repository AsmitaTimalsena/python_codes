print("-----------------NEPAL UTILITY SYSTEM-----------------")

while True:
    print("Menu:")
    print("1. BMI Calculator")
    print("2. Taxation System")
    print("3. Currency Converter")
    print("4. Remittance System")
    print("5. Lagani Kosh")
    print("6. Exit")
    user_choice = input("Select an option(1-6):").strip()

    if user_choice == "1":
        print("You selected BMI Calculator")
        print("https://github.com/bidhyabhattarai/BMI_calculator")

    elif user_choice == "2":
        print("You selected Taxation System")
        print("https://github.com/Anujakhatri/Taxation-system-nepal")
    elif user_choice == "3":
        print("You selected Currency Converter")
        print("https://github.com/sneharitas/currency_converter")

    elif user_choice == "4":
        print("You selected Remittance System")
        print("https://github.com/kopiladevkota/nepal_lagani_kosh")

    elif user_choice == "5":
        print("You selected Lagani Kosh")
        print("https://github.com/binisha77/nepal_remittance_calculator")

    elif user_choice == "6":
        print("You selected Exit")
        print("Exiting the program.........")
        break


    else:
        print("Invalid option. Please select a valid option from the menu.\n Please try again.")
        continue



        




