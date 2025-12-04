import pandas as pd
import numpy as np
import random


def sample_data_gen(filename="data/raw/employees.csv"):
    data = {
        "employee_id": [i for i in range(101, 121)],
        "name": [f"User_{i}" for i in range(101, 121)],
        "email": [f"user_{i}@company.com" for i in range(101, 121)],
        "salary": [random.randint(50000, 120000) for _ in range(20)],
        "join_date": pd.date_range(start="2020-01-01", periods=20)
        .strftime("%Y-%m-%d")
        .tolist(),
    }

    df = pd.DataFrame(data)

    # INJECT ERRORS

    # Duplicate IDs
    df.loc[2, "employee_id"] = 101

    # Missing Values
    df.loc[5, "name"] = np.nan
    df.loc[6, "salary"] = np.nan

    # Invalid logic
    df.loc[10, "salary"] = -5000

    # Bad Emails
    df.loc[15, "email"] = "kyrylo_kamennyk.com"

    print(f"generating data with errors to {filename}")
    df.to_csv(filename, index=False)


if __name__ == "__main__":
    sample_data_gen()
