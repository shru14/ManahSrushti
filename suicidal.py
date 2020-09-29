# Import libraries 
import numpy as np 
import matplotlib.pyplot as plt 
  
Questions_related_to_suicide = [
'Not at all',
'Several days', 
'more than half of the days', 
'nearly everyday'

]

data = [
2026,
157,
30,
30


]
# Creating explode data 
explode = (0.0, 0.0, 0.0, 0.1) 
  
# Creating color parameters 
colors = ( "orange", "grey", "beige", "pink") 
  
# Wedge properties 
wp = { 'linewidth' : 1, 'edgecolor' : "black" } 
arr = []
# Creating autocpt arguments 
def func(pct, allvalues): 
    absolute = int(pct / 100.*np.sum(allvalues)) 
    arr.append("{:.1f}%\n({:d})".format(pct, absolute))
    return "{:.1f}%".format(pct, absolute)
  
# Creating plot 
fig, ax = plt.subplots(figsize =(10, 7)) 
wedges, texts, autotexts = ax.pie(data,  
				  autopct = lambda pct: func(pct, data), 
                                  explode = explode,  
                                  labels = None, 
                                  shadow = True, 
                                  startangle = 45, 
				  radius=1,
                                  wedgeprops = wp, 
                                  textprops = dict(color ="black",fontsize="40")) 

bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"), bbox=bbox_props, zorder=0, va="center")
for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(arr[i], xy=(x, y), xytext=(1.25*np.sign(x), 1.4*y), horizontalalignment=horizontalalignment, **kw)
plt.tight_layout()
 
# Adding legend 
ax.legend(wedges, Questions_related_to_suicide, 
          title ="Questions_related_to_suicide", 
          loc ="center left", 
          bbox_to_anchor =(1, 0, 0.5, 1)) 

plt.setp(autotexts, size = 8, weight ="bold") 

plt.savefig("/home/neil/manasrushti/pie_charts/suicide_questions1.png", bbox_inches="tight")



    

    
    
