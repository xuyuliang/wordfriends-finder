import sqlite3

# Define database name and table name
DATABASE_NAME = "data.db"
TABLE_NAME = "coca"

def insert_data(data_list):
    """Inserts a list of data lines with sequential SNs into the database."""
    # Prepare data with SNs
    data_with_sn = []
    for i, line in enumerate(data_list):
        data_with_sn.append((i + 1, line[1:]))  # Add SN and content

    # Connect to the database (outside the loop for single connection)
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    # Create table if it doesn't exist (outside the loop)
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        sn INTEGER PRIMARY KEY,
        content TEXT
    )""")

    # Execute bulk insert
    cursor.executemany(f"INSERT INTO {TABLE_NAME} (sn,word ) VALUES (?, ?)", data_with_sn)

    # Commit changes after all insertions (once per connection)
    conn.commit()
    conn.close()

# def insert_data(sn,data):
#     """Inserts a line of data with a sequential SN into the database."""
#     content = data  # Extract content from line (skip SN)

#     # Connect to the database
#     conn = sqlite3.connect(DATABASE_NAME)
#     cursor = conn.cursor()

#     # Insert data
#     cursor.execute(
#         f"INSERT INTO {TABLE_NAME} (sn, word) VALUES (?, ?)", (sn, content)
#     )

#     # Save changes and close connection
#     conn.commit()
#     conn.close()


def main():
    """Reads the txt file and calls insert_data for each line."""
    try:
        # Open the file for reading
        datalist =[]
        with open("coca60000.txt", "r") as file:
            # Read lines one by one
            sn = 0
            for line in file:
                # Split line by some delimiter (assuming data is separated)
                data = line.strip()  # Remove whitespaces and split
                datalist.append(data)
        # print the size of datalist
        print(f"Read {len(datalist)} lines from coca60000.txt")
        insert_data(datalist)
        print(f"Data from coca60000.txt inserted into {DATABASE_NAME}")

    except FileNotFoundError:
        print(f"Error: File coca60000.txt not found.")


if __name__ == "__main__":
    main()
