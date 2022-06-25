from logzero import logger

star = '閵'

"""
    𤍽	𤑔 k,v  异体字\t本体字
    HeZi[𤑔]=HeZi[𤍽] if 𤍽 in 𤑔
    HeZi[v]=HeZi[k] if k in v
    """
doc = open("YiTiZi/YiTiZi.txt").read().splitlines()
YiTiZi = [x.split('\t') for x in doc]

path = "ChaiZi/ChaiZi.txt"
doc = open(path).read().splitlines()
ChaiZi = [x.split('\t') for x in doc]
# HeZi = {k:v for k,v in ChaiZi }


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


def chai(vocab_path, tgt, base_path):
    HeZi = {k: v for k, v in ChaiZi}
    JiZi = open(vocab_path).read().splitlines()
    JiZi = [x for x in JiZi if x]
    JiZi = set(JiZi)
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

    base0 = list(set(''.join(x for x in dic0.values())))
    base0.sort()
    with open(base_path, "w") as f:
        for x in base0:
            f.write(x+'\n')
    logger.info(''.join(set(base0)-JiZi))  #
    logger.info((JiZi-set(base0)))

    chars = list(dic0)
    chars.sort()
    with open(tgt, "w") as f:
        for x in chars:
            l = f"{x}\t{dic0[x]}"
            f.write(l+'\n')


if __name__ == "__main__":
    chai("JiZi/JiZi.txt", "HeZi/He2Ji.txt", "HeZi/BaseJi.txt")
    chai("YuanZi/YuanZi.txt", "HeZi/He2Yuan.txt", "HeZi/BaseYuanZi.txt")

