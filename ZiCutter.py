import unicodedata
import os

from logzero import logger

import HeZi

YuanZi = '⺀⺁⺂⺃⺄⺅⺆⺇⺈⺉⺊⺋⺌⺍⺎⺏⺐⺑⺒⺓⺔⺕⺖⺗⺘⺙⺚⺛⺜⺝⺞⺟⺠⺡⺢⺣⺤⺥⺦⺧⺨⺩⺪⺫⺬⺭⺮⺯⺰⺱⺲⺳⺴⺵⺶⺷⺸⺹⺺⺻⺼⺽⺾⺿⻀⻁⻂⻃⻄⻅⻆⻇⻈⻉⻊⻋⻌⻍⻎⻏⻐⻑⻒⻓⻔⻕⻖⻗⻘⻙⻚⻛⻜⻝⻞⻟⻠⻡⻢⻣⻤⻥⻦⻧⻨⻩⻪⻫⻬⻭⻮⻯⻰⻱⻲⻳⻴⻵⻶⻷⻸⻹⻺⻻⻼⻽⻾⻿⼀⼁⼂⼃⼄⼅⼆⼇⼈⼉⼊⼋⼌⼍⼎⼏⼐⼑⼒⼓⼔⼕⼖⼗⼘⼙⼚⼛⼜⼝⼞⼟⼠⼡⼢⼣⼤⼥⼦⼧⼨⼩⼪⼫⼬⼭⼮⼯⼰⼱⼲⼳⼴⼵⼶⼷⼸⼹⼺⼻⼼⼽⼾⼿⽀⽁⽂⽃⽄⽅⽆⽇⽈⽉⽊⽋⽌⽍⽎⽏⽐⽑⽒⽓⽔⽕⽖⽗⽘⽙⽚⽛⽜⽝⽞⽟⽠⽡⽢⽣⽤⽥⽦⽧⽨⽩⽪⽫⽬⽭⽮⽯⽰⽱⽲⽳⽴⽵⽶⽷⽸⽹⽺⽻⽼⽽⽾⽿⾀⾁⾂⾃⾄⾅⾆⾇⾈⾉⾊⾋⾌⾍⾎⾏⾐⾑⾒⾓⾔⾕⾖⾗⾘⾙⾚⾛⾜⾝⾞⾟⾠⾡⾢⾣⾤⾥⾦⾧⾨⾩⾪⾫⾬⾭⾮⾯⾰⾱⾲⾳⾴⾵⾶⾷⾸⾹⾺⾻⾼⾽⾾⾿⿀⿁⿂⿃⿄⿅⿆⿇⿈⿉⿊⿋⿌⿍⿎⿏⿐⿑⿒⿓⿔⿕⿖⿗⿘⿙⿚⿛⿜⿝⿞⿟⿰⿱⿲⿳⿴⿵⿶⿷⿸⿹⿺⿻⿼⿽⿾⿿、。〃〄々〆〇〈〉《》「」『』【】〒〓〔〕〖〗〘〙〚〛〜〝〞〟〠〡〢〣〤〥〦〧〨〩〪〭〮〯〫〬〰〱〲〳〴〵〶〷〸〹〺〻〼〽〾〿チ㄀㄁㄂㄃㄄ㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏㄐㄑㄒㄓㄔㄕㄖㄗㄘㄙㄚㄛㄜㄝㄞㄟㄠㄡㄢㄣㄤㄥㄦㄧㄨㄩㄪㄫㄬㄭㄮㄯㆠㆡㆢㆣㆤㆥㆦㆧㆨㆩㆪㆫㆬㆭㆮㆯㆰㆱㆲㆳㆴㆵㆶㆷㆸㆹㆺㆻㆼㆽㆾㆿ㇀㇁㇂㇃㇄㇅㇆㇇㇈㇉㇊㇋㇌㇍㇎㇏㇐㇑㇒㇓㇔㇕㇖㇗㇘㇙㇚㇛㇜㇝㇞㇟㇠㇡㇢㇣㇤㇥㇦㇧㇨㇩㇪㇫㇬㇭㇮㇯㐁㐃㐄㐅㐆㐧㐫㐬㐱㑒㒳㒸㒼㔾㔿㕚㚇㝉㝵㠪㠯㡀㡭㣺㥁㦮㬰㱐㸦䍃䍏䏍䘮䜌一丁丂七丅丆万丈三上下丌不与丏丐丑专且世丗丘丙业东両丣两严並丧丨丩个丫丬中丮丯丰丱串丳丵丶丷丸丹为主丿乀乁乂乃乄久乆乇么义之乌乍乎乏乐乑乒乓乖乗乘乙乚乛乜九乞也习乡书亅了亇予争亊事二亍于亏云互亓五井亘亙亚亜亞亟亠亡交亥亦产享京亶人亻亼亽亾今介仌从仑令以余來侖俞倉僉儿兀允兂元兄兆兇先光克兌免兎兒兔兜入內八公六共其具典兼冂内円冉冊冋册再冎冏冓冖冗冘农冡冫几凡凵凶凸凹出击函刀刁刂刃刄分刍刖列力办勹勺勻勿匀匃包匆匊匋匕化北匚匸區十卂千卄卅升午卉半卌卍卐卑卒卓卜卝卞占卣卤卩卫卬卯厂厃厄厓厤厶厷去厽叀參又叉及友双反发叒叕取叚口古句召可台史右各吅合吉吋同吏吕呂告呙咅咠咸咼品員啇喬單喿噩囗囚四回囟囪囬囷土圥圭坴垂垔垚埀堇堯士壬壴壽夂夅夆夊夋夌夕夗多大夨天太夫夬夭央失头夷夹夾奄奇奚奭女妟娄婁子孑孒孓孚孛宀安宗寸寺寽尃專小少尓尔尗尙尚尞尢尣尤尸尹尺屚屮屯屰山巛巜川州巟巠巤工左巨巫己已巳巴巾巿帀币市帇帚干平年幵并幷幸幺广廌廴廾廿开弋弓弔弗弚弜弟彐彑彔彖彡彳心忄必戈戉戊戋戌戍成我戔或戢戶户戸戼手扌才承支攴攵放敄敢敫文斗斤斥方无旡日旦早旲易昔昚昜是昷曰曱曲曳更曷曾會月有木朩未末本朮术朱朿束来東林果枼柬桼棥欠次止正此步歯歷歹歺殳殸殹殼毋毌母每比毛氏氐民气水氵氶永氺求沓火灬炎炏為無熏爪爫爭爲父爻爾爿片牙牛牜犬犭犮玄率玉王玍玨瓜瓦甘甚生用甩甫田由甲申甴电甹甾畀畐畢番畺畾疋疌疒癶癸發白百皮皿盍監目直真睘睪瞿矍矛矞矢矦石示礻票祭禸禹禺离禾秉秝穴立竹米粛粦糸糹系絲纟缶网罒罓罙羊羌義羽翏老耂者而耑耒耳聿肀肃肅肉肖肙臣臤臥自至臼臽臾臿舀與舌舛舟艮良色艸艹芈莫菐萬蒦虍虎虫血行衣衤衮褱襄襾西覀覃見见角言訁詹譱讠谷豆豈豊豐豕豖象豦豳豸貝貢貴買賁贝贲赤走足身車车辛辰辵辶遂邑邕酉酋釆采里重金釒钅長镸长門门阜阝隶隹隺隻隼雈雙雚雨霝靑青非面靣革韋韦韭音頁页風风飛飞食飠饣首香馬马骨高髟鬥鬯鬲鬼魚鱼鳥鸟鹵鹿麥麦麻黃黄黍黑黹黽黾鼎鼓鼠鼡鼻齊齐齒齿龍龙龜龟龠龰龴龵龶龸龹龺龻卑既爫者艹辶�𠀀𠀁𠀆𠀈𠀉𠀊𠀌𠀍𠀑𠀟𠁁𠁘𠁡𠁢𠁣𠁤𠁦𠁧𠁩𠁰𠁱𠁽𠁾𠁿𠂀𠂁𠂂𠂆𠂇𠂈𠂉𠂊𠂍𠂎𠂒𠂙𠂜𠂢𠂣𠂤𠂭𠂯𠂼𠂿𠃉𠃊𠃋𠃌𠃍𠃎𠃑𠃓𠃛𠃜𠃢𠃬𠄌𠄎𠄓𠄙𠆢𠑹𠔗𠔧𠕁𠕄𠕋𠕒𠕲𠘧𠘨𠙴𠚒𠡦𠤎𠤬𠥓𠥻𠥼𠥽𠦁𠦆𠦑𠦒𠦟𠫓𠬝𠬤𠱩𠷽𡆪𡆵𡈼𡕒𡗒𡗕𡗗𡗚𡗜𡗾𡘼𡙁𡤾𡬝𡭔𡯁𡰣𡰧𡰴𡳾𡳿𡴀𡷩𡸁𡾍𡿦𡿨𢀑𢀖𢀚𢀳𢁺𢄉𢆍𢇁𢇈𢇍𢊁𢌰𢎗𢎜𢎟𢎠𢎣𢎧𢎨𢎯𢎱𢏚𢑚𢖩𢦍𢦏𢦐𢦑𢦒𢪐𣅯𣅲𣇓𣎳𣎴𣎵𣎺𣏲𣐺𣒚𣥂𣦶𣫬𣬛𣶒𤉢𤊱𤓰𤕣𤕤𤣥𤣩𤦡𤮺𤯓𤰃𤰔𤰱𤰶𤱑𤲥𤴓𤴔𥁕𥄉𥆞𥈜𥈠𥈸𥘅𥝌𥫗𥸨𦈢𦉭𦍌𦏲𦘒𦝸𦣝𦣞𦥑𦥒𦥫𦥮𦥺𦫵𦰩𧑴𧘇𧰧𧰨𧾷𨈏𨈐𨈑𨤏𨳇𨸏𩇦𩇧𩇨𩙱𩙿𩰊𩰋𪓕𪓝𪚦𪛉𪜀𪜃𪜊𪤵𪩲𫂱𫝀𫝁𫝃𫝄𫝅𫝆𫝇𫝉𫝔𫝕𫝖𫞓𫞕𫞖𫞟𫞪𫟈𫟋𫟚𫠠𫠣𫡃𫡆𫡑𫤬𫧋𫩏𫩑𫩙𫬯𫭒𫯛𫵎𫷃𬂛𬊓𬺶𬺷𬺹𬺻𬻆𬻇𬻒𬻫𬼂𬼄𬼉𬼘𬼺𬽡𭀜𭅰𭈰𭐳𭕄𭖈𭠍𭴚𭺛𭺪𮂸𮍌𮠕𮠚屮廾'

