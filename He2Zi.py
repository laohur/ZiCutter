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


def chai(JiZi: list, ChaiZi: list, YiTiZi: list):
    HeZi = {k: v for k, v in ChaiZi}
    JiZi=set(x for x in JiZi if x in HeZi)
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

    doc = open(YiTiZiPath).read().splitlines()
    YiTiZi = [x.split('\t') for x in doc]

    doc = open(ChaiZiPath).read().splitlines()
    ChaiZi = [x.split('\t') for x in doc]

    HeZi = chai(JiZi, ChaiZi, YiTiZi)

    Base = set(''.join(x for x in HeZi.values()))

    diff = Base-set(JiZi)
    logger.info(''.join(diff))  #
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
    # JiZi = open("JiZi/JiZi.txt").read().splitlines()
    # build(JiZi, ChaiZiPath="ChaiZi/ChaiZi.txt", YiTiZiPath="YiTiZi/YiTiZi.txt",
    #       HeZiPath="HeZi/He2Ji.txt", JiZiPath="HeZi/JiZi.txt")


"""
[I 220626 19:01:53 HeZi:36] giveup:0 
[I 220626 19:01:54 HeZi:39] epoch:0 base:8204 --> 2611 
[I 220626 19:01:55 HeZi:36] giveup:0 
[I 220626 19:01:55 HeZi:39] epoch:1 base:2611 --> 1774 
[I 220626 19:01:56 HeZi:36] giveup:0 
[I 220626 19:01:57 HeZi:39] epoch:2 base:1774 --> 1760 
[I 220626 19:01:57 HeZi:36] giveup:0 
[I 220626 19:01:58 HeZi:39] epoch:3 base:1760 --> 1760 
[I 220626 19:01:58 HeZi:36] giveup:0 
[I 220626 19:01:59 HeZi:39] epoch:4 base:1760 --> 1760 
[I 220626 19:02:10 HeZi:36] giveup:1139 紪𠕚𦦾𭾊𨗼縀𣢔𨏼𪬢繐𠈚𠡘𫶇𩦫𫿝𤑖洊𩾒𨬋𤒢𤽪𥢁𭚐滯𭺺𢵴嘩⑤冔𣝄鞯𢁤藺𤏑𦢵𫴘𫸪𢇭栫𰒒𭖸𣧱𡩼𤑓𡻅𤢤梟𪦭㪞𮔒𫏗韀𩐯㯂𨶱在𫭇𰸛𡄉𨜑𠲁𭱐𮃞峌𢅊
嶌𥒛𠰡𢝪𦨧𥉼𧠁𧽋𠞆𩾓𥍙？𦅠𡗋𥠠蹛𤎭年𰖩𡒄𫭣𬗋𦠜𦇠𰜬𮯆𠘅𥗗𦽏䙊𩾣𭔥𰁿㮧𧷃𢺬𨒢𥠌③𡚅𡚇韢𨰔𭏬𮒿𮔜𠕙𤑎𭣞蟪瞱②㯊⑪𬋢躪�𡜒𡬜䌯䌯絻𭬍𭌨𭲞毷𢊣勖𤞐𪟥𬰶𫡿𬼗𮇓冐𰲞𢁎挔⑲媢懘𨘄𦣽𠏵𢂣𨺣 
𭥟⑫蔺𧱊𨺆嗚郻𣭌い𣩙𪦂𫋇崼閵𠏶𥝩𫨬嶋䃵𡖪巋⑭𧅍𠕦𫪮𭻋㠡𥤂𧎚𭫿𪵕𢳚𤊻𤎄𰿟椴毈躏𠪅𥕧𠭂𥲭焨𤲰𬿻𡽼𠋐𦛊𫆵𢊬廩𩐲𫉩𫏦𬩞𬟠𤴘𠀪�𩀵鄡鄡㥣𫰡𠬎躙𤨃𪞕𨏸锻𦾰𮓢鄢𨓼𮕹𠕖𤏷𭦢𢞨𢶈𦯤䢜𬄜樺𣻥  
捣蹸𰰏隝碫𤳩𰯳𰾶𮜟𩽃𩎰𣱭𦼯㦅𨎺𩏧𬚭𮩭𨶄段𭙺褄𛂦𤋛遰島𭱽𭭘懍𣝲𭽂𫩊𠩻䅿䲷𦼹𬯶𩃊凫𮒮嬅𤂃𧷧𩕤𡑩𦶀㟆𫨻𨓂岛𬚦𭸯𪋴𬹢㺺𪱇鶈慸𪣋潓𧋃𭚡𤈂𧮉𫒿𠻭𡜛𬬢𭽁𡩝𢶑𮑨𫞼澟𣗫𡐝𫺄𭻊𥛸𤌰归𭓁䠠𨚲�𩾏𫒯𩝷𪟊𬷶⑨⑨𦇵𫆯𬒢艜𭴺帶𨉨𩥜𩂲𠌵𡜈𤲱𦪴𨭤𨘬𩌵𮘥癝凛𨆴㵯𤾏寡𡖠𦾛𬡇𨺽焉𡠿𡥂𬜻鍛𢄓𮡭存嫋𣟦㒿𨮍摕𢈺𫸀譁䃀𡿢𦎮𰺣𡹭橞𧓂𭡣淒𦂰譓赗嬽⑦𤹄缎𫛓𬊷𢊸𰍏𥈨妻𡫛ℓ𢧝𨽅𪥀顲㥼𰄕𰬸𫑚葮𬀘𬻱𩻮�𠁑𢾟𣷑𧃱𰊎𡀫𠵄④④𰬢𢏻爨𰘀臶𩖋𣸼𭎯𩛖𡻜藺壺懔𦇅𧴇𨺔𨞴𩌗𬤝𰻮塅𢳃凄裊𭊰𬻑𭘲𡃦𡙞𧝥𭲳𫴢𭁟𬆸廪𠡼𤂶𤈊𧟺𬂋𭆱𭬢𥻼𡋬𭵄𦖶䡧煅𢝌𩋦𨔕𪦋𥤆𢋏䮉𡠄𧦮鏸𪂗𡉠𮔇𢞯𭈭𧁁𣔺𡇾𩌮⑯𫂵𪾫𭼾𠅤𠕮𩍽𰬜𧡉𫘙
𭖘𭄐𨄛鳧𠎑𥕠𡀮𢽵𬟘𰸚𫑀𡚣𧷄𤾤𦦰𤉐帽𡪍𦀒𡙪𨗍𫃅𰏕𭱎𧟾𬄒𧆕𭐥𬟏棲𮅏𥾳𦷠䖚𧞡𢠞𢯫𢰂𤶐𤚶𥋶𮚐𡝽𬐑𭅍𩉾𬋅𢶸𬻞𰂿㡌𦼇勗螐𭳩𦰌𬸴𢄩冒𮎳𬪙帴𠗩𦣩𢽢㒟𰐣䉮𠂶𠘟槝廗𤸼㜵僡澕𡺑𢤔𢯾𤆡冑𥞘𨣄𦍖�𤊳䙚䙚荐𭸞華殢𪼚𩈺𭁐㸑凜𫚘𭀣𪯜𬑓𨫍岿𣶀𢙮𧛕𢢐𫦱𩇆𭼪𮜩憓𬺡𪳦𫑴𫽲𣯀⑩𩏇𠰇㭚𫸼𨞶𠢨𮭹瑦𢞻壈𦋤𠝉寭𪠈𡫎𠨦𡯼鸶𢋴穟𣏱𣹂𥨗𧂑熶𥑯𭆩瑁瑁𨖮塢𨿩朂𩤣𠌥𰧿𧘧𪒜﨩稟𤕦霋袸𫲉𬔨𤒹𠳧𫦲𭗃𪄝𠆋𡫌
𫚃𮣝𠕬𭀥𪛃ササ𪲪𩋾𣨼𭧢㱕𦔀萺鷍𭇢𣓝𣻉𭵈𢛡𫓓𭻟𤪧璤擣𣧺𤲈𪊩艒𦘎𮄣𠆿𠆜𣓍𤓟𫟁𧋍𮚊𢮴𦺟𠓮𡷊𭮴鳳𤯑𢸣𤜓𦂔𫖤𫞌𡭳𫅆𭖲𭪚𰧬𰨇𪷤𦆚𠒎𬝂𭩟𠳲𭤋𠆗𪷺惠惠𦿬𦽹𤒐𠽠𪪨㠏𢻀𡓔𢺫𭻝熓𢡘𫲃鳬𦇩𡟼𦅵 
𭦁𮗙𡻺𫔴𤔞𮑩𩎶𧡕𦡣𫄊𮋍䕲爨𫖛𮇭𰓚𫲳𰟀隯𪗍𠓶𠆡𥮂𠆖𫝵𠱽𣞦𬊥𭜤㒻𰲟傿𭣕咝𣸰郪疄𢷭𥇳𦪠𨏦𠉯𠱜𨶇𰼾𣎋篶𫱮𭳘⑧䳋𬻥𠆣𫌈𣤝𪃑𥩷𰔇𰥡𱀠𫤵𠘡烏𨩩㴘𪉊𱈯𢤭𫄍𣆱螮𣍫𨜇𨪇鎢𥣼𠅂𢅦㒻𭱩𢀤𢭏𣪃萋華
𠌚𫿣𬔄𢋱冃𭣪𣺏韉𢨖𩋋𩾖⑮𡈌𪲒𫽐㠀𡏭𫋂𠦽𨽖銌㱭㒾𩕴ヨ𤫃𣥋𭳛𤇟𦆉枭𭽶𠰟𩏲𤺡𫷀嵨𥛣穗⑬𦻺𮡪コ𮧵𤓥𥛵嵽蝐㼮𢊇𤑇①𡾭𦮵𱈝轥恵𮕋賵𨟏𭶂𫅞㦊𦪷𠬷緞𡠹𤃢燷𩏬𭣨𦷊𨘛檁㫯丝𬅌𬋡䦄𢤅𭮖𪦾𧿗檩𡈘𣘖
𦾓𨀔𠎖瑖𤀙𮢇凜𡄁𭤪𡀀鴵椛𰑵𫳖𣹋溩𬾹𠍩𫮖𭌾𣺙↔𦵍𭵹𪜥𭲰𠕥𧂘𨺜𦗉𢷬𢀮𥭿𫌿𣄒𧵿𰅻𧒬𢞬𰭍𡉈𦀩褭𨎹䗖𨳀𬟉𭩩腶𦣵𩌴𣑛𬅅𭇩�𭸛𧑺𦑐𭂛𮔰𭡈△△𢉺⑥禀𢥁𭞕𧕔帽𫑾嘕𭙧よ𣿆蕙𣚝嫣𡚖蟂𫂠燣㨶韡𣐦𣖺𥄽
𬵪𭞛蔫𣌰𣟊𦡿冕𮃦𧂽㒽𧠊漹𢷍𰏼𠪕𩆐𧃹𠬣㛿𡼄𡣣𩃅𪽜𣦨𤴟蝃𠙒珔𪥼𫺆𰜊𢲄𩎂搗𮓠𣻴𤣽鷨𭙙冒𬒛𠩿𦊯冕𠘐𨩷𡜌𬀼𠩯𦻇銯𩎇𰂶㯛𦦺�𩏚𠌶鰞鰞𢤺䗡𭩲𧄟𪈽鄥㐭噝袅𤍾癛𰌬𭆴𥜘𧂶𰡹り𤁜嶹↷𤥥𠀄侟𧽞𨒸 
𫉿緀𮔙拵䑵壷𩜝𧬽𧹮𠐫悽𭔌𡹙𩸸𠏟𭭧𫑃𩼤𰒥𠛆α𡝣𢋕𣴁𩮟𭲀𣑊𪎐𭿖𰏓𥚕𤡔𢴶𬘄𰻆𥩴𨀬𬃅𬞶䧥𫹲𡅁嬝𧑍𦋓𮣨扗𧚇𭐣茬
[I 220626 19:02:10 HeZi:39] epoch:5 base:1760 --> 1719 
[I 220626 19:02:11 HeZi:36] giveup:0 
[I 220626 19:02:11 HeZi:39] epoch:6 base:1719 --> 1719 
[I 220626 19:02:12 HeZi:36] giveup:0 
[I 220626 19:02:13 HeZi:39] epoch:7 base:1719 --> 1719 
[I 220626 19:02:13 HeZi:100] 
[I 220626 19:02:13 HeZi:116] HeZi build success -> HeZi/He2Yuan.txt  HeZi/YuanZi.txt 
"""

