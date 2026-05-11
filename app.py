import pandas as pd
from data_cleaner import clean_data
from insights import generate_insights

df = pd.read_csv("sample_data.csv")

cleaned_df = clean_data(df)

print("Hello! I am your friendly neighborhood ChatBot!")
print("Type 'help' to see available commands.")

while True: 
    command = input("\nWhat can I help you with today? ").lower().strip()

    if command == "summarize data":
        print("\nDataset Shape (rows, columns):")
        print(cleaned_df.shape)
        print("\nSummary statistics:")
        print(cleaned_df.describe())

    elif command == "show missing values":
        print("\nMissing values before the clean:")
        print(df.isnull().sum())
        print("\nMissing values after the clean:")
        print(cleaned_df.isnull().sum())

    elif command == "clean data":
        print("\nClean Data Preview:")
        print(cleaned_df.head())

    elif command == "show insights":
        generate_insights(cleaned_df)
        
    elif command == "quit":
        print("Goodbye!")
        break
    
    elif command == "help":
        print("\nAvailable commands:")
        print("  summarize data")
        print("  show missing values")
        print("  clean data")
        print("  show insights")
        print("  quit")

    else: 
        print("Invalid command. Type 'help' to see available options.")