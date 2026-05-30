# Air New Zealand Domestic Flight System
# Demonstrates Single Inheritance in Python
# Parent Class: Flight
# Child Class: DomesticFlight 


class Flight:
    """
    Parent class representing a general flight.
    Shared attributes and methods are inherited
    by the DomesticFlight class.
    """

    def __init__(self, flightNumber, origin, destination,
                 departureTime, ticketPrice):

        # Shared / inherited attributes
        self.flightNumber = flightNumber
        self.origin = origin
        self.destination = destination
        self.departureTime = departureTime
        self.ticketPrice = ticketPrice

    def displayFlightInfo(self):
        """Displays general flight information."""

        print("\n===== FLIGHT INFORMATION =====")
        print(f"Flight Number : {self.flightNumber}")
        print(f"Origin        : {self.origin}")
        print(f"Destination   : {self.destination}")
        print(f"Departure Time: {self.departureTime}")
        print(f"Ticket Price  : NZD ${self.ticketPrice:.2f}")
        print("(Ticket prices vary from flight to flight)")

    def updateTicketPrice(self, newPrice):
        """Updates the ticket price."""

        self.ticketPrice = newPrice
        print(f"\nTicket price updated to NZD ${self.ticketPrice:.2f}")


class DomesticFlight(Flight):
    """
    Child class representing an Air New Zealand domestic flight.

    Inherits:
    - flightNumber
    - origin
    - destination
    - departureTime
    - ticketPrice

    Inherits Methods:
    - displayFlightInfo()
    - updateTicketPrice()
    """

    def __init__(self, flightNumber, origin, destination,
                 departureTime, ticketPrice, aircraftType):

        # Call parent constructor
        super().__init__(
            flightNumber,
            origin,
            destination,
            departureTime,
            ticketPrice
        )

        # DomesticFlight-specific attributes
        self.airline = "Air New Zealand"
        self.aircraftType = aircraftType
        self.visaRequired = False

        self.acceptedId = [
            "NZ Driver Licence",
            "Passport",
            "Birth Certificate",
            "Community Services Card",
            "Major Credit Card with Name",
            "Other NZ Acceptable Identification"
        ]

    def displayAirlineDetails(self):
        """Displays airline-specific information."""

        print("\n===== AIRLINE DETAILS =====")
        print(f"Airline       : {self.airline}")
        print(f"Aircraft Type : {self.aircraftType}")

    def checkTravelRequirements(self):
        """Displays domestic flight travel requirements."""

        print("\n===== TRAVEL REQUIREMENTS =====")

        visa_status = "Yes" if self.visaRequired else "No"

        print(f"Visa Required : {visa_status}")
        print("Passport Required : No")
        print("Note: Passport is accepted as valid identification.")

        print("\nAccepted Identification Documents:")

        for document in self.acceptedId:
            print(f"- {document}")


def main():
    """
    Main function demonstrating inheritance.
    """

    # Create DomesticFlight object
    flight1 = DomesticFlight(
        flightNumber="NZ421",
        origin="Auckland",
        destination="Wellington",
        departureTime="10:30 AM",
        ticketPrice=149.99,
        aircraftType="Airbus A320"
    )

    # Inherited method from Flight
    flight1.displayFlightInfo()

    # Inherited method from Flight
    flight1.updateTicketPrice(179.99)

    # Inherited method from Flight
    flight1.displayFlightInfo()

    # DomesticFlight-specific methods
    flight1.displayAirlineDetails()
    flight1.checkTravelRequirements()


# Program Entry Point
if __name__ == "__main__":
    main()
