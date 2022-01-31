#Module for Info Ext
# print token, dependency, POS tag 
def tok_func(nlp, text):
    doc = nlp(text)
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

def pattern_rec(nlp, text, pattern):

    from spacy.matcher import Matcher

    document = nlp(text)

    matcher = Matcher(nlp.vocab)
    matcher.add("matching_1", [pattern])

    matches = matcher(document)

    print("Printing the {} patterns: ".format(len(matches)))

    print('\n')
    
    for i in range(len(matches)):
        spa = document[matches[i][1]:matches[i][-1]]
        print(str(i+1) + '. ' +spa.text)

    span = document[matches[0][1]:matches[0][-1]]

    return span
