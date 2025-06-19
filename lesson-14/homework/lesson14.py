import json
import random
import requests

# ---------- Task 1: JSON Parsing ----------
def read_students():
    try:
        with open("students.json", "r") as file:
            students = json.load(file)
            for student in students:
                print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
    except FileNotFoundError:
        print("students.json file not found.")
    except json.JSONDecodeError:
        print("Invalid JSON format in students.json")

# ---------- Task 2: Weather API ----------
def fetch_weather():
    city = "Tashkent"
    api_key = "your_api_key_here"  #Replace with your real API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            print(f"Weather in {city}:")
            print(f"Temperature: {data['main']['temp']} °C")
            print(f"Humidity: {data['main']['humidity']}%")
            print(f"Condition: {data['weather'][0]['description']}")
        else:
            print("Failed to fetch weather data:", data.get("message"))
    except Exception as e:
        print("Error:", e)

# ---------- Task 3: JSON Modification ----------
def manage_books():
    try:
        with open("books.json", "r") as file:
            books = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        books = []

    while True:
        print("\nBook Manager: [1] Add [2] Update [3] Delete [4] Show [0] Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            books.append({"title": title, "author": author})
            print("Book added.")
        elif choice == "2":
            title = input("Enter title to update: ")
            for book in books:
                if book["title"] == title:
                    book["author"] = input("Enter new author: ")
                    print("Book updated.")
                    break
            else:
                print("Book not found.")
        elif choice == "3":
            title = input("Enter title to delete: ")
            books = [book for book in books if book["title"] != title]
            print("Book deleted.")
        elif choice == "4":
            for book in books:
                print(f"{book['title']} by {book['author']}")
        elif choice == "0":
            break
        else:
            print("Invalid option.")

    with open("books.json", "w") as file:
        json.dump(books, file, indent=4)

# ---------- Task 4: Movie Recommendation ----------
def recommend_movie():
    genre = input("Enter movie genre (e.g., Action, Comedy, Drama): ").lower()
    api_key = "your_api_key_here"  #Replace with your OMDB API key
    url = f"http://www.omdbapi.com/?apikey={api_key}&s={genre}&type=movie"

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("Response") == "True":
            movie = random.choice(data["Search"])
            print(f"Recommended Movie: {movie['Title']} ({movie['Year']})")
        else:
            print("No movies found in this genre.")
    except Exception as e:
        print("Error:", e)


# --------------------------- MAIN ---------------------------
print("\nTASK 1: JSON Parsing (Students)")
read_students()

print("\nTASK 2: Weather API")
fetch_weather()

print("\nTASK 3: JSON Modification (Books)")
manage_books()

print("\nTASK 4: Movie Recommendation System")
recommend_movie()


#students.json 
[
    {"name": "Ali", "age": 20, "grade": "A"},
    {"name": "Madina", "age": 19, "grade": "B"}
]


