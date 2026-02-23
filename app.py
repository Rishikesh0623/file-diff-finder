from flask import Flask, render_template, request
from diff_finder.set_diff import semantic_compare
from diff_finder.sequence_diff import structural_compare

app = Flask(__name__)

# Limit upload size (5MB)
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024


@app.route("/")
def home():
    return render_template("upload.html")


@app.route("/compare", methods=["POST"])
def compare():
    file1 = request.files.get("file1")
    file2 = request.files.get("file2")
    engine = request.form.get("engine")

    if not file1 or not file2:
        return "Both files must be uploaded", 400

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
        return "Invalid diff mode selected", 400


if __name__ == "__main__":
    app.run(debug=True)