import sys
sys.path.append('../utils/')
from pyx import graph, canvas, color, text, unit
import draw

# Define some pyx options:

unit.set(xscale=0.8)
text.set(mode="latex")
text.preamble(r"\usepackage{color}")
text.preamble(r"\usepackage{wasysym}")

# Now plot:

c = canvas.canvas()

the_plot = c.insert(graph.graphxy(height=3,width=10,\
                   x = graph.axis.linear(min = 0, max=10, title = 'x-axis'),\
                   y = graph.axis.linear(min = 0, max=10, title = 'y-axis')))

draw.text(the_plot,5.,5.,'This is my text!', color = color.cmyk.CornflowerBlue)
draw.arrow(the_plot, 2. , 5., 4., 5., -1, color.cmyk.CornflowerBlue)

c.writePDFfile('plot_with_text')
