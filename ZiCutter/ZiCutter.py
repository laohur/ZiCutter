import unicodedata
import os

from logzero import logger

from UnicodeTokenizer import UnicodeTokenizer

from ZiCutter import He2Zi

import importlib
from importlib.resources import files
# data_text = files('mypkg.data').joinpath('data1.txt').read_text()

YuanZi = '⺀⺁⺂⺃⺄⺅⺆⺇⺈⺉⺊⺋⺌⺍⺎⺏⺐⺑⺒⺓⺔⺕⺖⺗⺘⺙⺚⺛⺜⺝⺞⺟⺠⺡⺢⺣⺤⺥⺦⺧⺨⺩⺪⺫⺬⺭⺮⺯⺰⺱⺲⺳⺴⺵⺶⺷⺸⺹⺺⺻⺼⺽⺾⺿⻀⻁⻂⻃⻄⻅⻆⻇⻈⻉⻊⻋⻌⻍⻎⻏⻐⻑⻒⻓⻔⻕⻖⻗⻘⻙⻚⻛⻜⻝⻞⻟⻠⻡⻢⻣⻤⻥⻦⻧⻨⻩⻪⻫⻬⻭⻮⻯⻰⻱⻲⻳⻴⻵⻶⻷⻸⻹⻺⻻⻼⻽⻾⻿⼀⼁⼂⼃⼄⼅⼆⼇⼈⼉⼊⼋⼌⼍⼎⼏⼐⼑⼒⼓⼔⼕⼖⼗⼘⼙⼚⼛⼜⼝⼞⼟⼠⼡⼢⼣⼤⼥⼦⼧⼨⼩⼪⼫⼬⼭⼮⼯⼰⼱⼲⼳⼴⼵⼶⼷⼸⼹⼺⼻⼼⼽⼾⼿⽀⽁⽂⽃⽄⽅⽆⽇⽈⽉⽊⽋⽌⽍⽎⽏⽐⽑⽒⽓⽔⽕⽖⽗⽘⽙⽚⽛⽜⽝⽞⽟⽠⽡⽢⽣⽤⽥⽦⽧⽨⽩⽪⽫⽬⽭⽮⽯⽰⽱⽲⽳⽴⽵⽶⽷⽸⽹⽺⽻⽼⽽⽾⽿⾀⾁⾂⾃⾄⾅⾆⾇⾈⾉⾊⾋⾌⾍⾎⾏⾐⾑⾒⾓⾔⾕⾖⾗⾘⾙⾚⾛⾜⾝⾞⾟⾠⾡⾢⾣⾤⾥⾦⾧⾨⾩⾪⾫⾬⾭⾮⾯⾰⾱⾲⾳⾴⾵⾶⾷⾸⾹⾺⾻⾼⾽⾾⾿⿀⿁⿂⿃⿄⿅⿆⿇⿈⿉⿊⿋⿌⿍⿎⿏⿐⿑⿒⿓⿔⿕⿖⿗⿘⿙⿚⿛⿜⿝⿞⿟⿰⿱⿲⿳⿴⿵⿶⿷⿸⿹⿺⿻⿼⿽⿾⿿、。〃〄々〆〇〈〉《》「」『』【】〒〓〔〕〖〗〘〙〚〛〜〝〞〟〠〡〢〣〤〥〦〧〨〩〪〭〮〯〫〬〰〱〲〳〴〵〶〷〸〹〺〻〼〽〾〿チ㄀㄁㄂㄃㄄ㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏㄐㄑㄒㄓㄔㄕㄖㄗㄘㄙㄚㄛㄜㄝㄞㄟㄠㄡㄢㄣㄤㄥㄦㄧㄨㄩㄪㄫㄬㄭㄮㄯㆠㆡㆢㆣㆤㆥㆦㆧㆨㆩㆪㆫㆬㆭㆮㆯㆰㆱㆲㆳㆴㆵㆶㆷㆸㆹㆺㆻㆼㆽㆾㆿ㇀㇁㇂㇃㇄㇅㇆㇇㇈㇉㇊㇋㇌㇍㇎㇏㇐㇑㇒㇓㇔㇕㇖㇗㇘㇙㇚㇛㇜㇝㇞㇟㇠㇡㇢㇣㇤㇥㇦㇧㇨㇩㇪㇫㇬㇭㇮㇯㐁㐃㐄㐅㐆㐧㐫㐬㐱㑒㒳㒸㒼㔾㔿㕚㚇㝉㝵㠪㠯㡀㡭㣺㥁㦮㬰㱐㸦䍃䍏䏍䘮䜌一丁丂七丅丆万丈三上下丌不与丏丐丑专且世丗丘丙业东両丣两严並丧丨丩个丫丬中丮丯丰丱串丳丵丶丷丸丹为主丿乀乁乂乃乄久乆乇么义之乌乍乎乏乐乑乒乓乖乗乘乙乚乛乜九乞也习乡书亅了亇予争亊事二亍于亏云互亓五井亘亙亚亜亞亟亠亡交亥亦产享京亶人亻亼亽亾今介仌从仑令以余來侖俞倉僉儿兀允兂元兄兆兇先光克兌免兎兒兔兜入內八公六共其具典兼冂内円冉冊冋册再冎冏冓冖冗冘农冡冫几凡凵凶凸凹出击函刀刁刂刃刄分刍刖列力办勹勺勻勿匀匃包匆匊匋匕化北匚匸區十卂千卄卅升午卉半卌卍卐卑卒卓卜卝卞占卣卤卩卫卬卯厂厃厄厓厤厶厷去厽叀參又叉及友双反发叒叕取叚口古句召可台史右各吅合吉吋同吏吕呂告呙咅咠咸咼品員啇喬單喿噩囗囚四回囟囪囬囷土圥圭坴垂垔垚埀堇堯士壬壴壽夂夅夆夊夋夌夕夗多大夨天太夫夬夭央失头夷夹夾奄奇奚奭女妟娄婁子孑孒孓孚孛宀安宗寸寺寽尃專小少尓尔尗尙尚尞尢尣尤尸尹尺屚屮屯屰山巛巜川州巟巠巤工左巨巫己已巳巴巾巿帀币市帇帚干平年幵并幷幸幺广廌廴廾廿开弋弓弔弗弚弜弟彐彑彔彖彡彳心忄必戈戉戊戋戌戍成我戔或戢戶户戸戼手扌才承支攴攵放敄敢敫文斗斤斥方无旡日旦早旲易昔昚昜是昷曰曱曲曳更曷曾會月有木朩未末本朮术朱朿束来東林果枼柬桼棥欠次止正此步歯歷歹歺殳殸殹殼毋毌母每比毛氏氐民气水氵氶永氺求沓火灬炎炏為無熏爪爫爭爲父爻爾爿片牙牛牜犬犭犮玄率玉王玍玨瓜瓦甘甚生用甩甫田由甲申甴电甹甾畀畐畢番畺畾疋疌疒癶癸發白百皮皿盍監目直真睘睪瞿矍矛矞矢矦石示礻票祭禸禹禺离禾秉秝穴立竹米粛粦糸糹系絲纟缶网罒罓罙羊羌義羽翏老耂者而耑耒耳聿肀肃肅肉肖肙臣臤臥自至臼臽臾臿舀與舌舛舟艮良色艸艹芈莫菐萬蒦虍虎虫血行衣衤衮褱襄襾西覀覃見见角言訁詹譱讠谷豆豈豊豐豕豖象豦豳豸貝貢貴買賁贝贲赤走足身車车辛辰辵辶遂邑邕酉酋釆采里重金釒钅長镸长門门阜阝隶隹隺隻隼雈雙雚雨霝靑青非面靣革韋韦韭音頁页風风飛飞食飠饣首香馬马骨高髟鬥鬯鬲鬼魚鱼鳥鸟鹵鹿麥麦麻黃黄黍黑黹黽黾鼎鼓鼠鼡鼻齊齐齒齿龍龙龜龟龠龰龴龵龶龸龹龺龻卑既爫者艹辶�𠀀𠀁𠀆𠀈𠀉𠀊𠀌𠀍𠀑𠀟𠁁𠁘𠁡𠁢𠁣𠁤𠁦𠁧𠁩𠁰𠁱𠁽𠁾𠁿𠂀𠂁𠂂𠂆𠂇𠂈𠂉𠂊𠂍𠂎𠂒𠂙𠂜𠂢𠂣𠂤𠂭𠂯𠂼𠂿𠃉𠃊𠃋𠃌𠃍𠃎𠃑𠃓𠃛𠃜𠃢𠃬𠄌𠄎𠄓𠄙𠆢𠑹𠔗𠔧𠕁𠕄𠕋𠕒𠕲𠘧𠘨𠙴𠚒𠡦𠤎𠤬𠥓𠥻𠥼𠥽𠦁𠦆𠦑𠦒𠦟𠫓𠬝𠬤𠱩𠷽𡆪𡆵𡈼𡕒𡗒𡗕𡗗𡗚𡗜𡗾𡘼𡙁𡤾𡬝𡭔𡯁𡰣𡰧𡰴𡳾𡳿𡴀𡷩𡸁𡾍𡿦𡿨𢀑𢀖𢀚𢀳𢁺𢄉𢆍𢇁𢇈𢇍𢊁𢌰𢎗𢎜𢎟𢎠𢎣𢎧𢎨𢎯𢎱𢏚𢑚𢖩𢦍𢦏𢦐𢦑𢦒𢪐𣅯𣅲𣇓𣎳𣎴𣎵𣎺𣏲𣐺𣒚𣥂𣦶𣫬𣬛𣶒𤉢𤊱𤓰𤕣𤕤𤣥𤣩𤦡𤮺𤯓𤰃𤰔𤰱𤰶𤱑𤲥𤴓𤴔𥁕𥄉𥆞𥈜𥈠𥈸𥘅𥝌𥫗𥸨𦈢𦉭𦍌𦏲𦘒𦝸𦣝𦣞𦥑𦥒𦥫𦥮𦥺𦫵𦰩𧑴𧘇𧰧𧰨𧾷𨈏𨈐𨈑𨤏𨳇𨸏𩇦𩇧𩇨𩙱𩙿𩰊𩰋𪓕𪓝𪚦𪛉𪜀𪜃𪜊𪤵𪩲𫂱𫝀𫝁𫝃𫝄𫝅𫝆𫝇𫝉𫝔𫝕𫝖𫞓𫞕𫞖𫞟𫞪𫟈𫟋𫟚𫠠𫠣𫡃𫡆𫡑𫤬𫧋𫩏𫩑𫩙𫬯𫭒𫯛𫵎𫷃𬂛𬊓𬺶𬺷𬺹𬺻𬻆𬻇𬻒𬻫𬼂𬼄𬼉𬼘𬼺𬽡𭀜𭅰𭈰𭐳𭕄𭖈𭠍𭴚𭺛𭺪𮂸𮍌𮠕𮠚屮廾'


