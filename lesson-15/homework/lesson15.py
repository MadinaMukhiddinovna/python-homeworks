import sqlite3

# Connect to (or create) a new SQLite database file
conn = sqlite3.connect("roster.db")
cursor = conn.cursor()

# Step 1: Create table Roster
cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

# Step 2: Insert values
roster_data = [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
]

cursor.execute("DELETE FROM Roster")  # Clear existing data for repeated runs
cursor.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", roster_data)

# Step 3: Update Jadzia Dax to Ezri Dax
cursor.execute("""
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
""")

# Step 4: Display Name and Age of Bajoran species
cursor.execute("""
SELECT Name, Age FROM Roster
WHERE Species = 'Bajoran'
""")
results = cursor.fetchall()

print("Bajoran Members:")
for name, age in results:
    print(f"{name}, Age: {age}")

# Save changes and close connection
conn.commit()
conn.close()

# Connects to a SQLite database called roster.db
# Creates a table if it doesn't exist with Name, Species, Age
# Inserts 3 people into the table
# Updates "Jadzia Dax" to "Ezri Dax"
# Selects and prints all Bajorans' names and ages
