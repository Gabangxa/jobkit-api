from flask import Blueprint, request, jsonify
from enrichment.enricher import extract_skills, normalize_salary, classify_experience, classify_remote, TECH_TOOLS

enrich_bp = Blueprint("enrich", __name__)


@enrich_bp.route("/v1/jobs/enrich", methods=["POST"])
def enrich_description():
    body = request.get_json(silent=True)
    if not body or not body.get("description", "").strip():
        return jsonify({"error": "Field 'description' is required and must not be empty"}), 400

    desc = body["description"]
    skills = extract_skills(desc)
    salary = normalize_salary(desc)
    level = classify_experience("", desc)
    remote_type = classify_remote("", "", desc)
    tech_stack = [s for s in skills if s.lower() in TECH_TOOLS][:5]

    return jsonify({
        "skills": skills,
        "salary": salary,
        "experience_level": level,
        "remote_type": remote_type,
        "tech_stack": tech_stack,
    }), 200
