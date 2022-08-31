import unicodedata
import os
import collections

from logzero import logger

from ZiCutter.ZiCutter import ZiCutter 
import UnicodeTokenizer


def get_langs():
    alphabet = ''.join(chr(x) for x in range(ord('a'), ord('z')+1))
    langs = [x+y for x in alphabet for y in alphabet]
    return langs


def char_name(x):
    try:
        name = unicodedata.name(x)
        words = name.split(' ')
        return words
    except Exception as e:
        return []


def count_name():
    tokenizer = UnicodeTokenizer.UnicodeTokenizer()
    freq = collections.Counter()
    for i in range(0x110000):
        words = char_name(chr(i))
        if not words:
            continue
        x = words[-1][-2:].lstrip('-').lower()
        freq[x] += 1
    words = [(k, v) for k, v in freq.items()]
    words.sort(key=lambda x: -x[1])
    with open("name_tail_freq.txt", "w")as f:
        for k, v in words:
            f.write(f'{k}\t{v}\n')
    logger.info(freq)


def char_name_first(x):
    try:
        name = unicodedata.name(x)
        words = name.split(' ')
        return words[0]
    except Exception as e:
        logger.error(x)
        catg = unicodedata.category(x)
        return catg


def test_first(dir):
    p = dir+'/word_frequency.tsv'
    if not os.path.exists(p):
        return
    logger.info(p)
    store = collections.Counter()
    for l in open(p):
        t = l.split('\t')[0]
        if not t:
            continue
        names = [char_name_first(x) for x in t]
        if len(set(names)) > 1:
            logger.error((l, names))
        store[names[0]] += 1
    # logger.info(store)
    return store

def count_first():
    freq=collections.Counter()
    langs = get_langs()
    for lang in langs:
        # dir = f"C:/data/lang/{lang}"
        dir = f"C:/data/languages/{lang}"
        # test_lang(dir)
        c=test_first(dir)
        if c:
            freq|=c
    words = [(k, v) for k, v in freq.items()]
    words.sort(key=lambda x: -x[1])
    with open("name_first_freq.txt", "w")as f:
        for k, v in words:
            f.write(f'{k}\t{v}\n')
    logger.info(freq)



def test_module():
    from ZiCutter import ZiCutter

    logger.info((ZiCutter.Bigrams[:100], len(ZiCutter.Bigrams)))  # 2008
    logger.info((ZiCutter.GouJian, len(ZiCutter.GouJian)))  # 2365
    cutter=ZiCutter.ZiCutter()
    logger.info(len(cutter.vocab))  # 4399
    for i in range(0x10FFFF):
        c = chr(i)
        ts=cutter.cutChar(c)
        for x in ts:
            if x not in cutter.vocab:
                logger.error((chr(i),ts,unicodedata.name(c)))
                d=0

def test_lang(dir):

    # build
    cutter = ZiCutter(dir=dir)
    cutter.build()

    # use
    cutter = ZiCutter(dir=dir)
    line = "'〇㎡[คุณจะจัดพิธีแต่งงานเมื่อไรคะัีิ์ื็ํึ]Ⅷpays-g[ran]d-blanc-élevé » (白高大夏國)熵😀'\x0000熇"
    logger.info(cutter.tokenize(line))


if __name__ == "__main__":
    # count_name()
    # count_first()
    test_module()

    langs = ["", 'sw', 'ur', 'ar', 'en', 'fr',
             'ja', 'ru', 'zh', 'th', 'global']
    # langs = get_langs()

    for lang in langs:
        # dir = f"C:/data/lang/{lang}"
        dir = f"C:/data/languages/{lang}"
        if not os.path.exists(dir):
            continue
        test_lang(dir)
        # test_first(dir)
        # break


