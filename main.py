import json
from difflib import get_close_matches

def load(file_loc: str) -> dict:
    with open(file_loc, 'r') as response:
        data: dict = json.load(response)
        return data
    
def save(file_loc: str, data: dict):
    with open(file_loc, 'w') as response:
        json.dump(data, response, indent=2)

def best_match(user_question: str, question: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, question, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer(user_question: str, trained: dict) -> str | None:
    for qna in trained["questions"]:
        if user_question in qna["question"].lower():
            return qna["answer"]
    return None

def bot():
    trained: dict = load('train.json')
    while True:
        user_io = input("You: ").lower()
        print("\n")
        if user_io == "quit":
            break

        answer: str = get_answer(user_io, trained)

        if answer:
            print(f"Bot: {answer}")
        else:
            print("Out of my dataset, Give me more info on it! (or if you need this response to be skipped type skip)")
            print("\n")
            new_data = input("You: ").lower()

            if new_data != "skip":
                trained["questions"].append({"question": user_io, "answer": new_data})
                save('train.json', trained)
                print("Bot: Thank you for the response!")
                print("\n")

def start():
    print("Welcome to BMW Autos\n")
    print("How can I assist you today?\n")
    print("Would you like information about cars?\n")

if __name__ == '__main__':
    start()
    bot()
