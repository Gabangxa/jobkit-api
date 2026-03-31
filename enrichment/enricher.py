import re

SKILLS_TAXONOMY = [
    "Python", "JavaScript", "TypeScript", "React", "Node.js", "PostgreSQL", "Redis",
    "Docker", "Kubernetes", "AWS", "GCP", "Azure", "Terraform", "FastAPI", "Django",
    "Flask", "Go", "Rust", "Java", "Kotlin", "Swift", "GraphQL", "REST", "gRPC",
    "Kafka", "RabbitMQ", "Elasticsearch", "MongoDB", "MySQL", "SQLite", "Celery",
    "Git", "GitHub Actions", "CI/CD", "Agile", "Scrum", "JIRA", "Figma", "SQL",
    "Spark", "Hadoop", "dbt", "Airflow", "Pandas", "NumPy", "scikit-learn",
    "TensorFlow", "PyTorch", "LangChain", "OpenAI API", "Stripe API", "Twilio",
    "Sendgrid", "Postman", "Jest", "Pytest", "Selenium", "Playwright", "Vue.js",
    "Angular", "Next.js", "Tailwind CSS", "Bootstrap", "SASS", "Linux", "Bash",
    "C", "C++", "PHP", "Ruby", "Rails", "Elixir", "Phoenix", "Erlang", "Haskell",
    "Scala", "Databricks", "Snowflake", "BigQuery", "Redshift", "Metabase",
    "Tableau", "Power BI", "Looker", "Data visualization", "Machine learning",
    "Deep learning", "NLP", "Computer vision", "MLOps", "Feature engineering",
    "A/B testing", "Analytics", "Communication", "Leadership", "Mentoring",
    "Cross-functional collaboration", "Problem-solving",
]

TECH_TOOLS = {s.lower() for s in [
    "Python", "JavaScript", "TypeScript", "React", "Node.js", "PostgreSQL", "Redis",
    "Docker", "Kubernetes", "AWS", "GCP", "Azure", "Terraform", "FastAPI", "Django",
    "Flask", "Go", "Rust", "Java", "Kotlin", "Swift", "GraphQL", "REST", "gRPC",
    "Kafka", "RabbitMQ", "Elasticsearch", "MongoDB", "MySQL", "SQLite", "Celery",
    "Git", "GitHub Actions", "CI/CD", "Spark", "Hadoop", "dbt", "Airflow", "Pandas",
    "NumPy", "scikit-learn", "TensorFlow", "PyTorch", "LangChain", "OpenAI API",
    "Stripe API", "Twilio", "Sendgrid", "Jest", "Pytest", "Selenium", "Playwright",
    "Vue.js", "Angular", "Next.js", "Tailwind CSS", "Bootstrap", "SASS", "Linux",
    "Bash", "C", "C++", "PHP", "Ruby", "Rails", "Elixir", "Phoenix", "Erlang",
    "Haskell", "Scala", "Databricks", "Snowflake", "BigQuery", "Redshift",
    "Metabase", "Tableau", "Power BI", "Looker",
]}

_SKILLS_LOWER = {s.lower(): s for s in SKILLS_TAXONOMY}


def extract_skills(text: str) -> list[str]:
    text_lower = text.lower()
    counts = {}
    for lower_skill, canonical in _SKILLS_LOWER.items():
        # whole-word match to avoid false positives (e.g. "C" in "CI/CD")
        pattern = r'(?<![a-zA-Z0-9_/])' + re.escape(lower_skill) + r'(?![a-zA-Z0-9_/])'
        matches = re.findall(pattern, text_lower)
        if matches:
            counts[canonical] = len(matches)
    return sorted(counts.keys(), key=lambda s: -counts[s])