"""
[W 220831 23:19:47 ZiCutter:109]  C:/data/languages/global building
[I 220831 23:19:47 ZiCutter:112] receive roots:0 JiZi:2401
[I 220831 23:19:47 He2Zi:100] JiZi:2401 ChaiZi:94235 YiTiZi:27440
[I 220831 23:19:48 He2Zi:51] epoch:0 base:10715 --> 3236 
[I 220831 23:19:48 He2Zi:51] epoch:1 base:3236 --> 2876 
[I 220831 23:19:48 He2Zi:51] epoch:2 base:2876 --> 2875 
[I 220831 23:19:48 He2Zi:51] epoch:3 base:2875 --> 2875 
[I 220831 23:19:49 He2Zi:51] epoch:4 base:2875 --> 2859 
[I 220831 23:19:49 He2Zi:51] epoch:5 base:2859 --> 2858 
[I 220831 23:19:50 He2Zi:51] epoch:6 base:2858 --> 2858 
[I 220831 23:19:50 He2Zi:51] epoch:7 base:2858 --> 2858 
[I 220831 23:19:50 He2Zi:84] giveup v:501 ⺁⺂⺃⺅⺇⺉⺋⺍⺎⺏⺐⺑⺒⺓⺔⺖⺗⺘⺙⺛⺜⺞⺟⺠⺡⺢⺣⺤⺥⺦⺧⺨⺩⺪⺫⺬⺭⺮⺯⺰⺱⺲⺳⺴⺵⺶⺷⺹⺺⺽⺾⺿⻀⻁⻂⻃⻄⻅⻆⻇⻈⻉⻊
⻋⻌⻍⻎⻏⻐⻑⻒⻓⻔⻕⻖⻗⻘⻙⻚⻛⻜⻝⻞⻟⻠⻡⻢⻣⻤⻥⻦⻧⻨⻩⻪⻫⻬⻭⻮⻯⻰⻱⻲⻳⼀⼁⼂⼃⼄⼅⼆⼇⼈⼉⼊⼋⼌⼍⼎⼏⼐⼑⼒⼓⼔⼕⼖⼗⼘⼙⼚⼛⼜⼝⼞⼟⼠⼡⼢⼣⼤⼥⼦⼧⼨⼩⼪ 
⼫⼬⼭⼮⼯⼰⼱⼲⼳⼴⼵⼶⼷⼸⼹⼺⼻⼼⼽⼾⼿⽀⽁⽂⽃⽄⽅⽆⽇⽈⽉⽊⽋⽌⽍⽎⽏⽐⽑⽒⽓⽔⽕⽖⽗⽘⽙⽚⽛⽜⽝⽞⽟⽠⽡⽢⽣⽤⽥⽦⽧⽨⽩⽪⽫⽬⽭⽮⽯⽰⽱⽲⽳⽴⽵⽶⽷⽸⽹⽺⽻⽼⽽⽾ 
⽿⾀⾁⾂⾃⾄⾅⾆⾇⾈⾉⾊⾋⾌⾍⾎⾏⾐⾑⾒⾓⾔⾕⾖⾗⾘⾙⾚⾛⾜⾝⾞⾟⾠⾡⾢⾣⾤⾥⾦⾧⾨⾩⾪⾫⾬⾭⾮⾯⾰⾱⾲⾳⾴⾵⾶⾷⾸⾹⾺⾻⾼⾽⾾⾿⿀⿁⿂⿃⿄⿅⿆⿇⿈⿉⿊⿋⿌⿍⿎⿏⿐⿑⿒ 
⿓⿔⿕〇㇀㇃㇅㇆㇊㇋㇌㇍㇎㇏㇐㇑㇒㇔㇕㇖㇗㇘㇙㇚㇛㇜㇝㇞㇟㇠㇡㇢㇣㐃㐆㐧㔔㪳㫈䍏乁乄书亊亪円卍卐孒孓曱女卑既碑辶爵𠀀𠀈𠀌𠀍𠀑𠀟𠁢𠁦𠁧𠁩𠁰𠁱𠁾𠂀𠂂𠂍𠂣𠂼𠃉𠃛𠃢�𠄙𠑹𠒂𠕄𠖁��𠝎𠤬𠥃𠥻𠦁𠩳𡆵𡋬𡗒𡜏𡭔𡭳𡯁𡰴𡳿𢁺𢌰𢎗𢎜𢎧𢎱𢩯𢩴𢮮𣅲𣒚𣗭𣦶𣫬𣴁𤐁𤘍𤤃𤦡𤰃𤽆𥃅𥆞𥝌𥸨𦉭𦣵𦤄𦥒𦥫𦥺𦨃𦫵𦭩��𧺐𨈏𨈐𨈑𨳇𨳈𩂚𩇦𩇧𩇨𩙱𩰊𩰋𪓕𪓝𪚦𪛉𪛙𪛛𪭣𫇧𫝖𫩦𬫬𬺷𬻆𬼁𬼂𬼄𬼘𬽡𭅫𭔥𭖀�𭣔𭣚𭨘𭮱𭮴𭱐𭱽𭳄𭺪𮍠𮎳𮒮𮠕乁㠯𰁈𰑓
[I 220831 23:19:50 He2Zi:85] useless k:44 ce2o5p8mu9kvユ3↔gt④6w7③hコzf⑦4nayj01xl？irqdsb↷
[I 220831 23:19:50 He2Zi:104] HeZi:93746 Base:2365 
[I 220831 23:19:50 He2Zi:105]  useless: 36 e81xpl9yk6fwigzj0n3a24ucvh7otrqs5mbd
[I 220831 23:19:50 He2Zi:107] ('jizi diff', 2401, 0, '')
[I 220831 23:19:50 He2Zi:123] HeZi build success -> C:/data/languages/global\HeZi.txt  C:/data/languages/global\JiZi.txt
[I 220831 23:19:50 ZiCutter:98] C:/data/languages/global\JiZi.txt load  JiZi:2365
[I 220831 23:19:51 ZiCutter:49]   C:/data/languages/global\HeZi.txt JiZi:2365 --> loadHeZi 93746  values:2365
[I 220831 23:19:51 ZiCutter:103] C:/data/languages/global\HeZi.txt HeZi:93746 values:2365
[I 220831 23:19:51 ZiCutter:106] C:/data/languages/global loaded vocab:4399
[I 220831 23:19:51 ZiCutter:98] C:/data/languages/global\JiZi.txt load  JiZi:2365
[I 220831 23:19:51 ZiCutter:49]   C:/data/languages/global\HeZi.txt JiZi:2365 --> loadHeZi 93746  values:2365
[I 220831 23:19:51 ZiCutter:103] C:/data/languages/global\HeZi.txt HeZi:93746 values:2365
[I 220831 23:19:51 ZiCutter:106] C:/data/languages/global loaded vocab:4399
[I 220831 23:19:51 demo:114] ['##co', '7f', '##ap', 'he', '##id', 'ro', '##sq', 'ed', '##le', 'et', '##th', 'ai', '##th', 'u', '##th', 'en', '##th', 'an', '##th', 'a', '##th', 'an', '##th', 'at', '##th', 'ek', '##th', 'an', '##th', 'i', '##th', 'ng', '##th', 'ii', '##th', 'ae', '##th', 'ao', '##th', 'ek', '##th', 'gu', '##th', 'gu', '##th', 'aa', '##th', 'nu', '##th', 'e', '##th', 'ma', '##th', 'ee', '##th', 'ek', '##th', 'ng', '##th', 'ai', '##th', 'ua', '##th', 'ai', '##th', 'a', '##th', 'at', '##th', 'ii', '##th', 'i', '##th', 'at', '##th', 'ee', '##th', 'hu', '##th', 'it', '##th', 'ue', '##ri', 'et', '##ro', 'ht', 'p', 'a', 'y', 's', '##hy', 'us', 'g', '##le', 'et', 'r', 'a', 'n', '##ri', 'et', 'd', '##hy', 'us', 'b', 'l', 'a', 'n', 'c', '##hy', 'us', '##la', 'te', 'l', 'e', 'v', '##la', 'te', '##sp', 'ce', '##ri', 'rk', '##sp', 
'ce', '##le', 'is', '白', '高', '大', '夏', '國', '##ri', 'is', '⿰', '火', '商', '##gr', 'ce', '##ap', 'he', '##cc', 'x0', '0', '0', '⿰', '火', '高']
"""
