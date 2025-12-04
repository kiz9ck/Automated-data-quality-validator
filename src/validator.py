import pandas as pd


class DataValidator:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
        self.errors = pd.DataFrame()
        self.clean_data = self.df.copy()

    def validate(self):
        """Validation checks"""
        print("Starting Validation")

        # Check for missing values
        self._check_missing_values(["name", "salary", "email"])

        # Check for duplicates
        self._check_duplicates("employee_id")

        # Check logic
        self._check_logic("salary")

        # Check email
        self._check_email()

        return self.clean_data, self.errors

    def _check_missing_values(self, col):
        for col in col:
            is_null = self.clean_data[col].isnull()
            if is_null.any():
                bad_rows = self.clean_data[is_null].copy()
                bad_rows["error_reason"] = f"Missing value in {col}"
                self._add_errors(bad_rows)

                # Remove from clean data
                self.clean_data = self.clean_data[~is_null]

    def _check_duplicates(self, col):
        # Find duplicates
        is_dup = self.clean_data.duplicated(subset=[col], keep=False)
        if is_dup.any():
            bad_rows = self.clean_data[is_dup].copy()
            bad_rows["error_reason"] = f"Duplicate {col}"
            self._add_errors(bad_rows)

            self.clean_data = self.clean_data[~is_dup]

    def _check_logic(self, col):
        is_negative = self.clean_data[col] < 0
        if is_negative.any():
            bad_rows = self.clean_data[is_negative].copy()
            bad_rows["error_reason"] = f"Negative value in {col}"
            self._add_errors(bad_rows)

            self.clean_data = self.clean_data[~is_negative]

    def _check_email(self):
        # Does it contain '@'?
        is_bad_email = ~self.clean_data["email"].str.contains("@", na=False)
        if is_bad_email.any():
            bad_rows = self.clean_data[is_bad_email].copy()
            bad_rows["error_reason"] = "ivalid email dormat"
            self._add_errors(bad_rows)

            self.clean_data = self.clean_data[~is_bad_email]

    def _add_errors(self, bad_rows):
        self.errors = pd.concat([self.errors, bad_rows])
