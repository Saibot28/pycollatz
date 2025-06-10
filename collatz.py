import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

root = tk.Tk()  # create the main window 
root.withdraw() # hide the root window

def collatz():
    num=0

    global seqLength    # make seqLength global
    global graph_Y      # make graph_Y global
    seqLength = 1       # update sequence length to accord for skipped last iteration
    graph_Y = []        # create an empty list in graph_Y

    try:
        num = int(simpledialog.askstring("Input", "Enter Collatz sequence seed:"))      # open input window
    except (TypeError, ValueError):                                                     # handle unsupported inputs
        messagebox.showerror("Error", "Please input a valid integer.")
        return

    if num < 1:   # check if integer is positive and not equal to zero
        print("Please input a positive integer greater than zero.")
        return 

    while num != 1:
        seqLength += 1      # update sequence length
        print(num)
        graph_Y.append(num)
        if num%2==0:        # check if integer is even
            num = num//2
        elif num%2==1:      # check if integer is odd
            num = num*3+1
        
    print("1")                                          # print final number
    graph_Y.append(1)
    print("Collatz Sequence Length: "+str(seqLength))   # output sequence length

def plotGraph():

    fig, ax = plt.subplots()                        # create graph
    ax.set_title("Collatz Sequence Graph")
    ax.grid(True)                                   # enable grid
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Value')
    
    plt.subplots_adjust(bottom=0.2)                         # adjust for button
    
    ax_button = plt.axes([0.7, 0.05, 0.2, 0.075])           # specify button size
    log_button = Button(ax_button, 'Toggle Log/Linear')     # create button instance
    is_log_scale = [False]

    ax_button = plt.axes([0.125, 0.05, 0.2, 0.075])         # specify button size
    lbl_button = Button(ax_button, 'Show/Hide Labels')      # create button instance
    hide_labels = [False]
    
    graph_X = list(range(1, seqLength+1))           # make x-axis length equal to value of seqLength
    ax.plot(graph_X, graph_Y, marker='.')           # plot sequence graph

    for x, y in zip(graph_X, graph_Y):
        ax.text(x, y, y, fontsize=8, ha='left', va='bottom')    # add labels on points

    def toggle_scale(event):
        if is_log_scale[0]:
            ax.set_yscale('linear')     # makes graph linear
            is_log_scale[0] = False     # updates flag accordingly
        else:
            ax.set_yscale('log')        # makes graph logarithmic
            is_log_scale[0] = True      # updates flag accordingly
        fig.canvas.draw_idle()          # queues a redraw

    def toggle_labels(event):
        if hide_labels[0]:
            for x, y in zip(graph_X, graph_Y):
                ax.text(x, y, y, fontsize=8, ha='left', va='bottom')    # adds labels back
            hide_labels[0] = False                                      # updates flag accordingly
        else:
            for txt in ax.texts:        # go through all text elements in graph
                txt.remove()            # delete the text element
            hide_labels[0] = True       # updates flag accordingly
        fig.canvas.draw_idle()          # queues a redraw

    log_button.on_clicked(toggle_scale)     # links the button object to the log/lin toggle
    lbl_button.on_clicked(toggle_labels)
    plt.show()                              # display the created graph

collatz()       # run collatz() function
plotGraph()     # run plotGraph() function
