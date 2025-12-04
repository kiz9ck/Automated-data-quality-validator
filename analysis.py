import sqlite3
import pandas as pd


def run_analysis(db_path="data/validated_data.db"):
    try:
        # Connect to the db
        conn = sqlite3.connect(db_path)
        print(f"Connect to database: {db_path}")

        # Shows the top 5 highest paid employees
        sql_query = """
        SELECT name, salary, email, join_date
        FROM employees
        ORDER BY salary DESC
        LIMIT 5;
        """

        # Execute and load into pd
        df_results = pd.read_sql_query(sql_query, conn)

        # Display results
        if not df_results.empty:
            print(df_results)
        else:
            print("No data found. Maybe run main.py first?")

        conn.close()

    except sqlite3.Error as e:
        print(f"Database error: {e}")


if __name__ == "__main__":
    run_analysis()
