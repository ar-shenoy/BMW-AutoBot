BMW Autos Assistant

This script implements a conversational bot that provides information about BMW cars. It interacts with users through a command-line interface and can answer questions related to BMW models, features, specifications, and more.

**How to Use:**

**Starting the Bot:**

1. Run the script in your preferred Python environment.
2. You'll be greeted with a welcome message and prompted to input your query.

**Asking Questions:**

1. You can ask questions about BMW cars, such as model information, features, performance, and more.
2. The bot will attempt to provide relevant answers based on pre-trained data.

**Adding New Responses:**

1. If the bot doesn't have an answer to your question, it will prompt you to provide more information.
2. You can input the desired response, and the bot will save it for future reference.

**Exiting the Bot:**

- To exit the bot, simply type "quit" when prompted for input.

**Understanding the Code:**

**Function Definitions:**

- `load(file_loc: str) -> dict`: Loads JSON data from a file and returns it as a dictionary.
- `save(file_loc: str, data: dict)`: Saves a dictionary as JSON data to a file.
- `best_match(user_question: str, question: list[str]) -> str | None`: Finds the best matching question from a list given a user's question.
- `get_answer(user_question: str, trained: dict) -> str | None`: Retrieves an answer from the trained data based on the user's question.
- `bot()`: The main function controlling the conversation with the user.
- `start()`: Displays a welcome message at the beginning of the interaction.

**Understanding the Code Flow:**

- The script is structured into functions that handle loading and saving data, finding the best match for user questions, and interacting with the user.
- The main function (`bot()`) controls the conversation flow, while auxiliary functions handle data loading, saving, and processing.

**Requirements:**

- Python 3.x
- `json` module (for reading and writing JSON files)
- `difflib` module (for finding close matches to user questions)

**Note:**

- This script is designed to provide information about BMW cars only. If you have questions about other topics, the bot may not be able to provide relevant answers.
