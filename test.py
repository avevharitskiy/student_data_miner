from graph_tool.all import *
g = collection.data["football"]
print(g)
state = minimize_blockmodel_dl(g)
pos = arf_layout(g)
state.draw(pos=state.bfield, output="football-sbm-fit.svg")