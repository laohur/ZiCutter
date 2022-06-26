from logzero import logger

star = '閵'

"""
    𤍽	𤑔 k,v  异体字\t本体字
    HeZi[𤑔]=HeZi[𤍽] if 𤍽 in 𤑔
    HeZi[v]=HeZi[k] if k in v
    """


def split(dic0, JiZi, YiTi, epoch=0):
    giveup = set()
    dic1 = {}
    for k, v in dic0.items():
        if k == star:
            d = 0
        if k in giveup:
            continue
        if v in JiZi:
            dic1[k] = v
            continue
        u = ''
        for x in v:
            w = dic0[x]
            if w not in JiZi:
                w = YiTi.get(w, w)
                if epoch >= 5:
                    giveup.add(k)
                    # logger.info((k, v))
            u += w.strip()
        dic1[k] = u
        for x in giveup:
            if x in dic1:
                del dic1[x]
    logger.info(f"giveup:{len(giveup)} {''.join(giveup)}")
    base0 = set(''.join(x for x in dic0.values()))
    base1 = set(''.join(x for x in dic1.values()))
    logger.info((f"epoch:{epoch} base:{len(base0)} --> {len(base1)} "))
    return dic1


def chai(JiZi: set, ChaiZi: list, YiTiZi: list):
    HeZi = {k: v for k, v in ChaiZi}
    for x in JiZi:
        HeZi[x] = x

    YiTi = {}
    for k, v in YiTiZi:
        if k == star:
            d = 0  # '帽'  层次拆字 新构件
        if k in JiZi and v in JiZi:
            continue
        if k in JiZi and v not in JiZi:
            k = v
        YiTi[k] = v

    for k, v in YiTi.items():
        if v not in HeZi:  # v罕见
            k, v = v, k
        if v not in HeZi:  # v罕见
            logger.warning((k, v))
            continue
        if k in JiZi:
            continue
        if k in HeZi[v]:  # 更细
            HeZi[v] = HeZi[k]
        if v in HeZi:
            # if k < v:
            # logger.warning((k, v))
            HeZi[k] = HeZi[v]
        elif k in HeZi:  # None
            # logger.info((k, v)
            continue

    dic0 = {k: v for k, v in HeZi.items() if k and v}

    for i in range(8):
        dic1 = split(dic0, JiZi, YiTi, epoch=i)
        dic0 = dic1

    dic0 = {k: v for k, v in dic0.items() if k and v}
    return dic0


def build(JiZi, ChaiZiPath, YiTiZiPath,  HeZiPath, JiZiPath):
    JiZi = [x for x in JiZi if x]
    JiZi = set(JiZi)

    doc = open(YiTiZiPath).read().splitlines()
    YiTiZi = [x.split('\t') for x in doc]

    doc = open(ChaiZiPath).read().splitlines()
    ChaiZi = [x.split('\t') for x in doc]

    HeZi = chai(JiZi, ChaiZi, YiTiZi)

    Base = set(''.join(x for x in HeZi.values()))

    logger.info(''.join(Base-JiZi))  #
    assert len(set(Base)-JiZi) == 0

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


if __name__ == "__main__":
    # JiZi = open("YuanZi/YuanZi.txt").read().splitlines()
    # build(JiZi, ChaiZiPath="ChaiZi/ChaiZi.txt", YiTiZiPath="YiTiZi/YiTiZi.txt",
    #       HeZiPath="HeZi/He2Yuan.txt", JiZiPath="HeZi/YuanZi.txt")
    JiZi = open("JiZi/JiZi.txt").read().splitlines()
    build(JiZi, ChaiZiPath="ChaiZi/ChaiZi.txt", YiTiZiPath="YiTiZi/YiTiZi.txt",
          HeZiPath="HeZi/He2Ji.txt", JiZiPath="HeZi/JiZi.txt")