def slim(v):
    if len(v) <= 3:
        return v
    for x in v[1:-1]:
        if x < '⿰' or x > '⿻':
            w = v[0]+x+v[-1]
            return w
    if len(v)!=3:
        logger.error(v)
    return v


def valid(seq, Ji):
    for x in seq:
        if x not in Ji:
            return 0
    return 1


def odd(seq):
    s = slim(seq)
    for x in s:
        if not UnicodeTokenizer.detect_hanzi(x):
            return 1
    return 0


def loadHeZi(path, JiZi=set()):
    doc = open(path).read().splitlines()
    doc = [x.split('\t') for x in doc]
    doc = [(k, slim(v)) for k, v in doc]
    if JiZi:
        doc = [(k, v) for k, v in doc if valid(v, JiZi)]
    else:
        doc = [(k, v) for k, v in doc if not odd(k) ]
    HeZi = {k: v for k, v in doc if k != v}
    values = ''.join(HeZi.values())
    values = list(set(values))
    values.sort()
    logger.info(
        f"  {path} JiZi:{len(JiZi)} --> loadHeZi {len(HeZi)}  values:{len(values)}")
    return HeZi, values


def gen_bigrams():
    nums = ''.join(chr(i) for i in range(ord('0'), ord('9')+1))
    az = ''.join(chr(i) for i in range(ord('a'), ord('z')+1))
    alphabet = az+nums
    az2 = [x+y for x in az for y in az]
    nums2 = [x+y for x in nums for y in nums]
    grams2 = [x+y for x in alphabet for y in alphabet]
    idxs = ["#"+x for x in az2]
    words = list(alphabet)+grams2+idxs
    return words


