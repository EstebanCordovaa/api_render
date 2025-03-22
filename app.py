from flask import Flask, jsonify, request
from pickle import load as pload
app = Flask(__name__)


#Crear servicio
with open("model_dict_car_evaluation.pkl", "rb") as file:
    model_dict = pload(file)


@app.route('/', methods=['POST'])
def predict_car_eval():
    try:
        # Obtener los datos enviados en formato JSON
        buying = data.get('buying')
        maint = data.get('maint')
        doors = data.get('doors')
        persons = data.get('persons')
        lug_boot = data.get('lug_boot')
        safety = data.get('safety')
        
        # Realizar predicciones usando el modelo cargado
        prediction = model_dict['model'].predict([features])
        response = {
            'prediction': prediction.tolist(),
            'algorithm': model_dict['algorithm_name']
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
