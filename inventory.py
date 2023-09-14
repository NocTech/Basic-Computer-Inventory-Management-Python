import pandas as pd
import os

# Check if the inventory file exists, and create it if it doesn't.
inventory_file = "computer_inventory.csv"
if not os.path.exists(inventory_file):
    # Create a new empty inventory file with columns.
    df = pd.DataFrame(
        columns=["Computer Name", "Serial Number", "CPU", "RAM", "Storage"]
    )
    df.to_csv(inventory_file, index=False)


def add_computer(computer_name, serial_number, cpu, ram, storage, os):
    # Read the existing inventory data.
    df = pd.read_csv(inventory_file)

    # Create a new DataFrame for the computer to be added.
    new_computer = pd.DataFrame(
        {
            "Computer Name": [computer_name],
            "Serial Number": [serial_number],
            "CPU": [cpu],
            "RAM": [ram],
            "Storage": [storage],
            "Os": [os],
        }
    )

    # Concatenate the existing DataFrame with the new computer data.
    df = pd.concat([df, new_computer], ignore_index=True)

    # Save the updated DataFrame back to the inventory file.
    df.to_csv(inventory_file, index=False)
    print(f"Computer '{computer_name}' added to inventory.")


def display_inventory():
    # Read and display the current inventory data.
    df = pd.read_csv(inventory_file)
    if not df.empty:
        print("\nCurrent Computer Inventory:\n")
        print(df)
    else:
        print("\nThe inventory is empty.\n")


def main():
    while True:
        print("\nComputer Inventory Management")
        print("1. Add Computer (Auto)")
        print("2. Display Inventory")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            computer_name = input("Enter computer name: ")
            serial_number = input("Enter serial number: ")
            cpu = input("Enter CPU model: ")
            ram = input("Enter RAM size (GB): ")
            storage = input("Enter storage size (GB): ")
            os = input("Enter os name (Linux, Windows or something): ")
            add_computer(computer_name, serial_number, cpu, ram, storage, os)
        elif choice == "2":
            display_inventory()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
