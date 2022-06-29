import unicodedata
import os

from logzero import logger

from ZiCutter.ZiCutter import ZiCutter

import pkg_resources

# print(pkg_resources.resource_stream('ZiCutter', '*ChaiZi.txt'))
# print(pkg_resources.resource_filename('ZiCutter', '*ChaiZi.txt'))

if __name__ == "__main__":
    line = "'〇㎡[คุณจะจัดพิธีแต่งงานเมื่อไรคะัีิ์ื็ํึ]Ⅷpays-g[ran]d-blanc-élevé » (白高大夏國)😀熇'\x000𬼄"
    # cutter = ZiCutter(dir="")
    # for c in line:
    #     print(cutter.cutChar(c))

    # build
    cutter = ZiCutter(dir="")
    cutter.build()

    # use
    cutter = ZiCutter(dir="")
    for c in line:
        print(c, cutter.cutChar(c))

"""
[I 220629 20:52:42 ZiCutter:99] C:\ProgramData\Miniconda3\lib\site-packages\ZiCutter\HanZi\JiZi.txt load  JiZi:1719
[I 220629 20:52:43 ZiCutter:56]   C:\ProgramData\Miniconda3\lib\site-packages\ZiCutter\HanZi\HeZi.txt JiZi:3727 --> loadHeZi 92463  values:1041
[I 220629 20:52:43 ZiCutter:103] C:\ProgramData\Miniconda3\lib\site-packages\ZiCutter\HanZi\HeZi.txt HeZi:92463 values:1041
[I 220629 20:52:43 ZiCutter:106] vocab:3727
[I 220629 20:52:43 ZiCutter:111]  C:\ProgramData\Miniconda3\lib\site-packages\ZiCutter\HanZi building
[I 220629 20:52:43 He2Zi:122] JiZi:1755 ChaiZi:94235 YiTiZi:27440
[I 220629 20:52:46 He2Zi:70] epoch:0 base:11264 --> 3216 
[I 220629 20:52:46 He2Zi:70] epoch:1 base:3216 --> 1959 
[I 220629 20:52:47 He2Zi:70] epoch:2 base:1959 --> 1944 
[I 220629 20:52:47 He2Zi:70] epoch:3 base:1944 --> 1944 
[I 220629 20:52:48 He2Zi:70] epoch:4 base:1944 --> 1837 
[I 220629 20:52:48 He2Zi:70] epoch:5 base:1837 --> 1829 
[I 220629 20:52:49 He2Zi:70] epoch:6 base:1829 --> 1828 
[I 220629 20:52:49 He2Zi:70] epoch:7 base:1828 --> 1828 
[I 220629 20:52:50 He2Zi:104] giveup:246 㢿㤙㬋㮢㯛䂉䒭䗔䙈䞀䫛䳧侯候凫叏喉囙堠壺嬝嬽岛島帿捣搗枭梟槝猴瘊睺篌糇緱缑翭葔蟂袅裊鄇鄡鍭餱鯸不女﨩爵𠄏𠇡𠉀𠋫𠍋𠎖𠐲𠑼𠒎𠖁𠗦𠝷𠩳
𠪕𠬫𠳧𡀮𡆢𡋬𡏭𡐝𡑩𡕏𡖣𡗁𡙞𡚇𡟑𡠿𡭳𡷊𡹵𡻅𢆴𢇭𢉺𢉻𢊇𢋵𢍴𢏻𢜵𢦘𢰡𢳚𣀨𣀴𣘖𣚝𣝄𣣠𣤝𣤼𣥒𣹋𣻴𤂏𤆿𤒉𤜓𤟨𤠣𤡔𤤏𤧝𤬈𥀃𥅤𥉼𥛪𥦪𥧻𥱌𦃭𦃺𦆚𦑤𦔗𦚀𦞈𦣩𦥢𦬝𦮙𦳓𦺟𧃭𧇹𧐳𧒬𧙊𧩨𧯁𧱊𧳱𨁳𨄭�𨝧𨥻𨬀𨭤𨺅𩃺𩋴𩌖𩓆𩘋𩡧𩤷𩩵𩺟𪃶𪅺𪈱𪑻𪜭𪵕𪹍𫋇𫌈𫑃𫗯𫛺𫮖𫸪𫽐𫽲𬀘𬂔𬅌𬇼𬋢𬑟𬔨𬥽𬫺𬬢𬭤𬵈𬻑𬻘𬻞𬻥𭁐𭄩𭆴��𭏑𭏒𭒭𭔥𭖀𭖲𭗃𭚡𭜤𭥟𭬍𭬢𭭧𭮴𭱃𭱎𭱐𭱽𭲞𭲰𭵄𮅏𮌧𮍇𮎳𮒮𮓢𮗙𮚊𮡭𮬁𮭹乁凵�㠯㨮𥚚𰅜𰒥𰙌𰜬𰨇𰲞𰳞𰷾𰻮𱈄
[I 220629 20:52:50 He2Zi:105] useless:38 g6�3qujvoanwfhzisrチlk2195tpex47mdy8c0b
[I 220629 20:52:50 He2Zi:128] HeZi:94180 Base:1717 
[I 220629 20:52:50 He2Zi:129]  useless:rm8p9e1qvjncgua3y54h6xkt02チb�wsfl7odiz
[I 220629 20:52:50 He2Zi:131] (1755, 0)
[I 220629 20:52:50 He2Zi:132]
[I 220629 20:52:50 He2Zi:148] HeZi build success -> C:\ProgramData\Miniconda3\lib\site-packages\ZiCutter\HanZi\HeZi.txt  C:\ProgramData\Miniconda3\lib\site-packages\ZiCutter\HanZi\JiZi.txt
[I 220629 20:52:50 ZiCutter:99] C:\ProgramData\Miniconda3\lib\site-packages\ZiCutter\HanZi\JiZi.txt load  JiZi:1719
[I 220629 20:52:50 ZiCutter:56]   C:\ProgramData\Miniconda3\lib\site-packages\ZiCutter\HanZi\HeZi.txt JiZi:1755 --> loadHeZi 92463  values:1041
[I 220629 20:52:50 ZiCutter:103] C:\ProgramData\Miniconda3\lib\site-packages\ZiCutter\HanZi\HeZi.txt HeZi:92463 values:1041
[I 220629 20:52:50 ZiCutter:106] vocab:1755
[I 220629 20:52:50 ZiCutter:99] C:\ProgramData\Miniconda3\lib\site-packages\ZiCutter\HanZi\JiZi.txt load  JiZi:1719
[I 220629 20:52:51 ZiCutter:56]   C:\ProgramData\Miniconda3\lib\site-packages\ZiCutter\HanZi\HeZi.txt JiZi:3727 --> loadHeZi 92463  values:1041
[I 220629 20:52:51 ZiCutter:103] C:\ProgramData\Miniconda3\lib\site-packages\ZiCutter\HanZi\HeZi.txt HeZi:92463 values:1041
[I 220629 20:52:51 ZiCutter:106] vocab:3727
 ['#co', '15']
' ['#ap', 'he']
〇 ['〇']
㎡ ['#sq', 'ed']
[ ['#le', 'et']
ค ['#th', 'ai']
ุ ['#th', 'u']
ณ ['#th', 'en']
จ ['#th', 'an']
ะ ['#th', 'a']
จ ['#th', 'an']
ั ['#th', 'at']
ด ['#th', 'ek']
พ ['#th', 'an']
ิ ['#th', 'i']
ธ ['#th', 'ng']
ี ['#th', 'ii']
แ ['#th', 'ae']
ต ['#th', 'ao']
่ ['#th', 'ek']
ง ['#th', 'gu']
ง ['#th', 'gu']
า ['#th', 'aa']
น ['#th', 'nu']
เ ['#th', 'e']
ม ['#th', 'ma']
ื ['#th', 'ee']
่ ['#th', 'ek']
อ ['#th', 'ng']
ไ ['#th', 'ai']
ร ['#th', 'ua']
ค ['#th', 'ai']
ะ ['#th', 'a']
ั ['#th', 'at']
ี ['#th', 'ii']
ิ ['#th', 'i']
์ ['#th', 'at']
ื ['#th', 'ee']
็ ['#th', 'hu']
ํ ['#th', 'it']
ึ ['#th', 'ue']
] ['#ri', 'et']
Ⅷ ['#ro', 'ht']
p ['p']
a ['a']
y ['y']
s ['s']
- ['#hy', 'us']
g ['g']
[ ['#le', 'et']
r ['r']
a ['a']
n ['n']
] ['#ri', 'et']
d ['d']
- ['#hy', 'us']
b ['b']
l ['l']
a ['a']
n ['n']
c ['c']
- ['#hy', 'us']
é ['#la', 'te']
l ['l']
e ['e']
v ['v']
é ['#la', 'te']
  ['#sp', 'ce']
» ['#ri', 'rk']
  ['#sp', 'ce']
( ['#le', 'is']
白 ['白']
高 ['高']
大 ['大']
夏 ['⿱', '一', '夊']
國 ['⿴', '囗', '或']
) ['#ri', 'is']
😀 ['#gr', 'ce']
熇 ['⿰', '火', '高']
' ['#ap', 'he']
 ['#cc', '00']
0 ['0']
𬼄 ['𬼄']
"""
