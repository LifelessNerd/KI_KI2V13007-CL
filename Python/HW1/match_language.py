import langdetect as ld
import os
class LangMatcher:
    
    def __init__ (self, path):
        """:param path: The path to a directory with the saved ngram profiles
        Creates a dictionary whose keys are language names, and each value is itself a dictionary whose
        keys are ngrams and whose values are frequencies, stored under lang_dict"""
        self.lang_dict = {}
        os.chdir(path)
        for file in os.listdir():  # Loop through all files in provided dir
            temp_key_list = file.split("-")
            temp_key = temp_key_list[0]
            #print(temp_key)
            temp_value = ld.read_ngrams(file)
            self.lang_dict[temp_key] = temp_value
        
        
    def score(self, text, k_best = 1):
        
        gramlijst = []
        gramlijstwinnaars = []
        
        bigram = ld.ngram_table(text, 2, 200)
        trigram = ld.ngram_table(text, 3, 200)
        for alledingen in self.lang_dict:
            gramlijst.append([ld.cosine_similarity(self.lang_dict[alledingen], bigram), alledingen]) 
        #for alledingen in diedictoriarie:
            #gramlijst.append([ld.cosine_similarity(diedictoraie[alledingen], trigram), alledingen])
        gramlijst.sort(reverse = True)
        for i in range(k_best):
            gramlijstwinnaars.append(gramlijst[i][1])
        
        return gramlijstwinnaars


   
stringer = '''Nederland is een van de landen binnen het Koninkrijk der Nederlanden.[7] Nederland ligt voor het overgrote deel in het noordwesten van Europa, aan de Noordzee. Naast het Europese deel zijn er nog de drie bijzondere gemeenten in de Caribische Zee, die ook wel Caribisch Nederland worden genoemd. Europees Nederland wordt in het zuiden begrensd door België, langs de oostgrens door Duitsland en aan west- en noordzijde door de zee. De hoofdstad van Nederland is Amsterdam, de regeringszetel is Den Haag.
    Nederland heeft een inwonertal van 17.609.246 (31 maart 2022)[5] en met een oppervlakte van 41.543 km²[8] een bevolkingsdichtheid van 424 inwoners/km². Daarmee is Nederland het op vijftien na dichtst bevolkte land van de wereld; met de kleine stadstaten Monaco, Vaticaanstad en San Marino niet meegerekend is Nederland na Malta het dichtstbevolkte land in Europa. 18,41% van het oppervlak (7.650 km²) bestaat uit water en 81,59% uit land (33.893 km²). De bevolkingsdichtheid exclusief het wateroppervlakte is 519 inwoners/km² (31 januari 2022). Een groot deel van het land en de bevolking bevindt zich onder zeeniveau.[9] Het land wordt beschermd tegen het water door middel van een systeem van dijken en waterwerken. Door landwinning zijn polders gecreëerd. Bestuurlijk is het land verdeeld in twaalf provincies en circa 350 gemeenten.

Nederland werd onafhankelijk tijdens de Tachtigjarige Oorlog (1568-1648), waarin de gezamenlijke Noordelijke en Zuidelijke Nederlanden tegen de Spaanse overheersing in opstand kwamen. In 1579 vormden de Noordelijke Nederlanden de Unie van Utrecht, waarmee een nieuwe politieke entiteit ontstond. Met de Acte van Verlatinghe van 1581 werd door de gewesten van die unie, Stad en Lande (Groningen), Friesland, Overijssel, Gelderland, Utrecht, Holland, Zeeland, de onafhankelijkheid van de Republiek der Zeven Verenigde Nederlanden uitgeroepen. Deze werd vanaf 1609 bij het begin van het Twaalfjarig Bestand internationaal erkend en na de Vrede van Münster (1648) ook door Spanje. Vanaf de Franse tijd (1795-1813) ontwikkelde Nederland zich tot een natiestaat. De Nederlandse vorst regeerde anno 1815 ook over het huidige België en Luxemburg, evenals een aantal overzeese gebieden (Nederlands-Indië, Suriname en de Nederlandse Antillen). België werd echter onafhankelijk na de Belgische Revolutie in 1830 en Luxemburg maakte zich in 1890 los van de Nederlandse Kroon. De dekolonisatie maakte in de 20e eeuw ook een einde aan de Nederlandse koloniën. Behalve de drie Caribische bijzondere gemeenten onderhouden ook de landen Aruba, Curaçao en Sint Maarten een hechte band met Nederland en vormen sinds 2010 samen het Koninkrijk der Nederlanden.

Politiek is Nederland sinds de grondwetsherziening van 1848 een parlementaire democratie met een constitutionele monarchie, een staatsvorm waarbij de macht volgens de regels gedeeld wordt door de koning(in), de ministers onder wie de minister-president en de twee kamers van het parlement. Nederland was medeoprichter van onder meer de Europese Unie, de G-10, de NAVO, de Wereldhandelsorganisatie en de OESO. Met België en Luxemburg vormt het de Benelux. Den Haag speelt een belangrijke internationale rol op juridisch gebied, als locatie voor vier internationale tribunalen en Europol. In 2009 behoorde Nederland als 's werelds zevende economie naar bbp per hoofd van de bevolking tot de meest ontwikkelde landen. Het bezette in 2013 de vierde plaats in de index van de menselijke ontwikkeling. De Nederlandse economie steunt vooral op een zeer hoog ontwikkelde land- en tuinbouwsector, de dienstensector en de internationale handel, met name op de doorvoer van goederen naar Duitsland.
    die ook wel Caribisch Nederland worden genoemd. Europees Nederland wordt in het zuiden begrensd door België, langs de oostgrens door Duitsland en aan west- en noordzijde door de zee. De hoofdstad van Nederland is Amsterdam, de regeringszetel is Den Haag.
'''
dictero = ld.ngram_table(stringer, 2, 200)


langmatcher = LangMatcher("models/2-200")
print(langmatcher.score(stringer, 1))



