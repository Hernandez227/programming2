def length_words(sentence):
    '''
    Función que recibe una frase y devuelve un diccionario con las palabras que contiene y su longitud.
    '''
    words = sentence.split()
    lengths = map(len, words)
    return dict(zip(words, lengths))

print(length_words('Hola, como estan'))