from src.generator import sample_data_gen
from src.validator import DataValidator
from src.database import save_to_db
import os


def main():

    # Generate data
    input_file = "data/raw/employees.csv"
    sample_data_gen(input_file)

    # Validate data
    validator = DataValidator(input_file)
    clean_data, error_report = validator.validate()

    # Handle errors
    if not error_report.empty:
        print(f"\nFound {len(error_report)} corrupted records.")
        os.makedirs(os.path.dirname("data/processed/error_report.csv"), exist_ok=True)
        error_report.to_csv("data/processed/error_report.csv", index=False)
        print("Error report saved to data/processed/error_report.csv")
    else:
        print("No errors found!")

    # Save clean data to db
    save_to_db(clean_data)


if __name__ == "__main__":
    main()
