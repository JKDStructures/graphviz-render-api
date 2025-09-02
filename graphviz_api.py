from flask import Flask, request, send_file, jsonify
import tempfile, os
from graphviz import Source

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"}), 200

@app.route('/render', methods=['POST'])
def render_graph():
    try:
        data = request.get_json(silent=True) or {}
        dot_code = data.get('dot')
        fmt = data.get('format', 'pdf').lower()  # 'pdf' or 'png'

        if fmt not in ('pdf', 'png'):
            return jsonify({"error": "format must be 'pdf' or 'png'"}), 400
        if not dot_code:
            return jsonify({"error": "Missing 'dot' in request"}), 400

        with tempfile.TemporaryDirectory() as tmp:
            src = Source(dot_code)
            out = os.path.join(tmp, f"out.{fmt}")
            src.render(filename="out", directory=tmp, format=fmt, cleanup=True)
            return send_file(out, as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
