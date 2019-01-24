from pyecharts import Bar
bar = Bar('title', 'sub-title')

attrs = ['open','closed','resolved']
bar1 = [9,19,3]
bar2 = [1,26,2]

bar.add('IOS Bug Status', attrs, bar1, is_stack= True)  #if remove is_stack= True then the two bar is seperate
bar.add('Android Bug Status', attrs, bar2, is_stack= True)

bar.show_config()
bar.render()