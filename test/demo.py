import unicodedata
import os
import collections

from logzero import logger

from ZiCutter.ZiCutter import ZiCutter 

def char_name(x):
    try:
        name = unicodedata.name(x)
    except Exception as e:
        name=unicodedata.category(x)+" "+x
    return name

def test_module():
    from ZiCutter import ZiCutter

    logger.info((ZiCutter.GouJian, len(ZiCutter.GouJian)))  # 2365
    cutter=ZiCutter.ZiCutter()
    logger.info(len(cutter.vocab))  # 4399
    for i in range(0x10FFFF):
        c = chr(i)
        ts=cutter.cutToken(c)
        for x in ts:
            if x not in cutter.vocab:
                logger.error((chr(i),ts,char_name(c)))
                d=0

def test_lang(dir):
    cutter = ZiCutter(dir=dir)
    line = "'〇㎡[คุณจะจัดพิธีแต่งงานเมื่อไรคะัีิ์ื็ํึ]Ⅷpays-g[ran]d-blanc-élevé » (白高大夏國)熵😀'\x0000熇"
    logger.info(cutter.tokenize(line))


if __name__ == "__main__":
    # test_module()

    langs = ["", 'sw', 'ur', 'ar', 'en', 'fr',
             'ja', 'ru', 'zh', 'th', 'global']

    for lang in langs:
        # dir = f"C:/data/lang/{lang}"
        dir = f"C:/data/languages/{lang}"
        if not os.path.exists(dir):
            continue
        # build
        # cutter = ZiCutter(dir=dir)
        # cutter.build()
        test_lang(dir)
        # break


