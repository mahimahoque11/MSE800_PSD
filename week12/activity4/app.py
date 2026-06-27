from pathlib import Path

from flask import Flask, request, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_FOLDER = BASE_DIR / "static" / "uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "webp"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def home():
    image_url = None
    message = ""

    if request.method == "POST":
        image = request.files.get("image")

        if image and image.filename and allowed_file(image.filename):
            UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)
            filename = secure_filename(image.filename)
            image_path = UPLOAD_FOLDER / filename
            image.save(image_path)
            image_url = url_for("static", filename=f"uploads/{filename}")
            message = "Image uploaded successfully."
        else:
            message = "Please choose a valid image file."

    image_preview = ""
    if image_url:
        image_preview = f"""
        <section>
            <h2>Uploaded Image</h2>
            <img src="{image_url}" alt="Uploaded image" style="max-width: 500px; width: 100%; height: auto;">
        </section>
        """

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Flask Image Upload</title>
    </head>
    <body>
        <h1>Load and Display an Image</h1>
        <form method="POST" enctype="multipart/form-data">
            <label for="image">Choose an image from your computer:</label>
            <input type="file" id="image" name="image" accept="image/*" required>
            <button type="submit">Upload Image</button>
        </form>
        <p>{message}</p>
        {image_preview}
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
