from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import os
from deep_learning_tf_models import predictImagesClass
from deep_learning_torch_models import predict_images_class
import io
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

# Define a route for health check
@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy"})

@app.route("/classify", methods=["POST"])
@cross_origin()
def classify_image():
    result=''
    # Get the image data from the request
    image_data = request.files["image"]
    image_bytes = io.BytesIO(image_data.read())
    image_data.seek(0)
    model_name = request.form['model']
    print("Request has been received successfully")
    
    if model_name == 'resnet50':
        result = predict_images_class(model_name, image_bytes)
        
    elif model_name == 'nesnet_a_large':
        result = predict_images_class(model_name, image_bytes)
        
    elif model_name == 'inception_resnet_v2':
        model_name=os.getenv('MODEL_LOC')+'inception_resnet_v2.keras'
        result=predictImagesClass(model_name, image_bytes, image_width=299, image_height=299)
       
    elif model_name == 'custom_cnn':
        model_name=os.getenv('MODEL_LOC')+'custom_cnn.keras'
        result=predictImagesClass(model_name, image_bytes, image_width=256, image_height=256)

    response = {
        "status": "success",
        "message": result
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, host=os.getenv('HOST'), port=os.getenv('PORT'))