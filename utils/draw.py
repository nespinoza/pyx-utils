from pyx import text as pyx_text
from pyx import style as pyx_style
from pyx import deco as pyx_deco
from pyx import path as pyx_path

def text(g, x_coord, y_coord, text_input, text_size = -2, color = None):
	"""
 	Function that draws text in a given plot

	INPUTS:

		g		(Object) A graph-type object to which you want to add the text

		x_coord		(Double) x-coordinate (in plot units) at which you want to place
				the text

		y_coord		(Double) y-coordinate (in plot units) at which you want to place
				the text

		text_input	(String) Text that you want to add.

		text_size	(int, optional) Text size of the text added to the plot. Default is -2.

		color		(instance) Color instance that defines the color that you want the 
				text to have. Default is black.
	"""

	# First define the text attributes:
	textattrs = [pyx_text.size(text_size),pyx_text.halign.center, pyx_text.vshift.middlezero]

	# Now convert plot positions to pyx's:
	x0,y0 = g.pos(x_coord, y_coord)

	# If no color is given, draw black text. If color is given, draw text with the input color:
	if color is None:
		g.text(x0,y0,text_input,textattrs)
	else:
		# First, check which was the input color palette:
		color_dict = color.color
		if len(color_dict.keys()) == 4:
			color_string = str(color_dict['c'])+','+str(color_dict['m'])+','+str(color_dict['y'])+','+str(color_dict['k'])
			color_palette = 'cmyk'
		else:
                        color_string = str(color_dict['r'])+','+str(color_dict['g'])+','+str(color_dict['b'])
                        color_palette = 'rgb'
		# Now draw the text:
		g.text(x0, y0, r"\textcolor["+color_palette+"]{"+color_string+"}{"+text_input+"}",textattrs)

def arrow(g, x_coord_init, y_coord_init, x_coord_final, y_coord_final, size, line_color, stroke_color = None, fill_color = None):
        """
        Function that draws an arrow in a given plot

        INPUTS:

                g               (Object) A graph-type object to which you want to add the text

                x_coord_init    (Double) x-coordinate (in plot units) at which you want the arrow
                                to start.

                y_coord_init    (Double) y-coordinate (in plot units) at which you want the arrow
                                to start.

                x_coord_final   (Double) x-coordinate (in plot units) at which you want the arrow
                                to end.

                y_coord_final   (Double) y-coordinate (in plot units) at which you want the arrow
                                to end.

		size		(int) Size of the arrow.

		line_color	(instance) Instance color that defines the color of the line of the arrow.

		stroke_color	(instance, optional) Defines the stroke color (default is same as line_color).

		fill_color	(instance, optional) Defines the color fill of the arrow (default is same as 
				line_color).

        """

	if stroke_color is None:
		stroke_color = line_color
	if fill_color is None:
		fill_color = line_color

	x0,y0 = g.pos(x_coord_init , y_coord_init)
	xf,yf = g.pos(x_coord_final, y_coord_final)
	g.stroke(pyx_path.line(x0,y0,xf,yf),\
		[pyx_style.linewidth.normal, pyx_style.linestyle.solid, line_color,\
		 pyx_deco.earrow([pyx_deco.stroked([stroke_color]),\
		 pyx_deco.filled([fill_color])], size=0.1)])

def rectangular_band(g, x_coord_init, y_coord_init, x_coord_final, y_coord_final, band_color):
        """
        Function that draws a rectangular band around the given coordinates

        INPUTS:

                g               (Object) A graph-type object to which you want to add the text

                x_coord_init    (Double) x-coordinate (in plot units) at which you want the band
                                to start.

                y_coord_init    (Double) y-coordinate (in plot units) at which you want the band
                                to start.

                x_coord_final   (Double) x-coordinate (in plot units) at which you want the band
                                to end.

                y_coord_final   (Double) y-coordinate (in plot units) at which you want the band
                                to end.

                band_color      (instance) Instance color that defines the color of the band.

        """
	x0,y0 = g.pos(x_coord_init , y_coord_init)
	xf,yf = g.pos(x_coord_final, y_coord_final)

	x = x0
	y = y0
	w = np.abs(x0-xf)
	h = np.abs(y0-yf)

	g.fill(pyx_path.rect(x,y,w,h), [band_color])
