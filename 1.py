# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
# print('静夜思\n'
#  '床前明月光，\n'
#  '疑是地上霜。\n'
#  '举头望明月，\n'
#  '低头思故乡。')
# print
# '中文\n日文\n韩文'
year=[1950,1970,1990,2010]
pop=[2.519,3.692,5.263,6.972]
# plt.plot(year,pop)
# plt.show()
values=[0,0.6,1.4,1.6,2.2,2.5,2.6,3.2,3.5,3.9,4.2,6]
plt.hist(values,bins=10)
plt.show()

