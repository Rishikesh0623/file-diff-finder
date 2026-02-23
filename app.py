from flask import Flask, render_template, request
from werkzeug.exceptions import RequestEntityTooLarge
from diff_finder.set_diff import semantic_compare
from diff_finder.sequence_diff import structural_compare
import os

app = Flask(__name__)

# ----------------------------
# Configuration
# ----------------------------

# Limit upload size to 5MB
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024

# Allowed file extensions
ALLOWED_EXTENSIONS = {
    "txt", "py", "js", "java", "json",
    "yaml", "yml", "env", "cfg",
    "ini", "md", "html", "css"
}


# ----------------------------
# Helper Functions
# ----------------------------

def allowed_file(filename):
    return (
        "." in filename and
        filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


# ----------------------------
# Error Handlers
# ----------------------------

@app.errorhandler(RequestEntityTooLarge)
def handle_file_too_large(e):
    return "File too large. Maximum allowed size is 5MB.", 413


# ----------------------------
# Routes
# ----------------------------

@app.route("/")
def home():
    return render_template("upload.html")


@app.route("/compare", methods=["POST"])
def compare():

    file1 = request.files.get("file1")
    file2 = request.files.get("file2")
    engine = request.form.get("engine")

    # Basic validation
    if not file1 or not file2:
        return "Both files must be uploaded.", 400

    if not allowed_file(file1.filename) or not allowed_file(file2.filename):
        return "Unsupported file type. Only text/code files are allowed.", 400

    if engine == "semantic":
        results = semantic_compare(file1, file2)
        return render_template(
            "result.html",
            diff=results["diff"],
            engine="semantic"
        )

    elif engine == "structural":
        results = structural_compare(file1, file2)
        return render_template(
            "result.html",
            structural_html=results["html"],
            engine="structural"
        )

    else:
        return "Invalid diff mode selected.", 400


# ----------------------------
# Entry Point
# ----------------------------

if __name__ == "__main__":
    app.run(debug=True)