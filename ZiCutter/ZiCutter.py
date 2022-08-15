import unicodedata
import os

from logzero import logger

import UnicodeTokenizer

from ZiCutter import He2Zi


# 2365
GouJian = "↔↷③④⑦⺀⺄⺆⺈⺊⺌⺕⺝⺸⺼⿰⿱⿲⿳⿴⿵⿶⿷⿸⿹⿺⿻〢コユ㇁㇂㇄㇇㇈㇉㇓㐁㐄㐅㐌㐫㐬㐭㐮㐱㑒㒵㒸㒼㓁㓞㔾㕛㕣㖾㘝㚅㚇㚔㚘㝉㝡㝴㝵㞋㞢㞷㠩㠭㠯㡀㡭㡿㢲㢴㣇㣺㥯㪅㫄㫐㫒㫺㬅㬎㬥㬰㲋㳄㷠㸒㸚㸦㼌㼲㽞㿟䀠䂞䍃䏍䒑䖍䖒䖝䖵䙴䚻䜌䝿䡛䧹䪞一丁丂七丄丅丆万丈三上下丌不与丏丐丑专且丕世丘丙业东丞丢丣两严並丨丩个丫丬中丮丰丱串丵丶丷丸丹为主丽丿乀乂乃久乆乇么义之乌乍乎乏乐乑乔乖乗乘乙乚乛乜九乞也习乡乳乾亀亅了亇予争事二亍于亏亐云互亓五井亘亚亜亞亟亠亡亢交亥亦产亨亩享京亭亮亯亰亲亳亶亷人亻亼亾仁今介仌从仐仑仒仓仕他付仝代令以任企伊伏伐休会伯但位何佘余作佥使來侈侌侖侯侵便保俞信修倉倍候倠備僉僕儿兀允兂元兄充兆兇先光兊克兌免兑兒兓兔党兜兟入全兩兪八公六兮兰共关兵其具典兹兼冀冂冃冄内冈冉冊冋册再冎冏冐冒冓冖冗冘军农冝冡冥冫冬冷几凡凢凵凶凷凸凹出函凾刀刁刂刃刄刅分切刍刑刕刖列刘则初別利别到制刺則削剌前剡剽劉力功加劦助劫劳劵勃勇勉勒動務勞勤勹勺勻勾勿匀匂包匆匈匊匋匍匕化北匚匝匡匪匱匸匹区医匽匿區十卂千卄卅卆升午卉半卌华卑卒卓单卖南卜卝卞占卡卢卣卤卦卩卪卬卯印危即却卵卷卸卻厂厃厄历厈厉厌厓厘厚原厤厥厨厭厲厶厷厸去厼厽叀参參叅又叉及友双反叐发叒叔叕取受叚叜叟口古句另叩只召可台叱史右叵号司叹吂各吅合吉吊吋同名后吏向吕君吝吞否含启吳吴吹吾呂呆呈告员呙周命咅和咎咠咢咨咸咼哀品哉員哥哲唐商啇問啚啬啻善喜喬單喿嗇噩嚴囊囗囘囙囚四回囟因囧囬困囱囷固国圂圅國圍圓土圡圣圥在圭地圶圼坐坒坚坴垂垔垚埀埋埶執基堂堅堆堇堯塞墨壘士壬壯声壳壴壹壺壽夂处夅夆备夊夋夌复夏夒夕外夗夘多夜夢大夨天太夫夬夭央失夲头夷夸夹夻夾奂奄奇奈奉奎奏奐契奓奔奚奞奠奢奥奭女奴奻好如妄妙妟妥妻妾姑委姜威娄婁婴嬰嬴子孑孔孕孖字存孚孛孝孟季孤学孫孱學宀宁宂它宅宇守安宋完宏宓宗官定宛宜宝客宣室宮宰害家容宾宿寄寅密富寒察寧審寫寬寮寸对寺寻寽対寿封尃射将將專尉尊尋尌對小少尒尓尔尖尗尚尞尢尣尤尧尨尭就尸尹尺尻尼尽尾尿局居屈屋屎屏屑展屖屚属屠屡屬屮屯屰山屵屾岁岂岑岡岩岳岸峯島崇崑崔崖崙崩嵬嶲巂巛川州巟巠巢巤工左巧巨巩巫差己已巳巴巷巸巽巾巿帀市布希帚帛帝带師席帶常干平年幵并幷幸幺幻幼幽幾广広庄床底店庚府度庫庭庶康庸廉廌廛廣廩廴延廷建廾廿开弁弃弄弇弋式弓弔引弗弘弜弟弥弦弱張強强彊彌彎彐彑当彔录彖彗彡形彥彦彧彭彳役彼往待律徒得徙從復微徵心忄必忌忍志忝忠忩快念忽忿思怠急怱恆恒恩恭息悉患悤悲悶惠惡惢愁愈意愛感慈慧慮憂憲應戀戈戉戊戋戌戍戎成我戒戔或戚戠戢截戲戶户戹戼戾房所扁扇手扌才打托执承折拉拜拿掌推提摩支攴攵收攸改放政敄敏敕敖敗敝敞敢散敦敫敬数敷數斂文斉斊斗斤斥斩斬斯新方於施斿旁旋族无旡既旣日旦旧旨早旬旱旲时旾昆昇昌昍明昏易昔昗昜星春昬是昱昴昷時晃晋晏普景晶智暑暴曇曩曰曲曳更曷書曹曼曾替最朁會月有朋服朔朕朗望朝木朩未末本札朮术朱朵朶朿杀杏杜束条来東杲杳松析林枚果枝枲枼某柔查柬柰柴栗桀桑桼梁條梟梨棘棠棥森楚業楽榮樂樊欠次欣欮欲欶欽款歆歇歛止正此步武歨歪歮歯歰歲歴歷歸歹歺死殳段殷殸殹殺殻殿毋毌母每毒比毕毚毛毳氏氐民气氣水氵氶氷永氺氾求汝汞江沃沓沙沝泉法波泣泥泰洛洪活派流浦浪浮淡淮清渚渠湯滿漸火灬灭灰灵灷炅炎炏炗炙炭為烈烏烝焉無焦焱然煞熊熏燕營燮爪爫爭爯爰爱爲爵父爻爽爾爿片牙牚牛牜牟牢牧牪牽犀犬犭犮狂狄狊独狺猋猒猪献獻玄率玉王玟玨珎班琴瑟瑩瓜瓦甘甚生産用甫甬田由甲申电甶男甸甹画甾畀界畏畐留畜畟畢畧畨番畫異畱當畺畾疊疋疌疑疒疾癶癸癹登發白百皀皃的皆皇皋皐皕皮皷皿盃盆盇盈益盍盎监盒盖盛盡監盤盧目直相盾省眇眉看眔眞真眷眼眾着睘睪睿瞏瞢瞿矍矛矞矢矣知矦短石破碎磊磨示礻礼祟票祭禀禁禸禹禺离禽禾禿秀秃秉秋科秝秦移稟穀穌穴究穹空穿突窄窒立竒竜竝竟章童竹笑笠筆等答箕算箴節篤篭米粉粛粟粤粦粲糞糸糹系約納素索紫累細絜絫絲維綿縣繇纍纟缶网罒罔罕罗罙罡罢罪署罷羅羊羌羍美羔羕羗羞羡羣群義羲羸羽翁翏習翕翟翠翼老耂考者耆而耎耑耒耳耴耶耷聂聊聖聚聶聿肀肃肅肉肖肙肥肩肯育肴胃背胡胥能脊脩膚臣臤臧自臬臭臯臱至致臺臼臽臾臿舀舂舄與興舉舌舍舛舜舞舟般艮良色艸艹艾芒芔芬芮花芳芺芻苔苗苟若苦英茶茸荅草荒荣荼莆莧莫莽菆菊菐華萬落葉著葛董葵蒙蒦蒼蓋蓬蓺蔑蔡蕉蕭薄薛薦薰藍藏藥蘭虍虎虐虒虔處虖虗虘虚虛虜虞虫虽蚤蚩蜀蜜蟲蠡血行衍衛衣衤表衮衰袁袞褭褱襄襾西覀要覃見規覓覧親覽见角解言訁訇計詹誩諸讠谷豆豈豊豐豕豖豙象豦豩豪豸貇貝貞貟負貢貧貪貫責貳貴買費賁資賈賏賓賔賛賞賢賣質賴贊贝贡责贯贲贵赖赞赤赦走越足路蹇身躬車軍軎軟輦车辛辜辟辥辰辱農辵辶边达过近连迷追退送逆逐通速造逢連逮進遀遂過道達遣適遷遺邊邑邕那邦邪郎部郭都鄉酉酋配酓釆采里重野量金釒錢钅長镸长門閃閉開閏閑閒間閔閵閻闌门间闷阑阜阝阿降陳隆隊隋隡隨隱隶隹隺隻隼隽难雀雁集雈雋雍雐雔雙雚雜雝離難雨雩雪雲零雷需霍霜霝霞霸靈靑青非靡面靣革韋韦韭韯韱音頁頃項須頗頡頻顛页風风飛飞食飠養饣首香馬馮駦马骨高髟鬥鬯鬲鬼魚魯鮮鱼鲁鳥鳳鸟鹵鹿麃麗麥麦麻黃黄黍黎黑黒黨黹黽黾鼎鼓鼠鼻齊齋齐齒齿龍龙龜龟龠龰龱龴龵龶龷龸龹者艹？𠀁𠀃𠀆𠀉𠀎𠀐𠁁𠁣𠂆𠂇𠂈𠂉𠂊𠂋𠂎𠂒𠂔𠂛𠂡𠂢𠂤𠂬𠂭𠂹𠃊𠃋𠃌𠃍𠃎𠃑𠃓𠃔𠃜𠄌𠄎𠄠𠄢𠆢𠆥𠇍𠈌𠌵𠓜𠔉𠔥𠔼𠔽𠔿𠕀𠕁𠕋𠘧𠘨𠙻𠙼𠚏𠚒𠚤𠚪𠣏𠤎𠤕𠥓𠦄𠦑𠦝𠧒𠧗𠧪𠩺𠪚𠫓𠫔𠫤𠬛𠬝𠬞𠬢𠬤𠬶𠮛𠮦𠮷𠯑𠱠𠳮𠷎𡈼𡉀𡉵𡌥𡍮𡏳𡕒𡕩𡕰𡖅𡗗𡗜𡘆𡘤𡧱𡨄𡩧𡬠𡭽𡰣𡰥𡰪𡰯𡰱𡷈𡸁𡿨𡿩𡿪𡿺𢀖𢀛𢀩𢁙𢆉𢆰𢆶𢇁𢇇𢉖𢌬𢌿𢏚𢑑𢑚𢖻𢙣𢛳𢦏𢦒𢧵𢼄𢾕𣁋𣄼𣅀𣅽𣍘𣎳𣎵𣏋𣏼𣗥𣥂𣥖𣦵𣦼𣧄𣪊𣪠𣬉𣳾𣶒𤇾𤊽𤐫𤓰𤔔𤕨𤣩𤰇𤰔𤰞𤴓𤴔𤽄𥁑𥁕𥃦𥃩𥃭𥇡𥑟𥘅𥘈𥝢𥫗𥱡𦈢𦉪𦉬𦉼𦍌𦍒𦎧𦐇𦓔𦔮𦘒𦙃𦚏𦣝𦣞𦣻𦥑𦥔𦥯𦨉𦭝𦰩𧆞𧈧𧘇𧰨𧴪𧴮𧵩𧾷𨸏𨾴𩙿𩠐𩫏𩵋𪉷𪜀𪟽𪠲𪩲𫇦𫔭𫜸𫝀𫠣𫠩𫢉𫥞𫩏𫩠𫪡𫲽𫶧𬀷𬐘𬗌𬙙𬛸𬜯𬟩𬯁𬴘𬺻𬼉𬼖𭀰𭁈𭁨𭅰𭑈𭕄𭗼𭤨𭥫𭻾𮅕𮊿𮍌𮍏𮓗𮥼𮧮廾𰀁𰀄𰀈𰀉𰀕𰀠𰀡𰀢𰀪𰁜𰃮𰆊𰆘𰋙𰕎𰢴𰧭𰯲"


