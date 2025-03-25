def main():
    # Initialize the dictionary with 10 countries and their capitals
    country_capitals = {
        "Nigeria": "Abuja",
        "Ghana": "Accra",
        "Kenya": "Nairobi",
        "South Africa": "Cape Town",
        "Egypt": "Cairo",
        "France": "Paris",
        "Germany": "Berlin",
        "Senegal": "Dakar",
        "United Kingdom": "London",
        "Canada": "Ottawa"
    }

    while True:
        # Prompt the user to enter a country name
        country = input("Enter a country name: ").strip().title()

        # Look up the capital city
        if country in country_capitals:
            print(f"The capital of {country} is {country_capitals[country]}.")
        else:
            print("Sorry, the country you are looking for is not in the directory.")

        # Ask the user if they want to continue
        choice = input("Do you want to look up another country? (yes/no): ").strip().lower()
        if choice != "yes":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()