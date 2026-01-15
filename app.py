from flask import Flask, render_template, request
from PIL import Image
import logic
import requests
from io import BytesIO

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    ascii_art = None
    error = None

    if request.method == 'POST':
        try:
            image = None
            
            if 'file' in request.files and request.files['file'].filename != '':
                file = request.files['file']
                image = Image.open(file)
            
            elif 'image_url' in request.form and request.form['image_url'] != '':
                url = request.form['image_url']
                response = requests.get(url)
                response.raise_for_status() 
                image = Image.open(BytesIO(response.content))

            else:
                error = "Please upload a file or drop an image."

            if image:
                width = int(request.form.get('width', 100))
                ascii_art = logic.generate_ascii(image, width)

        except Exception as e:
            error = f"Error processing image: {str(e)}"

    return render_template('index.html', ascii_art=ascii_art, error=error)

if __name__ == '__main__':
    app.run(debug=True)