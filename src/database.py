import sqlite3
import pandas as pd


def save_to_db(df, db_name="data/validated_data.db", table_name="employees"):
    """Saves the df to a SQLite db"""
    if df.empty:
        print("No clean data")
        return

    conn = sqlite3.connect(db_name)
    df.to_sql(table_name, conn, if_exists="replace", index=False)

    print(f"Successfully saved {len(df)} records to {table_name} table in {db_name}")
    conn.close()
