from flask import Blueprint, request, jsonify, current_app

jobs_bp = Blueprint("jobs", __name__)

DEMO_KEY = "demo-key-jobkit-2026"


def _check_auth():
    key = request.headers.get("X-API-Key", "")
    if key != DEMO_KEY:
        return False
    return True


@jobs_bp.route("/v1/jobs/search")
def search_jobs():
    if not _check_auth():
        return jsonify({"error": "Invalid API key"}), 401

    # Rate limit check
    from server import check_rate_limit
    limited, response = check_rate_limit(request.headers.get("X-API-Key"))
    if limited:
        return response

    jobs = current_app.config["ENRICHED_JOBS"]

    q = request.args.get("q", "").lower().strip()
    location_filter = request.args.get("location", "").lower().strip()
    level_filter = request.args.get("level", "").strip()
    remote_filter = request.args.get("remote", "").strip()
    skills_filter = [s.strip() for s in request.args.get("skills", "").split(",") if s.strip()]

    try:
        page = max(1, int(request.args.get("page", 1)))
        per_page = min(50, max(1, int(request.args.get("per_page", 10))))
    except ValueError:
        page, per_page = 1, 10

    results = []
    for job in jobs:
        if q:
            title_lower = job["title"].lower()
            skills_lower = [s.lower() for s in job["skills"]]
            if q not in title_lower and not any(q in s for s in skills_lower):
                continue
        if location_filter and location_filter not in job["location"].lower():
            continue
        if level_filter and job["experience_level"] != level_filter:
            continue
        if remote_filter and job["remote_type"] != remote_filter:
            continue
        if skills_filter:
            job_skills_lower = {s.lower() for s in job["skills"]}
            if not all(sf.lower() in job_skills_lower for sf in skills_filter):
                continue
        results.append(job)

    total = len(results)
    start = (page - 1) * per_page
    end = start + per_page
    page_results = results[start:end]

    return jsonify({
        "total": total,
        "page": page,
        "per_page": per_page,
        "results": page_results,
    }), 200


@jobs_bp.route("/v1/jobs/<job_id>")
def get_job(job_id):
    if not _check_auth():
        return jsonify({"error": "Invalid API key"}), 401

    from server import check_rate_limit
    limited, response = check_rate_limit(request.headers.get("X-API-Key"))
    if limited:
        return response

    jobs_by_id = current_app.config["JOBS_BY_ID"]
    job = jobs_by_id.get(job_id)
    if job is None:
        return jsonify({"error": "Job not found"}), 404
    return jsonify(job), 200
