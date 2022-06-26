import unicodedata
import os

from logzero import logger

from ZiCutter import ZiCutter

if __name__ == "__main__":
    line = "'〇㎡[คุณจะจัดพิธีแต่งงานเมื่อไรคะัีิ์ื็ํึ]Ⅷpays-g[ran]d-blanc-élevé » (白高大夏國)😀熇'\x000𬼄"

    # build
    # cutter = ZiCutter(dir="")
    # cutter.build()

    # use
    cutter = ZiCutter(dir="")
    for c in line:
        print(cutter.cutChar(c))

"""
[I 220626 19:45:14 ZiCutter:32]   c:\code\ZiCutter\data/HeZi.txt --> loadHeZi 93330  values:1719
[I 220626 19:45:14 ZiCutter:74] ZiCutter load HeZi:93330 JiZi:1719
['#15']
['ap', '#e']
['〇']
['sq', '#d']
['le', '#t']
['th', '#i']
['th', '#u']
['th', '#n']
['th', '#n']
['th', '#a']
['th', '#n']
['th', '#t']
['th', '#k']
['th', '#n']
['th', '#i']
['th', '#g']
['th', '#i']
['th', '#e']
['th', '#o']
['th', '#k']
['th', '#u']
['th', '#u']
['th', '#a']
['th', '#u']
['th', '#e']
['th', '#a']
['th', '#e']
['th', '#k']
['th', '#g']
['th', '#i']
['th', '#a']
['th', '#i']
['th', '#a']
['th', '#t']
['th', '#i']
['th', '#i']
['th', '#t']
['th', '#e']
['th', '#u']
['th', '#t']
['th', '#e']
['ri', '#t']
['ro', '#t']
['p']
['a']
['y']
['s']
['hy', '#s']
['g']
['le', '#t']
['r']
['a']
['n']
['ri', '#t']
['d']
['hy', '#s']
['b']
['l']
['a']
['n']
['c']
['hy', '#s']
['la', '#e']
['l']
['e']
['v']
['la', '#e']
['sp', '#e']
['ri', '#k']
['sp', '#e']
['le', '#s']
['白']
['高']
['大']
['⿱', '首', '夊']
['⿴', '囗', '或']
['ri', '#s']
['gr', '#e']
['⿰', '火', '高']
['ap', '#e']

"""
