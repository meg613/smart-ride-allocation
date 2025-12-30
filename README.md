Smart Ride Allocation System (Python)
Overview

This project is a backend simulation of a ride-hailing platform similar to Uber. It focuses on intelligent driver allocation, dynamic pricing using surge multipliers, and ride lifecycle management including assignment, cancellation, and completion.

The goal of this project is to demonstrate problem-solving, system design, and backend logic using Python.

Key Concepts Used:
- Object-Oriented Programming (OOP)

- Greedy algorithm (nearest driver selection)

- Euclidean distance calculation

- Dynamic surge pricing

- State management (active rides & driver availability)

Features:

- Assigns the nearest available driver to a rider

- Calculates distance using Euclidean formula

- Applies surge pricing based on demand-supply ratio

- Supports ride cancellation and restores driver availability

- Handles ride completion and fare finalization

- Estimates ETA based on distance

Surge Pricing Logic

Surge pricing is calculated using the ratio of active ride requests to available drivers:

- Normal demand → 1.0x

- High demand → 1.5x

- Very high demand or no drivers → 2.0x

This simulates real-world dynamic pricing systems.
