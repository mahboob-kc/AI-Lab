def extract_statements(statement):
    """Extracts P and Q from the statement of the form 'if P then Q'."""
    if "if" in statement and "then" in statement:
        parts = statement.split("then")
        if len(parts) == 2:
            P = parts[0].replace("if", "").strip()
            Q = parts[1].strip()
            return P, Q
    return None, None

def modus_ponens(implication, premise):
    """Applies the Modus Ponens rule to deduce a conclusion."""
    P, Q = implication
    if premise.strip() == P:
        return Q
    else:
        return None

def resolve(clause1, clause2):
    """Resolve two clauses and return the result."""
    for literal in clause1:
        if -literal in clause2:
            # Resolve the two clauses
            new_clause = list(set(clause1 + clause2) - {literal, -literal})
            return new_clause if new_clause else None
    return None

def modus_ponens_menu():
    """Handles the Modus Ponens logic."""
    implication_statement = input("Enter the implication (e.g., 'if P then Q'): ")
    premise_statement = input("Enter the premise (e.g., 'P'): ")

    # Extract P and Q from the implication statement
    implication = extract_statements(implication_statement)
    
    if implication[0] is None or implication[1] is None:
        print("Invalid implication format. Please use 'if P then Q'.")
        return

    # Apply Modus Ponens
    conclusion = modus_ponens(implication, premise_statement)

    if conclusion:
        print(f"Using Modus Ponens, we conclude: {conclusion} is true.")
    else:
        print("Cannot be inferred using Modus Ponens.")

def resolve_menu():
    """Handles the resolution of clauses."""
    clauses = []
   
    print("Enter clauses (e.g., '1 -2' for [1, -2]). Type 'done' when finished:")
    while True:
        input_clause = input("Clause: ")
        if input_clause.lower() == 'done':
            break
        try:
            clause = list(map(int, input_clause.split()))
            clauses.append(clause)
        except ValueError:
            print("Invalid input. Please enter integers separated by spaces.")
   
    print(f"Current clauses: {clauses}")
   
    while True:
        new_clauses = []
        resolved_this_round = set()  # Track resolved pairs to avoid resolving the same pair multiple times

        # Attempt to resolve each pair of clauses
        for i in range(len(clauses)):
            if i in resolved_this_round:
                continue  # Skip already resolved clauses
            for j in range(i + 1, len(clauses)):
                resolved = resolve(clauses[i], clauses[j])
                if resolved is not None:
                    print(f"Resolving {clauses[i]} and {clauses[j]} gives {resolved}")
                    new_clauses.append(resolved)
                    resolved_this_round.add(i)  # Mark clauses as resolved
                    resolved_this_round.add(j)
                    break  # Break after resolving with one clause
                else:
                    print(f"Resolving {clauses[i]} and {clauses[j]} gives None")

        # If no resolutions were made this round, break
        if not new_clauses:
            break

        # Remove duplicates and update clauses
        clauses = [list(clause) for clause in set(tuple(sorted(clause)) for clause in new_clauses)]
        print(f"Current clauses: {clauses}")
   
    print(f"Final simplified clauses that cannot be further resolved: {clauses}")

def main():
    while True:
        print("\nMenu:")
        print("1. Modus Ponens")
        print("2. Resolution")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == '1':
            modus_ponens_menu()
        elif choice == '2':
            resolve_menu()
        elif choice == '3':
            print("Exiting the program.")
            break
            
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
