class Aquarium:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)

            cls.instance.fish_data = {
                "goldfish": {
                    "Common Goldfish": {
                        "Fish ID": "GF001",
                        "Quantity": 20,
                        "Color": "Orange",
                        "Average Weight": "0.3 kg",
                        "Water Type": "Freshwater",
                        "Feeding Time": "9:00 AM",
                        "Tank Number": "T1",
                        "Origin": "China",
                        "Lifespan": "10 years",
                        "Diet": "Fish flakes"
                    },
                    "Comet Goldfish": {
                        "Fish ID": "GF002",
                        "Quantity": 15,
                        "Color": "Golden Orange",
                        "Average Weight": "0.25 kg",
                        "Water Type": "Freshwater",
                        "Feeding Time": "9:30 AM",
                        "Tank Number": "T1",
                        "Origin": "United States",
                        "Lifespan": "12 years",
                        "Diet": "Pellets"
                    }
                },

                "shark": {
                    "Great White Shark": {
                        "Fish ID": "SH001",
                        "Quantity": 2,
                        "Color": "Gray and White",
                        "Average Weight": "900 kg",
                        "Water Type": "Saltwater",
                        "Feeding Time": "1:00 PM",
                        "Tank Number": "T2",
                        "Origin": "Pacific Ocean",
                        "Lifespan": "30 years",
                        "Diet": "Fish and squid"
                    },
                    "Hammerhead Shark": {
                        "Fish ID": "SH002",
                        "Quantity": 1,
                        "Color": "Dark Gray",
                        "Average Weight": "230 kg",
                        "Water Type": "Saltwater",
                        "Feeding Time": "1:30 PM",
                        "Tank Number": "T2",
                        "Origin": "Atlantic Ocean",
                        "Lifespan": "25 years",
                        "Diet": "Small fish"
                    }
                },

                "angelfish": {
                    "Freshwater Angelfish": {
                        "Fish ID": "AF001",
                        "Quantity": 18,
                        "Color": "Silver and Black",
                        "Average Weight": "0.05 kg",
                        "Water Type": "Freshwater",
                        "Feeding Time": "10:00 AM",
                        "Tank Number": "T3",
                        "Origin": "Amazon River",
                        "Lifespan": "10 years",
                        "Diet": "Flakes and worms"
                    },
                    "Altum Angelfish": {
                        "Fish ID": "AF002",
                        "Quantity": 10,
                        "Color": "Silver",
                        "Average Weight": "0.06 kg",
                        "Water Type": "Freshwater",
                        "Feeding Time": "10:30 AM",
                        "Tank Number": "T3",
                        "Origin": "South America",
                        "Lifespan": "8 years",
                        "Diet": "Small insects"
                    }
                },

                "tuna": {
                    "Bluefin Tuna": {
                        "Fish ID": "TN001",
                        "Quantity": 7,
                        "Color": "Blue and Silver",
                        "Average Weight": "250 kg",
                        "Water Type": "Saltwater",
                        "Feeding Time": "2:00 PM",
                        "Tank Number": "T4",
                        "Origin": "Atlantic Ocean",
                        "Lifespan": "15 years",
                        "Diet": "Small fish"
                    },
                    "Yellowfin Tuna": {
                        "Fish ID": "TN002",
                        "Quantity": 12,
                        "Color": "Yellow and Silver",
                        "Average Weight": "180 kg",
                        "Water Type": "Saltwater",
                        "Feeding Time": "2:30 PM",
                        "Tank Number": "T4",
                        "Origin": "Indian Ocean",
                        "Lifespan": "7 years",
                        "Diet": "Squid and fish"
                    }
                },

                "salmon": {
                    "Atlantic Salmon": {
                        "Fish ID": "SM001",
                        "Quantity": 22,
                        "Color": "Silver",
                        "Average Weight": "5 kg",
                        "Water Type": "Freshwater and Saltwater",
                        "Feeding Time": "11:00 AM",
                        "Tank Number": "T5",
                        "Origin": "North Atlantic Ocean",
                        "Lifespan": "6 years",
                        "Diet": "Small fish and insects"
                    },
                    "Chinook Salmon": {
                        "Fish ID": "SM002",
                        "Quantity": 14,
                        "Color": "Blue Green and Silver",
                        "Average Weight": "13 kg",
                        "Water Type": "Freshwater and Saltwater",
                        "Feeding Time": "11:30 AM",
                        "Tank Number": "T5",
                        "Origin": "North Pacific Ocean",
                        "Lifespan": "7 years",
                        "Diet": "Plankton and small fish"
                    }
                }
            }

        return cls.instance

    def show_all_fish(self):
        print("\nAuckland Aquarium Fish List")
        print("----------------------------")

        for fish_type in self.fish_data:
            total = 0

            for species in self.fish_data[fish_type]:
                total += self.fish_data[fish_type][species]["Quantity"]

            print("\nFish Category:", fish_type.title())
            print("Total Fish:", total)

            for species in self.fish_data[fish_type]:
                print("\nSpecies:", species)

                for info in self.fish_data[fish_type][species]:
                    print(info + ":", self.fish_data[fish_type][species][info])

    def search_fish(self):
        fish_type = input("Enter fish category to search: ").lower()

        if fish_type in self.fish_data:
            print("\nFish found:", fish_type.title())

            for species in self.fish_data[fish_type]:
                print("\nSpecies:", species)

                for info in self.fish_data[fish_type][species]:
                    print(info + ":", self.fish_data[fish_type][species][info])
        else:
            print("Fish category not found.")

    def update_fish_quantity(self):
        fish_type = input("Enter fish category: ").lower()

        if fish_type in self.fish_data:
            species_name = input("Enter species name: ")

            found = False

            for species in self.fish_data[fish_type]:
                if species.lower() == species_name.lower():
                    try:
                        quantity = int(input("Enter new quantity: "))

                        if quantity < 0:
                            print("Quantity cannot be negative.")
                        else:
                            self.fish_data[fish_type][species]["Quantity"] = quantity
                            print("Quantity updated successfully.")

                    except ValueError:
                        print("Please enter a valid number.")

                    found = True

            if found == False:
                print("Species not found.")
        else:
            print("Fish category not found.")


def main():
    aquarium1 = Aquarium()
    aquarium2 = Aquarium()


    while True:
        print("\nAuckland Aquarium Management System")
        print("1. Display all fish")
        print("2. Search fish")
        print("3. Update fish quantity")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            aquarium1.show_all_fish()

        elif choice == "2":
            aquarium1.search_fish()

        elif choice == "3":
            aquarium1.update_fish_quantity()

        elif choice == "4":
            print("Program ended.")
            break

        else:
            print("Invalid choice. Try again.")


main()