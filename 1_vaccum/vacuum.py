class VacuumWorld:
    def __init__(self):
        # Initialize lookup table, locations, current location, and dirty locations cleaned counter
        self.lookup_table = {
            ("A", 0): ("Location A has dirt. A is clean now. Move to location B.", 'B'),
            ("A", 1): ("Location A is clean. Move to location B.", 'B'),
            ("B", 0): ("Location B has dirt. B is clean now. Move to location A.", 'A'),
            ("B", 1): ("Location B is clean. Move to location A.", 'A')
        }
        self.locations = {}
        self.current_location = None
        self.dirty_locations_cleaned = 0  # Counter for dirty locations cleaned

    def set_initial_state(self):
        """
        Set the initial state of each location (A and B) and the initial location of the vacuum.
        """
        locations = ['A', 'B']
        
        for loc in locations:
            while True:
                state = input(f"Is location {loc} dirty or clean? (enter 'dirty' or 'clean'): ").strip().lower()
                if state in ['dirty', 'clean']:
                    self.locations[loc] = state.capitalize()  # Store the state with proper capitalization
                    break
                else:
                    print("Invalid input. Please enter 'dirty' or 'clean'.")

        while True:
            self.current_location = input("Enter the initial location (A or B): ").strip().upper()
            if self.current_location in ['A', 'B']:
                break
            else:
                print("Invalid location. Please enter 'A' or 'B'.")

    def display(self):
        """
        Display the current location and the state of all locations, but only show dirty locations.
        """
        print(f"Current Location: {self.current_location}")
        for loc, state in self.locations.items():
            if state == 'Dirty':  # Only display if location is dirty
                print(f"Location {loc}: {state}")
            elif loc == self.current_location and state == 'Clean':
                # Optionally print the current location if it's clean
                print(f"Location {loc}: Clean (Current Location)")

    def clean_current_location(self):
        # Clean the current location if it is dirty
        if self.locations[self.current_location] == 'Dirty':
            print(f"Cleaning location {self.current_location}.")
            self.locations[self.current_location] = 'Clean'
            self.dirty_locations_cleaned += 1  # Increment dirty locations cleaned counter
        else:
            print(f"Location {self.current_location} is already clean.")

    def decide_action(self):
        # Determine the state of the current location and decide the next action
        state = 0 if self.locations[self.current_location] == 'Dirty' else 1
        action, next_location = self.lookup_table[(self.current_location, state)]
        print(action)
        return next_location

    def move(self, new_location):
        # Move to a new location if it is valid
        if new_location in self.locations:
            print(f"Moving to location {new_location}.")
            self.current_location = new_location
        else:
            print(f"Invalid location: {new_location}")

    def perform_action(self):
        # Perform the cleaning, decide the next action, and move to the next location
        self.clean_current_location()
        next_location = self.decide_action()
        self.move(next_location)

    def all_clean(self):
        # Check if all locations are clean
        return all(state == 'Clean' for state in self.locations.values())

if __name__ == "__main__":
    total_dirty_locations_cleaned = 0  # Initialize total dirty locations cleaned counter across all simulations
    
    while True:
        vacuum_world = VacuumWorld()
        vacuum_world.set_initial_state()
        vacuum_world.display()
        
        # Reset dirty locations cleaned for the new simulation
        vacuum_world.dirty_locations_cleaned = 0
        
        # Continue performing actions until all locations are clean
        while not vacuum_world.all_clean():
            vacuum_world.perform_action()
            vacuum_world.display()
        
        # Update total dirty locations cleaned counter
        total_dirty_locations_cleaned += vacuum_world.dirty_locations_cleaned
        
        print(f"in this round {vacuum_world.dirty_locations_cleaned}   dirty locations cleaned!")
        print(f"Total performance measure: {total_dirty_locations_cleaned}")
        
        # Prompt user to continue or exit
        while True:
            restart = input("Would you like to run and clean? (yes/no): ").strip().lower()
            if restart in ['yes', 'no']:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        
        if restart != 'yes':
            print(f"Exiting the program. Total dirty locations cleaned across all simulations: {total_dirty_locations_cleaned}")
            break

