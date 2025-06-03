import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button

def collatz():
    num=0

    global seqLength    # make seqLength global
    global graph_Y      # make graph_Y global
    seqLength = 1       # update sequence length to accord for skipped last iteration
    graph_Y = []        # create an empty list in graph_Y

    try:
        num = int(input("Enter Collatz sequence seed: "))  # input seed and convert to integer
    except ValueError:
        print("Please input a valid integer.")
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
    
    plt.subplots_adjust(bottom=0.2)                 # adjust for button
    
    ax_button = plt.axes([0.7, 0.05, 0.2, 0.075])   # specify button position
    button = Button(ax_button, 'Toggle Log/Linear') # create button instance
    is_log_scale = [False]
    
    graph_X = list(range(1, seqLength+1))           # make x-axis length equal to value of seqLength
    ax.plot(graph_X, graph_Y, marker='.')           # plot sequence graph
    plt.show()                                      # display the created graph

    def toggle_scale(event):
        if is_log_scale[0]:
            ax.set_yscale('linear')
            is_log_scale[0] = False
        else:
            ax.set_yscale('log')
            is_log_scale[0] = True
        fig.canvas.draw_idle()




collatz()       # run collatz() function
plotGraph()     # run plotGraph() function