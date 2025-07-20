from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simple mock dictionary data in English and Spanish
DICTIONARY = {
    'en': {
        'apple': 'A round fruit with red or green skin and a crisp white flesh.',
        'book': 'A set of printed pages bound together.',
        'cat': 'A small domesticated carnivorous mammal with soft fur.'
    },
    'es': {
        'manzana': 'Una fruta redonda con piel roja o verde y pulpa blanca y crujiente.',
        'libro': 'Un conjunto de páginas impresas encuadernadas.',
        'gato': 'Un pequeño mamífero carnívoro domesticado con pelaje suave.'
    }
}

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        word = request.form.get('word', '').strip().lower()
        lang = request.args.get('lang', 'en')
        return redirect(url_for('word', word=word, lang=lang))
    return render_template('home.html')

@app.route('/word/<word>')
def word(word):
    lang = request.args.get('lang', 'en')
    lang = lang if lang in DICTIONARY else 'en'
    definition = DICTIONARY[lang].get(word.lower())
    return render_template('word.html', word=word, definition=definition, lang=lang)

if __name__ == '__main__':
    app.run(debug=True)
