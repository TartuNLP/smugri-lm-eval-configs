from lm_eval.filters.extraction import Filter
from lm_eval.api.registry import register_filter

def doc_to_text(doc):
    if doc["question"] == "cause":
        question = "What might be the cause of " + '"' + doc["premise"] + '"' + "?"
    else:
        question = "What might have happened as a result of " + '"' + doc["premise"] + '"' + "?"
    
    question = question + "\n" + "Options:" + "\n" + "- " + '"' + doc["choice1"] + '"' + "\n" + "- " + '"' + doc["choice2"] + '"'
    return question + "\n" + "Answer:"

def doc_to_choice(doc):
    return [doc["choice1"],  doc["choice2"]]


def list_fewshot_samples() -> list[dict]:
    return [
        {'premise': 'Mees keeras kraani lahti.', 'choice1': 'Tualett täitus veega.', 'choice2': 'Tilast voolas vett.', 'question': 'effect', 'label': 1, 'idx': 0, 'changed': False},
        {'premise': 'Hamburgeri liha pruunistus.', 'choice1': 'Kokk külmutas selle.', 'choice2': 'Kokk grillis seda.', 'question': 'cause', 'label': 1, 'idx': 4, 'changed': False},
        {'premise': 'Tüdruk leidis oma helveste seest putuka.', 'choice1': 'Ta kallas piima kaussi.', 'choice2': 'Ta kaotas oma isu.', 'question': 'effect', 'label': 1, 'idx': 1, 'changed': False},
        {'premise': 'Ma otsustasin ööseks koju jääda.', 'choice1': 'Ilmateade ennustas tormi.', 'choice2': 'Mu sõbrad käisid peale, et läheksin välja.', 'question': 'cause', 'label': 0, 'idx': 6, 'changed': False},
        {'premise': 'Naine jäi pensionile.', 'choice1': 'Ta sai oma pensioni kätte.', 'choice2': 'Ta maksis oma hüpoteegi ära.', 'question': 'effect', 'label': 0, 'idx': 2, 'changed': False}
    ]

@register_filter("remove_quotes")
class QuotesFilter(Filter):
    """ """

    def __init__(self) -> None:
        pass

    def apply(self, resps, docs):
        def filter_set(inst):
            filtered_resp = []
            for resp in inst:
                if resp.startswith('"') and resp.endswith('"'):
                    resp = resp[1:-1]

                filtered_resp.append(resp)

            return filtered_resp

        filtered_resps = [filter_set(resp) for resp in resps]

        return filtered_resps
