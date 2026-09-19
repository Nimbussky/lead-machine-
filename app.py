import os
import json
from datetime import datetime
from flask import Flask, render_template, request, jsonify, send_file
from lead_engine import LeadEngine

app = Flask(__name__)
app.config["RESULTS_FOLDER"] = os.path.join(os.path.dirname(__file__), "results")
os.makedirs(app.config["RESULTS_FOLDER"], exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/search", methods=["POST"])
def search():
    data = request.get_json()
    query = data.get("query", "").strip()
    location = data.get("location", "").strip()
    sources = data.get("sources", [])
    max_results = int(data.get("max_results", 50))

    if not query:
        return jsonify({"error": "Query is required"}), 400

    engine = LeadEngine()
    leads = engine.generate_leads(query, location, sources, max_results)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    excel_file = os.path.join(app.config["RESULTS_FOLDER"], f"leads_{timestamp}.xlsx")
    csv_file = os.path.join(app.config["RESULTS_FOLDER"], f"leads_{timestamp}.csv")
    engine.export_to_excel(excel_file)
    engine.export_to_csv(csv_file)

    results = {
        "total": len(leads),
        "leads": [lead.to_dict() for lead in leads],
        "excel_file": f"leads_{timestamp}.xlsx",
        "csv_file": f"leads_{timestamp}.csv",
        "query": query,
        "location": location,
    }
    return jsonify(results)

@app.route("/api/download/<filename>")
def download(filename):
    filepath = os.path.join(app.config["RESULTS_FOLDER"], filename)
    if os.path.exists(filepath):
        return send_file(filepath, as_attachment=True)
    return jsonify({"error": "File not found"}), 404

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("  AI LEAD GENERATION ENGINE - Web Interface")
    print("  Open http://localhost:5000 in your browser")
    print("=" * 60 + "\n")
    app.run(debug=True, port=5000)