"""
[I 220626 18:07:04 HeZi:36] giveup:0 
[I 220626 18:07:05 HeZi:39] epoch:0 base:8204 --> 2611 
[I 220626 18:07:05 HeZi:36] giveup:0 
[I 220626 18:07:06 HeZi:39] epoch:1 base:2611 --> 1774 
[I 220626 18:07:06 HeZi:36] giveup:0 
[I 220626 18:07:07 HeZi:39] epoch:2 base:1774 --> 1760 
[I 220626 18:07:07 HeZi:36] giveup:0 
[I 220626 18:07:08 HeZi:39] epoch:3 base:1760 --> 1760 
[I 220626 18:07:08 HeZi:36] giveup:0 
[I 220626 18:07:09 HeZi:39] epoch:4 base:1760 --> 1760 
[I 220626 18:07:19 HeZi:36] giveup:1139 丝鎢𢶈𭱐𫘙䲷𣔺䃀𪒜癛𡥂𦼯𫲃𫺆↷𬄒𤈂𫑚𧠊𢅦𫞼𧝥𰧿𤽪憓𣐦𪞕𩐯𡺑𮇭鄢𠳲𪷤䙊𮓢艜媢ℓ𛂦𥲭赗𩃅𫿝𫸀㒿𩜝𬅅𮢇𠕮𣻴�𬄜㯊㯊𢯫𬐑𭎯挔𦡣𥝩𨜑𢲄𧂘𨪇𠅤𭻋
𱈯𦊯𩉾𭁐𠝉𦡿壺壺𢻀𡚇䡧𭱎韀𡖠𧠁𬑓𬻘𭭘𢈺𨚲𦇵𦦰𧮉𭦁𰟀嘕𧃹𰬢㒽𡜌廩𫸪𭵄𣥋𣆱𱀠𡬜冃𢯾𤓟𬻞𰯳𫮖蔺澟鞯梟𮣨𫦲𬟠寭𬔨𭡣𦻺凜𩏇拵𤲱𧘧壷壷𰭍懍蔫𢋕𨘬𭣪𧡉嶋㴘𡅁𡖪𮒿𥋶蝐𡠿𥕧鳬𥾳䉮凜𢤅𧷄蝃 
𮡭𰅻缎𢺬𢮴帽鷨𨀔𩎰𪈽𤣽㼮﨩𣓝𩎇𫩊𮑩閵𢀤𢀮𦺟𭊰𭸛𢥁裊韢𣷑𧞡𧆕𬊥𦼇𨘄𩤣熓鍛𡜒㐭𬻥𦍖𨒢璤冐紪𡉈⑭㯂塢𨎺𮜩葮𬻑𡈌𭻝萺𣖺𭐣傿𠪅𡜈𰂿漹咝𤚶𫒿𭪚归𠓶㭚𠰟𦠜𬹢𠆋𡪍𫒯𢞬𠕙𮔇𠅂㠀𡿢滯𧷧⑬䦄㪞�𡾭淒淒𣌰𨶇在𨽅𬬢𮯆𰊎䅿𭲞𩏚②𠰡慸𣶀塅鴵𢾟𬷶𭘲𭬍𰂶𬚦𥮂郻蹛𤾏㒾段𢤔𬘄𪬢𦪴𨩷𧚇𭐥𣑊嬅𣸼𣺏𩥜𠻭𮚐𡩼懔躪𣑛茬𮃞𤡔𮜟𪛃𩾒𪊩𥩴𣟊𩈺⑲𰨇𨀬𬒛𦀩𩌵𩝷𦆉𪂗𧋍𣟦存𰻮𤀙𬜻𠱽𫂠𠘅𢋴𭣨𥢁𠌥𭣞𧄟⑯𦑐𭙧�
𨉨𭱽𨺣㒻𫚘㸑㸑𡙪𠭂勗𬻱𥠠㒟稟𫑀𰲞𤂶岛燷㒻嶌𤴟𧂶顲𥤂𠘡𡠹𥚕𫖛⑦𩀵𤜓𨒸𭼪𦋓𣺙𮗙𧟺𠰇𭏬𰰏𭲳㵯𫪮𫴢年𫚃𥣼𭣕𤑇𠗩𣗫𣿆𦯤𦷊𨺔𫭣𡷊䌯䌯𡯼𤎄𤕦㥼嶹鶈𬯶𡽼𠘟𢭏①燣𢝌悽𭩟𩌮㫯𬃅扗𪞌𠕥𫡿螮𭀣⑪  
䧥𠉯𢳃𣻥𠩯𧅍𠡘𦇅𠦽𡐝𣻉𫶇𭩲𮃦𬵪𨓂𡭳𫃅𣯀𤓥𩾖𠆿𠌵𭔥𬊷鳳躙冕𠌚𫋇𢞨𠛆𠲁嘩鄥𩦫𬀼𠱜𨳀ヨ𤃢𫝵𮅏𨗍橞𥇳𤍾𥑯𡣣𩍽𭂛轥𠬷𦪷朂螐鏸𠒎𠬎蟂𦇩𭓁𢷬𣏱𦢵𦨧𢇭𩖋緞𨏦𩋾𢊬䃵𢶑袸𪜥𰸛鰞𠏵𦽹𩌴遰𫤵𢞯�蕙蕙嗚𮇓𭳛𭺺爨㮧𦣽臶褄鸶𤾤𱈝䗖𠆜𨶄疄𢂣𠀪𤨃𥜘𪉊𪽜𭤋𮩭𤒐𬂋袅帽𩐲𰏕𰿟珔𧋃華𦣩𭆴𡗋𨎹𮎳䠠𠐫𤲰𦗉𨩩䢜𮕋𭻊𠏶𨜇𠁑𫆯𭲰𪋴𮡪𢄩𤂃𬋢𥛸䗡䗡𨭤𫱮㟆𭇢𤑎𦮵𩕤鳧𭔌煅𡄁𥭿𬋅𠨦𪦋𦂔𫔴冕枭𡚖𬪙𨶱 
𰺣䑵槝𣧺𨰔恵𰬸樺㦊搗𥉼𩏲𭽂𣞦𦾛𩻮𩾣𭶂𧒬𦣵銌𧛕𭳩𦀒𠆗𣱭𮑨𫺄𣪃𦖶コ𰔇褭𣄒𦼹𬤝𦷠𢢐𨗼𰏼𫟁𡠄焉𨱸𰑵𦻇𫿣毷萋𨆴𡻅𩿋𬆸𨄛𩋋𠽠爨𠋐𡻺躏𫓓𭵹𰥡𫄍𨏼穟？𣓍𭜤潓𡩝𦎮廪𧴇𤳩𢊣癝𡙞妻㺺𧑺𭌾𨣄𭀥
𠀄𭵈𪯜冒𡫛壈𰾶𬼗𩎶嫋霋𥒛帴𬡇𰐣△𤲈瞱鷍④𤒹𡟼𢋏锻𨬋𩮟𪵕𬰶𬇵廗𠙒𰒥繐⑧凄𭄐𢳚𠌶𰜊𡫌華𥗗𩌗𩕴𫳖𧁁𫑃𰍏𡝣𡄉𦾰𥩷𥛵𧵿𧽞𪗍𦦺�𩇆𫭇噝噝𫞌𪳦𭙙𫷀𰘀𫌈𪪨禀烏𭆩𰒒寡𫨬𤎭𫖤𰁿𨫍㨶㯛𡑩𡅓𡋬𩸸𪥼 
𣐩𠬣⑥𣭌𬅌𭱩𠕚𫋂𤒢𪱇𭚐𮧵𦶀𪣋𥨗𭭧𭤪𡚣𡓔𨽖𨏸𪼚𬾹𦦾𨺽𫉿穗𫸼𭦢絻㦅𧽋𢽢𤶐𣦨𫹲𰡹譓い𫑾𬺡サ崼𤴘𭸯𤏑𧦮𥄽𤫃𪠈𠏟藺𧑍𭈭冔𠂶𭖘𭮴嵨𭅍𢡘侟𧿗𢵴冑𬟏𨞶𪟥𡉠𥤆懘𫰡𢊇𫏦熶𢁎𠥖𧎚𡜛𪎐𢉺𭳘椛𮭹り
𫂵𠆖𪦭𭫿縀𤔞𤸼䙚𤺡𦪠𢷍𧷃𮔙䮉𨮍𢄓碫𣢔𭮖毈𦇠𫑴岿𫄊𠎖𭾊𭁟⑫𠎑𰲟𡀫𪲒𭞛郪𣹂𠡼𰬜𠘐𤉐𪟊⑩𠩿𠪕𠕖𦳓𤈊𠩻𡇾𫲉𥻼𠆣𡀮㡌𫉩𬩞𰸚𧂽𦋤𦰌𢊸𢺫⑤𥕠𧜵𨿩𬋡𭞕𪥀𡹙𫅞𭇩惠𡝽𤊻𢅊𤥥𨔕𫆵𬟘𩾓𡀀𣎋㠡𫅆𡈘𣴁
𮋍𰧬隯嵽𥍙𦘎殢𮞅𤞐𢏻𦾏峌𠕬𢞻捣椴𧱊瑁䕲𡫎摕𣹋𤢤𫨻𢶸㱭冒𤌰𥈨𮒮𰌬𡻜隝𦾓𫌿𤊳𢋱𭼾檁𤆡𩆐𭩩島𨞴𮘥韡檩𧓂⑮𭬢棲㠏㱕𠆡𩂲㥣銯⑨緀𭆱巋𭖸帶𣘖𭡈𦔀𢷭蟪𪷺焨𨓼𦛊𦅠𧡕𩽃𣍫𦵍𬝂𭖲㜵䳋𤪧勖𢁤𭲀�𢛡𤏷凛凛𫏗𪃑𪦂𣝄𨺜𢧝𦅵𠞆𪦾𡼄𩏧𬟉𤇟𫛓𠓮𮄣𡃦𡚅僡譁𬸴溩𫦱𭸞𮔒擣𩎂𩏬𩛖𬿻𮔰𣤝瑖𡒄𭚡篶𦽏澕よ𤯑𨖮𣸰𤁜𣧱𮣝賵𢴶𭥟𮚊𦆚𫽲藺𣚝𨟏𢸣𨺆栫𧕔𡹭煅𢨖𢰂𫲳𠵄洊𰄕③α𠕦𰜬𠈚𭽁𭌨𬀘嫣鄡𢤺𦿬𣩙𰖩𠍩↔�
𬗋腶腶𫽐𮕹𩃊𥛣𫴘𭴺𢙮㛿𢤭𰏓𭻟𢽵𪲪𤋛𭽶𬚭𡏭嬽蹸𬒢𮔜𦂰𧬽𧟾𰼾𥠌凫艒𭗃𪄝𤑖𩼤𮓠𬞶𥠂瑦韉𰻆𥞘𪾫𭿖嬝𤑓𠳧𭙺荐𨘛
[I 220626 18:07:19 HeZi:39] epoch:5 base:1760 --> 1719 
[I 220626 18:07:20 HeZi:36] giveup:0 
[I 220626 18:07:21 HeZi:39] epoch:6 base:1719 --> 1719 
[I 220626 18:07:21 HeZi:36] giveup:0 
[I 220626 18:07:22 HeZi:39] epoch:7 base:1719 --> 1719 
[I 220626 18:07:22 HeZi:100] 
"""

