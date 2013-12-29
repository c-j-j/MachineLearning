import matplotlib.pyplot as plt

def generate_scatter_graph(x_data,y_data,image_file, x_label="Population of City in 10,000s",y_label="Profit in $10,000s",
                 title="MarkerSize"):
    # Create a Figure object.
    fig = plt.figure(figsize=(5, 4))
    # Create an Axes object.
    ax = fig.add_subplot(1,1,1) # one row, one column, first plot
    # Plot the data.
    ax.scatter(x_data, y_data, color="red", marker="^")
    # Add a title.
    ax.set_title(title)
    # Add some axis labels.
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    # Produce an image.
    fig.savefig(image_file)


