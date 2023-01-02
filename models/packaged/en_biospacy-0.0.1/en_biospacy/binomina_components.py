import spacy
from spacy.tokens import Span
from spacy.language import Language

@Language.component("binomina")
def binomina(doc):
    previous_num = -1
    for i, span in enumerate(doc.spans["ruler"]):
        if span.label_ == "GENUS":
            previous_num = span.end
        if span.label_ == "SPECIES":
            if previous_num == span.start:
                new_span = Span(doc, previous_num-1, span.end, label="BINOMINA")
                doc.spans["ruler"].append(new_span)
    return doc
