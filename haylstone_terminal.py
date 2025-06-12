import os
import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend that writes to files
import matplotlib.pyplot as plt

def collatz():
    num = 0

    global seqLength
    global graph_Y
    seqLength = 1
    graph_Y = []

    try:
        num = int(input("Enter Collatz sequence seed: "))  # terminal input
    except ValueError:
        print("Error: Please input a valid integer.")
        return False

    if num < 1:
        print("Please input a positive integer greater than zero.") # terminal output
        return False

    while num != 1:
        seqLength += 1 
        print(num)
        graph_Y.append(num)
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1

    print("1")
    graph_Y.append(1)
    print("Collatz Sequence Length: " + str(seqLength))
    return True

def plot_and_save_graph(log_scale, show_labels, save_path):
    fig, ax = plt.subplots()
    ax.set_title("Collatz Sequence Graph")
    ax.grid(True)
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Value')

    if log_scale:
        ax.set_yscale('log')
    else:
        ax.set_yscale('linear')

    graph_X = list(range(1, seqLength + 1))
    ax.plot(graph_X, graph_Y, marker='.')

    if show_labels:
        for x, y in zip(graph_X, graph_Y):
            ax.text(x, y, str(y), fontsize=8, ha='left', va='bottom')

    plt.tight_layout()
    plt.savefig(save_path)
    plt.close(fig)
    print(f"Saved plot: {save_path}")

def plotGraph():
    # Create plots directory if it doesn't exist
    if not os.path.exists('plots'):
        os.makedirs('plots')

    # save plots to /plots/collatz_[scale]_[labels].png
    plot_and_save_graph(log_scale=False, show_labels=True, save_path='plots/collatz_linear_labels.png')
    plot_and_save_graph(log_scale=False, show_labels=False, save_path='plots/collatz_linear_nolabels.png')
    plot_and_save_graph(log_scale=True, show_labels=True, save_path='plots/collatz_log_labels.png')
    plot_and_save_graph(log_scale=True, show_labels=False, save_path='plots/collatz_log_nolabels.png')

if collatz():
    plotGraph()