def slim(v):
    if len(v) <= 3:
        return v
    for x in v[1:-1]:
        if x < '⿰' or x > '⿻':
            w = v[0]+x+v[-1]
            return w
    return v


def loadHeZi(path, lite=True):
    HeZi = {}
    for l in open(path):
        w = l.strip().split('\t')
        k, v = w
        if k[0] == star:
            d = 0
        if lite:
            v = slim(v)
        HeZi[k] = v
    values = ''.join(HeZi.values())
    values = list(set(values))
    values.sort()
    return HeZi,values


def gen_bigrams():
    nums = ''.join(chr(i) for i in range(ord('0'), ord('9')+1))
    az = ''.join(chr(i) for i in range(ord('a'), ord('z')+1))
    alphabet = az+nums
    az2 = [x+y for x in az for y in az]
    nums2 = [x+y for x in nums for y in nums]
    idxs= ["#"+x for x in alphabet]
    words = list(alphabet)+az2+nums2+idxs
    return words

Bigrams = gen_bigrams()

class ZiCutter:
    def __init__(self, dir=""):
        """
        HeZiBase="","Yuan","Ji"
        """
        self.HeZi = {}
        self.vocab = Bigrams
        self.HeZiPath=os.path.join(dir,"HeZi.txt")
        if os.path.exists(self.HeZiPath):
            HeZi, values = loadHeZi(self.HeZiPath)
            logger.info(
                f" ZiCutter {self.HeZiPath} --> loadHeZi {len(HeZi)} vocab:{len(values)}")
            self.HeZi = HeZi
            self.vocab += values
    
    def build(self,roots):
        JiZi = self.vocab+list(YuanZi)+roots
        HeZi.build(JiZi, ChaiZiPath="data/ChaiZi.txt", YiTiZiPath="data/YiTiZi.txt",
                         HeZiPath="data/HeZi.txt", BasePath="data/JiZI.txt")


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
            r = name[-1].lower()
            tokens += [l, '#'+r]
        except:
            r = ord(char) % 100
            s = '#'+f'0{r}'[-2:]
            tokens = [s]
        return tokens

    def cutChar(self, char):
        assert len(char) == 1
        if char in self.HeZi:
            t = self.cutHan(char)
            return list(t)
        else:
            t = self.cutRare(char)
            return t


if __name__ == "__main__":
    star = "𱊮"

    He2Yuan,vocab = loadHeZi("HeZi/He2Yuan.txt")
    He2Ji,vocab = loadHeZi("HeZi/He2Ji.txt")

    print(star, He2Yuan.get(star, star))
    print(star, He2Ji.get(star, star))
    """
    𱊮 ⿵亡鳥
    𱊮 ⿵亡鳥
    """
    line = "'〇㎡[คุณจะจัดพิธีแต่งงานเมื่อไรคะัีิ์ื็ํึ]Ⅷpays-g[ran]d-blanc-élevé » (白高大夏國)'"
    path = "HeZi/He2Yuan.txt"
    # path = "HeZi/He2Ji.txt"
    cutter = ZiCutter(path)
    for c in line:
        if c == '夏':
            d = 0
        print(cutter.cutChar(c))
