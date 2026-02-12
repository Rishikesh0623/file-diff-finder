from flask import Flask, render_template, request
from diff_finder import compare_files

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('upload.html')

@app.route('/compare', methods=['POST'])
def compare():
    file1 = request.files['file1']
    file2 = request.files['file2']

    if not file1 or not file2:
        return 'Both files must be uploaded', 400

    results = compare_files(file1, file2)

    return render_template('result.html', added=results['added'], removed=results['removed'])

if __name__ == '__main__':
    app.run(debug=True)