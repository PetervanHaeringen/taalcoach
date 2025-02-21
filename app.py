from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Voorbeeld oefeningen (met unieke ID's)
exercises = [
    {
        "id": 1,
        "type": "word_order",
        "sentence": ["ik", "huis", "naar", "ga"],
        "correct_order": ["ik", "ga", "naar", "huis"],
        "level": "A1"
    },
    {
        "id": 2,
        "type": "word_order",
        "sentence": ["ik", "loop", "straat", "op"],
        "correct_order": ["ik", "loop", "op", "straat"],
        "level": "A1"
    },
    {
        "id": 3,
        "type": "word_order",
        "sentence": ["de", "kat", "op", "de", "stoel", "zit"],
        "correct_order": ["de", "kat", "zit", "op", "de", "stoel"],
        "level": "A1"
    },
    {
        "id": 4,
        "type": "word_order",
        "sentence": ["groente", "kook", "ik", "de"],
        "correct_order": ["ik", "kook", "de", "groente"],
        "level": "A1"
    },
    {
        "id": 5,
        "type": "word_order",
        "sentence": ["ik", "boek", "een", "lees"],
        "correct_order": ["ik", "lees", "een", "boek"],
        "level": "A1"
    },
    {
        "id": 6,
        "type": "word_order",
        "sentence": ["school", "naar", "fietst", "zij"],
        "correct_order": ["zij", "fietst", "naar", "school"],
        "level": "A1"
    },
    {
        "id": 7,
        "type": "word_order",
        "sentence": ["koffie", "ochtend", "wij", "drinken", "de", "in"],
        "correct_order": ["wij", "drinken", "koffie", "in", "de", "ochtend"],
        "level": "A1"
    },
    {
        "id": 8,
        "type": "word_order",
        "sentence": ["het", "veld", "hij", "speelt", "voetbal", "op"],
        "correct_order": ["hij", "speelt", "voetbal", "op", "het", "veld"],
        "level": "A1"
    },
    {
        "id": 9,
        "type": "word_order",
        "sentence": ["van", "de", "hond", "blaft", "de", "buren"],
        "correct_order": ["de", "hond", "van", "de","buren","blaft"],
        "level": "A1"
    },
    {
        "id": 10,
        "type": "word_order",
        "sentence": ["appels", "graag", "eet", "ik"],
        "correct_order": ["ik", "eet", "graag", "appels"],
        "level": "A1"
    },
    {
        "id": 11,
        "type": "word_order",
        "sentence": ["moeder", "het", "kookt", "mijn", "avondeten"],
        "correct_order": ["mijn", "moeder", "kookt", "het", "avondeten"],
        "level": "A1"
    },
    {
        "id": 12,
        "type": "word_order",
        "sentence": ["de", "bank", "slaapt", "op", "de", "kat"],
        "correct_order": ["de", "kat", "slaapt", "op", "de", "bank"],
        "level": "A1"
    },
    {
        "id": 13,
        "type": "word_order",
        "sentence": ["de", "winkel", "gaan", "wij", "naar"],
        "correct_order": ["wij", "gaan", "naar", "de", "winkel"],
        "level": "A1"
    },
    {
        "id": 14,
        "type": "word_order",
        "sentence": ["leest", "een", "boek", "jij"],
        "correct_order": ["jij", "leest", "een", "boek"],
        "level": "A1"
    },
    {
        "id": 15,
        "type": "word_order",
        "sentence": ["de", "tuin", "de", "kinderen", "spelen", "in"],
        "correct_order": ["de", "kinderen", "spelen", "in", "de", "tuin"],
        "level": "A1"
    },
    {
        "id": 16,
        "type": "word_order",
        "sentence": ["de", "avond", "ik", "maak", "huiswerk", "in"],
        "correct_order": ["ik", "maak", "huiswerk", "in", "de", "avond"],
        "level": "A1"
    },
    {
        "id": 17,
        "type": "word_order",
        "sentence": ["naar", "luistert", "zij", "muziek"],
        "correct_order": ["zij", "luistert", "naar", "muziek"],
        "level": "A1"
    },
    {
        "id": 18,
        "type": "word_order",
        "sentence": ["een", "de", "bakker","brood", "hij", "koopt", "bij", "de"],
        "correct_order": ["hij", "koopt", "een", "brood", "bij", "de", "bakker"],
        "level": "A1"
    },
    {
        "id": 19,
        "type": "word_order",
        "sentence": ["wij", "de", "bioscoop", "zien", "in", "een", "film"],
        "correct_order": ["wij", "zien", "een", "film", "in", "de", "bioscoop"],
        "level": "A1"
    },
    {
        "id": 20,
        "type": "word_order",
        "sentence": ["schrijft", "een", "brief", "jij"],
        "correct_order": ["jij", "schrijft", "een", "brief"],
        "level": "A1"
    },
    {
        "id": 21,
        "type": "word_order",
        "sentence": ["een", "bal", "met", "speelt", "de", "jongen"],
        "correct_order": ["de", "jongen", "speelt", "met", "een", "bal"],
        "level": "A1"
    },
    {
        "id": 22,
        "type": "word_order",
        "sentence": ["het", "eten", "bij", "water", "drink", "ik"],
        "correct_order": ["ik", "drink", "water", "bij", "het", "eten"],
        "level": "A1"
    },
    {
        "id": 23,
        "type": "word_order",
        "sentence": ["tijdschrift", "leest", "zij", "een"],
        "correct_order": ["zij", "leest", "een", "tijdschrift"],
        "level": "A1"
    },
    {
        "id": 24,
        "type": "word_order",
        "sentence": ["foto", "maakt", "hij", "een"],
        "correct_order": ["hij", "maakt", "een", "foto"],
        "level": "A1"
    },
    {
        "id": 25,
        "type": "missing_word",
        "sentence": "Ik ___ een appel.",
        "correct_word": "eet",
        "level": "A1"
    },
    {
        "id": 26,
        "type": "missing_word",
        "sentence": "Zij ___ naar school.",
        "correct_word": "loopt",
        "level": "A1"
    },
    {
        "id": 27,
        "type": "missing_word",
        "sentence": "Wij ___ koffie in de ochtend.",
        "correct_word": "drinken",
        "level": "A1"
    },
    {
        "id": 28,
        "type": "missing_word",
        "sentence": "Hij ___ voetbal op het veld.",
        "correct_word": "speelt",
        "level": "A1"
    },
    {
        "id": 29,
        "type": "missing_word",
        "sentence": "De hond ___ 's nachts.",
        "correct_word": "blaft",
        "level": "A1"
    },
    {
        "id": 30,
        "type": "missing_word",
        "sentence": "Ik ___ graag appels.",
        "correct_word": "eet",
        "level": "A1"
    },
    {
        "id": 31,
        "type": "missing_word",
        "sentence": "Mijn moeder ___ het avondeten.",
        "correct_word": "kookt",
        "level": "A1"
    },
    {
        "id": 32,
        "type": "missing_word",
        "sentence": "De kat ___ op de bank.",
        "correct_word": "slaapt",
        "level": "A1"
    },
    {
        "id": 33,
        "type": "missing_word",
        "sentence": "Wij ___ naar de winkel.",
        "correct_word": "gaan",
        "level": "A1"
    },
    {
        "id": 34,
        "type": "missing_word",
        "sentence": "Jij ___ een boek.",
        "correct_word": "leest",
        "level": "A1"
    },
    {
        "id": 35,
        "type": "missing_word",
        "sentence": "De kinderen ___ in de tuin.",
        "correct_word": "spelen",
        "level": "A1"
    },
    {
        "id": 36,
        "type": "missing_word",
        "sentence": "Ik ___ huiswerk in de avond.",
        "correct_word": "maak",
        "level": "A1"
    },
    {
        "id": 37,
        "type": "missing_word",
        "sentence": "Zij ___ naar muziek.",
        "correct_word": "luistert",
        "level": "A1"
    },
    {
        "id": 38,
        "type": "missing_word",
        "sentence": "Hij ___ een brood bij de bakker.",
        "correct_word": "koopt",
        "level": "A1"
    },
    {
        "id": 39,
        "type": "missing_word",
        "sentence": "Wij ___ een film in de bioscoop.",
        "correct_word": "zien",
        "level": "A1"
    },
    {
        "id": 40,
        "type": "missing_word",
        "sentence": "Jij ___ een brief.",
        "correct_word": "schrijft",
        "level": "A1"
    },
    {
        "id": 41,
        "type": "missing_word",
        "sentence": "De jongen ___ met een bal.",
        "correct_word": "speelt",
        "level": "A1"
    },
    {
        "id": 42,
        "type": "missing_word",
        "sentence": "Ik ___ water bij het eten.",
        "correct_word": "drink",
        "level": "A1"
    },
    {
        "id": 43,
        "type": "missing_word",
        "sentence": "Zij ___ een tijdschrift.",
        "correct_word": "leest",
        "level": "A1"
    },
    {
        "id": 44,
        "type": "missing_word",
        "sentence": "Hij ___ een foto.",
        "correct_word": "maakt",
        "level": "A1"
    },
    {
        "id": 45,
        "type": "missing_word",
        "sentence": "Ik ___ naar school.",
        "correct_word": "ga",
        "level": "A1"
    }
    ]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/exercise/<int:exercise_id>')
def get_exercise(exercise_id):
    exercise = next((ex for ex in exercises if ex['id'] == exercise_id), None)
    return jsonify(exercise)

@app.route('/submit', methods=['POST'])
def submit():
    user_answer = request.json.get('answer')
    exercise_id = request.json.get('exercise_id')
    exercise = next((ex for ex in exercises if ex['id'] == exercise_id), None)
    
    if exercise:
        correct = False
        if exercise['type'] == 'word_order':
            user_words = user_answer.strip().split()
            correct = user_words == exercise['correct_order']
        elif exercise['type'] == 'missing_word':
            correct = user_answer.strip().lower() == exercise['correct_word'].lower()
        
        next_exercise_id = exercise_id + 1 if exercise_id < len(exercises) else None  # Volgende oefening

        return jsonify({
            'correct': correct,
            'feedback': 'Goed gedaan!' if correct else 'Probeer het nog eens!',
            'correct_answer': ' '.join(exercise.get('correct_order', [])) if 'correct_order' in exercise else exercise.get('correct_word'),
            'next_exercise_id': next_exercise_id
        })
    
    return jsonify({'error': 'Exercise not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
