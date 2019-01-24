from pyecharts import Bar
bar = Bar('title', 'sub-title')

attrs = ['open','closed','resolved']
bar1 = [9,19,3]
bar2 = [1,26,2]

bar.add('IOS Bug Status', attrs, bar1)
bar.add('Android Bug Status', attrs, bar2, is_convert= True)

bar.show_config()
bar.render()