def slim(v):
    if len(v) <= 3:
        return v
    for x in v[1:-1]:
        if x < '⿰' or x > '⿻':
            w = v[0]+x+v[-1]
            return w
    if len(v) != 3:
        logger.error(v)
    return v


def valid(seq, Ji):
    for x in seq:
        if x not in Ji:
            return 0
    return 1


def odd(seq):
    for x in seq:
        if not UnicodeTokenizer.detect_hanzi(x):
            return 1
    return 0


def loadHeZi(path, JiZi=set(GouJian)):
    doc = open(path).read().splitlines()
    doc = [x.split('\t') for x in doc]
    doc = [(k, v) for k, v in doc if valid(v, JiZi)]
    HeZi = {k: v for k, v in doc}
    values = ''.join(HeZi.values())
    values = list(set(values))
    values.sort()
    logger.info(
        f"  {path} JiZi:{len(JiZi)} --> loadHeZi {len(HeZi)}  values:{len(values)}")
    return HeZi, values


Nums = ''.join(chr(i) for i in range(ord('0'), ord('9')+1))
Az = ''.join(chr(i) for i in range(ord('a'), ord('z')+1))
Alphabet = Nums+Az


def gen_bigrams():
    # az2 = [x+y for x in az for y in az]
    # nums2 = [x+y for x in nums for y in nums]
    grams2 = [x+y for x in Alphabet for y in Alphabet]
    idxs = ["##"+x for x in Az]
    words = list(Alphabet)+grams2+idxs
    return words


