#Module for Info Ext
# print token, dependency, POS tag 
def tok_func(doc):
    for tok in doc:
        print(tok.text, "-->",tok.dep_,"-->", tok.pos_)
        print('\n')
    print('\n\n\n\n\n')

def vis_dependency_parsing(text):
    import spacy
    from spacy import displacy
    nlp = spacy.load("en_core_web_sm")
    document = nlp(text)
    displacy.render(document, style='dep', jupyter=True)
