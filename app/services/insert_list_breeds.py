import csv
import os
from environs import Env

env = Env()
env.read_env()


def insert_list_breeds_into_table():
    
    with open(env('BREEDS_CSV')) as f:
    reader = csv.DictReader(f)

    reader.to_sql('Breed', con=engine, index= False, if_exists= 'append')
    query = db.update(finaltable).where(finaltable.DataSource == None).values(DataSource == f[i])

    connection.execute(query)


Australian Shepherd
Australian ShepherdAmerican Cocker Spaniel
American Cocker SpanielAkita
AkitaAustralian Cattle Dog
Australian Cattle DogAlaskan Malamute
Alaskan MalamuteAiredale Terrier
Airedale TerrierAmerican Staffordshire Terrier
American Staffordshire TerrierAnatolian Shepherd Dog
Anatolian Shepherd DogAfghan Hound
Afghan HoundAmerican Eskimo Dog
American Eskimo DogAmerican Hairless Terrier
American Hairless TerrierAustralian Terrier
Australian TerrierAffenpinscher
AffenpinscherAmerican Water Spaniel
American Water SpanielAmerican English Coonhound
American English CoonhoundAmerican Foxhound
American Foxhound
Africanis
Aidi
Akbash Dog
Alano Espanol
Alapaha Blue Blood Bulldog
Alaskan Klee Kai
American Pit Bull Terrier
American Staghound
American White Shepherd
Appenzeller Sennenhund
Argentine Dogo
Ariege Pointer
Ariegeois
Australian Bulldog
Australian Kelpie
Australian Stumpy Tail Cattle Dog
Austrian Black and Tan Hound
Austrian Pinscher
Azawakh
Alaskan Husky
Alopekis
American Bulldog
Andalusian Hound
American Mastiff
That start with (A): A total of 40 breeds
Bulldog
BulldogBeagle
BeagleBoxer
BoxerBoston Terrier
Boston TerrierBernese Mountain Dog
Bernese Mountain DogBrittany
BrittanyBorder Collie
Border CollieBasset Hound
Basset HoundBelgian Malinois
Belgian MalinoisBichon Frise
Bichon FriseBloodhound
BloodhoundBullmastiff
BullmastiffBull Terrier
Bull TerrierBouvier des Flandres
Bouvier des FlandresBasenji
BasenjiBorder Terrier
Border TerrierBrussels Griffon
Brussels GriffonBoykin Spaniel
Boykin SpanielBorzoi
BorzoiBelgian Tervuren
Belgian TervurenBlack Russian Terrier
Black Russian TerrierBoerboel
BoerboelBeauceron
BeauceronBelgian Sheepdog
Belgian SheepdogBearded Collie
Bearded CollieBluetick Coonhound
Bluetick CoonhoundBriard
BriardBlack and Tan Coonhound
Black and Tan CoonhoundBedlington Terrier
Bedlington TerrierBerger Picard
Berger PicardBergamasco
Bergamasco
Barbet
Basset Bleu de Gascogne
Basset Fauve de Bretagne
Bavarian Mountain Hound
Belgian Shepherd Laekenois
Black Mouth Cur
Black Norwegian Elkhound
Blue Lacy
Blue Picardy Spaniel
Bohemian Shepherd
Bouvier des Ardennes
Bracco Italiano
Braque du Bourbonnais
Brazilian Terrier
Briquet Griffon Vendeen
Bukovina Sheepdog
Bulgarian Shepherd Dog
Basset Artesien Normand
Beagle-Harrier
Beaglier
Bolognese dog
Bull Arab
Broholmer
Biewer Terrier
Cavalier King Charles Spaniel
Cavalier King Charles SpanielCane Corso
Cane CorsoChihuahua
ChihuahuaCollie
CollieChesapeake Bay Retriever
Chesapeake Bay RetrieverCardigan Welsh Corgi
Cardigan Welsh CorgiCairn Terrier
Cairn TerrierChow Chow
Chow ChowChinese Crested
Chinese CrestedCoton De Tulear
Coton De TulearClumber Spaniel
Clumber SpanielCurly-Coated Retriever
Curly-Coated RetrieverCanaan Dog
Canaan DogCirneco dell’Etna
Cirneco dell’EtnaCesky Terrier
Cesky TerrierChinook
Chinook
Cão da Serra de Aires
Canadian Eskimo Dog
Caravan Hound
Carolina Dog
Carpathian Sheepdog
Catahoula Bulldog
Catahoula Leopard Dog
Catalan Sheepdog
Caucasian Ovcharka
Central Asian Ovtcharka
Cesky Fousek
Chart Polski
Cockapoo
Croatian Sheepdog
Czechoslovakian Wolfdog
Chippiparai
Chizer
Cotonese
Cairmal
Chorkie
Cockalier
Dachshund
DachshundDoberman Pinscher
Doberman PinscherDalmatian
DalmatianDogue de Bordeaux
Dogue de BordeauxDandie Dinmont Terrier
Dandie Dinmont Terrier
Danish-Swedish Farmdog
Deutsche Bracke
Dingo
Drentse Patrijshond
Drever
Dunker
Dutch Shepherd Dog
Dutch Smoushond
Dorgi
Dorkie
Double Doodle
English Springer Spaniel
English Springer SpanielEnglish Cocker Spaniel
English Cocker SpanielEnglish Setter
English SetterEnglish Toy Spaniel
English Toy SpanielEntlebucher Mountain Dog
Entlebucher Mountain DogEnglish Foxhound
English Foxhound
East Siberian Laika
East-European Shepherd
English Shepherd
Eurasier
French Bulldog
French BulldogFlat-Coated Retriever
Flat-Coated RetrieverField Spaniel
Field SpanielFinnish Lapphund
Finnish LapphundFinnish Spitz
Finnish Spitz
Fila Brasileiro
Finnish Hound
French Spaniel
Francais Blanc et Noir
German Shepherd
German ShepherdGolden Retriever
Golden RetrieverGerman Shorthaired Pointer
German Shorthaired PointerGreat Dane
Great DaneGerman Wirehaired Pointer
German Wirehaired PointerGreat Pyrenees
Great PyreneesGreater Swiss Mountain Dog
Greater Swiss Mountain DogGiant Schnauzer
Giant SchnauzerGordon Setter
Gordon SetterGerman Pinscher
German PinscherGreyhound
GreyhoundGlen of Imaal Terrier
Glen of Imaal TerrierGrand Basset Griffon Vendeen
Grand Basset Griffon Vendeen
Grand Bleu de Gascogne
German Longhaired Pointer
Goldendoodle
Greenland Dog
Griffon bleu de Gascogne
Havanese
HavaneseHarrier
Harrier
Hamilton Hound
Hokkaido Dog
Hovawart
Italian Greyhound
Italian GreyhoundIrish Wolfhound
Irish WolfhoundIrish Setter
Irish SetterIrish Terrier
Irish TerrierIrish Red and White Setter
Irish Red and White SetterIbizan Hound
Ibizan HoundIcelandic Sheepdog
Icelandic SheepdogIrish Water Spaniel
Irish Water Spaniel
Jack Russell Terrier
Jack Russell TerrierJapanese Chin
Japanese Chin
Jagdterrier
Jämthund
Japanese Spitz
Japanese Terrier
Keeshond
KeeshondKerry Blue Terrier
Kerry Blue TerrierKooikerhondje
KooikerhondjeKuvasz
KuvaszKomondor
Komondor
Kangal Dog
Korean Jindo
Karelian Bear Dog
Kishu Ken
Koolie
Kromfohrlander
Karst Shepherd
King Shepherd
Kyi-Leo
Labrador Retriever
Labrador RetrieverLhasa Apso
Lhasa ApsoLeonberger
LeonbergerLagotto Romagnolo
Lagotto RomagnoloLakeland Terrier
Lakeland TerrierLowchen
Lowchen
Large Munsterlander
Lancashire Heeler
Landseer
Lapponian Herder
Lucas Terrier
Lurcher
Miniature Schnauzer
Miniature SchnauzerMastiff
MastiffMiniature American Shepherd
Miniature American ShepherdMaltese
MalteseMiniature Pinscher
Miniature PinscherMiniature Bull Terrier
Miniature Bull TerrierManchester Terrier
Manchester Terrier
Miniature Poodle
Miniature Shar Pei
McNab
Miniature Bulldog
Mudi
Mountain Feist
Majestic Tree Hound
Maremma Sheepdog
Mal-Shi
Mountain Cur
Newfoundland
NewfoundlandNova Scotia Duck Tolling Retriever
Nova Scotia Duck Tolling RetrieverNorwegian Elkhound
Norwegian ElkhoundNeapolitan Mastiff
Neapolitan MastiffNorwich Terrier
Norwich TerrierNorfolk Terrier
Norfolk TerrierNorwegian Buhund
Norwegian BuhundNorwegian Lundehund
Norwegian Lundehund
New Guinea Singing Dog
Norrbottenspets
Northern Inuit Dog
Moscow Watchdog
Old English Sheepdog
Old English SheepdogOtterhound
Otterhound
Olde English Bulldogge
Poodle
PoodlePembroke Welsh Corgi
Pembroke Welsh CorgiPomeranian
PomeranianPug
PugPortuguese Water Dog
Portuguese Water DogPapillon
PapillonPekingese
PekingesePointer
PointerParson Russell Terrier
Parson Russell TerrierPumi
PumiPortuguese Podengo Pequeno
Portuguese Podengo PequenoPetit Basset Griffon Vendeen
Petit Basset Griffon VendeenPuli
PuliPolish Lowland Sheepdog
Polish Lowland SheepdogPlott Hound
Plott HoundPharaoh Hound
Pharaoh HoundPyrenean Shepherd
Pyrenean Shepherd
Polish Hunting Dog
Pakistani Mastiff
Patterdale Terrier
Perro de Presa Canario
Perro de Presa Mallorquin
Peruvian Inca Orchid
Picardy Spaniel
Plummer Terrier
Portuguese Pointer
Prazsky Krysarik
Pudelpointer
Pont-Audemer Spaniel
Pyrenean Mastiff
Polish Tatra Sheepdog
Puggle
Rottweiler
RottweilerRhodesian Ridgeback
Rhodesian RidgebackRat Terrier
Rat TerrierRedbone Coonhound
Redbone Coonhound
Rafeiro do Alentejo
Rajapalayam dog
Russian Spaniel
Russian Toy
Mioritic Shepherd Dog
Russian Tsvetnaya Bolonka
Siberian Husky
Siberian HuskyShih Tzu
Shih TzuShetland Sheepdog
Shetland SheepdogShiba Inu
Shiba InuSt. Bernard
St. BernardSoft Coated Wheaten Terrier
Soft Coated Wheaten TerrierScottish Terrier
Scottish TerrierSamoyed
SamoyedShar-Pei
Shar-PeiStaffordshire Bull Terrier
Staffordshire Bull TerrierStandard Schnauzer
Standard SchnauzerSchipperke
SchipperkeSpinone Italiano
Spinone ItalianoSilky Terrier
Silky TerrierSaluki
SalukiSmooth Fox Terrier
Smooth Fox TerrierSpanish Water Dog
Spanish Water DogScottish Deerhound
Scottish DeerhoundSealyham Terrier
Sealyham TerrierSwedish Vallhund
Swedish VallhundSkye Terrier
Skye TerrierSussex Spaniel
Sussex SpanielSloughi
Sloughi
Spanish Greyhound
Small Munsterlander
Saarloos wolfdog
Sapsali
Sarplaninac
Schapendoes
Seppala Siberian Sleddog
Shikoku dog
Shiloh Shepherd dog
Silken Windhound
Smaland Hound
South Russian Ovcharka
Spanish Mastiff
Serbian Hound
Swedish Lapphund
Shichon
Slovensky Cuvac
Stabyhoun
Tibetan Terrier
Toy Fox TerrierTibetan Spaniel
Tibetan SpanielTibetan Mastiff
Tibetan MastiffTreeing Walker Coonhound
Treeing Walker Coonhound
Toy Poodle
Tamaskan Dog
Thai Bangkaew Dog
Thai Ridgeback
Tornjak
Tosa Ken
Transylvanian Hound
Texas Heeler
Taco Terrier
Vizsla
Volpino Italiano
Weimaraner
WeimaranerWest Highland White Terrier
West Highland White TerrierWhippet
WhippetWirehaired Pointing Griffon
Wirehaired Pointing GriffonWire Fox Terrier
Wire Fox TerrierWelsh Terrier
Welsh TerrierWelsh Springer Spaniel
Welsh Springer SpanielWirehaired Vizsla
Wirehaired Vizsla
West Siberian Laika
Wetterhoun
Xoloitzcuintli
Yorkshire Terrier