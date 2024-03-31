from flask import Flask, request, jsonify
from gradio_client import Client
import re
app = Flask(__name__)

# Define your API key
# API_KEY = "your_api_key_here"
pattern = r'^[a-zA-Z][0-9][a-zA-Z][0-9].{11}$'
@app.route('/process_prompt/<api_key>/<int:seed>/<int:width>/<int:height>/<float:guidance_scale>/<prompt>', methods=['GET'])
def process_prompt(api_key, seed, width, height, guidance_scale, prompt):
    # Check if the provided API key matches the expected API key
    if  re.match(pattern, api_key):
        

    # Initialize the Gradio client with the API endpoint
        client = Client("https://playgroundai-playground-v2-5.hf.space/--replicas/77jhe/")
        # Send a request to the API endpoint with the provided parameters
        result = client.predict(
            prompt,
            prompt,         # Negative prompt (same as prompt)
            False,          # Do not use negative prompt
            seed,
            width,
            height,
            guidance_scale,
            True,           # Randomize seed
            api_name="/run" # Specify the API endpoint
        )

        # Return the prediction result
        return jsonify(result)
    else:
        return jsonify({"API Key": "Unauthorized, Invalid"}), 401
if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
