import random


def askQuestions():
    questions = [
        ("What's your name?", "name"),
        ("How old are you?", "age"),
        ("What's your favorite color?", "color"),
        ("What's your favorite food?", "food"),
        ("Which city do you live in?", "city"),
        ("Which SHS did you attend?", "shs"),
        ("What's your favorite soccer team?", "team")
    ]

    random.shuffle(questions)
    answers = {}

    for q, key in questions:
        answer = input(f"{q} ")
        answers[key] = answer

    return answers


def displaySummary(data):
    summary = (
        f"\nHello, {data['name']}!\n"
        f"You are {data['age']} years old, love the color {data['color']}, "
        f"and enjoy eating {data['food']}.\n"
        f"Life must be awesome in {data['city']}!\n"
        f"You went to {data['shs']} and support {data['team']} \n"
    )
    print(summary)
    return summary


def saveToFile(name, content, rating=None):
    filename = f"{name}.txt"
    with open(filename, "w") as file:
        file.write(content)
        if rating:
            file.write(f"\nUser rating: {rating}/5 stars\n")
    print(f"Summary saved to {filename}")


def main():
    while True:
        user_data = askQuestions()
        summary = displaySummary(user_data)

        save = input("Do you want to save this summary to a .txt file? (yes/no): ").lower()
        if save == "yes":
            rating = input("Rate the assistant from 1 to 5 stars: ")
            saveToFile(user_data["name"], summary, rating)
        else:
            print("Okay, file not saved.")

        restart = input("Do you want to restart the process? (yes/no): ").lower()
        if restart != "yes":
            print("Goodbye!")
            break

main()
