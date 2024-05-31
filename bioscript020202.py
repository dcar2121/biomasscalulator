import math
from typing import Dict

# Constants
PLANKS_CONSTANT = 6.62607015e-34
DECADANCE_CONSTANT = 1.0  # replace with actual value

# Function to calculate biomass_planks_constant_output
def calculate_biomass(planks_constant: float) -> float:
    """
    Calculate the biomass using Plank's constant.
    """
    biomass = planks_constant * 42
    return biomass

# Function to calculate energy output
def calculate_energy_output(biomass: float) -> float:
    """
    Calculate the energy output from biomass.
    """
    energy_output = biomass * 1.25
    return energy_output

# Function to collect biomass components from user
def collect_biomass_components() -> Dict[str, float]:
    """
    Collect the type and weight of biological materials from the user.
    """
    biomass_components = {}

    while True:
        material = input("Enter the type of biological material (or 'done' to finish): ")
        if material.lower() == "done":
            break

        weight = float(input(f"Enter the weight of the {material} in kilograms: "))
        biomass_components[material] = weight

    return biomass_components
# Function to collect biomass components from user
def collect_biomass_components() -> Dict[str, float]:
    """
    Collect the type and weight of biological materials from the user.
    """
    biomass_components = {}

    while True:
        material = input("Enter the type of biological material (or 'done' or 'finish' to finish): ")
        if material.lower() in ["done", "finish"]:
            break

        while True:
            try:
                weight = float(input(f"Enter the weight of the {material} in kilograms: "))
                biomass_components[material] = weight
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

    return biomass_components

# Function to calculate total biomass
def calculate_total_biomass(biomass_components: Dict[str, float]) -> float:
    """
    Calculate the total biomass from the components.
    """
    return sum(biomass_components.values())

# Function to calculate decadance
def calculate_decadance(biomass: float) -> float:
    """
    Calculate the decadance from biomass.
    """
    decadance = biomass * PLANKS_CONSTANT
    return decadance

# Main function to run the program
def main():
    """
    Main function to run the program.
    """
    # Calculate biomass
    biomass = calculate_biomass(PLANKS_CONSTANT)
    print(f"Calculated biomass: {biomass}")

    # Calculate energy output
    energy_output = calculate_energy_output(biomass)
    print(f"Energy output from biomass: {energy_output}")

    # Collect biomass components from user
    biomass_components = collect_biomass_components()

    # Calculate total biomass
    total_biomass = calculate_total_biomass(biomass_components)
    print(f"The total biomass is {total_biomass} kilograms.")

    # Calculate decadance
    decadance = calculate_decadance(total_biomass)
    print(f"The decadance is {decadance}.")
# Function to calculate total biomass
def calculate_total_biomass(biomass_components: Dict[str, float]) -> float:
    """
    Calculate the total biomass from the components.
    """
    return sum(biomass_components.values())

# Function to calculate decadance
def calculate_decadance(biomass: float) -> float:
    """
    Calculate the decadance from biomass.
    """
    decadance = biomass * PLANKS_CONSTANT
    return decadance

# Function to calculate total energy output
def calculate_total_energy_output(biomass_components: Dict[str, float]) -> float:
    """
    Calculate the total energy output from the biomass components.
    """
    total_biomass = calculate_total_biomass(biomass_components)
    target_biomass = calculate_biomass(PLANKS_CONSTANT) # Use Plank's constant
    biocalc_biomass = sum(biomass_components.values())  # Use the sum of the components
    decadance = calculate_decadance(total_biomass)      # Use the total biomass
    energy_output = calculate_energy_output(target_biomass) + calculate_energy_output(biocalc_biomass) + calculate_energy_output(decadance)
    return energy_output    

# Run the program
if __name__ == "__main__":
    main()
