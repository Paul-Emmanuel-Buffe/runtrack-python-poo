5-Day Object-Oriented Programming (OOP) Learning Project
This repository contains exercises from a 5-day journey to learn Object-Oriented Programming in Python. The project progresses from basic class definitions to a complete implementation of the Ship of Theseus philosophical thought experiment.
Project Overview
The Ship of Theseus is a thought experiment that raises the question of whether an object that has had all of its components replaced remains fundamentally the same object. Our final project implements this concept through Python classes, allowing users to replace ship parts and track the changes.
Day-by-Day Progress
Day 1: Introduction to Classes
Started with the very basics of OOP:

Creating a simple class with constructor
Class attributes and instance variables
Basic class instantiation

Example:
pythonCopyclass Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

# Direct instantiation printing
print(Operation(1, 3))
Day 2: Methods and Object Behavior
Advanced to implementing class methods:

Instance methods
String representation with __str__
Basic operations within classes

Day 3: Inheritance and Class Relationships
Explored inheritance concepts:

Parent and child classes
Method overriding
The super() function to call parent methods

Day 4: Encapsulation and Access Control
Learned about data protection:

Private and protected attributes
Getter and setter methods
Class vs instance attributes

Day 5: The Ship of Theseus Project
Applied all concepts in a comprehensive project:

Created the Part class to represent ship components
Developed the Ship class with part management functionality
Implemented a specialized RacingShip class
Added history tracking to monitor all changes
Built an interactive menu system for user interaction

Project Structure

Part class: Represents individual ship components with name and material properties
Ship class: Manages a collection of parts and tracks modification history
RacingShip class: Extends the Ship class with speed characteristics
Interactive menu: Allows users to modify the ship and view its state

Features

Ship Part Management:

Add new parts to the ship
Replace existing parts with new ones
Change the material of parts


History Tracking:

Records all modifications to the ship
Shows the complete history of changes


Interactive Interface:

Display the current state of the ship
Modify parts through a user-friendly menu
View specialized attributes like maximum speed



Usage
Run the main script to interact with the Ship of Theseus simulation:
bashCopypython ship_of_theseus.py
Follow the on-screen menu to:

View the current state of the ship
Replace parts
Modify materials
Display the modification history
View the ship's maximum speed

Learning Outcomes
This project demonstrates proficiency in:

Class definition and instantiation
Inheritance and polymorphism
Encapsulation and data protection
Object interaction and management
User interface design for object manipulation

Future Improvements
Potential enhancements for this project:

Graphical representation of the ship
Saving and loading ship configurations
Simulation of ship performance based on parts and materials
Multi-ship racing capabilities
