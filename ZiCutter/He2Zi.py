from logzero import logger

import UnicodeTokenizer
import collections

star = '䖵'

"""
    𤍽	𤑔 k,v  异体字\t本体字
    HeZi[𤑔]=HeZi[𤍽] if 𤍽 in 𤑔
    HeZi[v]=HeZi[k] if k in v
异体字 冃	帽
    """


def valid(seq, Ji):
    for x in seq:
        if x not in Ji:
            return 0
    return 1


def split(dic0: dict, JiZi: set, YiTi: set, epoch=0):
    dic1 = {}
    for k, v in dic0.items():
        # if epoch >= 4 and star in v:
        #     logger.info((k, v))

        if valid(v, JiZi):
            dic1[k] = v
            continue

        if epoch >= 4:
            if k in YiTi:
                u = YiTi[k]
                u = dic0.get(u, u)
                if valid(u, JiZi):
                    dic1[k] = u
                    continue

        if epoch >= 5:
            u = ''.join(YiTi.get(x, x) for x in v)
            dic1[k] = u
            continue

        u = ''.join(dic0.get(x, x) for x in v)
        dic1[k] = u

    base0 = set(''.join(x for x in dic0.values()))
    base1 = set(''.join(x for x in dic1.values()))
    logger.info((f"epoch:{epoch} base:{len(base0)} --> {len(base1)} "))
    return dic1


def chai(JiZi: set, ChaiZi: list, YiTiZi: list):
    HeZi = {}
    for k, v in ChaiZi:
        if not UnicodeTokenizer.detect_hanzi(k):
            continue
        HeZi[k] = v

    for x in JiZi:
        HeZi[x] = x

    YiTi = {k: v for k, v in YiTiZi}

    dic0 = HeZi
    for i in range(8):
        dic1 = split(dic0, JiZi, YiTi, epoch=i)
        dic0 = dic1

    dic1 = {}
    giveup = []
    useless = []
    for k, v in dic0.items():
        if UnicodeTokenizer.detect_hanzi(k):
            if valid(v, JiZi):
                dic1[k] = v
            else:
                giveup.append(k)
        else:
            useless.append(k)
    giveup.sort()
    logger.info(f"giveup v:{len(giveup)} {''.join(giveup)}")
    logger.info(f"useless k:{len(useless)} {''.join(useless)}")
    return dic1


def build(JiZi, ChaiZiPath, YiTiZiPath,  HeZiPath, JiZiPath):
    JiZi = [x for x in JiZi if x]
    JiZi = set(JiZi)

    doc = open(YiTiZiPath).read().splitlines()
    YiTiZi = [x.split('\t') for x in doc]

    doc = open(ChaiZiPath).read().splitlines()
    ChaiZi = [x.split('\t') for x in doc]
    ChaiZi = [x for x in ChaiZi if UnicodeTokenizer.detect_hanzi(x[0])]

    logger.info(f"JiZi:{len(JiZi)} ChaiZi:{len(ChaiZi)} YiTiZi:{len(YiTiZi)}")
    HeZi = chai(JiZi, ChaiZi, YiTiZi)

    Base = set(''.join(x for x in HeZi.values()))
    logger.info(f"HeZi:{len(HeZi)} Base:{len(Base)} ")
    logger.info(f" useless: {len(JiZi-Base)} {''.join(JiZi-Base)} ")
    diff = Base-JiZi
    logger.info(("jizi diff", len(JiZi),  len(diff), ''.join(diff)))
    assert len(diff) == 0

    Base = list(Base)
    Base.sort()
    with open(JiZiPath, "w") as f:
        for x in Base:
            f.write(x+'\n')

    chars = list(HeZi)
    chars.sort()
    with open(HeZiPath, "w") as f:
        for x in chars:
            l = f"{x}\t{HeZi[x]}"
            f.write(l+'\n')

    logger.info(f"HeZi build success -> {HeZiPath}  {JiZiPath}")


