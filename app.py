from flask import Flask, request, jsonify
from src.pipelines.prediction_pipeline import PredictionPipeline, CustomClass

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON data from request
        json_data = request.get_json()
        
        # Create CustomClass instance with JSON data
        data = CustomClass(
            age=int(json_data.get("age")),
            workclass=int(json_data.get("workclass")),
            education_num=int(json_data.get("education_num")),
            marital_status=int(json_data.get("marital_status")),
            occupation=int(json_data.get("occupation")),
            relationship=int(json_data.get("relationship")),
            race=int(json_data.get("race")),
            sex=int(json_data.get("sex")),
            capital_gain=int(json_data.get("capital_gain")),
            capital_loss=int(json_data.get("capital_loss")),
            hours_per_week=int(json_data.get("hours_per_week")),
            native_country=int(json_data.get("native_country"))
        )

        # Get prediction
        final_data = data.get_data_DataFrame()
        pipeline_prediction = PredictionPipeline()
        pred = pipeline_prediction.predict(final_data)

        # Return prediction result
        return jsonify({
            "status": "success",
            "prediction": int(pred[0]),
            "income_category": "<=50K" if pred[0] == 0 else ">50K"
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

#---------------------Test-----------------------------------
# from src.logger import logging

# def main():

#     try:
#         logging.info("Starting the application")

#         logging.info("Step 1: Initializing application")
#         x = 5
#         y = 2

#         logging.info(f"Step 2: Performing operation: x={x}, y={y}")
#         result = x + y

#         logging.info(f"Step 3: Operation result: {result}")

#         if result > 10:
#             logging.warning(f"Step 4: Result {result} is greater than 10")
#         else:
#             logging.error(f"Step 4: Result {result} is less then 10")

#     except Exception as e:

#         logging.error("An error occurred in the main function", exc_info=True)
#         raise e
    
# if __name__ == "__main__":
#     logging.info("="*50)
#     logging.info("Application Run Started")
#     logging.info("="*50)

#     try:
#         main()
#         logging.info("Application completed successfully")
#     except Exception as e:
#         logging.error("Application failed", exc_info=True)
#     finally:
#         logging.info("="*50)
#         logging.info("Application execution has ended")
#         logging.info("="*50)
