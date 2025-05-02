import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Read the data file
file_path = "data.csv"
df = pd.read_csv(file_path, encoding="unicode_escape")

def program():
    while True:
        print("-"*60)
        print(" "*5,"Welcome To Dashboard")
        print("-"*60)
        print(" 1. Login \n 0. Exit the Program")
        try:
            choice = int(input("Select your choice : "))
            if choice == 1:
                login()
                break
            elif choice == 0:
                print("Exited the program Successfully")
                exit()
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def login():
    username = "admin"
    password = "password"
    
    max_attempts = 3
    attempts = 0
    
    while attempts < max_attempts:
        input_username = input("Enter your username: ")
        input_password = input("Enter your password: ")
        
        if input_username == username and input_password == password:
            print("-"*60)
            print(" "*5,"Welcome to Admin Panel of Data Management server ")
            print("-"*60)
            list_option()
            selectOption()
            break
        else:
            attempts += 1
            remaining = max_attempts - attempts
            print(f"Incorrect username or password. {remaining} attempts remaining.")
            if remaining == 0:
                print("Maximum login attempts reached. Program terminated.")
                exit()

def selectOption():
    while True:
        try:
            input_choice = int(input("Select your choice : "))
            if input_choice == 1:
                edit_record()
            elif input_choice == 2:
                delete_record()
            elif input_choice == 3:
                add_record()
            elif input_choice == 4:
                search_record()
            elif input_choice == 5:
                show_record()
            elif input_choice == 6:
                show_plot()
            elif input_choice == 0:
                print("Exiting the program")
                exit()
            else:
                print("Invalid choice. Please try again.")
                list_option()
        except ValueError:
            print("Please enter a valid number.")
            list_option()

def list_option():
    print("\nWhat would you like to do today?")
    print(" 1. Edit Record \n 2. Delete Record \n 3. Add record \n 4. Search Record \n 5. Show Record \n 6. Show Graph \n 0. Exit the Program")
    print("-"*60)
    print(" "*5,"DATA MANAGEMENT OF ALL INDIA INDEX 2013-2022")
    print(" "*5,"Login Time:",datetime.datetime.now())
    print("-"*60)

def show_columns():
    print("\nAvailable columns:")
    for col in df.columns:
        print(col)

def edit_record():
    print("-"*10)
    print("Enter the required values below to edit the data")
    print("-"*10)
    
    show_columns()
    
    try:
        year = int(input("Enter Year to Edit : "))
        column_name = input("Enter Column Name : ")
        
        if column_name not in df.columns:
            print("Invalid column name. Please try again.")
            return
        
        value = input("Enter Value : ")
        if column_name != "Sector" and column_name != "Month":
            try:
                value = float(value)
            except ValueError:
                print("Please enter a valid number for this column.")
                return
        
        df.loc[df['Year'] == year, column_name] = value
        df.to_csv(file_path, index=False)
        print(f"\n{column_name} Record for Year {year} has been Updated Successfully")
        
    except ValueError:
        print("Please enter a valid year.")
    
    list_option()

def delete_record():
    sector_to_delete = input("Enter Sector to delete : ")
    if sector_to_delete in df['Sector'].values:
        df_new = df[df['Sector'] != sector_to_delete]
        df_new.to_csv(file_path, index=False)
        print(f"\nSuccessfully Removed {sector_to_delete} Sector from the data")
    else:
        print("Sector not found.")
    list_option()

def add_record():
    try:
        new_record = {
            'Sector': input("Enter Sector Name : "),
            'Year': int(input("Enter Year : ")),
            'Month': input("Enter Month : "),
            'Cereals and products': float(input("Enter Cereals and products : ")),
            'Meat and fish': float(input("Enter Meat and fish : ")),
            'Egg': float(input("Enter Egg : ")),
            'Milk and products': float(input("Enter Milk and products : ")),
            'Oils and fats': float(input("Enter Oils and fats : ")),
            'Fruits': float(input("Enter Fruits : ")),
            'Vegetables': float(input("Enter Vegetables : ")),
            'Pulses and products': float(input("Enter Pulses and products : ")),
            'Sugar and Confectionery': float(input("Enter Sugar and Confectionery : ")),
            'Spices': float(input("Enter Spices : ")),
            'Non-alcoholic beverages': float(input("Enter Non-alcoholic beverages : ")),
            'Prepared meals, snacks, sweets etc.': float(input("Enter Prepared meals, snacks, sweets etc. : ")),
            'Food and beverages': float(input("Enter Food and beverages : ")),
            'Pan, tobacco and intoxicants': float(input("Enter Pan, tobacco and intoxicants : ")),
            'General index': float(input("Enter General index : "))
        }
        
        df_new = pd.concat([df, pd.DataFrame([new_record])], ignore_index=True)
        df_new.to_csv(file_path, index=False)
        print("\nRecord Added Successfully")
        
    except ValueError:
        print("Please enter valid numeric values for the indices.")
    
    list_option()

def search_record():
    sector = input("Enter Sector to search : ")
    results = df[df['Sector'].str.contains(sector, case=False, na=False)]
    if len(results) > 0:
        print("\nSearch Results:")
        print(results)
    else:
        print("No records found.")
    list_option()

def show_record():
    print("\nAll Records:")
    print(df)
    list_option()

def show_plot():
    plt.figure(figsize=(12, 6))
    for sector in df['Sector'].unique():
        sector_data = df[df['Sector'] == sector]
        plt.plot(sector_data['Year'], sector_data['General index'], label=sector)
    
    plt.title('General Index Trends by Sector (2013-2022)')
    plt.xlabel('Year')
    plt.ylabel('General Index')
    plt.legend()
    plt.grid(True)
    plt.show()
    list_option()

if __name__ == "__main__":
    program()
list_option()
selectOption()
