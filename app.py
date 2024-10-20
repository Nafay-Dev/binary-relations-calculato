from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def calculate_binary_relations(set_a, set_b):
    size_a = len(set_a)
    size_b = len(set_b)
    total_relations = 2 ** (size_a * size_b)  # Total relations for Cartesian product
    return total_relations, size_a, size_b

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    set_a = list(set(data['set_a'].split(',')))
    set_b = list(set(data['set_b'].split(',')))

    total_relations, size_a, size_b = calculate_binary_relations(set_a, set_b)

    response = {
        'total_relations': total_relations,
        'size_a': size_a,
        'size_b': size_b,
        'elements_a': set_a,
        'elements_b': set_b
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