"""
[I 230105 00:28:29 ZiCutter:89] C:/data/languages/global\JiZi.txt load  JiZi:10508
[I 230105 00:28:29 ZiCutter:41]   C:/data/languages/global\HeZi.txt JiZi:10508 --> loadHeZi 94391  values:10508
[I 230105 00:28:29 ZiCutter:94] C:/data/languages/global\HeZi.txt HeZi:94391 values:10508
[I 230105 00:28:29 ZiCutter:97] C:/data/languages/global loaded vocab:10644
[W 230105 00:28:29 ZiCutter:100]  C:/data/languages/global building
[I 230105 00:28:29 ZiCutter:103] receive roots:0 JiZi:2401
[I 230105 00:28:29 He2Zi:98] JiZi:2401 ChaiZi:94235 YiTiZi:27440
[I 230105 00:28:30 He2Zi:49] epoch:0 base:10715 --> 3236 
[I 230105 00:28:30 He2Zi:49] epoch:1 base:3236 --> 2876 
[I 230105 00:28:30 He2Zi:49] epoch:2 base:2876 --> 2875
[I 230105 00:28:30 He2Zi:49] epoch:3 base:2875 --> 2875
[I 230105 00:28:30 He2Zi:49] epoch:4 base:2875 --> 2859
[I 230105 00:28:30 He2Zi:49] epoch:5 base:2859 --> 2858
[I 230105 00:28:31 He2Zi:49] epoch:6 base:2858 --> 2858
[I 230105 00:28:31 He2Zi:49] epoch:7 base:2858 --> 2858
[I 230105 00:28:31 He2Zi:82] giveup v:501 ⺁⺂⺃⺅⺇⺉⺋⺍⺎⺏⺐⺑⺒⺓⺔⺖⺗⺘⺙⺛⺜⺞⺟⺠⺡⺢⺣⺤⺥⺦⺧⺨⺩⺪⺫⺬⺭⺮⺯⺰⺱⺲⺳⺴⺵⺶⺷⺹⺺⺽⺾⺿⻀⻁⻂⻃⻄⻅⻆⻇⻈⻉⻊ 
⻋⻌⻍⻎⻏⻐⻑⻒⻓⻔⻕⻖⻗⻘⻙⻚⻛⻜⻝⻞⻟⻠⻡⻢⻣⻤⻥⻦⻧⻨⻩⻪⻫⻬⻭⻮⻯⻰⻱⻲⻳⼀⼁⼂⼃⼄⼅⼆⼇⼈⼉⼊⼋⼌⼍⼎⼏⼐⼑⼒⼓⼔⼕⼖⼗⼘⼙⼚⼛⼜⼝⼞⼟⼠⼡⼢⼣⼤⼥⼦⼧⼨⼩⼪ 
⼫⼬⼭⼮⼯⼰⼱⼲⼳⼴⼵⼶⼷⼸⼹⼺⼻⼼⼽⼾⼿⽀⽁⽂⽃⽄⽅⽆⽇⽈⽉⽊⽋⽌⽍⽎⽏⽐⽑⽒⽓⽔⽕⽖⽗⽘⽙⽚⽛⽜⽝⽞⽟⽠⽡⽢⽣⽤⽥⽦⽧⽨⽩⽪⽫⽬⽭⽮⽯⽰⽱⽲⽳⽴⽵⽶⽷⽸⽹⽺⽻⽼⽽⽾ 
⽿⾀⾁⾂⾃⾄⾅⾆⾇⾈⾉⾊⾋⾌⾍⾎⾏⾐⾑⾒⾓⾔⾕⾖⾗⾘⾙⾚⾛⾜⾝⾞⾟⾠⾡⾢⾣⾤⾥⾦⾧⾨⾩⾪⾫⾬⾭⾮⾯⾰⾱⾲⾳⾴⾵⾶⾷⾸⾹⾺⾻⾼⾽⾾⾿⿀⿁⿂⿃⿄⿅⿆⿇⿈⿉⿊⿋⿌⿍⿎⿏⿐⿑⿒ 
⿓⿔⿕〇㇀㇃㇅㇆㇊㇋㇌㇍㇎㇏㇐㇑㇒㇔㇕㇖㇗㇘㇙㇚㇛㇜㇝㇞㇟㇠㇡㇢㇣㐃㐆㐧㔔㪳㫈䍏乁乄书亊亪円卍卐孒孓曱女卑既碑辶爵𠀀𠀈𠀌𠀍𠀑𠀟𠁢𠁦𠁧𠁩𠁰𠁱𠁾𠂀𠂂𠂍𠂣𠂼𠃉𠃛𠃢�𠄙𠑹𠒂𠕄𠖁��𠝎𠤬𠥃𠥻𠦁𠩳𡆵𡋬𡗒𡜏𡭔𡭳𡯁𡰴𡳿𢁺𢌰𢎗𢎜𢎧𢎱𢩯𢩴𢮮𣅲𣒚𣗭𣦶𣫬𣴁𤐁𤘍𤤃𤦡𤰃𤽆𥃅𥆞𥝌𥸨𦉭𦣵𦤄𦥒𦥫𦥺𦨃𦫵𦭩��𧺐𨈏𨈐𨈑𨳇𨳈𩂚𩇦𩇧𩇨𩙱𩰊𩰋𪓕𪓝𪚦𪛉𪛙𪛛𪭣𫇧𫝖𫩦𬫬𬺷𬻆𬼁𬼂𬼄𬼘𬽡𭅫𭔥𭖀�𭣔𭣚𭨘𭮱𭮴𭱐𭱽𭳄𭺪𮍠𮎳𮒮𮠕乁㠯𰁈𰑓
[I 230105 00:28:31 He2Zi:83] useless k:41 szt9xq↷nl6r1bivmk72d38ycue↔g④o0⑦5③fhw4paj
[I 230105 00:28:31 He2Zi:102] HeZi:93749 Base:2365
[I 230105 00:28:31 He2Zi:103]  useless: 36 lkvh5uyt6mqp2zr8109wxdce4o37bgnijsaf
[I 230105 00:28:31 He2Zi:105] ('jizi diff', 2401, 0, '')
[I 230105 00:28:31 He2Zi:121] HeZi build success -> C:/data/languages/global\HeZi.txt  C:/data/languages/global\JiZi.txt
[I 230105 00:28:31 ZiCutter:89] C:/data/languages/global\JiZi.txt load  JiZi:2365
[I 230105 00:28:31 ZiCutter:41]   C:/data/languages/global\HeZi.txt JiZi:2365 --> loadHeZi 93749  values:2365
[I 230105 00:28:31 ZiCutter:94] C:/data/languages/global\HeZi.txt HeZi:93749 values:2365
[I 230105 00:28:31 ZiCutter:97] C:/data/languages/global loaded vocab:2501
[I 230105 00:28:31 ZiCutter:89] C:/data/languages/global\JiZi.txt load  JiZi:2365
[I 230105 00:28:31 ZiCutter:41]   C:/data/languages/global\HeZi.txt JiZi:2365 --> loadHeZi 93749  values:2365
[I 230105 00:28:31 ZiCutter:94] C:/data/languages/global\HeZi.txt HeZi:93749 values:2365
[I 230105 00:28:31 ZiCutter:97] C:/data/languages/global loaded vocab:2501
[I 230105 00:28:31 demo:114] ['##15', '##39', '##95', '##17', '##91', '##88', '##40', '##3', '##92', '##32', '##92', '##33', '##4', '##14', '##36', '##8', '##37', '##49', '##5', '##56', '##91', '##91', '##34', '##9', '##48', '##17', '##39', '##56', '##29', '##52', '##19', '##88', '##32', '##33', '##37', '##36', '##60', '##39', '##55', '##61', '##38', '##93', '##51', 'p', 'a', 'y', 's', '##45', 'g', '##91', 'r', 'a', 'n', '##93', 'd', '##45', 'b', 'l', 'a', 'n', 'c', '##45', '##33', 'l', 'e', 'v', '##33', '##32', '##87', '##32', '##40', '白', '高', '大', '夏', '國', '##41', '⿰', '火', '商', '##12', '##39', '##0', '0', '0', '⿰', '火', '高']
"""
