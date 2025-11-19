# AI Agent – Gemini-Powered Python Chat Assistant

This project is a terminal-based conversational AI assistant built using the Google Gemini model.  
It includes conversation history, retry handling, a simple moderation filter, and a typing animation for more natural interaction.

---

## Features

- Integrates with Google Gemini 2.5 Flash model  
- Maintains conversation history for contextual replies  
- Basic bad-word filtering for safer interactions  
- Built-in retry logic to handle API rate limits  
- Typing-effect output for realistic responses  
- Clean, simple, and extensible Python structure  
- Supports exit commands: `stop`, `exit`, `quit`, `bye`

---

## Requirements

- Python 3.9 or higher  
- Google Gemini API key  
- Install dependencies:

bash
```pip install google-generativeai```


## How to Run
Save the code as agent.py
Open your terminal inside the project folder

```Run: python agent.py```

## How the Agent Works

Takes user input from the terminal
Checks for exit commands
Runs a bad-word filter
Appends the input to the conversation history
Sends the request to Gemini using generate_content()
Prints output using a typing-effect function
Stores the AI response back into history for context


## Configuration

Model behavior can be adjusted:

```
generation_config={
    "temperature": 0.8,
    "top_p": 0.9,
    "top_k": 40
}
```

Increase temperature → more creative output
Decrease temperature → more stable, factual output

## Bad-Word Filter

The agent includes a simple keyword-based filter:

```bad_words = ["badword1", "badword2", "badword3"]```

You can add or remove words as needed.


