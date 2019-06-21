Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import matplotlib.pyplot as plt
>>> import numpy as np
>>> x = np.arange(10,100,5)
>>> len(x)
18
>>> y = x ** 2
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x00000209B900DFD0>]
>>> plt.show()
>>> x = np.array([-5,-4,-3,-2,-1,0,1,2,3,4,5])
>>> y = x**2
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x00000209BAAA64A8>]
>>> plt.show()
>>> x = np.random.randint(10,1000,50)
>>> y = np.random.randint(10,1000,50)
>>> len(y)
50
>>> x = np.arange(1,101,2)
>>> len(x)
50
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x00000209BAC3CD68>]
>>> plt.show()
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x00000209BAB057F0>]
>>> plt.show()
>>> plt.plot(x,y,'o')
[<matplotlib.lines.Line2D object at 0x00000209BAB5F550>]
>>> plt.show()
>>> y = np.linspace(20,200)
>>> len(y)
50
>>> plt.plot(x,y,'o')
[<matplotlib.lines.Line2D object at 0x00000209BABB9358>]
>>> plt.show()
>>> x = np.array([350,120,30,44])
>>> label = np.array(['BJP','Cong','SP+BSP','Others'])
>>> plt.pie(x,label)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    plt.pie(x,label)
  File "C:\Python37\lib\site-packages\matplotlib\pyplot.py", line 2805, in pie
    data is not None else {}))
  File "C:\Python37\lib\site-packages\matplotlib\__init__.py", line 1810, in inner
    return func(ax, *args, **kwargs)
  File "C:\Python37\lib\site-packages\matplotlib\axes\_axes.py", line 2848, in pie
    x += expl * math.cos(thetam)
