# AI_chatbot_miniProject
## Project Structure

AI_chatbot_miniProject
│
├── level1_rule_based_bot
├── level2_nlp_bot
└── level3_reasoning_bot

# Tic-Tac-Toe — AI Player

Mini AI project demonstrating Level 1 (Rule-Based), Level 2 (NLP), and Level 3 (Reasoning) chatbots using Python.
# AI Chatbot Mini Project

This project demonstrates three types of chatbots:

1. Level 1 – Rule Based Chatbot
2. Level 2 – NLP Chatbot
3. Level 3 – Reasoning Chatbot

Built using Python for AI Lab.


# Tic-Tac-Toe — AI Player

A Tic-Tac-Toe game with a graphical interface (built with Tkinter) where you play against an AI opponent that uses game-tree search logic to decide its moves.

> Part of the [AI_chatbot_miniProject](https://github.com/anushka0015/AI_chatbot_miniProject) repository — see the `tic_tac_toe/` folder.

## What it does

- Renders a classic 3×3 Tic-Tac-Toe board in a Tkinter GUI window
- Lets the user click a cell to make their move
- The AI opponent responds by evaluating possible future board states using game-tree search, picking the move that gives it the best outcome
- Detects and displays the game result: win, loss, or draw

## How it works

1. **Board representation** — the 3×3 grid is stored as a simple data structure tracking each cell's state (empty, X, or O)
2. **Game loop** — after each human move, the board is checked for a win/draw; if the game continues, control passes to the AI
3. **AI decision-making** — the AI explores possible moves using game-tree logic, scoring outcomes (win/loss/draw) to pick its next move
4. **GUI updates** — Tkinter redraws the board after every move and displays the final result when the game ends

## Tech Stack

- **Language:** Python
- **GUI:** Tkinter (Python's built-in GUI toolkit)
- **AI logic:** Game-tree search

## Running it locally

```bash
git clone https://github.com/anushka0015/AI_chatbot_miniProject.git
cd AI_chatbot_miniProject/tic_tac_toe
python tic_tac_toe.py
```

*(Adjust the filename above to match whatever the entry-point script is actually named in the folder.)*

Requires Python 3 with Tkinter available (Tkinter ships with most standard Python installations).

## Possible future improvements

- Add difficulty levels (e.g., random-move AI vs. optimal-play AI)
- Add a scoreboard to track wins/losses/draws across multiple rounds
- Polish the UI with custom colors, fonts, and win-highlighting animations
- Add a "vs Human" two-player mode alongside "vs AI"

## About

Built as a hands-on way to practice implementing game-tree based decision-making and connecting game logic to a simple GUI.
