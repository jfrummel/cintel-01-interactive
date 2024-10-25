import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render
from shinyswatch import theme

ui.page_opts(
    title="My PyShiny App with an Interactive Slider", fillable=True, theme=theme.superhero
)

with ui.sidebar():
    ui.input_slider("selected_number_of_bins", "Number of Bins", 1, 150, 50)
    

@render.plot(alt="A histogram of number of bins selected")
def histogram():
    np.random.seed(3)
    x = 100 + 15 * np.random.randn(437)
    plt.hist(x, input.selected_number_of_bins(), color="purple", density=True)
    plt.grid()
    plt.title(f"My histogram with {input.selected_number_of_bins()} bins selected")
