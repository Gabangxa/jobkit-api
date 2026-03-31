import os
import time
from collections import defaultdict
from flask import Flask, jsonify
from flask_cors import CORS

from data.jobs_seed import SEED_JOBS
from enrichment.enricher import enrich
from routes.jobs import jobs_bp
from routes.enrich import enrich_bp
from routes.skills import skills_bp
from routes.system import system_bp

app = Flask(__name__)
CORS(app)

# Rate limiter: per API key — 10 req / 60s
_rate_store: dict[str, list[float]] = defaultdict(list)
RATE_LIMIT = 10
RATE_WINDOW = 60  # seconds


def check_rate_limit(api_key: str):
    now = time.time()
    window_start = now - RATE_WINDOW
    timestamps = _rate_store[api_key]
    # Prune old entries
    _rate_store[api_key] = [t for t in timestamps if t > window_start]
    if len(_rate_store[api_key]) >= RATE_LIMIT:
        return True, (jsonify({"error": "Rate limit exceeded"}), 429)
    _rate_store[api_key].append(now)
    return False, None


# Pre-enrich all seed records at startup
print(f"Enriching {len(SEED_JOBS)} seed jobs...")
ENRICHED = [enrich(j) for j in SEED_JOBS]
JOBS_BY_ID = {j["id"]: j for j in ENRICHED}
print(f"Done. {len(ENRICHED)} jobs ready.")

app.config["ENRICHED_JOBS"] = ENRICHED
app.config["JOBS_BY_ID"] = JOBS_BY_ID

app.register_blueprint(jobs_bp)
app.register_blueprint(enrich_bp)
app.register_blueprint(skills_bp)
app.register_blueprint(system_bp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port, debug=False)
