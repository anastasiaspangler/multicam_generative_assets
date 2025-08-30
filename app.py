from flask import Flask, render_template_string, send_from_directory, abort, url_for
from flask import render_template, request, jsonify
from replicate_helper import send_to_replicate
from flask import send_from_directory
import os
app = Flask(__name__)
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route("/viewer/<object_name>")
def viewer(object_name):
    # Just renders the HTML template with the object name injected
    return render_template("viewer.html", object_name=object_name)

@app.route("/models/<object_name>")
def models(object_name):
    base = f"/files/{object_name}/replicate_predictions/{object_name}_output"
    data = {
        "name": object_name,
        "glb": f"{base}.glb",  # keep if you want
        # "video": f"/files/{object_name}/replicate_predictions/{object_name}_color_video.mp4",
        "images": [
            f"/files/{object_name}/img_a1.png",
            f"/files/{object_name}/img_a2.png",
            f"/files/{object_name}/img_b1.png",
            f"/files/{object_name}/img_b2.png",
        ],
    }
    return jsonify(data)


@app.route("/files/<path:filename>")
def files(filename):
    # NOTE: Files are served through this method to avoid Flask's static folder
    #       The intent is to preserve backend flexibility for research code

    directory = "local_storage/"
    fpath = directory + filename
    if not os.path.isfile(fpath):
        abort(404, description=f"File not found: {fpath}")

    return send_from_directory(directory, filename)

@app.route('/replicate', methods=['POST'])
def post_replicate():
    data = request.form.to_dict()
    name = data["name"]
    abs_paths = [data["path_a"], data["path_b"], data["path_c"], data["path_d"]]
    api_response = send_to_replicate(name, abs_paths)
    if api_response:
        return jsonify({
            "received": data,
            "status": "pass",
            "preview": str(f"http://127.0.0.1:5000/viewer/{name}")
        })
    return jsonify({"status": "fail"})

@app.route("/test_image/<object_name>")
def test_image(object_name):
    # the image we expect to exist for this test
    img_rel = f"{object_name}/img_a1.png"

    if not os.path.isfile(img_rel):
        return f"Test image not found at {img_rel}", 404

    html = """
    <!doctype html>
    <html>
      <head><meta charset="utf-8"><title>Test Image - {{ object_name }}</title></head>
      <body>
        <h3>Test image for {{ object_name }}</h3>
        <p>If this is blank, open the image URL directly:</p>
        <pre>{{ files_url }}</pre>
        <img src="{{ files_url }}" alt="test image" style="max-width:600px; display:block; margin-top:10px;">
      </body>
    </html>
    """
    files_url = url_for('files', filename=img_rel)
    return render_template_string(html, object_name=object_name, files_url=files_url)


if __name__ == '__main__':
    app.run(debug=True)


