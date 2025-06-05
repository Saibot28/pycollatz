# Collatz Sequence Visualizer

This is a small Python program that generates and visualizes the Collatz sequence for any positive integer seed, with a toggleable logarithmic view.

### Features

- Input any positive integer as a starting seed
- Interactive matplotlib graph of the full Collatz sequence
- Toggle between linear and logarithmic Y-axis scaling with a single button
- Labels on every data point for maximum clarity and insight

### Why

The Collatz conjecture is one of the simplest unsolved problems in mathematics — take any positive integer, halve it if it's even, or triple it and add one if it's odd, and repeat. The conjecture states that eventually, every number reaches a loop of 4, 2, 1.

This visualizer isn't trying to solve the conjecture. It just makes watching the chaos a little more beautiful.

### Usage

1. Run the script:
    ```bash
    python3 collatz.py
    ```

2. Enter any positive integer into the popup window.

3. View the sequence plotted with labeled points.

4. Click the "Toggle Log/Linear" button to switch between Y-axis scales and explore the behavior visually.

### Requirements

- Python 3.x
- `matplotlib` (usually installable with `pip install matplotlib`)
- `tkinter` (included with most Python installations)

---

Made for fun. Use it, break it, or build on it. Just don’t try to prove Collatz with it. (Unless you do. In which case, DM me.)