if __name__ == "__main__":
    JiZi = open("YuanZi/YuanZi.txt").read().splitlines()
    build(JiZi, ChaiZiPath="ChaiZi/ChaiZi.txt", YiTiZiPath="YiTiZi/YiTiZi.txt",
          HeZiPath="HeZi/He2Yuan.txt", JiZiPath="HeZi/YuanZi.txt")
    JiZi = open("ChaiZi/GouJian.txt").read().splitlines()
    build(JiZi, ChaiZiPath="ChaiZi/ChaiZi.txt", YiTiZiPath="YiTiZi/YiTiZi.txt",
          HeZiPath="HeZi/He2Ji.txt", JiZiPath="HeZi/JiZi.txt")


"""
sup="候侯𢀖枭島"

[I 220717 23:34:02 He2Zi:99] JiZi:1128 ChaiZi:94235 YiTiZi:27440
[I 220717 23:34:03 He2Zi:50] epoch:0 base:10733 --> 2698 
[I 220717 23:34:04 He2Zi:50] epoch:1 base:2698 --> 1299 
[I 220717 23:34:04 He2Zi:50] epoch:2 base:1299 --> 1257 
[I 220717 23:34:05 He2Zi:50] epoch:3 base:1257 --> 1257 
[I 220717 23:34:05 He2Zi:50] epoch:4 base:1257 --> 1241 
[I 220717 23:34:06 He2Zi:50] epoch:5 base:1241 --> 1240 
[I 220717 23:34:06 He2Zi:50] epoch:6 base:1240 --> 1240 
[I 220717 23:34:07 He2Zi:50] epoch:7 base:1240 --> 1240 
[I 220717 23:34:08 He2Zi:83] giveup v:509 㕽㤙㨮㮧㯛䅮䌲䒭䖚䗼䙧䚃䡧䢢䤌以似倉傖兜凔凫卣嗆嗚嚑囙场塢壺姒娰嬝嬽岛嵢嵨愴戧扬拟拣捣搶摀旸曛杨梟槍殇汤泤溩滄炀炼烫熏熓熗燛燻爋牄獊獯玚瑦瑲畅
疡瘡矄砀笖篬篼纁练肠臐艙苡荡蒼蔸薰蘍螐螥蟂袅裊觞謒賶蹌逌鄔鄡醺鉯鎢鑂钖铴飏饧鰞鶬不女都卑既暑碑署者辶爵𠀀𠀈𠀉𠀌𠀍𠀑𠀟𠀳𠁣𠁦𠁧𠁩𠁰𠁱𠁾𠂀𠂂𠂍𠂣𠂼𠃉𠃓𠃢𠄏�𠄙𠇡𠉀𠌥𠍋𠎖𠏧𠏳𠐲𠑜𠑹𠑼𠒂𠒎𠕄𠖁��𠚒𠛖𠝎𠞆𠠈𠤬𠥃𠥐𠥻𠦁𠧠𠨝𠩳𠬫𠭬𠳎𠳧𡀮𡀴𡄀𡆢𡆵𡋬𡏭𡐝𡑩𡒝𡓕𡓽𡕏𡖣𡗒𡚇𡚎𡜏𡠄𡠿𡤂𡭳𡯁𡰣𡰴𡳿𡷊𡸁𡼻𢁹𢁺𢄓��𢉺𢊇𢋵𢌰𢍴𢎗𢎜𢎧𢎱𢏻𢜁𢞬𢣤𢦐𢦘𢮮𢳚𢷠𣀨𣀴𣅲𣋃𣌕𣎰𣒚𣘖𣘛𣝄𣢔𣤝𣤦𣥒𣦶𣪃𣫬𣯙𣴁𤀙𤂏𤋅𤏬𤐁�𤑎𤑕𤒉𤓂𤘍𤚬𤜓𤤃𤤳𤦓𤦡𤨗𤩤𤪠𤰃𤸣𤸼𥃅𥄤𥅤𥆞𥉼𥏲𥙩𥪈𥴻𥵯𥸨𥻲𥻼𦃹𦄓𦆚𦇟𦈮𦉭𦋦𦜸𦞛𦢁𦣩𦥒𦥫𦥺𦧀𦨃𦫯𦫵𦭢𦭩𦲿𦶀𦷿𦺟𦼃𧃭𧒬𧙊𧰣𧰾𧱊𧳱𧽋𧽜𨈏𨈐𨈑𨒝𨔍𨗰𨙃𨙡𨛕𨜾𨭤𨮤𨳇𨳈𨶆𨶇𨷒𨷔𨺅𨺪𩂚𩇦𩇧𩇨𩈺𩌗𩕹𩙱�𩝷𩪱𩮩𩮷𩰊𩰋𪄝𪇑𪈧𪓕𪓝𪙎𪚦𪛉𪛙𪜀𪜭𪟮𪤇𪦔𪦭𪰻𪼧𪾏𫀞𫄸𫈄𫉩𫕜𫖤𫚊𫝖𫠣𫠪𫡆𫣵𫤤𫧙𫩦𫲊𫵵𫸪𫸼𫼟𫽲𫾙𬀘𬂱𬅌��𬋢𬍡𬐂𬐠𬒃𬓸𬔎𬚤𬚭𬛹𬟝𬟾𬠊𬡧𬦅𬦏𬫤𬬡𬬢𬰌𬲰𬵈𬺷𬺻𬻆𬻒𬻘𬻴𬼂𬼄𬼘𬼺𬽡𬿠𬿿𭂄𭂛𭂸𭂺𭆴𭇩𭉅�𭋒𭌨𭔈𭔥𭖀𭖲𭙪𭚡𭜤𭞶𭟇𭣔𭣚𭥟𭨘𭬍𭬝𭬢𭭧𭭪𭮴𭯸𭱎𭱐𭱽𭲞𭲰𭳄𭳵𭴚𭴭𭵄𭸳𭺪𭾊𭾏𮅏𮍌𮍠𮎳𮒮𮓢𮖥𮗙𮚊𮛸𮠕𮡭𮭹乁㠯㨮𰀤𰅜𰆶𰑓𰒥𰓋𰗧𰙌𰝔𰤓𰧕𰨇𰰢𰲞𰷟𱁱
[I 220717 23:34:08 He2Zi:84] useless k:0
[I 220717 23:34:08 He2Zi:103] HeZi:93778 Base:1128 
[I 220717 23:34:08 He2Zi:104]  useless: 0
[I 220717 23:34:08 He2Zi:106] ('jizi diff', 1128, 0, '')
[I 220717 23:34:08 He2Zi:122] HeZi build success -> HeZi/He2Yuan.txt  HeZi/YuanZi.txt
[I 220717 23:34:08 He2Zi:99] JiZi:2365 ChaiZi:94235 YiTiZi:27440
[I 220717 23:34:09 He2Zi:50] epoch:0 base:10679 --> 3200 
[I 220717 23:34:10 He2Zi:50] epoch:1 base:3200 --> 2840 
[I 220717 23:34:10 He2Zi:50] epoch:2 base:2840 --> 2839 
[I 220717 23:34:11 He2Zi:50] epoch:3 base:2839 --> 2839 
[I 220717 23:34:11 He2Zi:50] epoch:4 base:2839 --> 2823 
[I 220717 23:34:12 He2Zi:50] epoch:5 base:2823 --> 2822 
[I 220717 23:34:12 He2Zi:50] epoch:6 base:2822 --> 2822 
[I 220717 23:34:13 He2Zi:50] epoch:7 base:2822 --> 2822 
[I 220717 23:34:13 He2Zi:83] giveup v:501 ⺁⺂⺃⺅⺇⺉⺋⺍⺎⺏⺐⺑⺒⺓⺔⺖⺗⺘⺙⺛⺜⺞⺟⺠⺡⺢⺣⺤⺥⺦⺧⺨⺩⺪⺫⺬⺭⺮⺯⺰⺱⺲⺳⺴⺵⺶⺷⺹⺺⺽⺾⺿⻀⻁⻂⻃⻄⻅⻆⻇⻈⻉⻊⻋⻌⻍⻎⻏⻐⻑⻒
⻓⻔⻕⻖⻗⻘⻙⻚⻛⻜⻝⻞⻟⻠⻡⻢⻣⻤⻥⻦⻧⻨⻩⻪⻫⻬⻭⻮⻯⻰⻱⻲⻳⼀⼁⼂⼃⼄⼅⼆⼇⼈⼉⼊⼋⼌⼍⼎⼏⼐⼑⼒⼓⼔⼕⼖⼗⼘⼙⼚⼛⼜⼝⼞⼟⼠⼡⼢⼣⼤⼥⼦⼧⼨⼩⼪⼫⼬⼭⼮⼯⼰⼱⼲⼳⼴⼵⼶⼷⼸⼹⼺ 
⼻⼼⼽⼾⼿⽀⽁⽂⽃⽄⽅⽆⽇⽈⽉⽊⽋⽌⽍⽎⽏⽐⽑⽒⽓⽔⽕⽖⽗⽘⽙⽚⽛⽜⽝⽞⽟⽠⽡⽢⽣⽤⽥⽦⽧⽨⽩⽪⽫⽬⽭⽮⽯⽰⽱⽲⽳⽴⽵⽶⽷⽸⽹⽺⽻⽼⽽⽾⽿⾀⾁⾂⾃⾄⾅⾆⾇⾈⾉⾊⾋⾌⾍⾎⾏⾐⾑⾒⾓⾔⾕⾖ 
⾗⾘⾙⾚⾛⾜⾝⾞⾟⾠⾡⾢⾣⾤⾥⾦⾧⾨⾩⾪⾫⾬⾭⾮⾯⾰⾱⾲⾳⾴⾵⾶⾷⾸⾹⾺⾻⾼⾽⾾⾿⿀⿁⿂⿃⿄⿅⿆⿇⿈⿉⿊⿋⿌⿍⿎⿏⿐⿑⿒⿓⿔⿕〇㇀㇃㇅㇆㇊㇋㇌㇍㇎㇏㇐㇑㇒㇔㇕㇖㇗㇘㇙㇚㇛㇜㇝㇞㇟㇠㇡㇢ 
㇣㐃㐆㐧㔔㪳㫈䍏乁乄书亊亪円卍卐孒孓曱女卑既碑辶爵𠀀𠀈𠀌𠀍𠀑𠀟𠁢𠁦𠁧𠁩𠁰𠁱𠁾𠂀𠂂𠂍𠂣𠂼𠃉𠃛𠃢𠄓𠄙𠑹𠒂𠕄𠖁𠙴𠝎𠤬𠥃𠥻𠦁𠩳𡆵𡋬𡗒�𡭔𡭳𡯁𡰴𡳿𢁺𢌰𢎗𢎜𢎧𢎱𢩯𢩴𢮮𣅲𣒚𣗭𣦶𣫬𣴁𤐁𤘍𤤃𤦡𤰃𤽆𥃅𥆞𥝌��𦉭𦣵𦤄𦥒𦥫𦥺𦨃𦫵𦭩𦱫𧺐𨈏𨈐𨈑𨳇𨳈𩂚𩇦𩇧𩇨𩙱𩰊𩰋𪓕𪓝𪚦𪛉𪛙𪛛𪭣𫇧𫝖𫩦𬫬𬺷𬻆𬼁𬼂𬼄𬼘𬽡𭅫𭔥𭖀𭣔𭣚𭨘𭮱𭮴��𭱽𭳄𭺪𮍠𮎳𮒮𮠕乁㠯𰁈𰑓�
[I 220717 23:34:13 He2Zi:84] useless k:8 ↔⑦↷ユ③コ？④
[I 220717 23:34:13 He2Zi:103] HeZi:93746 Base:2365 
[I 220717 23:34:13 He2Zi:104]  useless: 0
[I 220717 23:34:13 He2Zi:106] ('jizi diff', 2365, 0, '')
[I 220717 23:34:14 He2Zi:122] HeZi build success -> HeZi/He2Ji.txt  HeZi/JiZi.txt
"""
