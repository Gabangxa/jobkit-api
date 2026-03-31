"""150+ synthetic job records for JobKit API demo data."""
import uuid

_ROLES = [
    "Software Engineer", "Data Scientist", "DevOps Engineer", "Product Manager",
    "Frontend Engineer", "Backend Engineer", "ML Engineer", "Full Stack Engineer",
    "Site Reliability Engineer", "Security Engineer",
]

_COMPANIES = [
    "Acme Corp", "Bright Labs", "CloudNine", "DataStream", "EdgeWorks",
    "FinStack", "GridBase", "Harbour AI", "Ironclad Systems", "JetBridge",
    "Keystone Tech", "LumenSoft", "Metafield", "Nexus Analytics", "Orbit Digital",
    "Polaris HQ", "QuantumLeap", "RiverFlow", "Stellar Code", "TowerPoint",
]

_LOCATIONS = [
    "Remote", "New York, NY", "San Francisco, CA", "Austin, TX",
    "London, UK", "Berlin, Germany", "Toronto, Canada",
]

_LEVELS_DATA = [
    ("Junior", "junior", "We are looking for a junior engineer with 0-2 years of experience."),
    ("Mid", "mid-level", "We need a mid-level engineer who can work independently."),
    ("Senior", "senior", "We are seeking a senior engineer with 5+ years of experience."),
    ("Lead", "lead", "We are hiring a tech lead to guide a team of engineers."),
    ("Staff", "staff engineer", "We need a staff engineer to set technical direction."),
    ("Principal", "principal", "We are looking for a principal engineer to define architecture."),
]

_SALARY_EXAMPLES = [
    ("$90,000–$120,000", "USD annual"),
    ("$120,000–$150,000", "USD annual"),
    ("$150,000–$190,000", "USD annual"),
    ("$80k-$110k", "USD annual"),
    ("$110k-$140k", "USD annual"),
    ("$140k-$180k", "USD annual"),
    ("$200k-$250k", "USD annual"),
    ("$75/hr", "USD hourly"),
    ("$95/hr", "USD hourly"),
    ("£60,000", "GBP annual"),
    ("£80,000", "GBP annual"),
    ("€70,000", "EUR annual"),
    ("€90,000", "EUR annual"),
]

_SKILL_SETS = {
    "Software Engineer": {
        "techs": ["Python", "Java", "Go", "PostgreSQL", "Docker", "Kubernetes", "AWS", "Git", "CI/CD", "REST"],
        "soft": ["Communication", "Problem-solving", "Agile", "Scrum"],
    },
    "Data Scientist": {
        "techs": ["Python", "Pandas", "NumPy", "scikit-learn", "TensorFlow", "PyTorch", "SQL", "Spark", "BigQuery", "Airflow"],
        "soft": ["Analytics", "Communication", "A/B testing", "Feature engineering"],
    },
    "DevOps Engineer": {
        "techs": ["Docker", "Kubernetes", "Terraform", "AWS", "GCP", "Linux", "Bash", "GitHub Actions", "CI/CD", "Kafka"],
        "soft": ["Communication", "Problem-solving", "Leadership"],
    },
    "Product Manager": {
        "techs": ["JIRA", "Figma", "SQL", "Analytics", "REST"],
        "soft": ["Leadership", "Communication", "Cross-functional collaboration", "Agile", "Scrum"],
    },
    "Frontend Engineer": {
        "techs": ["JavaScript", "TypeScript", "React", "Vue.js", "Next.js", "Tailwind CSS", "Bootstrap", "SASS", "GraphQL", "Jest"],
        "soft": ["Communication", "Problem-solving", "Figma"],
    },
    "Backend Engineer": {
        "techs": ["Python", "Node.js", "Go", "PostgreSQL", "Redis", "MongoDB", "Docker", "AWS", "REST", "GraphQL"],
        "soft": ["Problem-solving", "Agile", "Communication"],
    },
    "ML Engineer": {
        "techs": ["Python", "TensorFlow", "PyTorch", "scikit-learn", "MLOps", "Airflow", "Docker", "AWS", "Spark", "Kafka"],
        "soft": ["Machine learning", "Deep learning", "NLP", "Feature engineering", "Communication"],
    },
    "Full Stack Engineer": {
        "techs": ["JavaScript", "TypeScript", "React", "Node.js", "PostgreSQL", "Docker", "AWS", "GraphQL", "Redis", "CI/CD"],
        "soft": ["Problem-solving", "Communication", "Agile"],
    },
    "Site Reliability Engineer": {
        "techs": ["Linux", "Bash", "Kubernetes", "Docker", "Terraform", "AWS", "GCP", "Kafka", "Elasticsearch", "GitHub Actions"],
        "soft": ["Problem-solving", "Communication", "Leadership"],
    },
    "Security Engineer": {
        "techs": ["Python", "Linux", "Bash", "AWS", "Docker", "Kubernetes", "Terraform", "Git", "CI/CD", "REST"],
        "soft": ["Problem-solving", "Communication", "Leadership", "Analytics"],
    },
}

