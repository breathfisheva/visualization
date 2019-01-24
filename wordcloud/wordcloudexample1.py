import pyecharts
from pyecharts import WordCloud

myWordCloud = WordCloud("绘制词云",width=1000, height=620)
name = ['Sam S Club', 'Macys', 'Amy Schumer', 'Jurassic World', 
        'Charter Communications', 'Chick Fil A', 'Planet Fitness', 'Pitch Perfect', 
        'Express', 'Home', 'Johnny Depp', 'Lena Dunham',
        'Lewis Hamilton', 'KXAN', 'Mary Ellen Mark', 'Farrah Abraham', 
        'Rita Ora', 'Serena Williams', 'NCAA baseball tournament', 'Point Break'] 
value = [ 10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112, 965,
         847, 582, 555, 550, 462, 366, 360, 282, 273, 265] 
myWordCloud.add("",name,value,word_size_range=[20,100])

myWordCloud.show_config()
myWordCloud.render()