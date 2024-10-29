# Import required dependencies
import plotly.express as px
import palmerpenguins # This package provides palmer penguin dataset.
from shiny.express import input, ui
from shinywidgets import render_plotly

##############################
# Get dataset to be presented and load into pandas dataframe
###############################
# Dataset Description
###############################
# species: penguin species (Chinstrap, Adelie, or Gentoo)
# island: island name (Dream, Torgersen, or Biscoe) in the Palmer Archipelago
# bill_length_mm: length of the bill in millimeters
# bill_depth_mm: depth of the bill in millimeters
# flipper_length_mm: length of the flipper in millimeters
# body_mass_g: body mass in grams
# sex: MALE or FEMALE

# Use the built-in function to load the Palmer Penguins dataset
penguins_df = palmerpenguins.load_penguins()

###########################
#Define and Design our user interface.
############################

ui.page_opts(title="Arnold Atchoe- Palmer Peguins", fillable=True)
with ui.layout_columns():

############################
# Render the desired charts and visuals
############################
    @render_plotly
    def plot1():
        return px.histogram(penguins_df, x="bill_length_mm")

    @render_plotly
    def plot2():
        return px.histogram(penguins_df, x="body_mass_g")
