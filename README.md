# HaylStone
> A small Python visualizer for the Collatz sequence with interactive graphs and terminal support.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

HaylStone is a small Python program that generates and visualizes the Collatz sequence for any positive integer seed, with an optional logarithmic view and toggleable labels, and a terminal-friendly version included.

### Features

- Input any positive integer as a starting seed
- Interactive matplotlib graph of the full Collatz sequence
- Toggle between linear and logarithmic Y-axis scaling
- Toggleable labels on every data point
- A second program that will run in the terminal and save images of the plot.

### Why

The Collatz conjecture is one of the simplest unsolved problems in mathematics — take any positive integer, halve it if it's even, or triple it and add one if it's odd, and repeat. The conjecture states that eventually, every number reaches a loop of 4, 2, 1.

This visualizer isn't trying to solve the conjecture. It just visualizes it.

### Usage

1. Clone the repository and enter it:
    ```bash
    git clone https://github.com/Saibot28/HaylStone
    cd HaylStone
    ```
    
2. Run the script:
    ```bash
    python3 haylstone.py
    ```
    or:
    ```bash
    python3 haylstone_terminal.py
    ```

3. Enter any positive integer into the popup window.

4. View the sequence plotted linearly or logarithmically with or without labeled points. (For the terminal version, go to the `plots` directory and open the images)

### Requirements

- Python 3.x
- `matplotlib` (usually installable with `pip install matplotlib`)
- `tkinter` (included with most Python installations) (not required for haylstone_terminal)

---

Made for fun. Use it, break it, or build on it. Just don’t try to prove Collatz with it. (Unless you do. In which case, DM me.)

## License

This project is licensed under the [MIT License](./LICENSE).
