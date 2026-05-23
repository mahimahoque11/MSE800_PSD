# Auckland Aquarium Management System

## Project Overview

The Auckland Aquarium Management System is a Python-based application developed to manage fish information in an aquarium located in Auckland, New Zealand.

The system stores and manages different categories of fish along with multiple species and detailed information about each species. Users can display all fish records, search fish categories, and update fish quantities through a menu-driven interface.

This project demonstrates the implementation of the Singleton Design Pattern in Python.


# Fish Categories Included

The system contains the following fish categories:

1. Goldfish
2. Shark
3. Angelfish
4. Tuna
5. Salmon

Each category contains multiple species with detailed aquarium information.


# Features

The system allows users to:

- Display all fish categories and species
- Search fish categories
- View fish details
- Update fish quantity
- Store aquarium data in a centralized system
- Demonstrate Singleton Design Pattern implementation


# Fish Details Stored

Each fish species contains the following information:

- Fish ID
- Quantity
- Color
- Average Weight
- Water Type
- Feeding Time
- Tank Number
- Origin
- Lifespan
- Diet


# Design Pattern Used

## Singleton Design Pattern

The Singleton Design Pattern ensures that only one instance of the Aquarium class exists throughout the program.

This is useful because:
- The aquarium should have only one centralized management system
- All fish data should remain consistent across the application
- Multiple objects should not create separate aquarium databases

### Singleton Verification

The program creates two aquarium objects:

aquarium1 = Aquarium()
aquarium2 = Aquarium()