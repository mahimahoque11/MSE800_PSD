# Air New Zealand Flight Management System
# Demonstrates Hybrid/Hierarchical Inheritance in Python

class Flight:
    """Parent class representing a general flight."""

    def __init__(self, flightNumber, origin, destination, departureTime, ticketPrice):
        self.flightNumber = flightNumber
        self.origin = origin
        self.destination = destination
        self.departureTime = departureTime
        self.ticketPrice = ticketPrice

    def displayFlightInfo(self):
        print("\n===== FLIGHT INFORMATION =====")
        print(f"Flight Number : {self.flightNumber}")
        print(f"Origin        : {self.origin}")
        print(f"Destination   : {self.destination}")
        print(f"Departure Time: {self.departureTime}")
        print(f"Ticket Price  : NZD ${self.ticketPrice:.2f}")

    def updateTicketPrice(self, newPrice):
        self.ticketPrice = newPrice
        print(f"\nTicket price updated to NZD ${self.ticketPrice:.2f}")

    def calculateFlightCost(self):
        return self.ticketPrice


class PassengerFlight(Flight):
    """Child class representing flights that carry passengers."""

    def __init__(self, flightNumber, origin, destination, departureTime, ticketPrice, passengerCapacity, airline):
        super().__init__(flightNumber, origin, destination, departureTime, ticketPrice)
        self.passengerCapacity = passengerCapacity
        self.airline = airline
        self.reservedSeats = 0  # Internal tracker for methods

    def displayAirline(self):
        print("\n===== AIRLINE INFORMATION =====")
        print(f"Airline            : {self.airline}")
        print(f"Passenger Capacity : {self.passengerCapacity}")

    def checkSeats(self):
        availableSeats = self.passengerCapacity - self.reservedSeats
        print(f"Available Seats    : {availableSeats}")
        return availableSeats

    def reserveSeat(self, passengerName):
        if self.reservedSeats < self.passengerCapacity:
            self.reservedSeats += 1
            print(f"Seat reserved for {passengerName}.")
        else:
            print("No seats available.")


class FreightFlight(Flight):
    """Child class representing cargo-only flights."""

    def __init__(self, flightNumber, origin, destination, departureTime, ticketPrice, cargoWeight, freightType):
        super().__init__(flightNumber, origin, destination, departureTime, ticketPrice)
        self.cargoWeight = cargoWeight
        self.freightType = freightType

    def displayFreightInfo(self):
        print("\n===== FREIGHT INFORMATION =====")
        print(f"Freight Type : {self.freightType}")
        print(f"Cargo Weight : {self.cargoWeight} kg")

    def calculateCargoFee(self):
        cargoFee = self.cargoWeight * 2.50
        print(f"Cargo Fee    : NZD ${cargoFee:.2f}")
        return cargoFee

    def loadCargo(self, description, weight):
        self.cargoWeight += weight
        print(f"Loaded Cargo : {description}")
        print(f"Updated Cargo Weight: {self.cargoWeight} kg")


class DomesticFlight(PassengerFlight):
    """Child class representing domestic passenger flights within NZ."""

    def __init__(self, flightNumber, origin, destination, departureTime, ticketPrice, passengerCapacity, airline):
        super().__init__(flightNumber, origin, destination, departureTime, ticketPrice, passengerCapacity, airline)
        
        # Internal defaults setting exactly matching diagram values
        self.visaRequired = False
        self.acceptedId = [
            "NZ Driver Licence",
            "Passport",
            "Birth Certificate",
            "Community Services Card",
            "Major Credit Card with Name",
            "Other NZ Acceptable Identification"
        ]

    def checkTravelRequirements(self):
        print("\n===== DOMESTIC TRAVEL REQUIREMENTS =====")
        print(f"Visa Required     : {'Yes' if self.visaRequired else 'No'}")

    def displayAcceptedId(self):
        print("\nAccepted Identification Documents:")
        for document in self.acceptedId:
            print(f"- {document}")

    def verifyPassangerId(self, passengerId):
        # Name matching exact diagram label typo for compatibility
        if passengerId in self.acceptedId:
            print(f"{passengerId} is accepted for domestic travel.")
            return True
        print(f"{passengerId} is not accepted for domestic travel.")
        return False


class InternationalFlight(PassengerFlight):
    """
    Child class representing international flights.
    Inherits DIRECTLY from PassengerFlight, NOT DomesticFlight.
    """

    def __init__(self, flightNumber, origin, destination, departureTime, ticketPrice, 
                 passengerCapacity, airline, countryOfArrival, visaRequired):
        
        # Bypasses DomesticFlight and talks to PassengerFlight directly
        super().__init__(flightNumber, origin, destination, departureTime, ticketPrice, passengerCapacity, airline)
        
        self.passportRequired = True
        self.countryOfArrival = countryOfArrival
        self.visaRequired = visaRequired

    def checkVisaStatus(self):
        print("\n===== INTERNATIONAL VISA STATUS =====")
        print(f"Country of Arrival : {self.countryOfArrival}")
        print(f"Visa Required      : {'Yes' if self.visaRequired else 'No'}")

    def displayCountryInfo(self):
        print("\n===== COUNTRY INFORMATION =====")
        print(f"Destination Country: {self.countryOfArrival}")

    def verifyPassport(self, passportNo):
        if passportNo:
            print(f"Passport {passportNo} verified successfully.")
            return True
        print("Passport verification failed.")
        return False


# ==========================================================
# Main Execution Execution
# ==========================================================
def main():
    # DomesticFlight (Omitted handling list declaration externally)
    domesticFlight = DomesticFlight(
        flightNumber="NZ421", origin="Auckland", destination="Wellington",
        departureTime="10:30 AM", ticketPrice=179.99, passengerCapacity=180, airline="Air New Zealand"
    )

    # InternationalFlight (Inherits from PassengerFlight directly)
    internationalFlight = InternationalFlight(
        flightNumber="NZ101", origin="Auckland", destination="Singapore",
        departureTime="11:45 PM", ticketPrice=899.99, passengerCapacity=300, 
        airline="Air New Zealand", countryOfArrival="Singapore", visaRequired=True
    )

    # FreightFlight
    freightFlight = FreightFlight(
        flightNumber="NZF500", origin="Auckland", destination="Christchurch",
        departureTime="2:00 AM", ticketPrice=1200.00, cargoWeight=500.0, freightType="Medical Supplies"
    )

    # Execution Validation
    domesticFlight.displayFlightInfo()
    domesticFlight.displayAirline()
    domesticFlight.checkTravelRequirements()
    domesticFlight.displayAcceptedId()
    domesticFlight.verifyPassangerId("Passport")

    internationalFlight.displayFlightInfo()
    internationalFlight.displayAirline()
    internationalFlight.checkVisaStatus()
    internationalFlight.displayCountryInfo()
    internationalFlight.verifyPassport("NZ1234567")

    freightFlight.displayFlightInfo()
    freightFlight.displayFreightInfo()
    freightFlight.calculateCargoFee()


if __name__ == "__main__":
    main()