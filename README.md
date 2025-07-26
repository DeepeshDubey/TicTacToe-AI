<h1 align="center">🎮 Tic Tac Toe AI with Minimax Algorithm</h1>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.8%2B-blue" alt="Python Version">
  <img src="https://img.shields.io/badge/GUI-Tkinter-orange" alt="GUI">
</p>

<p align="center">A complete implementation of the classic Tic Tac Toe game featuring an unbeatable AI opponent using the Minimax algorithm, packaged with a clean Tkinter GUI interface.</p>

<h2>📌 Table of Contents</h2>
<ul>
  <li><a href="#features">Features</a></li>
  <li><a href="#demo">Demo</a></li>
  <li><a href="#installation">Installation</a></li>
  <li><a href="#how-to-play">How to Play</a></li>
  <li><a href="#project-structure">Project Structure</a></li>
  <li><a href="#algorithm-explained">Algorithm Explained</a></li>
  <li><a href="#screenshots">Screenshots</a></li>
  <li><a href="#contributing">Contributing</a></li>
  <li><a href="#license">License</a></li>
</ul>

<h2 id="features">✨ Features</h2>
<ul>
  <li><strong>Human vs AI gameplay</strong> with intuitive GUI</li>
  <li><strong>Unbeatable AI</strong> powered by Minimax algorithm</li>
  <li><strong>Responsive interface</strong> with Tkinter</li>
  <li><strong>Game state tracking</strong> (win/lose/draw detection)</li>
  <li><strong>Restart functionality</strong> at any point</li>
  <li><strong>Modular codebase</strong> following OOP principles</li>
</ul>

<h2 id="how-to-play">🎮 How to Play</h2>
<ul>
  <li>You play as <strong>X</strong>, the AI is <strong>O</strong></li>
  <li>Click any empty cell to make your move</li>
  <li>The AI will respond automatically</li>
  <li>Game ends when:
    <ul>
      <li>A player gets 3 in a row (horizontally, vertically, or diagonally)</li>
      <li>The board is full (draw)</li>
    </ul>
  </li>
  <li>Click "Restart" to play again</li>
</ul>

<h2 id="project-structure">📂 Project Structure</h2>
<pre>
TicTacToe-AI/
├── main.py          # Application entry point
├── game.py          # Core game logic and AI implementation
├── gui.py           # Tkinter GUI setup and event handling
├── constants.py     # Game constants and configurations
├── README.md        # Project documentation
└── requirements.txt # Python dependencies
</pre>

<h2 id="algorithm-explained">🧠 Algorithm Explained</h2>
<h3>Minimax Implementation</h3>
<p>The AI uses the Minimax algorithm with backtracking to evaluate all possible game states:</p>

<pre><code>def minimax(board, is_maximizing):
    # Base cases
    winner = check_winner(board)
    if winner == AI:
        return 1
    elif winner == HUMAN:
        return -1
    elif is_board_full(board):
        return 0
    
    # Recursive case
    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                score = minimax(board, False)
                board[i] = EMPTY
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN
                score = minimax(board, True)
                board[i] = EMPTY
                best_score = min(score, best_score)
        return best_score
</code></pre>

<p>Key characteristics:</p>
<ul>
  <li><strong>Depth-first search</strong> of game tree</li>
  <li><strong>Optimal play</strong> assumption (AI never loses)</li>
  <li><strong>Recursive backtracking</strong> to evaluate moves</li>
  <li><strong>Score propagation</strong> from terminal states</li>
</ul>

<hr>
<p align="center"><strong>Enjoy the game!</strong> 🚀 For any questions, please open an issue in the repository.</p>
