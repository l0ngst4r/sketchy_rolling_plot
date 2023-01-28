# sketchy_rolling_plot

Created these files in order to try an animated plotting method in a cartoony style.

When starting main.py, it calls the data_gen.py in asynch and runs it parallel with main.py to generate some random data,
writes it into a csv, which main.py can read and plot real time.

Once the plotting gets cluttered (after 200 pairs of data read) it starts scrolling so the data showed remains 200 datapoints at any time.

Matplotlib has a XKCD cartoony style, which was a bit buggy on my system, so created a similar.

Requirements for the venv also included, as well a little howto for both venv and on installing the font attached.