"""

[I 220626 19:00:37 HeZi:36] giveup:0 
[I 220626 19:00:38 HeZi:39] epoch:0 base:12939 --> 9944
[I 220626 19:00:38 HeZi:36] giveup:0
[I 220626 19:00:39 HeZi:39] epoch:1 base:9944 --> 9831
[I 220626 19:00:39 HeZi:36] giveup:0
[I 220626 19:00:40 HeZi:39] epoch:2 base:9831 --> 9831
[I 220626 19:00:40 HeZi:36] giveup:0
[I 220626 19:00:40 HeZi:39] epoch:3 base:9831 --> 9831
[I 220626 19:00:41 HeZi:36] giveup:0
[I 220626 19:00:41 HeZi:39] epoch:4 base:9831 --> 9831
[I 220626 19:00:43 HeZi:36] giveup:316 α𮕋⑪𣑛⑮𣥋𫑀𣺏𭣞𭱩𤏑𮑩𭔌𭥟𭊰𦣩𤌰𫹲𥭿𪂗𭱽𮔰𥄽𬃅𭇢𤽪𧆕𮗙𮓢𫅞𭵄𡯼⑨𬻥𭾊𦣵𭁟𠰟𦯤𫭣𧿗𭁐𤥥𢨖𢇭𭚡𫸀𠆗𦮵𭔥𬄒𠰇𨓂⑬𭶂𦍖𣤝⑲𭬢𮃞𭆴𩜝𣓝𭣕⑤𭵈𠋐𬝂⑧𧃱𬗋𠌚𭏬い𤲱𭫿𭻋𬜻𮞅𮭹ℓ𢊇𭱎𠳧𢏻𣧺𭤋𭼾𫏦𭀣𭴺↔𧅍𭙧𪛃𡙪り𭺺𭽂𨔕𡚇𤴘𠍩𤉐𦔀𡽼𨱸𬅅𢁤𭐥𭆱𩮟𬾹𩛖𤂃挔𤨃𤕦𧓂𨖮𭇩�𬻘𛂦𮜟𩎇𮣝𦇵𡟼ココ𨘄𭄐サ𣪃𠬷𮡪𠆖𬅌𭳘𥕠𭳛𧷄𡋬𬼗𤔞？𮚊𤜓𧴇②𨭤𮢇𠪕𪠈 
𭩲𠰡𫆯𭅍𭤪△𭧢𭲞𮣨𢉺𭱐⑭𩃅𮯆𮔜𡐝𫩊⑦⑥𠨦𥩷①𰨇𡭳𫴢𡙞𣐦𣸰𭦁ヨ𮒮㭚𣖺𦪴𦘎𡅁𮇓𬿻𣢔𭡈𩽃𠬣𡅓𭐣⑩𪊩𬟏𧟺𫑃𭖲𫺄𠐫嬽𧟾�𦇅𮓠𩌮𮎳𭪚𭮴𫓓③③𧕔𢁎𥒛𭀥𭩩𰐣𩥜𬻑𥾳𠩿𭣪⑯𧡉𰲞𤋛𬻱𡚅𥨗𦖶䦄𣞦𭙙𤁜𧡕𣧱�𦰌𮅏𭮖𮒿𬻞𣍫𪦂↷↷𩍽𮡭𢮴𦡿𣺙𧦮𠀪𪦾䮉𧑺𭻊𮄣𨒢𧷧𭩟𠆋𠗩𣏱𣗫𧂘𠝉𥑯𨄛⑫𡩝𠎖𬬢𠢨𧁁𮔇𧘧𣴁𢻀𧱊𬋢𭬍𥍙④𭦢𠲁𫸪𠅂𣭌�𥮂𨀔𫒯𨰔𦗉𡣣𫤵𢺬𭭧𣸼𦷠𬔨𨽅𢧝𢋱𭽶よ𡄉𩃊
[I 220626 19:00:44 HeZi:39] epoch:5 base:9831 --> 9799
[I 220626 19:00:44 HeZi:36] giveup:0
[I 220626 19:00:45 HeZi:39] epoch:6 base:9799 --> 9799
[I 220626 19:00:45 HeZi:36] giveup:0
[I 220626 19:00:45 HeZi:39] epoch:7 base:9799 --> 9799
[I 220626 19:00:46 HeZi:100]
[I 220626 19:00:46 HeZi:116] HeZi build success -> HeZi/He2Ji.txt  HeZi/JiZi.txt
"""
