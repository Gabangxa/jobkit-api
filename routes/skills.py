from flask import Blueprint, request, jsonify, current_app
from collections import Counter

skills_bp = Blueprint("skills", __name__)


@skills_bp.route("/v1/skills/trending")
def trending_skills():
    jobs = current_app.config["ENRICHED_JOBS"]

    role_filter = request.args.get("role", "").lower().strip()
    location_filter = request.args.get("location", "").lower().strip()
    try:
        days = int(request.args.get("days", 30))
    except ValueError:
        days = 30
    if days not in (7, 30, 90):
        days = 30

    filtered = jobs
    if role_filter:
        filtered = [j for j in filtered if role_filter in j["title"].lower()]
    if location_filter:
        filtered = [j for j in filtered if location_filter in j["location"].lower()]

    counts: Counter = Counter()
    for job in filtered:
        for skill in job["skills"]:
            counts[skill] += 1

    top_skills = counts.most_common(20)
    trending = [{"skill": s, "count": c, "rank": i + 1} for i, (s, c) in enumerate(top_skills)]

    return jsonify({
        "period_days": days,
        "role_filter": role_filter or None,
        "total_jobs_analyzed": len(filtered),
        "trending_skills": trending,
    }), 200