_DESCRIPTIONS = {
    "Software Engineer": [
        "We are building next-generation infrastructure to power millions of transactions daily. "
        "Our team values clean code, pragmatic architecture, and continuous improvement. "
        "You will design and implement scalable backend services, participate in code reviews, "
        "and collaborate with cross-functional teams. Strong Python and Go skills are required, "
        "along with experience deploying to AWS with Docker and Kubernetes. "
        "Familiarity with PostgreSQL, Redis, and REST API design is essential. "
        "We practice CI/CD and Agile development. The salary range is {salary}.",

        "Join our engineering team and help us scale our platform to handle millions of users. "
        "You will write high-quality Python code, build REST APIs, design database schemas in PostgreSQL, "
        "and work closely with the DevOps team on CI/CD pipelines. Experience with Docker and Kubernetes "
        "is a plus. We love engineers who are obsessed with correctness and performance. {remote} "
        "Compensation: {salary}.",
    ],
    "Data Scientist": [
        "We are expanding our data science team to help drive product decisions through data. "
        "You will build and deploy machine learning models using Python, Pandas, scikit-learn, and PyTorch. "
        "Experience with A/B testing frameworks, feature engineering, and working with large datasets "
        "on Spark or BigQuery is expected. Familiarity with Airflow for pipeline orchestration is a plus. "
        "Our culture values reproducibility and rigor. Compensation: {salary}. {remote}",

        "As a Data Scientist, you will own the full lifecycle of ML experiments — from data exploration "
        "to production deployment. We use Python, TensorFlow, NumPy, and SQL daily. Knowledge of NLP "
        "or Computer vision is a strong plus. Our data platform runs on BigQuery and Snowflake. "
        "We're looking for someone with strong Analytics skills and great Communication. {remote} "
        "Salary: {salary}.",
    ],
    "DevOps Engineer": [
        "We are looking for a DevOps Engineer to own our cloud infrastructure. You will manage "
        "Kubernetes clusters on AWS and GCP, write Terraform modules, automate CI/CD pipelines with "
        "GitHub Actions, and ensure platform reliability. Expertise in Docker, Linux, and Bash scripting "
        "is required. Experience with Kafka and Elasticsearch is highly valued. {remote} Salary: {salary}.",

        "Help us build a world-class developer platform. You will design and maintain our infrastructure "
        "using Terraform, Kubernetes, and Docker. Experience with AWS or GCP is required. "
        "You will own our GitHub Actions pipelines, improve observability with Elasticsearch, "
        "and ensure 99.9% uptime. Strong Linux and Bash skills are essential. {remote} Pay: {salary}.",
    ],
    "Product Manager": [
        "We are seeking a Product Manager to lead our core product roadmap. You will work closely "
        "with engineering, design, and sales teams. Proficiency with JIRA, Figma, and SQL for data "
        "analysis is required. Strong Leadership, Communication, and Cross-functional collaboration "
        "skills are essential. Experience with Agile and Scrum methodologies expected. {remote} "
        "Salary: {salary}.",

        "Own the product vision and roadmap for our B2B SaaS platform. Work with engineers and designers "
        "in Figma and JIRA to ship high-impact features. Use SQL and Analytics to drive decisions. "
        "Excellent Communication and Leadership skills required. We value managers who are empathetic "
        "and data-driven. {remote} Compensation: {salary}.",
    ],
    "Frontend Engineer": [
        "Build beautiful, performant user interfaces for millions of customers. You will work with "
        "TypeScript, React, and Next.js. Expertise in Tailwind CSS, SASS, and component-driven design "
        "is required. Experience with GraphQL and Jest for testing is a plus. We use Figma for design "
        "handoff. Excellent Communication and problem-solving skills valued. {remote} Salary: {salary}.",

        "Join our frontend team to craft delightful experiences. Strong JavaScript and TypeScript skills "
        "required, with React and Vue.js being our primary frameworks. You will write unit tests with "
        "Jest and integration tests with Playwright. Bootstrap, Tailwind CSS, and SASS experience helpful. "
        "{remote} Compensation: {salary}.",
    ],
    "Backend Engineer": [
        "We're looking for a Backend Engineer to build the data layer of our platform. "
        "You will design REST and GraphQL APIs using Python or Node.js, manage data in PostgreSQL "
        "and MongoDB, and use Redis for caching. Docker and AWS experience required. "
        "Strong Problem-solving skills and Agile methodology familiarity expected. "
        "{remote} Salary: {salary}.",

        "Design and build scalable backend services using Go or Python. You will own API design "
        "for REST endpoints, manage PostgreSQL schemas, and optimize Redis usage for high-performance "
        "caching. Experience with Docker and cloud infrastructure (AWS or GCP) is required. "
        "{remote} Pay range: {salary}.",
    ],
    "ML Engineer": [
        "Join our ML team to take models from research to production. You will design MLOps pipelines, "
        "work with PyTorch and TensorFlow models, orchestrate workflows with Airflow, and deploy "
        "containerized ML services on AWS using Docker. Experience with Kafka for real-time inference "
        "and Spark for batch processing is a big plus. Deep learning and NLP background valued. "
        "{remote} Salary: {salary}.",

        "We are scaling our machine learning infrastructure. You will work on Feature engineering, "
        "model training pipelines using scikit-learn and PyTorch, and production deployments. "
        "Strong Python skills required along with experience in Docker, AWS, and MLOps tooling. "
        "Knowledge of Computer vision or NLP is a strong differentiator. {remote} Compensation: {salary}.",
    ],
    "Full Stack Engineer": [
        "Build features end-to-end, from React frontend to Node.js backend to PostgreSQL database. "
        "TypeScript is our primary language. We use GraphQL for API communication, Redis for caching, "
        "and Docker plus AWS for deployment. CI/CD pipelines via GitHub Actions. Strong JavaScript "
        "and communication skills needed. {remote} Salary: {salary}.",

        "Own entire features from database to UI. You will write TypeScript, build React components, "
        "create REST and GraphQL APIs in Node.js, manage PostgreSQL data models, and deploy via "
        "Docker on AWS. Experience with CI/CD, Redis, and Agile practices required. "
        "{remote} Compensation: {salary}.",
    ],
    "Site Reliability Engineer": [
        "Ensure the reliability and scalability of our production systems. You will manage Kubernetes "
        "clusters, write Terraform for infrastructure as code, run GitHub Actions CI/CD, and monitor "
        "with Elasticsearch. Expert Linux and Bash skills required. AWS and GCP experience expected. "
        "On-call rotation included. {remote} Salary: {salary}.",

        "Own reliability across our microservices platform. Strong Kubernetes and Docker skills required. "
        "Experience with Kafka, Elasticsearch, and Terraform expected. You will write automation scripts "
        "in Bash, manage Linux systems, and improve observability pipelines on AWS or GCP. "
        "{remote} Pay: {salary}.",
    ],
    "Security Engineer": [
        "Protect our platform and customer data. You will conduct security reviews, automate security "
        "testing in CI/CD pipelines, manage AWS IAM policies, harden Docker and Kubernetes deployments, "
        "and monitor with Elasticsearch. Strong Python and Linux skills required. "
        "Familiarity with Bash, Terraform, and REST API security best practices expected. "
        "{remote} Salary: {salary}.",

        "Build and run our security engineering function. You will own infrastructure security on AWS, "
        "automate vulnerability scanning in GitHub Actions, harden Kubernetes configurations with "
        "Terraform, and write tooling in Python and Bash. Strong problem-solving and communication "
        "skills needed. {remote} Compensation: {salary}.",
    ],
}

