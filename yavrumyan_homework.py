text_id = 1
text_type = 'fiction'
text_title = 'Animal Farm'
text_author = 'George Orwell'
text_publication_data = 1983
text_genre = 'Fairy Story'
its_annotated = True
number_of_sentences = 1605
number_of_tokens = 32156

tokens_per_sentence = number_of_tokens / number_of_sentences
biblio_data = text_author, text_title, text_genre, text_publication_data

Label1_for_web = 'Annotated: ' + str(its_annotated)
Label2_for_web = 'Tokens per Sentence: ' + str(tokens_per_sentence)
Label3_for_web = 'Tokens per Sentence (average): ' + str(int(tokens_per_sentence))

print(biblio_data)
print(Label1_for_web)
print(Label2_for_web)
print(type(tokens_per_sentence))
print(Label3_for_web)
print(type(its_annotated))