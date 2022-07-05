import unicodedata
import os

from logzero import logger

from ZiCutter.ZiCutter import ZiCutter


def test_lang(dir):
    import logzero
    from logzero import logger
    logzero.logfile(os.path.join(dir, "ZiCutterBuild.log"), mode='w')

    # build
    cutter = ZiCutter(dir=dir)
    cutter.build()

    # use
    cutter = ZiCutter(dir=dir)
    line = "'〇㎡[คุณจะจัดพิธีแต่งงานเมื่อไรคะัีิ์ื็ํึ]Ⅷpays-g[ran]d-blanc-élevé » (白高大夏國)😀熇'\x0000𧭏"
    print(cutter.tokenize(line))


if __name__ == "__main__":
    langs = ['sw', 'ur', 'ar', 'en', 'fr', 'ja', 'ru', 'zh', 'th','global']
    # langs = get_langs()

    for lang in langs:
        # dir = f"C:/data/lang/{lang}"
        dir = f"C:/data/languages/{lang}"
        test_lang(dir)


"""
[I 220704 00:27:13 ZiCutter:105] C:\ProgramData\Miniconda3\lib\site-packages\ZiCutter\HanZi\JiZi.txt load  JiZi:1719
[I 220704 00:27:14 ZiCutter:55]   C:\ProgramData\Miniconda3\lib\site-packages\ZiCutter\HanZi\HeZi.txt JiZi:3727 --> loadHeZi 92463  values:1041
[I 220704 00:27:14 ZiCutter:109] C:\ProgramData\Miniconda3\lib\site-packages\ZiCutter\HanZi\HeZi.txt HeZi:92463 values:1041
[I 220704 00:27:14 ZiCutter:112] vocab:3727
[I 220704 00:27:14 ZiCutter:113] C:\ProgramData\Miniconda3\lib\site-packages\ZiCutter\HanZi loaded
[I 220704 00:27:14 ZiCutter:116]  C:/data/languages/global building
[I 220704 00:27:14 ZiCutter:121] vocab:3727 JiZi:1755
[I 220704 00:27:14 He2Zi:122] JiZi:1755 ChaiZi:94235 YiTiZi:27440
[I 220704 00:27:17 He2Zi:70] epoch:0 base:11264 --> 3216 
[I 220704 00:27:17 He2Zi:70] epoch:1 base:3216 --> 1959 
[I 220704 00:27:18 He2Zi:70] epoch:2 base:1959 --> 1944 
[I 220704 00:27:18 He2Zi:70] epoch:3 base:1944 --> 1944 
[I 220704 00:27:19 He2Zi:70] epoch:4 base:1944 --> 1837 
[I 220704 00:27:19 He2Zi:70] epoch:5 base:1837 --> 1829 
[I 220704 00:27:20 He2Zi:70] epoch:6 base:1829 --> 1828 
[I 220704 00:27:20 He2Zi:70] epoch:7 base:1828 --> 1828 
[I 220704 00:27:21 He2Zi:104] giveup:246 㢿㤙㬋㮢㯛䂉䒭䗔䙈䞀䫛䳧侯候凫叏喉囙堠壺嬝嬽岛島帿捣搗枭梟槝猴瘊睺篌糇緱缑翭葔蟂袅裊鄇鄡鍭餱鯸不女﨩爵𠄏𠇡𠉀𠋫𠍋𠎖𠐲𠑼𠒎𠖁𠗦𠝷𠩳
𠪕𠬫𠳧𡀮𡆢𡋬𡏭𡐝𡑩𡕏𡖣𡗁𡙞𡚇𡟑𡠿𡭳𡷊𡹵𡻅𢆴𢇭𢉺𢉻𢊇𢋵𢍴𢏻𢜵𢦘𢰡𢳚𣀨𣀴𣘖𣚝𣝄𣣠𣤝𣤼𣥒𣹋𣻴𤂏𤆿𤒉𤜓𤟨𤠣𤡔𤤏𤧝𤬈𥀃𥅤𥉼𥛪𥦪𥧻𥱌𦃭𦃺𦆚𦑤𦔗𦚀𦞈𦣩𦥢𦬝𦮙𦳓𦺟𧃭𧇹𧐳𧒬𧙊𧩨𧯁𧱊𧳱𨁳𨄭�𨝧𨥻𨬀𨭤𨺅𩃺𩋴𩌖𩓆𩘋𩡧𩤷𩩵𩺟𪃶𪅺𪈱𪑻𪜭𪵕𪹍𫋇𫌈𫑃𫗯𫛺𫮖𫸪𫽐𫽲𬀘𬂔𬅌𬇼𬋢𬑟𬔨𬥽𬫺𬬢𬭤𬵈𬻑𬻘𬻞𬻥𭁐𭄩𭆴��𭏑𭏒𭒭𭔥𭖀𭖲𭗃𭚡𭜤𭥟𭬍𭬢𭭧𭮴𭱃𭱎𭱐𭱽𭲞𭲰𭵄𮅏𮌧𮍇𮎳𮒮𮓢𮗙𮚊𮡭𮬁𮭹乁凵�㠯㨮𥚚𰅜𰒥𰙌𰜬𰨇𰲞𰳞𰷾𰻮𱈄
[I 220704 00:27:21 He2Zi:105] useless:38 trxチcepqsb9�6m8zafjiw30n4kgdlhu1oy7v25
[I 220704 00:27:21 He2Zi:128] HeZi:94180 Base:1717 
[I 220704 00:27:21 He2Zi:129]  useless:whチc1sy0zafe746rnv8pdlbjgk52�qiu3xmot9
[I 220704 00:27:21 He2Zi:131] (1755, 0)
[I 220704 00:27:21 He2Zi:132]
[I 220704 00:27:21 He2Zi:148] HeZi build success -> C:/data/languages/global\HeZi.txt  C:/data/languages/global\JiZi.txt
[I 220704 00:27:21 ZiCutter:105] C:/data/languages/global\JiZi.txt load  JiZi:1719
[I 220704 00:27:22 ZiCutter:55]   C:/data/languages/global\HeZi.txt JiZi:3727 --> loadHeZi 92463  values:1041
[I 220704 00:27:22 ZiCutter:109] C:/data/languages/global\HeZi.txt HeZi:92463 values:1041
[I 220704 00:27:22 ZiCutter:112] vocab:3727
[I 220704 00:27:22 ZiCutter:113] C:/data/languages/global loaded
[I 220704 00:27:22 ZiCutter:105] C:/data/languages/global\JiZi.txt load  JiZi:1719
[I 220704 00:27:23 ZiCutter:55]   C:/data/languages/global\HeZi.txt JiZi:3727 --> loadHeZi 92463  values:1041
[I 220704 00:27:23 ZiCutter:109] C:/data/languages/global\HeZi.txt HeZi:92463 values:1041
[I 220704 00:27:23 ZiCutter:112] vocab:3727
[I 220704 00:27:23 ZiCutter:113] C:/data/languages/global loaded
['#co', '15', '#ap', 'he', '〇', '#sq', 'ed', '#le', 'et', '#th', 'ai', '#th', 'u', '#th', 'en', '#th', 'an', '#th', 'a', '#th', 'an', '#th', 'at', '#th', 'ek', '#th', 'an', '#th', 'i', '#th', 'ng', '#th', 'ii', '#th', 'ae', '#th', 'ao', '#th', 'ek', '#th', 'gu', '#th', 'gu', '#th', 'aa', '#th', 'nu', '#th', 'e', '#th', 'ma', '#th', 'ee', '#th', 'ek', '#th', 'ng', '#th', 'ai', '#th', 'ua', '#th', 'ai', '#th', 'a', '#th', 'at', '#th', 'ii', '#th', 'i', '#th', 'at', '#th', 'ee', '#th', 'hu', '#th', 'it', '#th', 'ue', '#ri', 'et', '#ro', 'ht', 'p', 'a', 'y', 's', '#hy', 'us', 'g', '#le', 'et', 'r', 'a', 'n', '#ri', 'et', 'd', '#hy', 'us', 'b', 'l', 'a', 'n', 'c', '#hy', 
'us', '#la', 'te', 'l', 'e', 'v', '#la', 'te', '#sp', 'ce', '#ri', 'rk', '#sp', 'ce', '#le', 'is', '白', '高', '大', '⿱', '一', '夊', '⿴', '囗', '或', '#ri', 'is', '#gr', 'ce', '⿰', '火', '高', '#ap', 'he', '#cc', '00', '0', '0', '⿰', '言', '至']
"""
