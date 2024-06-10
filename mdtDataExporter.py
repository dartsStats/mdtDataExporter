import sqlite3
import pandas as pd

def export_table_to_csv(database_file, table_name, csv_file):
    """
    Export a specific table from an SQLite database to a CSV file.

    Parameters:
    - database_file: str, path to the SQLite database file.
    - table_name: str, name of the table to export.
    - csv_file: str, path to the output CSV file.
    """
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(database_file)
        
        # Read the table into a pandas DataFrame
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
        
        # Export the DataFrame to a CSV file
        df.to_csv(csv_file, index=False)
        
        print(f"Table '{table_name}' has been exported to '{csv_file}' successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the connection
        conn.close()

if __name__ == "__main__":
    import argparse

    # Set up command line arguments
    parser = argparse.ArgumentParser(description="Export X01 tables from a My Dart Training database to CSV files.")
    parser.add_argument("database_file", help="Path to the My Dart Training database file.")
    parser.add_argument("output_dir", help="Directory where the output CSV files will be saved.")

    # Parse the arguments
    args = parser.parse_args()

    # Export the tables to CSV
    export_table_to_csv(args.database_file, 'xGame', args.output_dir + '/xGame.csv')
    export_table_to_csv(args.database_file, 'aufnahme', args.output_dir + '/aufnahme.csv')