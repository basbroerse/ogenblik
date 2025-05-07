# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 14:25:21 2024

@author: basbr
"""
import numpy as np
import pandas as pd

# 3000 most frequent word tokens in Sonar 500 corpus
basicwords_nl = frozenset("""
. de , van het een en in dat is op te zijn voor met ik die niet ) ( : " maar er
' aan - ook je als om ? hij ze bij dan nog was naar uit of door we heeft over
wat al tot worden meer hebben wordt geen wel jaar kan ! dit nu zich zo hun deze
werd moet mijn haar na kunnen zou veel tegen ... 1 had ; twee heb zal daar toch
andere goed eerste wil moeten waar mensen / onder nieuwe gaat gaan 2 dus hem u
ons me ben weer hier alleen toen omdat hoe doen zegt onze alle heel tussen
maken mij grote eens '' zij waren uur komt iets komen staat zoals euro wij 3
drie af * volgens tijd want altijd één zelf wie zonder mee weet man vooral
eigen ja tweede enkele leven zelfs plaats keer zien toe dag alles jaren laten
the 4 men echt werden zullen willen nooit weg 0 % zeker kinderen laatste kon
tijdens net week kwam terug mag .. 5 land krijgen europese staan per werk
zeggen binnen minder even procent aantal steeds laat niets blijft 6 miljoen
beter samen ging blijven werken zo'n elkaar zit verder anders rond nederland
ten hadden gewoon lang artikel vier misschien via geven vandaag zei iedereen \]
eerst moest jij re goede waarom 10 sinds pas geleden weten later hele geld
wereld zouden mogelijk hen iemand vraag brussel groot belgië vrouw doet houden
deel bijna elke vinden echter huis gisteren vaak \[ vanaf nodig maakt kreeg
opnieuw vind allemaal zitten snel vlaamse nemen ter volgende vijf krijgt achter
der maanden dagen minister stad erg uw denk natuurlijk da la politie nee derde
belgische nederlandse weinig amerikaanse terwijl ligt ga zeer a helemaal
geweest vorig hebt den 7 duidelijk kleine 20 commissie regering vrouwen daarom
gemaakt wanneer manier jullie beste spelen enige vindt 8 waarin naam soms
eigenlijk verschillende groep zie begin paar tien lijkt bijvoorbeeld eerder
gedaan graag weken onderzoek gezien geval mogen bent 15 europa oude voorzitter
partij vragen geeft genoeg seizoen enkel landen open vorige bovendien frank
meteen vlaanderen wilde moment welke kans zes politieke antwerpen zondag zaken
club stond raad bedrijf mannen elk 12 brengen buiten ooit beetje grootste hand
naast slechts 9 ziet probleem bekend nieuw titel niemand problemen vader maakte
school 25 zaterdag vrij ander markt dood 11 gent thuis morgen dezelfde moeilijk
denken aldus jonge einde daarna le 't bestaat moeder stellen eind vast jan
blijkt boven kijken zetten water boek vanuit muziek 30 zaak kind ouders deed
zowel 14 wedstrijd ` 18 vond bedrijven ploeg zoveel gemeente meeste afgelopen
soort punten meest kunt maand les quote geworden & extra zodat sociale meter
film gebruik gebruikt doe beide kom liggen franse halen vroeg zag gezegd
president politiek dingen uiteindelijk langs = hoop valt houdt september b
sommige miljard lange best d belang des vlaams familie zeg liet zat hoofd | ge
13 bezig à helft nationale neemt juni 16 zorgen ervan sterk jongeren auto et
mei stuk daarmee handen januari niks lid kwamen konden druk trouwens ongeveer
start immers frankrijk 17 internationale nieuws recht vele p belangrijk prijs
2004 oktober bank rol overheid waarop informatie foto burgemeester waarbij ogen
langer vroeger betalen mooi parlement brugge juist echte kant verhaal bepaalde
zichzelf beginnen waarvan volledig verordening inderdaad basis nadat klein hoge
juli zin lopen duitse wist mens zoon economische anderen hetzelfde radio oorlog
werkt toekomst speelt 2005 's gaf horen meestal huidige reden periode stelt
minuten .... acht verwacht totaal gelijk bestaan daarbij 19 vol december succes
god maart 21 daarvoor hoor gehad ruim ni amsterdam begon loopt idee april
begint licht > eten precies kosten bleef slecht hoog duitsland vorm betekent
eeuw financiële vallen rest ver vrijdag zeven woord jou peter kort grond
premier programma bleek wachten genomen 24 spelers 50 22 gegeven terecht 100
gebied ronde verenigde belangrijke zware partijen plaatsen z'n nr. aandacht
november nam waardoor punt rode gelukkig rust dienst nummer plan staten woorden
kijk publiek hoewel rekening dacht gemeenschap situatie zoek unie volgend
voorbije mocht feit zoeken gebeurt intussen new weekend kamer 23 moesten klaar
koning leden doel trekken gebruiken zwaar verkiezingen britse helpen leren + i
belangrijkste vs trainer centrum gekomen gevonden kregen augustus vierde kennen
waarschijnlijk namen dollar mooie volgen dochter «ik waarmee 2003 daarvan
vertelt buitenlandse lijst komende spreken 2000 gevolg tegenover korte proberen
half vrije maandag top won zet gevallen gingen onderwijs straat vlak steun and
winnen daardoor beeld vrienden maatregelen denkt ene bijzonder nederlands
ruimte vormen leggen europees liep geschiedenis finale gevoel inwoners ondanks
volgt niveau 2001 februari praten hard geloof richting strijd leuk buurt cd&v
blz. heer paul gratis antwoord betrokken voorlopig  gekregen 2002 wellicht
verloren volk begonnen directeur gebracht vld lol economie speelde project --
schepen info winst organisatie voetbal werknemers stemmen 40 verschil momenteel
gebeuren brengt wet systeem internet hoger kilometer leuven nacht oud tom alsof
marc viel liever kopen actie woensdag kun betreft ieder sport wonen gehouden
bevolking kerk wegens fc akkoord vraagt straks cijfers lezen orde algemeen
leiden beleid bart normaal uiteraard ma twintig rijden kost hart jongens
producten wagen oog richtlijn l én irak 28 meisje samenwerking blijkbaar kent
hulp erop klanten jongen namelijk macht 26 hoogte nie 27 schrijven graden
genoemd nauwelijks anderlecht verleden boeken waarde heen oplossing 2006
ziekenhuis du eén luc reeks vriend provincie lokale contact controle donderdag
vanavond witte overigens overal avond geboren deur kiezen ondertussen besluit
keuze hield voldoende blij bepaald media sterke zomer zwarte zee geef rechter
liefde lijn bestuur nou team taal beroep tekst resultaat regio to wou
resultaten oostende dinsdag krant termijn voorbeeld indien slag vertrouwen
doelpunten stand kennis s voorstel inmiddels hoeveel wijze 31 geweld vergeten
david voorbij vervolgens dieren mening gezet groter dankzij woning frans voeren
brand foto's bezoek «de m gesteld telkens 60 hé vertellen leeftijd ontwikkeling
ervaring cultuur geldt lag plannen krijg meisjes aandeel gevraagd km kunst
liefst nogal ervoor china leger lidstaten leerlingen haalde kracht bracht
sprake dicht johan dergelijke ne aandelen crisis los stap groen meerderheid
bezoekers kritiek gewonnen parijs actief eindelijk bedoeling halve persoon ken
tevreden legt iedere delen beslissing 29 relatie kop personen gezicht schreef
betere leek israël leider behalve noemen fout mechelen slechte jong geheel
wacht john daarnaast verkocht gevolgen daarin trekt bang negen bieden c ergens
universiteit klasse voorkomen gang jongste maak gegevens lichaam vervangen
lekker opdracht ii stelde omgeving gebeurd neem minstens direct 2007 «we
slachtoffer groei rug lucht brusselse prijzen bekende verkeer personeel raakte
he gegaan gebouw patrick name kaart gij hou onlangs gewone pakken kwaliteit
twaalf wilt heet scholen moeite midden links doden juiste geschreven «het
verkoop kader amerika tafel voelen stem website bal york voorzien regels sector
museum gesloten advies slachtoffers hoeft biedt contract kansen verkopen jouw
openbare k last plus italiaanse band spel wedstrijden rechtbank verband alvast
indruk hoort activiteiten genk federale 80 gezin antwerpse hoogste un italië
bouwen productie politici voorstellen proces mogelijke beslist spanje _ neer
invloed dertig middelen verslag spreekt gespeeld dirk word opgenomen pb
vastgesteld gebeurde omzet geloven zette 70 leiding zoiets klinkt justitie
stonden telt on amper wilden inzake discussie zon for optreden algemene
gemeenten o feiten peeters ministerie veld dans e moord ontstaan gevaar stoppen
speciale match duur dragen belgen veiligheid aanwezig centrale beperkt trok t
daarop 35 tegenwoordig onmiddellijk loop bewoners rusland hoofdstad verliezen
tv veranderen verlies baan keren kwestie buitenland honderd schade vuur rustig
tel. bed londen 00 brief café eenmaal fr. broer diverse jeugd kortrijk voel
bush vaste gesprek bijlage 1999 merk openbaar mevrouw enorm bron maatschappij
samenleving beelden wim werkte spaanse dank vanwege bedrag sp.a voelt reactie
gehoord dient steden ok beschikking pijn aarde wa toepassing stel schrijft 200
gekozen collega's burgers allerlei dorp hangt post erin provinciale positie cel
internationaal eisen geel haalt 90 advocaat koers 1996 enorme persoonlijke
verlaten kwijt zolang absoluut banken beurs gebrek vriendin goeie kabinet
stappen zege nochtans energie verloor sluiten functie binnenkort positief
standard vrijheid afstand plek winkel welk zorgt voormalige volle verdrag
leterme sociaal hans tegelijk studenten dl rotterdam geluk zowat jammer
roeselare mogelijkheden amerikanen moderne tonen bestaande reed noemt televisie
makkelijk debat mis lijken haag gemiddelde carrière site officiële aanleiding
veroordeeld diensten 1995 bereiken reeds eu sneller regelmatig plots eveneens
geraakt westen wk zorg hof technische das leidt grotere initiatief militaire
auto's betaald terrein hopen russische vijftien grens ontvangen woont pour
sommigen rechten omstandigheden bureau voelde groepen vakantie bereid groene
gewerkt val sfeer respect vlamingen bewijzen oh mogelijkheid gouden probeert
verwachten brandweer rij volledige gemiddeld vijfde hotel rekenen bestuurder
overwegende bedoeld geert wint regen perfect verantwoordelijk persoonlijk blijf
voordeel vijftig product moslims dienen wind n bus comité totale opleiding
redenen gesproken une kijkt risico hasselt voet deden dagelijks waarvoor
beweging nadien kwaad dak bereikt voorsprong vonden gericht klassieke officieel
turkije michel gemakkelijk \\ zaal hangen zaten 1998 werking drinken
overwinning michael films mezelf kaarten handel stil rijk noch droog zomaar
voorwaarden meneer schuld se verhalen vakbonden natuur aangezien verplicht
overeenkomst bedraagt steken rapport mond nodige maakten helaas prins zuiden
dossier uren diep erbij eerlijk studie as pak eigenaar slaan hogere klopt wegen
genieten bergen tour charleroi betreffende bloed uitgevoerd
verantwoordelijkheid jaarlijks thomas kampioen overleden sprak 2008 rechts
vaker leveren coach sturen job overleg station keek you allen parket waaronder
centraal deelnemers gestolen pieter reis nederlanders uitspraak alweer waard
boodschap zwart verklaring engeland speler duizenden toegang tijden eg publieke
gedacht opgepakt h f verboden geregeld bewust lacht angst eraan geplaatst sorry
park que elf bouw zulke cd begrijpen gek ware gele bedankt vereniging voordat
probeerde schrijver gevangenis islam koop hoopt positieve huizen laag waregem
competitie kleur guy wijn versie slapen verdwenen karakter honderden overtuigd
ah harde speciaal onmogelijk bos praktijk 45 albert zoekt waarheid zagen
belgisch zogenaamde di gehaald tientallen noorden 1994 gisteravond koen
afdeling boete lager gewond hoorde chinese rood boom aanpak 75 daarover dokter
nergens beneden directie gevolgd woningen 32 ongeval wees tuin gedurende ding
merken brussels stukken gebouwd rechtstreeks doelman degelijk gentse zekerheid
gedrag democratie toont vooruit 500 x veilig huwelijk passen mijnheer
tentoonstelling aalst lachen wakker wijzen warm baas soorten hond leeft m'n
gewijzigd daders karel vóór ermee onderzoeken qui bert wallonië bezit campagne
klant verdwijnen keuken doordat velen tijdje partner steven welkom ziekte
bijzondere principe raken robert sk effect lichte concurrentie besloten
reageren grenzen groetjes neen medewerkers materiaal ontslag engels turkse
levert model gebieden ofwel lage afgesloten poging ouder hoek serieus
historische voortaan bekijken vreemd vergelijking volgde kern starten veranderd
onderhandelingen herman draait probeer muur jezelf restaurant agenten ogenblik
noodzakelijk fiets gebouwen stijl au vrede aanvankelijk ziek taak vlucht kust
aanbod kim verkeerd engelse duizend verdienen beurt vroegere vertelde 33 eiland
kevin wijst sta begrip past roman onderwerp fortis kandidaten feest flink legde
mate collega soldaten betrekking voeten ondernemingen opgericht moeilijke
oorzaak wijk vlees hè 'n bescherming geest straf woordvoerder japan trein
meerdere verschillen tenminste est traditionele draaien behandeling 1997 zover
combinatie organiseren smaak ie beiden wereldoorlog computer milieu forum vormt
wél gelegen vertrekken recente type limburg oudere wit lief plezier voortdurend
ton manager zestig voort spoor lieten eur verbonden polen avonds bef projecten
tevens j. zorgde inhoud elders reacties il gemeenteraad kende tachtig janssens
uitgebreid vrijwel winnaar bewijs lees vzw veertig neus middel opvallend banen
eeg baby iran instellingen gelegenheid onderneming leuke gerecht vanmorgen
dikke generatie yves festival begrijp werkelijkheid toestand afrika bedoelde
luik nationaal betaalt selectie financieel vielen el eric winter oudste
economisch zelden afkomstig besloot evenwel commerciële reageert bevat c8 blok
sluit franstalige spijt thuisploeg bedoel aanval slot ploegen kv duren mark
dieven leidde vertrek ministers vandaar dichter aanslag organiseert verdere
spits begroting sterker luisteren ideeën verhofstadt podium klacht veroorzaakt
maria waalse plaatselijke acties n-va doelpunt israëlische willem blijken
behoorlijk beschikbaar georganiseerd telefoon mochten wapens par gebaseerd live
twijfel 65 eruit middag bleven 150 olympische operatie 300 oppervlakte
organisaties tegenstelling it anderzijds duurt goe beschouwd drugs deuren pers
oppositie afscheid binnenlandse thema 34 jezus definitief bepalingen serie
louis snelheid relatief bepalen verkeerde blik ongetwijfeld winkels culturele
papier joden afhankelijk olie minuut snelle kandidaat utrecht stof eer
weliswaar eventueel ernstig 36 interessant oosten mama lot 99 hoeven groeien
achteraf gelezen international bod plaatse afghanistan vergadering redactie
prima vervoer procedure bellen helpt allez zo. b. 1992 praat 1993 sloeg belg
zodra redden m. oké min onderdeel uitleg netwerk scoorde lukt willy ontdekt
hoofdpunten trots tenslotte lokeren groot-brittannië uitbreiding droom p. arm
fase clubs erger training filip komst tc gesprekken 46 eentje specifieke
medische oprichting set behoort aanslagen houding armen missen topic studio
betekenis jaarlijkse vliegen behouden mooiste getroffen berichten waarden
stijging militairen programma's bijdrage stijn financiën vb visie
belangstelling glas hopelijk seconden verzoek gerust sindsdien koningin vis
eenvoudig haal vermijden andré meent standaard gelegd dreigt talent destijds
bomen koffie da's gekocht ps draagt bestond 1991 gevaarlijk philippe d.
commentaar roepen 1990 patiënten vliegtuig verjaardag gasten aanwezigheid zak
chris <p> fouten ineens fijn gezondheid theater zult 02 inzet instituut
palestijnse teken werkelijk brug wisten gezond troepen uitvoering luchthaven
gemeenschappen auteur reizen dames rock george verzet vrees democratische
kranten gezinnen bericht kleuren vermoord koninklijke defensie benen menselijke
vreemde 55 turnhout joodse allebei redelijk a. editie kindje haast kiest stukje
pierre eddy jos gebleven partners jarenlang investeringen zus gelet datum
standpunt vermoedelijk waarna < motor sur voorstelling vergeet maxima
commissaris professor beschikken zeventig japanse minste martin erik vooraf
literatuur voorkeur kwart euh schip technisch roept voorgesteld show scoren
india sporen slagen tekort prachtige individuele 01 regionale gezocht inkomsten
voornamelijk 38 compleet negatieve nederlaag sven lagere beveren boonen wens
vermogen v. conflict goedgekeurd dubbele geslaagd 98 teksten hallo stichting
toevallig goud negentig pagina tegenstander antwoorden koninkrijk 37 traditie
roger mist behoren stijgen stadsbestuur letterlijk mekaar kleinere vrt westerse
natuurlijke interview straten toon gsm kris goederen zekere geleid belastingen
g beleggers vanmiddag haven rijdt scheidsrechter overeenkomstig streek speelden
wetenschap hiervoor klachten industrie zone uitzondering richten arbeiders
pakte zesde burger slaat inkomen ervaren ontwikkelen prachtig tegelijkertijd
eventuele verklaarde washington tijdelijk link rand zingen bel seks kleren
hiermee communautaire republiek agenda hugo onafhankelijk voert verdeeld wagens
digitale momenten leiders gemeentebestuur gedachten externe heilige vannacht
rome aangeboden gewezen lierse regeling waaraan an 42 hemel geheim islamitische
planten ontslagen noemde tja beschermen aangepast gestuurd instelling raakt
verscheen verdient concert oranje vrouwelijke spa kwartaal absolute feite stop
ruzie verschenen fans verschijnen buren 250 onvoldoende geschorst fietsen
duidelijke 97 voldoen idd qua interne jean ambtenaren been steunen wereldwijd
supporters beslissen gewest ek verbeteren verdachte renners steeg tienen
voorbereiding verandering zicht treden dromen madrid reclame interesse nood
dader sterven oostenrijk aanzien world conclusie normale omhoog sloot
lid-staten behoefte ontstond papa leverde management consument blauwe
uitsluitend omroep heren rit ingediend durven landbouw overname langzaam beker
simpel paus diens uiterlijk verteld bier evolutie begrepen brede verliest
walter kantoor beschikt nummers test kamp my league geleerd 400 jacques
afspraken maximaal gaven pensioen koos dringend aangehouden autoriteiten tal
ernstige achtergrond dr. luister wetgeving dure dier volop 44 allochtonen
hoeveelheid instantie es opgesteld daarentegen piet tenzij geluid behandeld
bewezen menen contacten steve verdediging favoriete y geraken maat boeren
ongeluk gelooft uitvoeren geopend stoffen afloop miljoenen schoenen c. riep
anderhalf moeilijker journalisten beslag lieve adres fonds maatschappelijke
gedeelte analyse meester klas tony wetenschappelijke regisseur boot katholieke
c6 markten dendermonde gemeenschappelijke gast vn mede san bezoeken arts out
gebruikte belangen afspraak nachts alsnog liepen investeren gelden categorie
hierbij getuigen elementen blad vlot bond ramp treedt trap ring normen teveel
prestatie tim bloemen verandert mol grotendeels voedsel bijdragen 85 opvolger
overige gevoelens gebeurtenissen zwanger uitspraken kunstenaar zulte eindigde
logisch aard verdedigen omwille berlijn communicatie waarover usd moe gestegen
ontwikkeld wensen g. strategie alternatief vogels vaststelling 39 stilaan
chauffeur geprobeerd zetels 43 slaap evenwicht raakten gezelschap geweldig
album dubbel lagen wezen huid erover kunstenaars voormalig leest opnemen banden
cercle fiscale aanleg dik deelnemen wolken verdacht united voertuig rijke u.
onbekende 1000 record kristof onderzocht opklaringen warme structuur ideale
ochtend veertien 48 bekeken stuur voorwaarde integratie sneeuw groeit tellen
openen vertrokken oorsprong aanmerking creëren studies be v pvda km² ajax gat
populair nederlander ingezet 1989 portugal belasting negatief uiterst grondwet
beheer moskou vloer roken artsen bevindt stevig prestaties lijden onderzoekers
stadion gedragen evenmin schuldig brood ach bijkomende formule tekenen verre
luidt iii voren budget s. voorbeelden overzicht hierdoor lastig techniek vos
vrachtwagen oudenaarde technologie duitsers enig gaten gelijke zwitserland
koppel berg ce trouw loon collectie werkgevers koud leeg eh guido opening
beperkte voorzichtig vermeld gepland fabriek rente richard toekomstige schoot
eet stopt bob aandeelhouders schrik controleren christelijke toeristen city
risico's 20.00 james kilo gevoerd breed geschikt vluchten oorspronkelijke
sint-niklaas kapitaal kanten greep werkloosheid maal oren minst 41 schorsing
rolleyes belangrijker smet inspanningen historisch pakt real getrokken
kruispunt vorst that zweden trek love st. las beperken verhouding verwachtingen
bestuurders liter toonde evenveel opzichte firma danny arabische verklaard
breken france westerlo achterstand hoi leert raar uitslag € afrikaanse vandaan
journalist klagen geslagen charles kwartier maes zakken schoon onafhankelijke
liedje gewicht realiteit socialistische werkgever meldt zen stevige stemming
bedragen terugkeer aa barcelona boos regel details kleiner tmf klap tis acteur
passagiers aardig spanning gedachte big verscheidene vechten finales schat
fransen concrete rik oproep goedkoper verenigd onzer slotte protest jo bruno
uitstekend integendeel schieten imago onderdelen theorie gedwongen franstaligen
locatie 20.30 overleed cda tegenstanders zevende zwakke concept martens
overtuigen bronnen constant populaire boord jeroen pink fantastisch ingang
linkse college amsterdamse belga religieuze opent onafhankelijkheid vieren
toerisme no haat politicus 2009 congo luxemburg meegemaakt iraakse golf aankoop
gooien kasteel tips coalitie mss betekenen revolutie overeenstemming redacteur
bibliotheek saddam verklaart maatregel champions marcel kiezers dode «in 52
brak vtm zaventem zijde overgenomen reageerde arme super hetgeen paard naartoe
juridische naties zestien opmerkelijk dagelijkse vroege geweten melk vvd stilte
hielden identiteit aangenomen 2010 getrouwd dertien leer pleit portefeuille dom
respectievelijk duo diezelfde makkelijker stak rob broers strand vergelijken
daartoe griekse staatssecretaris lijf kosovo cheer broek hout stijgt toezicht
dossiers fors voordelen e-mail zichtbaar regime @ sowieso jury papieren koude
melden ontwerp verkozen h. toeval dikwijls doorgaans namens verrassing
bevestigd marokkaanse applaus beloften cup geheime vluchtelingen toegepast
leeuw verschijnt schaal australië geïnteresseerd effectief danken armoede von
scherp gewonden wetten voorts automatisch massaal vrezen bord stroom houten
jongere zanger inclusief alcohol uitgesproken ruime cm geconfronteerd stelling
fusie geslacht verlopen pakistan plant zuid-afrika vooruitgang verhogen knie
aparte gepleegd
""".split())

def numData(data):
    mean   = np.mean(data)
    mode  = max(set(list(data)), key=list(data).count)
    median = np.median(data)
    var    = np.var(data)
    std    = np.std(data)
    minnie = min(data)
    maxie  = max(data)
    
    return mean, mode, median, var, std, minnie, maxie
    
def typeToken(tokens, lemmas): 
    basic_words = 0
    
    for token in tokens:
        if token in basicwords_nl:
            basic_words += 1
            
    ttr = len(lemmas) / len(tokens) 
    ttr_basic = basic_words / len(tokens)
    
    return ttr, ttr_basic

def removePOS(data):
    non_cats = ['PUNCT','SYM','X']
    existing_cats = data.index
    to_remove = []
    
    for cat in non_cats:
        if cat in existing_cats:
            to_remove.append(cat)
    
    return to_remove

def partOfSpeech(data):
    # https://universaldependencies.org/u/pos/
    to_remove = removePOS(data)
    
    counts = data.value_counts()
    counts.drop(to_remove,inplace=True)
    
    nouns = counts['NOUN'] / counts.sum()
    verbs = counts['VERB'] / counts.sum()
    adjs = counts['ADJ'] / counts.sum()
    advs = counts['ADV'] / counts.sum()
    adps = counts['ADP'] / counts.sum()
    prons = counts['PRON'] / counts.sum()
        
    return nouns, verbs, adjs, advs, adps, prons

def processData(z_data, t_data, l_data, d_data, p_data):
    n = len(z_data)
    
    z = np.zeros((n,7))     # statistieken voor zinnen
    d = np.zeros((n,7))     # statistieken voor dependency lengths
    t = []                  # aantal tokens per boek
    l = []                  # aantal unieke lemma's per boek
    r = np.zeros((n,2))     # statistieken voor tyke-token ratio
    p = np.zeros((n,5))     # statistieken voor woordsoorten
    
    for i in range(n):
        zinnen = z_data.iloc[i].dropna()
        tokens = t_data.iloc[i].dropna()
        lemmas = l_data.iloc[i].dropna()
        dependencies = d_data.iloc[i].dropna()
        pos = p_data.iloc[i].dropna()
        
        z_mean, z_mode, z_median, z_var, z_std, z_minnie, z_maxie = numData(zinnen)
        d_mean, d_mode, d_median, d_var, d_std, d_minnie, d_maxie = numData(dependencies)
        ttr, ttr_basic = typeToken(tokens, lemmas)
        p_nouns, p_verbs, p_adjs, p_advs, p_adps, p_prons = partOfSpeech(pos)
        
        z[i] = [z_mean, z_mode, z_median, z_var, z_std, z_minnie, z_maxie]
        d[i] = [d_mean, d_mode, d_median, d_var, d_std, d_minnie, d_maxie]
        t.append(len(tokens))
        l.append(len(lemmas))
        r[i] = [ttr, ttr_basic]
        p[i] = [p_nouns, p_verbs, p_adjs, p_advs, p_adps, p_prons]
    
    # data opslaan in dataframe
    df = pd.DataFrame((z[:,0],z[:,1],z[:,2],z[:,3],z[:,4],z[:,5],z[:,6],t,l,r[:,0],r[:,1],d[:,0],d[:,1],d[:,2],d[:,3],d[:,4],d[:,5],d[:,6],p[:,0],p[:,1],p[:,2],p[:,3],p[:,4],p[:,5]),index=['z_mean','z_mode','z_median','z_variance','z_std','z_min','z_max','tokens','lemmas','ttr','ttr_basic','d_mean','d_mode','d_median','d_variance','d_std','d_min','d_max','nouns','verbs','adjs','advs','adps','prons'],columns=z_data.index).transpose()

    return df

def main():
    # inputbestanden per variabele en tijdsperiode
    zin70 = '70zinnen.csv'
    tok70 = '70tokens.csv'
    lem70 = '70lemmas.csv'
    zin10 = '10zinnen.csv'
    tok10 = '10tokens.csv'
    lem10 = '10lemmas.csv'
    dep70 = '70dependencies.csv'
    dep10 = '10dependencies.csv'
    pos70 = '70pos.csv'
    pos10 = '10pos.csv'
    
    # bestanden inlezen
    data_z70 = pd.read_csv(zin70,index_col=0)
    data_t70 = pd.read_csv(tok70,index_col=0,dtype=str)
    data_l70 = pd.read_csv(lem70,index_col=0,dtype=str)
    data_d70 = pd.read_csv(dep70,index_col=0)
    data_p70 = pd.read_csv(pos70,index_col=0,dtype=str)
    data_z10 = pd.read_csv(zin10,index_col=0)
    data_t10 = pd.read_csv(tok10,index_col=0,dtype=str)
    data_l10 = pd.read_csv(lem10,index_col=0,dtype=str)  
    data_d10 = pd.read_csv(dep10,index_col=0)
    data_p10 = pd.read_csv(pos10,index_col=0,dtype=str)
    
    # data verwerken
    df70 = processData(data_z70, data_t70, data_l70, data_d70, data_p70)
    df10 = processData(data_z10, data_t10, data_l10, data_d10, data_p10)
    
    # bestand om resultaten in op te slaan
    file_out = 'spacyStatistieken.xlsx'
    sheets = ['Canoniek','Moderne bestsellers']
    
    with pd.ExcelWriter(file_out) as writer:
        df70.to_excel(writer, sheet_name=sheets[0])
        df10.to_excel(writer, sheet_name=sheets[1])

if __name__ == "__main__":
    main()