_REMOTE_PHRASES = {
    "Remote": "This is a fully remote position.",
    "New York, NY": "This role is based in our New York, NY office. Hybrid arrangements possible.",
    "San Francisco, CA": "We are based in San Francisco, CA. Onsite preferred.",
    "Austin, TX": "Located in Austin, TX. In-office 3 days a week.",
    "London, UK": "Based in our London, UK office. Hybrid model.",
    "Berlin, Germany": "Berlin, Germany office. Flexible hybrid schedule.",
    "Toronto, Canada": "Toronto, Canada office. Hybrid model available.",
}


def _make_job(idx: int, role: str, company: str, location: str,
              level_tuple: tuple, salary_str: str, desc_idx: int, date: str) -> dict:
    level_name, level_keyword, level_phrase = level_tuple
    remote_phrase = _REMOTE_PHRASES.get(location, "")

    desc_template = _DESCRIPTIONS[role][desc_idx % len(_DESCRIPTIONS[role])]
    description = f"{level_phrase} {desc_template.format(salary=salary_str, remote=remote_phrase)}"

    return {
        "id": str(uuid.uuid5(uuid.NAMESPACE_OID, f"jobkit-{idx}")),
        "title": f"{level_keyword.title()} {role}" if level_name not in ("Mid",) else role,
        "company": company,
        "location": location,
        "raw_description": description,
        "posted_at": date,
        "source": "seed",
    }


def build_seed_jobs() -> list[dict]:
    import itertools
    jobs = []
    dates = [
        "2026-03-01", "2026-03-05", "2026-03-10", "2026-03-15",
        "2026-03-18", "2026-03-20", "2026-03-25", "2026-03-28", "2026-03-30",
    ]
    combos = list(itertools.product(
        enumerate(_ROLES),
        _LOCATIONS,
        enumerate(_LEVELS_DATA),
    ))
    idx = 0
    for (ri, role), location, (li, level_tuple) in combos:
        salary_str = _SALARY_EXAMPLES[(idx) % len(_SALARY_EXAMPLES)][0]
        company = _COMPANIES[(idx) % len(_COMPANIES)]
        date = dates[idx % len(dates)]
        desc_idx = (ri + li) % 2
        jobs.append(_make_job(idx, role, company, location, level_tuple, salary_str, desc_idx, date))
        idx += 1
        if idx >= 420:  # cap to avoid enormous list; 420 >> 150 required
            break

    return jobs


SEED_JOBS: list[dict] = build_seed_jobs()