TypeError: can't multiply sequence by non-int of type 'float'
>>> plt.pie(x,labels=label)
([<matplotlib.patches.Wedge object at 0x00000209BB1A44A8>, <matplotlib.patches.Wedge object at 0x00000209BB1A4A20>, <matplotlib.patches.Wedge object at 0x00000209BB1A4F60>, <matplotlib.patches.Wedge object at 0x00000209BB28D4E0>], [Text(-0.4789067718142159, 0.9902768824477762, 'BJP'), Text(0.025407808006599936, -1.0997065259842282, 'Cong'), Text(0.8543273560182371, -0.6929103612725737, 'SP+BSP'), Text(1.0646791179350081, -0.2765110772340467, 'Others')])
>>> plt.show()
>>> plt.pie(x,labels=label,startangle=90)
([<matplotlib.patches.Wedge object at 0x00000209BB056780>, <matplotlib.patches.Wedge object at 0x00000209BB056D30>, <matplotlib.patches.Wedge object at 0x00000209BB0602B0>, <matplotlib.patches.Wedge object at 0x00000209BB0607F0>], [Text(-0.9902768824477762, -0.47890677181421587, 'BJP'), Text(1.0997065259842282, 0.025407808006599867, 'Cong'), Text(0.6929103612725737, 0.8543273560182371, 'SP+BSP'), Text(0.27651107723404683, 1.0646791179350081, 'Others')])
>>> plt.show()
>>> plt.pie(x,labels=label,startangle=90,autopct='%1.1f%%')
([<matplotlib.patches.Wedge object at 0x00000209BB094DD8>, <matplotlib.patches.Wedge object at 0x00000209BB09F5F8>, <matplotlib.patches.Wedge object at 0x00000209BB09FD68>, <matplotlib.patches.Wedge object at 0x00000209BB0A6518>], [Text(-0.9902768824477762, -0.47890677181421587, 'BJP'), Text(1.0997065259842282, 0.025407808006599867, 'Cong'), Text(0.6929103612725737, 0.8543273560182371, 'SP+BSP'), Text(0.27651107723404683, 1.0646791179350081, 'Others')], [Text(-0.5401510267896961, -0.2612218755350268, '64.3%'), Text(0.5998399232641244, 0.013858804367236289, '22.1%'), Text(0.3779511061486765, 0.46599673964631105, '5.5%'), Text(0.1508242239458437, 0.5807340643281862, '8.1%')])
>>> plt.show()
>>> plt.pie(x,labels=label,startangle=90,autopct='%1.2f%%')
([<matplotlib.patches.Wedge object at 0x00000209BB298F60>, <matplotlib.patches.Wedge object at 0x00000209BB298978>, <matplotlib.patches.Wedge object at 0x00000209BABB07B8>, <matplotlib.patches.Wedge object at 0x00000209BABB0F60>], [Text(-0.9902768824477762, -0.47890677181421587, 'BJP'), Text(1.0997065259842282, 0.025407808006599867, 'Cong'), Text(0.6929103612725737, 0.8543273560182371, 'SP+BSP'), Text(0.27651107723404683, 1.0646791179350081, 'Others')], [Text(-0.5401510267896961, -0.2612218755350268, '64.34%'), Text(0.5998399232641244, 0.013858804367236289, '22.06%'), Text(0.3779511061486765, 0.46599673964631105, '5.51%'), Text(0.1508242239458437, 0.5807340643281862, '8.09%')])
>>> plt.show()
>>> plt.pie(x,labels=label,startangle=90,autopct='%1.2f%%',shadow = True)
([<matplotlib.patches.Wedge object at 0x00000209BAB83AC8>, <matplotlib.patches.Wedge object at 0x00000209BAB6AE48>, <matplotlib.patches.Wedge object at 0x00000209BAB78CC0>, <matplotlib.patches.Wedge object at 0x00000209BAB715C0>], [Text(-0.9902768824477762, -0.47890677181421587, 'BJP'), Text(1.0997065259842282, 0.025407808006599867, 'Cong'), Text(0.6929103612725737, 0.8543273560182371, 'SP+BSP'), Text(0.27651107723404683, 1.0646791179350081, 'Others')], [Text(-0.5401510267896961, -0.2612218755350268, '64.34%'), Text(0.5998399232641244, 0.013858804367236289, '22.06%'), Text(0.3779511061486765, 0.46599673964631105, '5.51%'), Text(0.1508242239458437, 0.5807340643281862, '8.09%')])
>>> plt.show()
>>> plt.pie(x,labels=label,startangle=90,autopct='%1.2f%%',shadow = True,explode=[0,0.2,0,0])
([<matplotlib.patches.Wedge object at 0x00000209BAC44710>, <matplotlib.patches.Wedge object at 0x00000209BAC443C8>, <matplotlib.patches.Wedge object at 0x00000209BADC37F0>, <matplotlib.patches.Wedge object at 0x00000209BADB0898>], [Text(-0.9902768824477762, -0.47890677181421587, 'BJP'), Text(1.2996531670722697, 0.0300274094623453, 'Cong'), Text(0.6929103612725737, 0.8543273560182371, 'SP+BSP'), Text(0.27651107723404683, 1.0646791179350081, 'Others')], [Text(-0.5401510267896961, -0.2612218755350268, '64.34%'), Text(0.7997865643521659, 0.01847840582298172, '22.06%'), Text(0.3779511061486765, 0.46599673964631105, '5.51%'), Text(0.1508242239458437, 0.5807340643281862, '8.09%')])
>>> plt.show()
>>> plt.pie(x,labels=label,startangle=90,autopct='%1.2f%%',shadow = True,explode=[0,0,0,0.2])
([<matplotlib.patches.Wedge object at 0x00000209B901AB00>, <matplotlib.patches.Wedge object at 0x00000209B6C10048>, <matplotlib.patches.Wedge object at 0x00000209B6C107F0>, <matplotlib.patches.Wedge object at 0x00000209B6C1EBA8>], [Text(-0.9902768824477762, -0.47890677181421587, 'BJP'), Text(1.0997065259842282, 0.025407808006599867, 'Cong'), Text(0.6929103612725737, 0.8543273560182371, 'SP+BSP'), Text(0.3267858185493281, 1.2582571393777369, 'Others')], [Text(-0.5401510267896961, -0.2612218755350268, '64.34%'), Text(0.5998399232641244, 0.013858804367236289, '22.06%'), Text(0.3779511061486765, 0.46599673964631105, '5.51%'), Text(0.20109896526112492, 0.7743120857709149, '8.09%')])
>>> plt.show()
>>> 
