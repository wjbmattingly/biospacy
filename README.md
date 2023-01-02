![bispacy logo](https://github.com/wjbmattingly/biospacy/raw/main/images/biospacy-logo.png)

BioSpaCy is a [spacy](www.spacy.io) pipeline for processing biology texts. Currently, the pipeline uses heuristics (rules) to identify: FAMILY, SUBFAMILY, ORDER, GENUS, SPECIES, and BINOMINA. To prevent the EntityRuler from Erasing the subcomponents off a binomina hit, all binomina entities are labeled with a SpanRuler.
