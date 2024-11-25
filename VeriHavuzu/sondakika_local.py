import requests as req
from bs4 import BeautifulSoup

class Local():
    header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
    url = "https://www.sondakika.com/"
    sehirler = {
    "Adana": ["Aladağ", "Ceyhan", "Çukurova", "Feke", "İmamoğlu", "Karaisalı", "Karataş", "Kozan", "Pozantı",
              "Saimbeyli", "Sarıçam", "Seyhan", "Tufanbeyli", "Yumurtalık", "Yüreğir"],

    "Adıyaman": [ "Besni", "Çelikhan", "Gerger", "Gölbaşı", "Kâhta", "Samsat", "Sincik", "Tut"],

    "Afyonkarahisar": ["Başmakçı", "Bayat", "Bolvadin", "Çay", "Çobanlar", "Dazkırı", "Dinar",
                       "Emirdağ", "Evciler", "Hocalar", "İhsaniye", "İscehisar", "Kızılören", "Sandıklı", "Sinanpaşa",
                       "Sultandağı", "Şuhut"],

    "Ağrı": [ "Diyadin", "Doğubayazıt", "Eleşkirt", "Hamur", "Patnos", "Taşlıçay", "Tutak"],

    "Aksaray": ["Ağaçören",  "Eskil", "Gülağaç", "Güzelyurt", "Ortaköy", "Sarıyahşi"],

    "Amasya": [ "Göynücek", "Gümüşhacıköy", "Hamamözü", "Merzifon", "Suluova", "Taşova"],

    "Ankara": ["Akyurt", "Altındağ", "Ayaş", "Balâ", "Beypazarı", "Çamlıdere", "Çankaya", "Çubuk", "Elmadağ",
               "Etimesgut", "Evren", "Gölbaşı", "Güdül", "Haymana", "Kalecik", "Kahramankazan", "Keçiören",
               "Kızılcahamam", "Mamak", "Nallıhan", "Polatlı", "Pursaklar", "Sincan", "Şereflikoçhisar", "Yenimahalle"],

    "Antalya": ["Akseki", "Aksu", "Alanya", "Döşemealtı", "Elmalı", "Finike", "Gazipaşa", "Gündoğmuş", "İbradı",
                "Demre", "Kaş", "Kemer", "Kepez", "Konyaaltı", "Korkuteli", "Kumluca", "Manavgat", "Muratpaşa",
                "Serik"],

    "Ardahan": [ "Çıldır", "Damal", "Göle", "Hanak", "Posof"],

    "Artvin": ["Ardanuç", "Arhavi",   "Borçka", "Hopa", "Murgul", "Şavşat", "Yusufeli"],

    "Aydın": ["Bozdoğan", "Buharkent", "Çine", "Didim", "Efeler", "Germencik", "İncirliova", "Karacasu", "Karpuzlu",
              "Koçarlı", "Köşk", "Kuşadası", "Kuyucak", "Nazilli", "Söke", "Sultanhisar", "Yenipazar"],

    "Balıkesir": ["Altıeylül", "Ayvalık", "Balya", "Bandırma", "Bigadiç", "Burhaniye", "Dursunbey", "Edremit", "Erdek",
                  "Gömeç", "Gönen", "Havran", "İvrindi", "Karesi", "Kepsut", "Manyas", "Marmara", "Savaştepe",
                  "Sındırgı", "Susurluk"],

    "Bartın": ["Amasra",  "Kurucaşile", "Ulus"],

    "Batman": [ "Beşiri", "Gercüş", "Hasankeyf", "Kozluk", "Sason"],

    "Bayburt": ["Aydıntepe", "Demirözü"],

    "Bilecik": [ "Bozüyük", "Gölpazarı", "İnhisar", "Osmaneli", "Pazaryeri", "Söğüt", "Yenipazar"],

    "Bingöl": ["Adaklı", "Genç", "Karlıova", "Kiğı", "Solhan", "Yayladere", "Yedisu"],

    "Bitlis": ["Adilcevaz", "Ahlat", "Güroymak", "Hizan", "Mutki", "Tatvan"],

    "Bolu": [ "Dörtdivan", "Gerede", "Göynük", "Kıbrıscık", "Mengen", "Mudurnu", "Seben", "Yeniçağa"],

    "Burdur": ["Ağlasun", "Altınyayla", "Bucak",  "Çavdır", "Çeltikçi", "Gölhisar", "Karamanlı", "Kemer",
               "Tefenni", "Yeşilova"],

    "Bursa": ["Büyükorhan", "Gemlik", "Gürsu", "Harmancık", "İnegöl", "İznik", "Karacabey", "Keles", "Kestel",
              "Mudanya", "Mustafakemalpaşa", "Nilüfer", "Orhaneli", "Orhangazi", "Osmangazi", "Yenişehir", "Yıldırım"],

    "Çanakkale": ["Ayvacık", "Bayramiç", "Biga", "Bozcaada", "Çan", "Eceabat", "Ezine", "Gelibolu",
                  "Gökçeada", "Lapseki", "Yenice"],

    "Çankırı": ["Atkaracalar", "Bayramören",  "Çerkeş", "Eldivan", "Ilgaz", "Kızılırmak", "Korgun",
                "Kurşunlu", "Orta", "Şabanözü", "Yapraklı"],

    "Çorum": ["Alaca", "Bayat", "Boğazkale",  "Dodurga", "İskilip", "Kargı", "Laçin", "Mecitözü", "Oğuzlar",
              "Ortaköy", "Osmancık", "Sungurlu", "Uğurludağ"],

    "Denizli": ["Acıpayam", "Babadağ", "Baklan", "Bekilli", "Beyağaç", "Bozkurt", "Buldan", "Çal", "Çameli", "Çardak",
                "Çivril", "Güney", "Honaz", "Kale", "Merkezefendi", "Pamukkale", "Sarayköy", "Serinhisar", "Tavas"],

    "Diyarbakır": ["Bağlar", "Bismil", "Çermik", "Çınar", "Çüngüş", "Dicle", "Eğil", "Ergani", "Hani", "Hazro",
                   "Kayapınar", "Kocaköy", "Kulp", "Lice", "Silvan", "Sur", "Yenişehir"],

    "Düzce": ["Akçakoca", "Cumayeri", "Çilimli", "Gölyaka", "Gümüşova", "Kaynaşlı", "Yığılca"],

    "Edirne": ["Enez", "Havsa", "İpsala", "Keşan", "Lalapaşa", "Meriç", "Merkez", "Süloğlu", "Uzunköprü"],

    "Elâzığ": ["Ağın", "Alacakaya", "Arıcak", "Baskil",  "Karakoçan", "Keban", "Kovancılar", "Maden", "Palu",
               "Sivrice"],

    "Erzincan": ["Çayırlı", "İliç", "Kemah", "Kemaliye", "Otlukbeli", "Refahiye", "Tercan", "Üzümlü"],

    "Erzurum": ["Aşkale", "Aziziye", "Çat", "Hınıs", "Horasan", "İspir", "Karaçoban", "Karayazı", "Köprüköy", "Narman",
                "Oltu", "Olur", "Palandöken", "Pasinler", "Pazaryolu", "Şenkaya", "Tekman", "Tortum", "Uzundere",
                "Yakutiye"],

    "Eskişehir": ["Alpu", "Beylikova", "Çifteler", "Günyüzü", "Han", "İnönü", "Mahmudiye", "Mihalgazi", "Mihalıççık",
                  "Odunpazarı", "Sarıcakaya", "Seyitgazi", "Sivrihisar", "Tepebaşı"],

    "Gaziantep": ["Araban", "İslahiye", "Karkamış", "Nizip", "Nurdağı", "Oğuzeli", "Şahinbey", "Şehitkâmil",
                  "Yavuzeli"],

    "Giresun": ["Alucra", "Bulancak", "Çamoluk", "Çanakçı", "Dereli", "Doğankent", "Espiye", "Eynesil", 
                "Görele", "Güce", "Keşap", "Piraziz", "Şebinkarahisar", "Tirebolu", "Yağlıdere"],

    "Gümüşhane": ["Kelkit", "Köse", "Kürtün", "Şiran", "Torul"],

    "Hakkâri": ["Çukurca",  "Şemdinli", "Yüksekova"],

    "Hatay": ["Altınözü", "Antakya", "Arsuz", "Belen", "Defne", "Dörtyol", "Erzin", "Hassa", "İskenderun", "Kırıkhan",
              "Kumlu", "Payas", "Reyhanlı", "Samandağ", "Yayladağı"],

    "Iğdır": ["Aralık",  "Karakoyunlu", "Tuzluca"],

    "Isparta": ["Aksu", "Atabey", "Eğirdir", "Gelendost", "Gönen", "Keçiborlu", "Senirkent", "Sütçüler",
                "Şarkikaraağaç", "Uluborlu", "Yalvaç", "Yenişarbademli"],

    "İstanbul": ["Adalar", "Arnavutköy", "Ataşehir", "Avcılar", "Bağcılar", "Bahçelievler", "Bakırköy", "Başakşehir",
                 "Bayrampaşa", "Beşiktaş", "Beykoz", "Beylikdüzü", "Beyoğlu", "Büyükçekmece", "Çatalca", "Çekmeköy",
                 "Esenler", "Esenyurt", "Eyüp", "Fatih", "Gaziosmanpaşa", "Güngören", "Kadıköy", "Kağıthane", "Kartal",
                 "Küçükçekmece", "Maltepe", "Pendik", "Sancaktepe", "Sarıyer", "Silivri", "Sultanbeyli", "Sultangazi",
                 "Şile", "Şişli", "Tuzla", "Ümraniye", "Üsküdar", "Zeytinburnu"],

    "İzmir": ["Aliağa", "Balçova", "Bayındır", "Bayraklı", "Bergama", "Beydağ", "Bornova", "Buca", "Çeşme", "Çiğli",
              "Dikili", "Foça", "Gaziemir", "Güzelbahçe", "Karabağlar", "Karaburun", "Karşıyaka", "Kemalpaşa", "Kınık",
              "Kiraz", "Konak", "Menderes", "Menemen", "Narlıdere", "Ödemiş", "Seferihisar", "Selçuk", "Tire",
              "Torbalı", "Urla"],

    "Kahramanmaraş": ["Afşin", "Andırın", "Çağlayancerit", "Dulkadiroğlu", "Ekinözü", "Elbistan", "Göksun", "Nurhak",
                      "Onikişubat", "Pazarcık", "Türkoğlu"],

    "Karabük": ["Eflani", "Eskipazar",  "Ovacık", "Safranbolu", "Yenice"],

    "Karaman": ["Ayrancı", "Başyayla", "Ermenek", "Kazımkarabekir", "Sarıveliler"],

    "Kars": ["Akyaka", "Arpaçay", "Digor", "Kağızman",  "Sarıkamış", "Selim", "Susuz"],

    "Kastamonu": ["Abana", "Ağlı", "Araç", "Azdavay", "Bozkurt", "Cide", "Çatalzeytin", "Daday", "Devrekani",
                  "Doğanyurt", "Hanönü", "İhsangazi", "İnebolu",  "Küre", "Pınarbaşı", "Seydiler",
                  "Şenpazar", "Taşköprü", "Tosya"],

    "Kayseri": ["Akkışla", "Bünyan", "Develi", "Felahiye", "Hacılar", "İncesu", "Kocasinan", "Melikgazi", "Özvatan",
                "Pınarbaşı", "Sarıoğlan", "Sarız", "Talas", "Tomarza", "Yahyalı", "Yeşilhisar"],

    "Kırıkkale": ["Bahşılı", "Balışeyh", "Çelebi", "Delice", "Karakeçili", "Keskin", "Sulakyurt",
                  "Yahşihan"],

    "Kırklareli": ["Babaeski", "Demirköy", "Kofçaz", "Lüleburgaz", "Pehlivanköy", "Pınarhisar", "Vize"],

    "Kırşehir": ["Akçakent", "Akpınar", "Boztepe", "Çiçekdağı", "Kaman",  "Mucur"],

    "Kilis": ["Elbeyli",  "Musabeyli", "Polateli"],

    "Kocaeli": ["Başiskele", "Çayırova", "Darıca", "Derince", "Dilovası", "Gebze", "Gölcük", "İzmit", "Kandıra",
                "Karamürsel", "Kartepe", "Körfez"],

    "Konya": ["Ahırlı", "Akören", "Akşehir", "Altınekin", "Beyşehir", "Bozkır", "Cihanbeyli", "Çeltik", "Çumra",
              "Derbent", "Derebucak", "Doğanhisar", "Emirgazi", "Ereğli", "Güneysınır", "Hadım", "Halkapınar", "Hüyük",
              "Ilgın", "Kadınhanı", "Karapınar", "Karatay", "Kulu", "Meram", "Sarayönü", "Selçuklu", "Seydişehir",
              "Taşkent", "Tuzlukçu", "Yalıhüyük", "Yunak"],

    "Kütahya": ["Altıntaş", "Aslanapa", "Çavdarhisar", "Domaniç", "Dumlupınar", "Emet", "Gediz", "Hisarcık", 
                "Pazarlar", "Şaphane", "Simav", "Tavşanlı"],

    "Malatya": ["Akçadağ", "Arapgir", "Arguvan", "Battalgazi", "Darende", "Doğanşehir", "Doğanyol", "Hekimhan", "Kale",
                "Kuluncak", "Pütürge", "Yazıhan", "Yeşilyurt"],

    "Manisa": ["Ahmetli", "Akhisar", "Alaşehir", "Demirci", "Gölmarmara", "Gördes", "Kırkağaç", "Köprübaşı", "Kula",
               "Salihli", "Sarıgöl", "Saruhanlı", "Selendi", "Soma", "Şehzadeler", "Turgutlu", "Yunusemre"],

    "Mardin": ["Artuklu", "Dargeçit", "Derik", "Kızıltepe", "Mazıdağı", "Midyat", "Nusaybin", "Ömerli", "Savur",
               "Yeşilli"],

    "Mersin": ["Akdeniz", "Anamur", "Aydıncık", "Bozyazı", "Çamlıyayla", "Erdemli", "Gülnar", "Mezitli", "Mut",
               "Silifke", "Tarsus", "Toroslar", "Yenişehir"],

    "Muğla": ["Bodrum", "Dalaman", "Datça", "Fethiye", "Kavaklıdere", "Köyceğiz", "Marmaris", "Menteşe", "Milas",
              "Ortaca", "Seydikemer", "Ula", "Yatağan"],

    "Muş": ["Bulanık", "Hasköy", "Korkut", "Malazgirt",  "Varto"],

    "Nevşehir": ["Acıgöl", "Avanos", "Derinkuyu", "Gülşehir", "Hacıbektaş", "Kozaklı", "Ürgüp"],

    "Niğde": ["Altunhisar", "Bor", "Çamardı", "Çiftlik", "Ulukışla"],

    "Ordu": ["Akkuş", "Altınordu", "Aybastı", "Çamaş", "Çatalpınar", "Çaybaşı", "Fatsa", "Gölköy", "Gülyalı",
             "Gürgentepe", "İkizce", "Kabadüz", "Kabataş", "Korgan", "Kumru", "Mesudiye", "Perşembe", "Ulubey", "Ünye"],

    "Osmaniye": ["Bahçe", "Düziçi", "Hasanbeyli", "Kadirli",  "Sumbas", "Toprakkale"],

    "Rize": ["Ardeşen", "Çamlıhemşin", "Çayeli", "Derepazarı", "Fındıklı", "Güneysu", "Hemşin", "İkizdere", "İyidere",
             "Kalkandere", "Pazar"],

    "Sakarya": ["Adapazarı", "Akyazı", "Arifiye", "Erenler", "Ferizli", "Geyve", "Hendek", "Karapürçek", "Karasu",
                "Kaynarca", "Kocaali", "Pamukova", "Sapanca", "Serdivan", "Söğütlü", "Taraklı"],

    "Samsun": ["Alaçam", "Asarcık", "Atakum", "Ayvacık", "Bafra", "Canik", "Çarşamba", "Havza", "İlkadım", "Kavak",
               "Ladik", "Ondokuzmayıs", "Salıpazarı", "Tekkeköy", "Terme", "Vezirköprü", "Yakakent"],

    "Siirt": ["Siirt", "Tillo", "Baykan", "Eruh", "Kurtalan", "Pervari", "Şirvan"],

    "Sinop": ["Ayancık", "Boyabat", "Dikmen", "Durağan", "Erfelek", "Gerze", "Saraydüzü",  "Türkeli"],

    "Sivas": ["Akıncılar", "Altınyayla", "Divriği", "Doğanşar", "Gemerek", "Gölova", "Hafik", "İmranlı", "Kangal",
              "Koyulhisar",  "Suşehri", "Şarkışla", "Ulaş", "Yıldızeli", "Zara", "Gürün"],

    "Şanlıurfa": ["Akçakale", "Birecik", "Bozova", "Ceylanpınar", "Eyyübiye", "Halfeti", "Haliliye", "Harran", "Hilvan",
                  "Karaköprü", "Siverek", "Suruç", "Viranşehir"],

    "Şırnak": ["Beytüşşebap", "Cizre", "Güçlükonak", "İdil", "Silopi", "Uludere"],

    "Tekirdağ": ["Çerkezköy", "Çorlu", "Ergene", "Hayrabolu", "Kapaklı", "Malkara", "Marmara Ereğlisi", "Muratlı",
                 "Saray", "Süleymanpaşa", "Şarköy"],

    "Tokat": ["Almus", "Artova", "Başçiftlik", "Erbaa", "Niksar", "Pazar", "Reşadiye", "Sulusaray",  "Turhal",
              "Yeşilyurt", "Zile"],

    "Trabzon": ["Akçaabat", "Araklı", "Arsin", "Beşikdüzü", "Çarşıbaşı", "Çaykara", "Dernekpazarı", "Düzköy", "Hayrat",
                "Köprübaşı", "Maçka", "Of", "Ortahisar", "Sürmene", "Şalpazarı", "Tonya", "Vakfıkebir", "Yomra"],

    "Tunceli": ["Çemişgezek", "Hozat", "Mazgirt", "Nazımiye", "Ovacık", "Pertek", "Pülümür"],

    "Uşak": ["Banaz", "Eşme", "Karahallı", "Sivaslı", "Ulubey"],

    "Van": ["Bahçesaray", "Başkale", "Çaldıran", "Çatak", "Edremit", "Erciş", "Gevaş", "Gürpınar", "İpekyolu",
            "Muradiye", "Özalp", "Saray", "Tuşba"],

    "Yalova": ["Altınova", "Armutlu", "Çınarcık", "Çiftlikköy", "Termal"],

    "Yozgat": ["Akdağmadeni", "Aydıncık", "Boğazlıyan", "Çandır", "Çayıralan", "Çekerek", "Kadışehri", "Saraykent",
               "Sarıkaya", "Sorgun", "Şefaatli", "Yenifakılı", "Yerköy"],

    "Zonguldak": ["Alaplı", "Çaycuma", "Devrek", "Gökçebey", "Kilimli", "Kozlu", "Karadeniz Ereğli"]}




    def __init__(self, city: str):
        url = self.url
        header = self.header
        self.city = city.lower().replace("şçğüöı", "scguoi")
        g = req.get(url+self.city, headers=header).text
        self.soup = BeautifulSoup(g, "html.parser")
        
    def current_news(self):
        news = {
            "city": self.city,
            "title": self.soup.find("a", {"class": "content"}).span.text,
            "about": self.soup.find("p", {"class": "news-detail news-column"}).text
        }
        return news
   
    def news(self, limit: int=10000):
        news = {}
        n = 1
        for i in self.soup.find_all("li", {"class": "nws"}):
            if n <= limit:
                news[n] = {
                    "tarih": i.find("span", {"class": "mdate"}).text.strip(),
                    "city": self.city,
                    "city2": "",
                    "title": i.find("a", {"class": "content"}).span.text,
                    "content": i.find("p", {"class": "news-detail news-column"}).text
                    
                }
            n+=1
        return news
    