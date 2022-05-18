from flask import Blueprint, jsonify, request
from app.utils.utilities import predict_pipeline

predict_bp = Blueprint("predict", __name__)


@predict_bp.post("/predict")
def predict():
    data = request.json
    try:
        sample = data["text"]
    except KeyError:
        return jsonify({"error": "No text sent"})

    sample = [sample]
    predictions = predict_pipeline(sample)
    try:
        result = jsonify(predictions[0])
    except TypeError as e:
        result = jsonify({"error": str(e)})
    return result