Bigrams = gen_bigrams()


class ZiCutter:
    def __init__(self, dir=""):
        """
        HeZiBase="","Yuan","Ji"
        """
        self.vocab = set(Bigrams) | set(YuanZi)
        self.HeZi = {}

        self.here = os.path.dirname(__file__)
        self.HanZi = os.path.join(self.here, "HanZi")

        self.dir = self.dir if dir else self.HanZi
        self.HeZiPath = os.path.join(self.dir, "HeZi.txt")
        self.JiZiPath = os.path.join(self.dir, "JiZi.txt")
        # print(files('ZiCutter'))
        # data_text = files('ZiCutter').joinpath('ChaiZi.txt').read_text()
        self.load()

    def load(self):
        JiZi=set(YuanZi)
        if os.path.exists(self.JiZiPath):
            values = open(self.JiZiPath).read().splitlines()
            JiZi |= set(values)
        logger.info(            f"{self.JiZiPath} load  JiZi:{len(JiZi)}")
        JiZi |= self.vocab

        HeZi, values = loadHeZi(self.HeZiPath, self.vocab)
        logger.info(f"{self.HeZiPath} HeZi:{len(HeZi)} values:{len(values)}")
        self.HeZi = HeZi
        self.vocab |= set(values)
        logger.info(f"vocab:{len(self.vocab)}")

    def build(self, roots=[]):
        import logzero
        logzero.logfile(os.path.join(self.dir,"build.log"),"w")
        logger.info(f" {self.dir} building")
        self.vocab = set(Bigrams)
        self.HeZi = {}
        self.HeZiPath = os.path.join(self.dir, "HeZi.txt")
        self.JiZiPath = os.path.join(self.dir, "JiZi.txt")
        JiZi = Bigrams+list(YuanZi)+roots
        JiZi=[ x for x in JiZi if len(x)==1 ]
        self.vocab=set(JiZi)
        He2Zi.build(JiZi, ChaiZiPath=os.path.join(self.HanZi, "ChaiZi.txt"), YiTiZiPath=os.path.join(self.HanZi, "YiTiZi.txt"),
                    HeZiPath=self.HeZiPath, JiZiPath=self.JiZiPath)
        self.load()

    def cutHan(self, zi, shrink=True):
        ids = self.HeZi.get(zi, zi)
        if shrink:
            s = slim(ids)
            return s
        return ids

    def cutRare(self, char):
        assert len(char) == 1
        tokens = []
        try:
            name = unicodedata.name(char)
            l = name[:2].lower().split('-')[0].split()[0]
            r = name[-2:].lower().strip()
            tokens += ['#'+l, r]
        except:
            catg = unicodedata.category(char)
            l = catg[:2].lower()
            r = ord(char) % 100
            s = f'0{r}'[-2:]
            tokens = ['#'+l, s]
        return tokens

    def cutChar(self, char):
        assert len(char) == 1
        if char in self.vocab:
            return [char]
        if char in self.HeZi:
            t = self.cutHan(char)
            return list(t)
        else:
            t = self.cutRare(char)
            return t


