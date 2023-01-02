import spacy
import binomina_components
import toml
import glob

pipeline_data = toml.load("../project.toml")["pipeline_data"]

def load_patterns(directory):
    patterns = []
    files = glob.glob(f"{directory}/*.txt")
    for file in files:
        file = file.replace("\\", "/")
        print(file)
        with open(file, "r", encoding="utf-8") as f:
            words = f.read().splitlines()
        label = file.split("/")[-1].split(".")[0].upper()
        print(label)
        for word in words:
            if label == "SPECIES":
                patterns.append({"pattern": word, "label": label})
            else:
                patterns.append({"pattern": [{"LOWER": word.lower()}], "label": label})
    return patterns



patterns = load_patterns("../assets/taxonomy")


nlp = spacy.blank("en")
nlp.add_pipe("sentencizer")
ruler = nlp.add_pipe("span_ruler", name="plant_taxonomy")
ruler.add_patterns(patterns)
nlp.add_pipe("binomina")

for name, val in pipeline_data.items():
    nlp.meta[name] = val

nlp.to_disk("../models/biospacy-pipeline")
