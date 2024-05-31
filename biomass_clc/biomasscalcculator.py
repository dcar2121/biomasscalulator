import math
from typing import Dict

# Constants
PLANKS_CONSTANT = 6.62607015e-34

# Function to calculate biomass
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

# Function to calculate total biomass
def calculate_total_biomass(biomass_components: Dict[str, float]) -> float:
    """
    Calculate the total biomass from the components.
    """
    total_biomass = sum(biomass_components.values())
    return total_biomass

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

# Run the program
if __name__ == "__main__":
    main()