if __name__ == "__main__":
    star = "𱊮"

    HeZi, vocab = loadHeZi("data/ChaiZi.txt", set(YuanZi))

    print(star, HeZi.get(star, star))
    """
    𱊮 ⿵亡鳥
    𱊮 ⿵亡鳥
    """
    line = "'〇㎡[คุณจะจัดพิธีแต่งงานเมื่อไรคะัีิ์ื็ํึ]Ⅷpays-g[ran]d-blanc-élevé » (白高大夏國)😀熇'\x0000"

    # build
    cutter = ZiCutter(dir="")
    cutter.build()

    # use
    cutter = ZiCutter(dir="")
    for c in line:
        print(cutter.cutChar(c))

"""
[I 220626 19:34:03 He2Zi:36] giveup:0 
[I 220626 19:34:04 He2Zi:39] epoch:0 base:8204 --> 2611 
[I 220626 19:34:05 He2Zi:36] giveup:0 
[I 220626 19:34:08 He2Zi:39] epoch:1 base:2611 --> 1774 
[I 220626 19:34:09 He2Zi:36] giveup:0 
[I 220626 19:34:11 He2Zi:39] epoch:2 base:1774 --> 1760 
[I 220626 19:34:11 He2Zi:36] giveup:0 
[I 220626 19:34:12 He2Zi:39] epoch:3 base:1760 --> 1760 
[I 220626 19:34:12 He2Zi:36] giveup:0 
[I 220626 19:34:13 He2Zi:39] epoch:4 base:1760 --> 1760 
[I 220626 19:34:31 He2Zi:36] giveup:1139 𫟁𥝩𥩴𪦭島𬔄毈𩦫𪷺𭙺𤎄紪𣌰𮢇𭴺𢊸䢜𠉯捣𭸛𫦱𰜊𰓚𩕴𫺄㱭蝐𭣕𮣝𫹲𬄒𨺽㒻𫉩𭅍𫲃𭲰②𠏟𦡿𧷃𰿟𢰂⑥燣𮇓𦀩𡖠𨔕𫏦④𤈊𫆵㥣𫑾𠋐䃵𦯤⑨扗い𭳛𭽂𠆖𩖋⑧�𰂿𤾤𩃊𣻴𠬎𭀥𤴟𭞕𦪷𭣞𢉺𰡹韡韡𬔨𰯳𰻆𦷠㒟螐𢺫𡪍𬂋𭎯𣧱𥤆𬚦𦪠𪬢𡇾𬪙𢡘𡹭𥕠𰻮嬅𣐦𤈂侟𦷊帽華蔫△𢞨𤫃𧠁𩐲𤀙𣹋𪥀𫑀𡺑𣨼𮯆𧡉𡜛𪲪𢮴茬韀煅𨟏嵽𨜑𤲈𭆴𤺡𪜥艒𡹙𧿗𧁁𧒬𣞦𪈽冐𦗉𮧵𠎑𥍙𭣨𫓓塅𣖺�
𭓁𬵪𣟦𢴶帽𦻺𣗫𡉠𡏭瞱瞱譓𩕤𪳦𣝄𰟀𠕙𧽋𤏑𪟥嘩𢝪𤃢䃀𨒸疄𤔞𢋴𤑖𨓼𬟏ヨ𥑯𨏼冑𢠞𠩻𤓟𢤭𭆱𤌰𪒜葮𠓮腶褭𫺆慸㥼𢝌𣸰𧂘𭡈𭸞𢯫𤒹𩤣顲顲淒𥲭𥻼𧄟𡠄𠈚𭁐賵𨩩搗殢廩𤡔𫽲𠝉鍛朂𩎇𤓥𬰶㒾𩃅𭆩檁𭤋 
臶𤑓𥚕𫨬𮑨𧂽𭭧𡃦𦇵𮔙𠎖𢢐鴵𧴇𭖘𭇩𦻇𡀀𦽏𭲳𡯼冕𦼇𢅊𤴘𦂰𩋾𤢤𭖲𪦋𤚶勖𦦺𫘙𭙧𫨻𬋢𡄁𢶸𢾟𨶱𩋋𭙙𭩩𦨧𰍏𦢵𡖪岛𩸸滯𫌈䑵𤥥𥛵𦪴ℓ𪪨𤍾𭪚癛𬞶𫌿𠞆⑭嬝𩥜𫳖𮕹𠗩𬾹𪄝𣑊𡠹𨄛𣔺𰧬𭀣𣢔㠀𬆸懍𣥋𫰡𮔇�𠱽𫂵𮇭𢋕𠛆𢤔𬿻𣯀𥣼𮘥りり𠌵𣴁𬀘𮋍𥛸穟𨺆𨳀𤾏𠩯𦘎𰏕𣍫𭿖𡀮繐𠲁𭦁𮔒𠌶𢨖𦾰𧘧𪛃𮃞𰺣鳧拵𡣣𩻮𪊩𬃅㡌𤨃𧕔溩𬻥𰘀𬯶𡅁𦋓𫮖𫦲𨶄𥠠𠕦𤕦𪽜鷍𡗋𬼗嘕艜凄𰂶爨𤪧𢋏𠡼䖚𰸛𥤂𦅠𪗍𢁎𩉾𭳘𠌥↷𩿋𡻺穗禀�
䦄䦄𧵿𫅆𦦰銌𥈨𭁟𭫿塢嵨𥗗𭬢𤑎萋𫖛䗖珔𣺏𪥼𧂶𠕚⑮𭩲𥜘𭵹𰬸韢𨗍蹛𨞴𠅤𩇆蹸⑤𣻉𫉿噝𡉈鰞𡫛𦺟𫩊𤎭𪲒㱕冒𱈯𪾫霋𣟊𧱊𬋅𰨇𧡕𤇟𠒎棲𠦽𥾳𦮵𮜩𰏼𰒒𬒛𭏬𢲄𮎳⑪𥋶㠡𧓂𡚅𥉼鄢𨓂𨭤𩎂𨖮𠆡𢭏䙊𨺔𮒮蝃𨘬�
𠕮嫋嫋瑦𩋦郪𫔴𡫌𣧺𬊷𨿩嫣𫄊𬜻𠻭𠽠䗡𢺬𩐯惠𨀬𫑴𥢁𦣽𤒐𩾓䮉𭱎𧟺𨽖𰰏媢𦍖㜵𭚐𰒥帴𣿆𧞡𥕧𰜬𫞌𥭿𠘐𫋇𩆐﨩壺𢷍𢯾𤉐𠰇栫𭽶𢊇𩀵𩏬𪞕𭬍𫛓𭻟𫴘㒽懔𰾶焉𭇢鏸𧬽𩏧𮞅𢶈𦶀𢙮𢄓𦼹擣峌𫽐嬽𤆡𧽞𠩿㵯𰧿
𨰔③𢥁𪎐𫋂𥛣𭜤𡻜𧹮凫𥠌凜𢛡𥇳𧂑寡袅𧃱𦦾𫂠𩛖𬐑郻𧟾𫭇譁𣷑𢈺㐭緀摕𫃅嶋𢋱𪯜冔𭗃𭵄𰑵𠢨絻𫚃𬟠𤑇𩜝𠘅𫞼𧑺𢏻𭱩𭐣丝𰭍𦖶𩎰𰁿𣪃𠘡鶈𥞘𧚇𢷭𫆯𬅌𭚡𭌾𥮂𭦢𢊬𦇩𪞌𠱜𠵄𤽪𧦮𠡘𦾓𨞶𩾖華𭱐𮗙𩌵𧎚𰬢
蟪𠬣𭂛蟂僡𧋃𨗼𢀮𬋡碫𠭂𮚐𫡿𭸯𦇠𦰌𠏵⑫巋𰐣𡙞緞隯𢇭𦆚𢀤𠀪𬝂𬸴㨶㴘𢷬𦀒𦔀𫲉𧋍咝𣦨𡚖コ𨚲𬻑𢁤𡥂𣭌𡭳𧃹澟𭖸𫑃𬡇㠏𨎺α𮭹漹𭻊藺嶌𢄩𠁑𨪇懘𤶐𭳩𠐫寭𢵴𡓔𤜓𦽹燷荐𩈺𢊣挔𣱭归𦎮槝𢶑𱀠㟆癝锻�𮓢䉮䉮𢳚𭻝瑁𬇵𡜒㦅㪞𡈌𦆉𮚊𭱽潓𢅦𦳓𤳩𡟼𠆜裊𨫍𤁜㫯𢸣樺㒿𣆱𢞯𬻘𦠜𡿢𫱮𡩼𭔥𭮴𮡭𭮖𪠈𮔰妻𪦂𡬜𨘛𰖩鄥𩌗𭡣𤋛熶𬗋𤸼𬊥𠆣𠳲䡧𬻱䳋𛂦存⑦䕲鎢壈𤹄⑩冕𠆗𨣄𮃦璤𮒿烏䧥蔺𡚣縀𧷄𫝵𣘖枭𣶀𭲞恵𰏓𢂣
㛿躪𦡣𧅍鳳橞躙𨎹爨𣝲⑲𪷤熓𨺜𩌴𫶇𮄣䙚傿𡄉𡽼悽𦅵𪂗𫸼𭌨𭧢𭵈𭺺𬩞岿𦣵𨺣𭤪𣄒憓𩮟袸𮣨㼮勗①𨒢𫅞𭩟𣑛𰊎凛𤊳𠘟𡼄𠳧𭄐褄𪦾𠏶𩌮𨜇𩽃𨀔𮩭𦵍𭥟𦾏𩏇𠆋𬺡瑖𡝽赗𣓍年𫄍椛轥𨬋𡩝𠨦𩍽梟𡋬𭘲𠀄䌯𫖤�𨏸𣎋冃冃𭽁𦿬𫒿𣏱𨏦𬟘𠪕鳬𣤝𬀼𦂔𡙪㯊螮𭈭𠂶𨽅𩾏𫑚㯂⑯𫭣𮓠𭼾𡑩𧆕𫿣𡐝𬚭𪉊𭾊𪃑𡈘？サ𣺙𢞬𰬜𤞐㸑𰌬𠕖𠰡躏𧝥𩼤𭣪𢽵𥠂𤲱𭻋㮧凜𭶂𫏗隝𦊯𬑓𣸼檩㒻𡜌𢽢䠠洊𬻞𮔜𢧝𨩷藺𫪮𢤅𦼯𢳃𦛊𣚝𧠊𮅏𢤺缎㯛
崼銯𫷀よ𬄜𬤝㦊毷𠕥鸶𰅻鄡鷨𡾭壷𨉨䅿澕𩏲𪋴𰔇𨮍𤣽𭭘𩂲𡷊𠰟𤂃𦇅廗煅𤲰𧜵𰲟𬬢𣻥㺺𪟊𥒛焨𦾛𭐥𬹢𡚇𭔌𬷶在𦑐椴𠅂𠙒廪𡻅𰲞𱈝𨱸𫴢𠆿𥄽⑬冒鞯𩾒韉𠬷𡫎𩏚蕙𠓶𬘄𰸚𮕋𬅅閵𫲳遰𬟉𨶇篶𣹂𢞻𧛕𪱇𤏷𭊰
𰥡𨘄𣓝㭚𥨗𢻀𤂶𤯑𭼪𠥖𰄕𮜟𡠿𩾣𫸪𠪅䲷𦋤𪣋嗚𫿝𫸀𥩷𪼚萺𠌚𠕬𭞛段𡝣𧑍𫒯𡜈𮡪嶹𦣩𡀫𣐩𬒢𠍩𤒢𡅓𭲀𮑩𰼾𪵕帶𨆴稟
[I 220626 19:34:32 He2Zi:39] epoch:5 base:1760 --> 1719 
[I 220626 19:34:32 He2Zi:36] giveup:0 
[I 220626 19:34:33 He2Zi:39] epoch:6 base:1719 --> 1719 
[I 220626 19:34:33 He2Zi:36] giveup:0 
[I 220626 19:34:34 He2Zi:39] epoch:7 base:1719 --> 1719 
[I 220626 19:34:34 He2Zi:101] 
[I 220626 19:34:34 He2Zi:117] HeZi build success -> HeZi.txt  JiZI.txt
[I 220626 19:34:35 ZiCutter:32]   HeZi.txt --> loadHeZi 93330  values:1719
[I 220626 19:34:35 ZiCutter:74] ZiCutter load HeZi:93330 JiZi:1719
[I 220626 19:34:35 ZiCutter:32]   HeZi.txt --> loadHeZi 93330  values:1719
[I 220626 19:34:35 ZiCutter:74] ZiCutter load HeZi:93330 JiZi:1719
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
