
_fewshot_samples = [
    {
            "context": "Charles Hoy Fort (6. elokuuta (joidenkin lähteiden mukaan 9.) 1874 – 3. toukokuuta 1932) oli yhdysvaltalainen kirjailija ja paranormaalien ilmiöiden tutkija.",
            "question": "Milloin Charles Fort syntyi?",
            "answers": { "text": [ "6. elokuuta (joidenkin lähteiden mukaan 9.) 1874" ], "answer_start": [ 18 ] },
            "title": "Charles Fort",
            "id": "finnish--7633091408814529542-0"
        }
        ,
        {
            "context": 'Altruismi ([1], ”toinen”[2]) tarkoittaa epäitsekästä ja pyyteetöntä[3] [4] toimintaa, jossa toisen hyvä asetetaan oman edun edelle.[5] Altruismin vastakohta on egoismi.[6] Termin esitti ranskalainen filosofi Auguste Comte vuonna 1851, jolloin hän määritteli altruismin uhrautumiseksi muiden eduksi.[1]',
            "question": "Mitä on altruismi?",
            "answers": { "text": [ "epäitsekästä ja pyyteetöntä[3] [4] toimintaa, jossa toisen hyvä asetetaan oman edun edelle" ], "answer_start": [ 44 ] },
            "title": "Altruismi",
            "id": "finnish-8742325368463988542-0"
        },
        {
            "context": "Wagnerin mestariteoksia ovat hänen myöhäiskauden oopperansa, jotka veivät koko taidesuunnan kehitystä eteenpäin. Jotkut pitävät Tristan ja Isoldea (1857–59) Wagnerin suurimpana yksittäisenä oopperana. Nürnbergin mestarilaulajat (1861–67) on Wagnerin ainoa komedia (lukuun ottamatta unohdettua Liebesverbotia). Nibelungin sormus -tetralogia (1852–74) on neljän oopperan germaaniseen mytologiaan perustuva teossarja. Sen säveltäminen vei 26 vuotta, ja esitykset kestävät yhteensä noin 15 tuntia. Sormussarjaa on kutsuttu musiikinhistorian kunnianhimoisimmaksi hankkeeksi. Wagnerin viimeinen ooppera Parsifal (1877-1882), joka tehtiin Bayreuthin avajaisia silmällä pitäen, on syvämietteinen ja uskonnollissävytteinen Graalin maljan legendaan perustuva työ.",
            "question": "Mikä oli Wilhelm Wagner viimeinen sävellys?",
            "answers": { "text": [ "Parsifal" ], "answer_start": [ 597 ] },
            "title": "Richard Wagner",
            "id": "finnish-5452460901119467072-29"
        }
        ,
        {
            "context": "Harz on horstivuoristo Pohjois-Saksassa[1]. Se muodostaa luonnollisen rajan Ala-Saksin, Saksi-Anhaltin ja Thüringenin osavaltioiden välille.",
            "question": "Missä Harz sijaitsee?",
            "answers": { "text": [ "Pohjois-Saksassa" ], "answer_start": [ 25 ] },
            "title": "Harz",
            "id": "finnish-273387981684821181-0"
        }
        ,
        {
            "context": "Ahmaa tavataan Suomessa, Ruotsissa, Norjassa, Venäjällä sekä Aasiassa ja Pohjois-Amerikassa. Se on väriltään tummanruskea ja hartioiden kohdalta vajaat puoli metriä korkea. Naaras painaa keskimäärin noin 10 kg ja uros jopa 28 kg. Ahma on raadonsyöjä ja peto.",
            "question": "Miten paljon täysikasvuinen ahma painaa?",
            "answers": { "text": [ "Naaras painaa keskimäärin noin 10 kg ja uros jopa 28 kg" ], "answer_start": [ 173 ] },
            "title": "Ahma",
            "id": "finnish-4904655636784261750-1"
        }
]

_eng = {
    "context": "Charles Hoy Fort (August 6 (according to some sources, August 9), 1874 – May 3, 1932) was an American writer and researcher of paranormal phenomena.",
    "question": "When was Charles Fort born?",
    "title": "Charles Fort",
    "answers": { "answer_start": [73], "text": ["August 6 (according to some sources, August 9), 1874"] },
    "id": "finnish--7633091408814529542-0"
}

def list_fewshot_samples() -> list[dict]:
    return _fewshot_samples


def doc_to_text_cot_oneshot(doc):
    _fin = _fewshot_samples[0]
    return f'Title: {_fin["title"]}\nPassage: {_fin["context"]}\nQuestion: {_fin["question"]}\nAnswer: Let\'s think step by step. The passage {_fin["context"]} can be translated from Finnish to English as "{_eng["context"]}" and the question "{_fin["question"]}" can be translated as "{_eng["question"]}". The answer in English is "{_eng["answers"]["text"][0]}". Therefore, the answer in Finnish is "{_fin["answers"]["text"][0]}"\n\nTitle: {doc["title"]}\nPassage: {doc["context"]}\nQuestion: {doc["question"]}\nAnswer:'
