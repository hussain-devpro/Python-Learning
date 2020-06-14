import plotly
import plotly.offline as offline

offline.plot([{'x': [1,2,3], 'y': [3, 1, 5]}], filename="my_plots/my_offline.html")
offline.init_notebook_mode(connected=True)