# 1358
Bigrams = gen_bigrams()


class ZiCutter:
    def __init__(self, dir=""):
        """
        HeZiBase="","Yuan","Ji"
        """
        self.vocab = set()
        self.HeZi = {}

        self.here = os.path.dirname(__file__)
        self.HanZiDir = os.path.join(self.here, "HanZi")

        self.dir = dir
        self.load(dir)

    def load(self, dir):
        JiZi = set(GouJian)
        self.vocab = set(Bigrams) | JiZi
        HeZiPath = os.path.join(dir, "HeZi.txt")
        if not os.path.exists(HeZiPath):
            dir = self.HanZiDir
        HeZiPath = os.path.join(dir, "HeZi.txt")

        JiZiPath = os.path.join(dir, "JiZi.txt")
        if os.path.exists(JiZiPath):
            JiZi = open(JiZiPath).read().splitlines()
            JiZi = set(JiZi)
            logger.info(f"{JiZiPath} load  JiZi:{len(JiZi)}")
        else:
            logger.info(f" no {JiZiPath}, use YuanZi JiZi:{len(JiZi)}")

        HeZi, values = loadHeZi(HeZiPath, JiZi)
        logger.info(f"{HeZiPath} HeZi:{len(HeZi)} values:{len(values)}")
        self.HeZi = HeZi
        self.vocab |= JiZi
        logger.info(f"{dir} loaded vocab:{len(self.vocab)}")

    def build(self, roots=[]):
        logger.warning(f" {self.dir} building")
        vocab = set(Bigrams) | set(GouJian) | set(x for x in roots)
        JiZi = [x for x in vocab if len(x) == 1]
        logger.info(f"receive roots:{len(roots)} JiZi:{len(JiZi)}")
        HeZiPath = os.path.join(self.dir, "HeZi.txt")
        JiZiPath = os.path.join(self.dir, "JiZi.txt")
        He2Zi.build(JiZi, ChaiZiPath=os.path.join(self.HanZiDir, "ChaiZi.txt"), YiTiZiPath=os.path.join(self.HanZiDir, "YiTiZi.txt"),
                    HeZiPath=HeZiPath, JiZiPath=JiZiPath)
        self.load(self.dir)

    def cutHan(self, zi, shrink=True):
        ids = self.HeZi.get(zi, zi)
        if shrink:
            s = slim(ids)
            return s
        return ids

    def cutRare(self, char):
        tokens = []
        try:
            name = unicodedata.name(char)
            l = name[0].lower()
            r = name[-2:].strip().lstrip('-').lower()
            tokens += ['##'+l, r]
        except:
            catg = unicodedata.category(char)
            l = catg[0].lower()
            r = ord(char) % 100
            s = f'0{r}'[-2:]
            tokens = ['##'+l, s]
        return tokens

    def cutChar(self, char):
        if char in self.vocab:
            return [char]
        if char in self.HeZi:
            t = self.cutHan(char)
            return list(t)
        else:
            t = self.cutRare(char)
            return t

    def tokenize(self, line):
        tokens = []
        for x in line:
            tokens += self.cutChar(x)
        tokens = [x for x in tokens if x]
        return tokens
