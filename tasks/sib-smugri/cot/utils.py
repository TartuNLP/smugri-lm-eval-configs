
'''
Let's think step by step.
The premise "L'uomo aprì il rubinetto." can be translated from Estonian into English as "The man turned on the faucet."
The first option "Il gabinetto si riempì d'acqua." can be translated as "The toilet filled with water.", whereas the second option "Dell'acqua fluì dal beccuccio." can be translated as "Water flowed from the spout."
If the man turned on the faucet then it makes sense that water flowed from the spout as a result.
Therefore, the answer is "Dell'acqua fluì dal beccuccio.".
'''
categories = ['health', 'science/technology', 'entertainment', 'health', 'sports']

_vro = ['Nigu mõnõq tõõsõki eksperdiq, om tä skeptiline tuu kotusõ päält, kas diabiiti om võimalik ravviq, tä nimmas, et nail vällälöüdmiisil olõ-õi määnestki tähtsüst inemiisi jaos, kel om jo 1. tüübi diabiit.', '„Tä ehit’ Wi-Fi-ga ussõkellä,“ ütel’ tä.', '2017. aastaga lõpun astõ Siminoff üles ostmiskanali QVC pääl.', 'Olkõq, et üts katsõvaktsiin paistus vähendävät Ebolahe kuulmist, olõ-õi seenuq löüt ruuhi, miä pasnuq olõmanolõva nakkusõ ravimisõs.', 'USA Võimlõmisliit tukõ sõltumaldaq uur’mist, miä või päävävalgõlõ tuvvaq tuu, kuis jäi Larry Nassari ohvridõ julgõhe vällä tuud halvastõ ümbrekäümise osakaal nii kavvas tähele pandmaldaq, ja võtt umas miä taht tarvilidsõq ni pasliguq muutmisõq.']

_liv = ['Neiku mingizt mūd ažātundijid, ta kōdlõb iļ sīe, või tsukkõrrujjõ sōb aŗštõ, merkõs, ku nänt līedamiztõn äb ūo tǟdzitõ rovztõn, kīendõn jõbā um 1. tīp tsukkõrrujā.', 'Ta ētiz WiFi-ukskīela, kītiz ta.', '2017. āigast lopāndõksõs Siminoff vȯļ vȯstõkskanālõs QVC.', 'Sīel āigal, ku ikš eksperimentāl pūotimi vaindiji Ebollõ kūolimizt, seņtš äb ūo sieldõ lieudtõd aiņi, mis kõlbõkstõ teb kuostāntimiz pierāst.', 'USA Gymnastics tigūb īžpīlõbt tuņšlimizt, mis võib eitõ sieldõmt sīen, kui Larry Nassar oppõrd julgstiz kītõd kiužimiz tõuk võiž nei kōgiņ vȱlda tǟdõl panmõt, ja ummistõb amād vajāglizt ja parāzāigalizt mȭitõkst.']

_kpv = ['Мукӧд экспертъяс моз, индӧмӧн, мый тайӧ восьтӧмъяс инмытӧмӧсь йӧзлы, кодъяслӧн эм нин 1 сикаса диабет, сійӧ стӧча оз шу, мый диабет позьӧ бурдӧдны.', 'Сійӧ Wi-Fi-а ӧдзӧсӧ триньган вӧчис, шуис сійӧ.', '2017 во помын Смирнофф петкӧдчис QVC ньӧбасян канал вылын.', 'Кӧть и сюрис экспериментальнӧй вакцина, коді вермӧ чинтыны кулалӧмсӧ Эбола вирусысь, ньӧти лекарство эз на петкӧдлы тӧдчана бурдӧдӧм ӧнія висьӧмысь.', 'АӦШса Гимнастика ошкӧ асшӧр расследуйтӧм, коді вермас эськӧ гӧгӧрвоӧдны, кыдзи та мында нӧйтӧм, повтӧма петкӧдлӧм ловйӧн кольӧм Ларри Наскарлӧн жертваясӧн, вермис та мый дыра кольны казявтӧмӧн, да сулалӧ став колана да лӧсялана вежсьӧмъяс дор.']

_est = ['Nagu mõned teisedki eksperdid, on ta skeptiline selle koha pealt, kas diabeeti on võimalik ravida, märkides, et neil leidudel pole mingit tähtsust inimeste jaoks, kellel on juba 1. tüübi diabeet.', '„Ta ehitas Wi-Fi-ga uksekella,“ ütles ta.', '2017. aasta lõpus esines Siminoff ostukanalil QVC.', 'Olgugi, et üks eksperimentaalne vaktsiin näib vähendavat Ebolasse suremust, ei ole senini leitud ravimeid, mis sobiksid olemasoleva nakkuse ravimiseks.', 'USA Võimlemisliit toetab sõltumatut uurimist, mis võib päevavalgele tuua selle, kuidas jäi Larry Nassari ohvrite julgelt kirjeldatud väärkohtlemise osakaal nii kauaks märkamatuks, ja võtab omaks mis tahes vajalikud ning asjakohased muudatused.']

