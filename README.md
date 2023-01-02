![bispacy logo](https://github.com/wjbmattingly/biospacy/raw/main/images/biospacy-header.png)

BioSpaCy is a [spacy](www.spacy.io) pipeline for processing biology texts. Currently, the pipeline uses rulers and heuristics to identify:

- DOMAIN
- KINGDOM
- PHYLUM
  - PHYLUM-ANIMALIA
  - PHYLUM-BACTERIA
  - PHYLUM-FUNGI
  - PHYLUM-PLANTS
  - PHYLUM-PROTISTA
- CLASS (NOT INCLUDED YET)
- FAMILY (Plants only)
- SUBFAMILY (Plants only)
- ORDER (Plants only)
- GENUS (Plants only)
- SPECIES (Plants only)
- BINOMINA (Plants only)

# Installation

```python
pip install en_biospacy
```

# Usage

```python
import spacy
from spacy import displacy
text = """
Nephrolepis exaltata, known as the sword fern[1] or Boston fern,
is a species of fern in the family Lomariopsidaceae
(sometimes treated in the families Davalliaceae or Oleandraceae,
or in its own family, Nephrolepidaceae).
"""
nlp = spacy.load("en_biospacy")
doc = nlp(text)
for span in doc.spans["ruler"]:
    print(span.text, span.label_)
```

## Expected Output

```
Nephrolepis GENUS
exaltata SPECIES
Lomariopsidaceae FAMILY
Davalliaceae FAMILY
Oleandraceae FAMILY
Nephrolepis exaltata BINOMINA
```

Data for domains, kingdoms, phyla came from [Wikipedia](www.wikipedia.org). Data for plant family, subfamily, order, genus, and species came from [The World of Flora Online](http://www.worldfloraonline.org/)

# Citation to Data
"WFO (2022): World Flora Online. Version 2022.07. Published on the Internet; http://www.worldfloraonline.org. Accessed on: 1 January 2023".