def normalize_salary(text: str) -> dict | None:
    # USD dollar range: $120,000–$150,000 or $120k-$150k or $120,000-$150,000
    m = re.search(
        r'\$([0-9,]+(?:k)?)\s*[–\-]\s*\$([0-9,]+(?:k)?)',
        text, re.IGNORECASE
    )
    if m:
        raw = m.group(0)
        min_val = _parse_amount(m.group(1))
        max_val = _parse_amount(m.group(2))
        hourly = bool(re.search(r'/\s*hr', text, re.IGNORECASE))
        return {
            "min": min_val, "max": max_val,
            "currency": "USD",
            "period": "hourly" if hourly else "annual",
            "raw": raw,
        }

    # plain k-range: 100k-130k or 100k–130k
    m = re.search(r'([0-9]+k)\s*[–\-]\s*([0-9]+k)', text, re.IGNORECASE)
    if m:
        raw = m.group(0)
        min_val = _parse_amount(m.group(1))
        max_val = _parse_amount(m.group(2))
        return {
            "min": min_val, "max": max_val,
            "currency": "USD",
            "period": "annual",
            "raw": raw,
        }

    # Hourly rate: $75/hr
    m = re.search(r'\$([0-9,]+(?:\.[0-9]+)?)\s*/\s*hr', text, re.IGNORECASE)
    if m:
        raw = m.group(0)
        return {
            "min": _parse_amount(m.group(1)),
            "max": None,
            "currency": "USD",
            "period": "hourly",
            "raw": raw,
        }

    # GBP: £60,000 or £60k
    m = re.search(r'£([0-9,]+(?:k)?)', text)
    if m:
        raw = m.group(0)
        return {
            "min": _parse_amount(m.group(1)),
            "max": None,
            "currency": "GBP",
            "period": "annual",
            "raw": raw,
        }

    # EUR: €80,000 or €80k
    m = re.search(r'€([0-9,]+(?:k)?)', text)
    if m:
        raw = m.group(0)
        return {
            "min": _parse_amount(m.group(1)),
            "max": None,
            "currency": "EUR",
            "period": "annual",
            "raw": raw,
        }

    return None


def _parse_amount(s: str) -> int:
    s = s.replace(',', '').strip()
    if s.lower().endswith('k'):
        return int(float(s[:-1]) * 1000)
    return int(float(s))


def classify_experience(title: str, description: str) -> str:
    combined = (title + ' ' + description).lower()
    if re.search(r'\bprincipal\b', combined):
        return "Principal"
    if re.search(r'\bstaff (engineer|software)\b', combined):
        return "Staff"
    if re.search(r'\b(tech lead|engineering lead|lead engineer)\b', combined):
        return "Lead"
    if re.search(r'\b(lead)\b', combined):
        return "Lead"
    if re.search(r'\b(senior|sr\.)\b', combined) or re.search(r'\b(5\+|6\+|7\+) years\b', combined):
        return "Senior"
    if re.search(r'\b(junior|jr\.)\b', combined) or re.search(r'\b(entry.level|0.?2 years|1.?2 years)\b', combined):
        return "Junior"
    return "Mid"


def classify_remote(title: str, location: str, description: str) -> str:
    combined = (title + ' ' + location + ' ' + description).lower()
    if re.search(r'\bhybrid\b', combined):
        return "Hybrid"
    if re.search(r'\bremote\b', combined):
        return "Remote"
    if re.search(r'\b(on.?site|in.?office)\b', combined):
        return "Onsite"
    return "Unspecified"


def enrich(record: dict) -> dict:
    desc = record.get("raw_description", "")
    title = record.get("title", "")
    location = record.get("location", "")

    skills = extract_skills(title + ' ' + desc)
    salary = normalize_salary(desc)
    level = classify_experience(title, desc)
    remote_type = classify_remote(title, location, desc)
    tech_stack = [s for s in skills if s.lower() in TECH_TOOLS][:5]

    return {
        "id": record["id"],
        "title": title,
        "company": record.get("company", ""),
        "location": location,
        "posted_at": record.get("posted_at", ""),
        "source": record.get("source", "seed"),
        "skills": skills,
        "salary": salary,
        "experience_level": level,
        "remote_type": remote_type,
        "tech_stack": tech_stack,
    }