_fin = ['Eräiden muiden asiantuntijoiden tapaan hän suhtautuu epäilyksellä siihen, voidaanko diabetes parantaa. Hän huomauttaa, että näillä löydöksillä ei ole merkitystä ihmisille, joilla on jo 1-tyypin diabetes.', 'Hän sanoi rakentaneensa Wi-Fi-ovikellon.', 'Vuoden 2017 lopulla Siminoff esiintyi QVC-ostostelevisiokanavalla.', 'Vaikka eräs kokeellinen rokote tuntuukin voivan vähentää ebolan kuolleisuusastetta, tähän mennessä minkään lääkkeen ei ole osoitettu selvästi soveltuvan jo saadun tartunnan hoitamiseen.', 'Yhdysvaltain voimisteluliitto tukee yksityistä tutkimusta, joka voi auttaa ymmärtämään, kuinka niin räikeä väärinkäyttö kuin se, josta Larry Nassarin uhrit ovat rohkeasti kertoneet, on voinut jäädä huomaamatta niin pitkään. Liitto myös toivottaa tervetulleiksi kaikki tarvittavat muutokset.']

_eng = ['Like some other experts, he is skeptical about whether diabetes can be cured, noting that these findings have no relevance to people who already have Type 1 diabetes.', 'He built a WiFi door bell, he said.', 'In late 2017, Siminoff appeared on shopping television channel QVC.', 'While one experimental vaccine appears able to reduce Ebola mortality, up until now, no drugs have been clearly demonstrated suitable for treating existing infection.', 'USA Gymnastics supports an independent investigation that may shine light on how abuse of the proportion described so courageously by the survivors of Larry Nassar could have gone undetected for so long and embraces any necessary and appropriate changes.']

def _generate_CoT_examples(sentences, language):
    examples = []
    for i in range(5):
        example = f"Sentence: {sentences[i]}\nAnswer: Let's think step by step.\nThe sentence \"{sentences[i]}\" can be translated from {language} to English as \"{_eng[i]}\". The most appropriate category for this sentence from the given list is \"{categories[i]}\"."
        examples.append(example)
    return examples

_cot_est = _generate_CoT_examples(_est, "Estonian")
_cot_fin = _generate_CoT_examples(_fin, "Finnish")
_cot_kpv = _generate_CoT_examples(_kpv, "Komi")
_cot_liv = _generate_CoT_examples(_liv, "Livonian")
_cot_vro = _generate_CoT_examples(_vro, "Võro")

def _doc_to_text(doc):
    return f"Sentence: {doc['sentence']}\nAnswer:"

def doc_to_text_cot_oneshot_vro(doc):
    question = _doc_to_text(doc)
    return _cot_vro[0] + "\n\n" + question

def doc_to_text_cot_oneshot_liv(doc):
    question = _doc_to_text(doc)
    return _cot_liv[0] + "\n\n" + question

def doc_to_text_cot_oneshot_kpv(doc):
    question = _doc_to_text(doc)
    return _cot_kpv[0] + "\n\n" + question

def doc_to_text_cot_oneshot_est(doc):
    question = _doc_to_text(doc)
    return _cot_est[0] + "\n\n" + question

def doc_to_text_cot_oneshot_fin(doc):
    question = _doc_to_text(doc)
    return _cot_fin[0] + "\n\n" + question


def doc_to_text_cot_threeshot_vro(doc):
    question = _doc_to_text(doc)
    return "\n\n".join(_cot_vro[:3]) + "\n\n" + question

def doc_to_text_cot_threeshot_liv(doc):
    question = _doc_to_text(doc)
    return "\n\n".join(_cot_liv[:3]) + "\n\n" + question

def doc_to_text_cot_threeshot_kpv(doc):
    question = _doc_to_text(doc)
    return "\n\n".join(_cot_kpv[:3]) + "\n\n" + question

def doc_to_text_cot_threeshot_est(doc):
    question = _doc_to_text(doc)
    return "\n\n".join(_cot_est[:3]) + "\n\n" + question

def doc_to_text_cot_threeshot_fin(doc):
    question = _doc_to_text(doc)
    return "\n\n".join(_cot_fin[:3]) + "\n\n" + question


def doc_to_text_cot_fiveshot_vro(doc):
    question = _doc_to_text(doc)
    return "\n\n".join(_cot_vro) + "\n\n" + question

def doc_to_text_cot_fiveshot_liv(doc):
    question = _doc_to_text(doc)
    return "\n\n".join(_cot_liv) + "\n\n" + question

def doc_to_text_cot_fiveshot_kpv(doc):
    question = _doc_to_text(doc)
    return "\n\n".join(_cot_kpv) + "\n\n" + question

def doc_to_text_cot_fiveshot_est(doc):
    question = _doc_to_text(doc)
    return "\n\n".join(_cot_est) + "\n\n" + question

def doc_to_text_cot_fiveshot_fin(doc):
    question = _doc_to_text(doc)
    return "\n\n".join(_cot_fin) + "\n\n" + question