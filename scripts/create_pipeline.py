import spacy
import toml
pipeline_data = toml.load("../project.toml")["pipeline_data"]
print(pipeline_data)
def load_patterns(file, label):
    with open(file, "r", encoding="utf-8") as f:
        patterns = f.read().splitlines()
    all_patterns = []
    for pattern in patterns:
        all_patterns.append({"pattern": pattern, "label": label})
    return all_patterns

genera = load_patterns("../data/genus_names.txt", "GENUS")
species = load_patterns("../data/species_names.txt", "SPECIES")
families = load_patterns("../data/family_names.txt", "FAMILY")
orrder = load_patterns("../data/order_names.txt", "ORDER")
subfamily = load_patterns("../data/subfamily_names.txt", "SUBFAMILY")

patterns = genera+species+families+order+subfamily

binomina_pattern = [
            {"pattern":
            [
                {"ENT_TYPE": "GENUS"},
                {"ENT_TYPE": "SPECIES"}
            ],
            "label": "BINOMINA"}
          ]

nlp = spacy.blank("en")
nlp.add_pipe("sentencizer")
ruler = nlp.add_pipe("entity_ruler")
ruler.add_patterns(patterns)
binomina_ruler = nlp.add_pipe("span_ruler",
                        name="binomina"
                        )
binomina_ruler.add_patterns(binomina_pattern)

for name, val in pipeline_data.items():
    nlp.meta[name] = val

nlp.to_disk("../biospacy/models/biospacy-pipeline")
