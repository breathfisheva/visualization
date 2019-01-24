
from pyecharts import Bar
bar = Bar('title', 'sub-title')
bar.add('bug status',['open','closed','resolved'],[9,19,3])
bar.show_config()
bar.render()