"""
[I 220626 18:08:50 HeZi:36] giveup:0 
[I 220626 18:08:51 HeZi:39] epoch:0 base:12939 --> 9944 
[I 220626 18:08:51 HeZi:36] giveup:0 
[I 220626 18:08:52 HeZi:39] epoch:1 base:9944 --> 9831 
[I 220626 18:08:52 HeZi:36] giveup:0 
[I 220626 18:08:53 HeZi:39] epoch:2 base:9831 --> 9831 
[I 220626 18:08:53 HeZi:36] giveup:0 
[I 220626 18:08:54 HeZi:39] epoch:3 base:9831 --> 9831 
[I 220626 18:08:54 HeZi:36] giveup:0 
[I 220626 18:08:55 HeZi:39] epoch:4 base:9831 --> 9831 
[I 220626 18:08:56 HeZi:36] giveup:316 𠰟𣥋𛂦𣧺𮡪↔𮅏𨽅𬻥𠩿𡅓𠪕𢁤𦔀𧕔𠬷𥕠𥒛𢺬𭀥𰨇𦖶𥨗𭽶よ𡣣𡟼𭽁𭐣𤔞𢇭𫑀𨭤𧅍𩍽𤽪𧱊𣸼𭅍𭖲⑫𣪃𧆕𮗙𠨦�𩽃𪂗𮎳𫸀𭱽𡅁𩃅ℓℓ𨖮𡯼𮔇𧁁𤨃𮇓𮭹①𭴺𮑩𮔰α𦪴�⑩⑩𣢔⑤𬅌𮯆𭐥𩃊𬾹𭮖𡩝い𬗋𠗩𣏱𮚊𣍫𡙪𤂃𧿗𤌰𦇅𰐣嬽䮉𤥥𭽂𬻱𭜤⑦𧘧△𫚃𮣨𣗫挔𨄛𠅂𭏬𣧱𤏑𠢨𬻞𣐦𦡿𠌚𠳧𮕋②𠆗𢧝𧑺𪠈𮢇𭤋𠐫𭫿𬟏𤲱𭣞𭻋𥑯𭆱⑮𫏦𭩩𭁟𭵈𦰌𭩟𦘎𨱸𦷠𨒢𭇢⑪𭄐𬻑𭱩𧡕𢁎𢏻𩥜𢻀𫆯𫸪𥮂𮒿⑬𥄽𫓓𭱎𦣵𩮟𤕦𧟺り𢊇𰒥𩛖𦗉𡄉𫺄𨘄𭔌𮓠𭣪𬄒𭦁𠝉𧷧𪦂𮃞𧦮𮒮䦄𭡈𬜻𠍩𭚡𮡭㭚𠬣𭧢𫴢𭲞𡋬𭪚𩜝𨀔𭣕𥭿𡙞𣴁𡽼𮞅𦣩𡚅𫅞𪛃�𥩷𦇵𭬢𣞦𡚇𡐝𩎇𬿻ヨヨ𪊩③𨔕⑯𨓂𤜓𣓝𧡉𥍙𧃱𤴘𧓂𮣝𭩲𭳘𭔥𮓢𣺙𮜟𣸰𬋢𤋛⑥⑲ 
𰲞𠆖𢋱𮔜𣭌𫩊𭳩サ𫒯𭶂𭁐𣖺𠰇𤁜𦮵𣤝𥾳𭙧𭵄𭦢？𭙙𦯤⑭𠲁𭺺𡭳𭻊𭆴𬅅𭊰𭼾④𢨖𭾊𭱐𧟾𦍖⑨𬝂𭀣𠀪𬻘𭬍𧷄𤉐コ𭮴𬔨𬃅𮄣𢉺𠰡𩌮𭇩𪦾𫤵⑧𨰔𠋐𠎖↷𫑃𫭣𢮴𣑛𧂘𭭧𭥟𭤪𧴇𠆋𭳛
[I 220626 18:08:57 HeZi:39] epoch:5 base:9831 --> 9799 
[I 220626 18:08:57 HeZi:36] giveup:0 
[I 220626 18:08:58 HeZi:39] epoch:6 base:9799 --> 9799 
[I 220626 18:08:58 HeZi:36] giveup:0 
[I 220626 18:08:59 HeZi:39] epoch:7 base:9799 --> 9799 
[I 220626 18:08:59 HeZi:100] 
"""