"""
[I 220625 06:41:43 HeZi:43] giveup:0 
[I 220625 06:41:43 HeZi:46] epoch:0 base:12943 --> 9945 
[I 220625 06:41:44 HeZi:43] giveup:0 
[I 220625 06:41:45 HeZi:46] epoch:1 base:9945 --> 9831 
[I 220625 06:41:45 HeZi:43] giveup:0 
[I 220625 06:41:46 HeZi:46] epoch:2 base:9831 --> 9831 
[I 220625 06:41:51 HeZi:43] giveup:318 𬾹𣐦𨽅𡙞𭮖𭇩𦇵𭻊𭖲𭽁𣺙𭇢𥄤𢊇𭫿𣥋嬽𣏱𫸪𮚊𦔀𦣩𡟼𮯆𭁐𥭿𬄒𭱩り𮬿𫓓𮅏𪊩𠰇𣓝𬻑𨭤𢋱𮔇⑫𭀣④𬋢𠳧𧷧𫒯𩃊𢏻ℓ玈𥨗𬅅𩃅⑭𮤩𣸰𫑃？𧂘𡅁𠌚𬎝𭿥𬝂𫴢𭼾𠍩
𦇅𣤝⑨𩍽𬃅𢨖𨓂𨖮𪭔𬻱𮗙𥑯𭅍𭬢𭱐𮇓⑬𠋐𩌮𮢇𫩊𬗋𭐥𨰔𠬣𮜟𨔕𭥟コ𡐝𮃞𮓠𧘧𫺄𬿻𭐣𢺬△𭽶𡄉𡚅𧦮𮔜𮔰𮑩𫚃𦮵⑮𮞅𭲞𪦾𨘄�𠰡⑦⑦①⑥𣸼𧟾𭡈𪠈⑯𭴺𣞦𦦞𣪃𧿗𮎳𠲁𡽼𣧱𪦂𤂃𣴁𤁜𠨦𤴘𭁟𥾳挔𭳛𭤪𮕋𭾊𧃱𡚇𧆕𠗩
𭣞𦰌𤉐↔𬻞𫤵𪑄𫸀𭽂𭵈𮓢𤜓𭆱䮉𧟺𪒓𭏬𩄹𭱽𢁤𭐢𦯤𢏾𡙪𬬢⑪𮮡𦷠𦗉𦍖𭺺𤕦𭀥𠰟𮣝𰨇𭮴𤲱𤏑𨱸𡣣𬼗𧱆𧅍𭊰𭬍𤌰𬻘𫑀𭆴𡅓�𠐫𭩟𤽪𠆗𫹲𭩲𠆋⑩⑩𧴇𭚡𧁁𨄛𢉺𥒛𪂗𠪕サ𢇭α𠅂𮡭𰲞𭣕𫭣𮡪𭦢𧕔𭙧𡯼𮒿𢁎𭵄ヨ𭦁 
よ𮭹𣭌𛂦𠆖𦣵𡩝𥮂𭳘𬜻⑤𥟃𦘎𭣪𭤋𣺏𭄐𭶂𨀔𭪚𮒮い𧓂𠝉𭱎𧑺𥄽𣧺𬅌𤋛↷𦡿𪛃𩛖𮈏𡭳𭛄𤨃𮄣𭔌𤥥𢮴𬻥⑲𭳩𮣨𢐸②𨟧𫏦𣑛𧡉𦪴𦖶𭩩𩎇⑧𤣧𡋬𣍫𭭧𭔥𣗫③𰒥㢳𫫱𭙙𭜤𬔨𧱊𩥜𧷄𤔞𠎖𧡕
[I 220625 06:41:52 HeZi:46] epoch:3 base:9831 --> 9799 
[I 220625 06:41:53 HeZi:43] giveup:0 
[I 220625 06:41:54 HeZi:46] epoch:4 base:9799 --> 9799 
[I 220625 06:41:54 HeZi:99] 
[I 220625 06:41:54 HeZi:100] set()


[I 220625 06:43:45 HeZi:43] giveup:0 
[I 220625 06:43:45 HeZi:46] epoch:0 base:8203 --> 2609 
[I 220625 06:43:46 HeZi:43] giveup:0 
[I 220625 06:43:47 HeZi:46] epoch:1 base:2609 --> 1774 
[I 220625 06:43:47 HeZi:43] giveup:0 
[I 220625 06:43:48 HeZi:46] epoch:2 base:1774 --> 1760 
[I 220625 06:43:49 HeZi:43] giveup:0 
[I 220625 06:43:49 HeZi:46] epoch:3 base:1760 --> 1760 
[I 220625 06:43:50 HeZi:43] giveup:0 
[I 220625 06:43:51 HeZi:46] epoch:4 base:1760 --> 1760 
[I 220625 06:44:03 HeZi:43] giveup:1137 𠨞赗𢋱擳洊𩕴𬪙𭻊𢉺𢯫𢨖𢲄𭶂冔𡠄岛𣓍𩃊𫲃𧷄𬸴𫄍𭘲䐚𪜥鯽𰂿𭡈𡥂𦍖𤣧㐭𫘙𪭔𭁟𭥟𮚐𫉩𬊷凛𣹂㑡𠘐遰𭵄𮔂𥛣𡜒𤀙𭀣サ𨂢隝𦪴帽嫋冕𧡉𤍾鳳𠓮𡹙𤂶𤑇�𢂣𥾳𬝋𰜬𰘀𤂃𡄁𮢇ヨヨ𠩻卿𪉊𢺬冒𢤭𨱸𦀒漹い拵𧂽嬅㛿𫭣萺勖𤳩𭞖卿𡅓𭬢𡾭𮅏𬄜鳬𦇅𨪇𥨗𨺣𮬐𠆿𣑊𪪨𪊩卽𦪠嶌𡃦𦠜唧𡚣𫸼𭮴𠎑𠈚瀄𤃢𱀠𤊵皍𥭿𫨬𣩃𠕦𣝲螐𥇳㒟𠝉𡫎𠭂𤑓𭲳燣𮡪𫕝𠋐𡈘𭜤𫴘𦡿𨗼𰂶�𠏵𤏑𬷶りり𨏸𭇢𮄣𮔇檩𥟃帽𣚝𧴇𫖛㺺𨽅𬊥槝𬼗缎𦯤𡉠𛂦𡠹𦊯𧮉㮧𩏇𦦰𭗃𣩙𭿥喞𩀵𩾏𬃅𦾛躏焉𮣝𡻺𠥖𢋴煅⑤𮑩㒽𢏻𧅍𡑩𩃅㠏𤓟𤥥躪𦰌𠩯𧑺㠀㠀𭺺𧠁䗡凜𫄊㦊鍛碫隯𫧙𥈨𬻘𨔕𪠂𰭍𤒐𭐢𨶇𪦂𨶄𤋛𡭳𩥜郻
𫓓𠒎玈玈䅿𦦺𨏼𫮖𠎖𮬿𫶇𣎮稟𠙒𣺏𰸛㙿𧷧𭌨𰓚艜𠠑𦽏𫦲𦛊𭤋𬆸𩾖𤴘𫏦𭿖𧓂㨶𦾓𡻅丝嗚𭽁卿𤑎𧄟𤞐𩼚𭌟𭽶𣺙㸑𧒬蔺𪈽𫉿𣸰𥩴𭦢𰛤𦇩𮘥𨘛𮔕𡩝壷檁𦘎𣴁㱭媢𦣩袅𨉨𩋋𨽖𮤩幯𩾓𢭏𫪮𬶎𣿆櫛𦺟𦷠莭𠽠𭡣𧑍
𮡭𤆡𭚐𭆴凜閵𬾹篶𥻼𬯶㡌𪄝㫯𩍽𫃅𰸸禀𧜵𦺄凫𦂰𠍩𩿋𤓚𢄓𥮂𨜑𨩩𢶑𬔨𭱐𭊰𠏟𩌵冃𪞌𡼄燨𢝪𡠿𠌶櫛𢤻𰺣𠆡𩼤即滯𥛵𫡿在𥣮𡚖𢐸䳋𰌬𰧿𧟺𪣋褭𬻑䙊𢽵𰄕𱇵𡺑𭌾𤚶𡣣𭱩扗疄𩾒𥒛𤎄𭀋𭔥𢺫𰬜𭻝𤒢𪾅𠕚𥲭 
堲𤉐𫩊𭖸慸𬜻𣗫𭼪𢸣𩺀𮚊焨⑫𠰡蟂𫺄𠡘𡙞𡷊𨗍②𤓥𠰇𫲉蹸𤹄𤢤藺𡖖𠁑𠲁鰿懘α𫃖傿𰸲𠰟𢊸堲㯛𦏁瞱𪦭崼蝍蠞𨩷𩄹𭁐𡀀𨟧𨬋↔𠂶𤸼𦂔𦵍鷨𭓁𠕙𮜩瑁𣑛𬐑𧋍𪼯𬒛𭛄𢰂𮒿𣹜鰞帰𫫱𰅻𫦱𨒸𨓂𢐱𬋢瑖𢯾捣𠛆𠞆
𥤆𣪃𡄉𰁿𨘬𨜇廩𩆐𫞌𥉼𭵈節𣔺𪂗⑭𡙪𣛬𭐥𠰱𠌵𡖥𫺆𮔒𤪧𩌗𫋇归𤽪䡧𬬢搗𮃞𩤣锻𪦋𨆴𨺜𩏧𭏬⑥㒻澟𣦨樺𤲰𪡰𡒄𣤝𣻉𰟀𦮵茬𫖤𧱆𪵕𭩟椴𭲝𡏭𣞦𬅅𮇓韡𤨃𫒿𭣞𭩲𱈯鳧コ𡅁𤒹𫹲𮯆𤇟𦦞𡿢𤊻𭻟𫑾廗鄢𡽼𢛡𰡹�𮔰𫚃﨩﨩𩐯𬇵嘩𧦮𣟦𠆖爨𨺽挔𭸛𫔴𩦫𣆱譁𦋤𠌚䂀𩼿𨓼𡐝𢴶𫛓𬁋銯荐葮𠅂𨮍段年𠐫⑨𩌴島𢙮𠷌𫽲𣯀𨎺𭫿𠆗𬋡𥕧蝃蹛䖚𣄒卿𭂛𨜮𰰏𬻥𧹮𪳦𧁁𠪕𭤪䉮𣐦𦽹犧𢄩𧟾𭔌𩇆梟鲫𡉈𢤔𣝄𢏾𮔜𫑀熓䌯𧱊𭖘𭦁節𤕦𰏕△
𥑯𨖮𡬜𰑵癝𭭘𤲱𧽞㥼𤯑𠗩𭆩𠡼𭪚韉𣟊𮣨𨰔𠨠𠱜𡇾𥠌𤈊𥄤𪬢𭭧𥋟懍𠆋𭬍躙𨶱珔𪷤𨞴𮎳𣎋𢽢𩮟𪎐𮕋𨭤擣𪑄𮓢𫟁揤癛𦨧𢐯𩐲嵽毈𪥀莭𠌥韀𬅌𧽋𧂶𰏼𪲒㦢𫰡鴵𭣕𠘅𩼜塅鷍𰯳𣍫𦔀𠕥𢊬𭾊𥤂𩌮揤㜵𫨻𪯜𫲳𢋏�𤾤椛椛𫑴𣭌㯊𩾣𠪅𧃹𭼾𧿗𢅦𤏷㠡䕲𡀫蔫𢁎蝐𤁜𬂋𫷀𰲞爨𩜝𠳧𭽂鄥𧆕𦾏⑯⑩𧂘𥄽𨘄𰿟鸶𤔞𢶸𰻮𰒥䠠ℓ𣸼𢶈𬿻嘕𮃦𫝵𢾟𪦾𦗉𬀘𢢐𭳛𮓠𠓶𡖪㴘㴘𠨍𦆚廪𧡕嬝𩎶𬻱𭚡𤡔侟䮉↷嬽𠕖緞節𪛃𭸞即𬄒𭲞㯂嫣𣱭𦀩䢜 
𠬣𰨇𩼱𣻴𭱽𦢵賵𢊣𭐣煅𤶐𠵄枭𧷃巋𪒓𣏱𤊳冒𠕬？𤑖曦𬎝⑦𦾰⑮𨀬𡟼𨚲澕𫒯𫞼𬗋𰲟𢷍𪃑𧋃𤣽𪠈壺𨳀𬟠𰒒華𡚅䃵𢅊𫚘壈𤌰𰼾𬡇𢮴𩻮𭸯𭮖𧠊銌𦇵𭙺⑬𢁤𰧬䑵絻𨞶𭆱䗻𤎭咝𨟏𣶀燷𢇭𦷊冐𠨦𧕔𩈺𥋶𩏬𩖋𫸪𨣄𪽜
𰜊𦶀𣨼𩛖𰇘𨎹𦦾𦳓峌𥚕𧝥𨭷𩝷𣹋𪽦𢷭𬛋㘉嶹𢳃帴㱕羲𦪷㩘𡻜鄡𦎮𦻺𡯼𣡑𡋬𫴢𢀮𦿬𢞬殢𬚭𩎂𭙙烏𨺆𬒢𮜟𫑚𦼇𭱎𫿣𪼚𥱳爔𣥋𪟥𮕹冑𢈺𤴟𮒮𡖠𭈭𭳩𬝂䙚𮮡裊𰸚螮𮔙腶𩪶𤫈𰊎𢋕𫳖嶋𠳲袸𭲰𣌀塢𰞍䲷㵯瑦�𧞡㢳㢳𣌸𤺡𥗗𥠈𭀥𩎇帶𰩁𩋦𨙌𣘖𰏓㦅顲⑪𱈝𡹭𰻆𦖶𬻞𤲈𤜓𤾏𣧱㒾𠘟よ𧛕𫂵𠻭𦋓𭖲𣁚藺𦆉熶𭇩①存懔𫌈𭩩䲙𠕮𦣵𬩞𭳘朂䗖栫③岿𡚇𠘡𧎚㬢𪋴𭣨𮞅轥𨀔㟆𢊇𦼹⑲𢀤溩冕𨜊𮇭𢝌𣐩𢤅㒿嵨華𡓔𧂑𧘧𭅍㒻𭴺𢷬𡗋
𫸀𮈏𣓝㪞縀噝𣻥㸅𧃱𨄛臶𫤵𭲀𡈌𥠠⑧𫿝𩋾𰔇鞯𡀮𬑓𧚇𭣪𨺔𥞘𥜘毷𢳚鎢𬚦𰖩摕𢵴𣧺𦡣𨏦𭄐𮗙𮧵𭎯𮑨𰓜𩉾𫏗𫭇艒𧑂
[I 220625 06:44:04 HeZi:46] epoch:5 base:1760 --> 1719 
[I 220625 06:44:04 HeZi:43] giveup:0 
[I 220625 06:44:05 HeZi:46] epoch:6 base:1719 --> 1719 
[I 220625 06:44:06 HeZi:43] giveup:0 
[I 220625 06:44:07 HeZi:46] epoch:7 base:1719 --> 1719 
[I 220625 06:44:07 HeZi:99] 
[I 220625 06:44:07 HeZi:100] set()
"""
