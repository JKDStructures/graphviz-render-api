
from flask import Flask, request, send_file, jsonify
import tempfile
import os
from graphviz import Source

app = Flask(__name__)

@app.route('/render', methods=['POST'])
def render_graph():
    try:
        data = request.json
        dot_code = data.get('dot')
        format = data.get('format', 'pdf')  # 'pdf' or 'png'

        if not dot_code:
            return jsonify({"error": "Missing 'dot' in request"}), 400

        with tempfile.TemporaryDirectory() as tmpdirname:
            src = Source(dot_code)
            output_path = os.path.join(tmpdirname, f"output.{format}")
            src.render(filename="output", directory=tmpdirname, format=format, cleanup=True)
            return send_file(output_path, as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
