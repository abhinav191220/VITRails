VITrails: Console-Based Railway Booking Simulation Documentation

1. Problem Statement

Modern railway travel is fragmented, requiring users to switch between multiple services for booking, tracking, and on-board services. The core need is a unified platform (VITrail) for secure ticket booking and real-time journey management.
This VITrails Console Simulation focuses specifically on modeling the complex ticket booking and 8-berth seat allotment mechanism to demonstrate the core logical flow required for successful reservation and ticket generation.

2. Scope of the Project (Console Simulation)

The scope is limited to a core-path ticket booking simulation within a console environment.
Included: Console UI, pre-defined routes/trains (BHOPAL, AMARAVATI, etc.), date validation (DDMMYYYY format), simulated random seat allocation (Lower, Middle, Upper, etc.), mock payment simulation, and structured ticket generation.
Excluded: Graphical UI, real-time database integration, dynamic pricing, actual seat inventory management, external API integration, real-time tracking, and on-board service modules.

3. Target Users

The project targets two distinct user groups:
For the full VITrail App:
General and Frequent Railway Travelers seeking a fast, unified, and modern travel management experience.

For the Console Simulation Script:
Developers and Engineers using it as a proof-of-concept for testing booking logic and data flow.
Students and Testers verifying the integrity of the Python code and the 8-berth remainder seat allotment logic.

4. High-Level Features
   
The simulation provides the following core functionalities:
Route Search: Allows users to input a Source and Destination city, validating against a pre-defined route list.
Date Validation: Enforces the DDMMYYYY format and ensures the booking is for the present day or a future date.
Train Selection: Enables the user to choose an available train from the filtered options.
Seat Allotment Simulation: Randomly assigns a Coach and Seat Number (1-72) and uses the modulo-8 remainder logic to determine the precise berth type (LB, MB, UB, SL, SU).

Mock Payment Gateway: Simulates a financial transaction with basic card/PIN validation and a processing delay.

Ticket Generation: Prints a finalized, structured confirmation ticket with all journey and allotment details.
