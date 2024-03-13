import spacy

nlp = spacy.load("en_core_web_sm")
text = "Apple was founded by Steve Jobs and Steve Wozniak."  # Example text
doc = nlp(text)
print([(ent.text, ent.label_) for ent in doc.ents])  # Should print entities
