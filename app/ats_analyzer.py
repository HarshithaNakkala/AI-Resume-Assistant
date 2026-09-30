# ATS Compatibility Analyzer

SKILLS = [
    "python",
    "java",
    "c",
    "c++",
    "javascript",
    "typescript",
    "html",
    "css",
    "react",
    "angular",
    "node.js",
    "nodejs",
    "flask",
    "django",
    "spring",
    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "aws",
    "azure",
    "gcp",
    "docker",
    "kubernetes",
    "git",
    "github",
    "linux",
    "terraform",
    "jenkins",
    "ci/cd",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "pandas",
    "numpy",
    "scikit-learn",
]


def extract_skills(text):
    """
    Find known technical skills inside a text.
    """

    text = text.lower()

    found_skills = set()

    for skill in SKILLS:
        if skill in text:
            found_skills.add(skill)

    return found_skills


def analyze_ats(resume_text, job_description):
    """
    Compare resume skills with skills mentioned
    in the job description.
    """

    resume_skills = extract_skills(resume_text)
    required_skills = extract_skills(job_description)

    matched_skills = resume_skills.intersection(required_skills)
    missing_skills = required_skills - resume_skills

    if len(required_skills) == 0:
        score = 0
    else:
        score = (len(matched_skills) / len(required_skills)) * 100

    return {
        "score": round(score, 2),
        "matched": sorted(matched_skills),
        "missing": sorted(missing_skills),
        "required": sorted(required_skills),
    }

def format_skill(skill):
    special_names = {
        "aws": "AWS",
        "gcp": "GCP",
        "c": "C",
        "c++": "C++",
        "sql": "SQL",
        "html": "HTML",
        "css": "CSS",
        "github": "GitHub",
        "javascript": "JavaScript",
        "typescript": "TypeScript",
        "node.js": "Node.js",
        "ci/cd": "CI/CD",
        "machine learning": "Machine Learning",
        "deep learning": "Deep Learning",
    }

    return special_names.get(skill, skill.title())

def generate_recommendations(missing_skills):
    recommendations = []

    for skill in missing_skills:
        recommendations.append(
            f"Consider adding {format_skill(skill)} "
            "if you genuinely have experience with it."
        )

    return recommendations

if __name__ == "__main__":

    resume = """
    BTech student with experience in Python, AWS, Docker and SQL.
    """

    job_description = """
    We are looking for a developer with Python, AWS, Docker,
    Kubernetes and SQL experience.
    """

    result = analyze_ats(resume, job_description)

    print("\nATS COMPATIBILITY")
    print("------------------")

    print(f"Score: {result['score']}%")

    print("\nMatched:")

    for skill in result["matched"]:
        print(f"✓ {format_skill(skill)}")

    print("\nMissing:")

    for skill in result["missing"]:
        print(f"✗ {format_skill(skill)}")

    print("\nRecommendations:")

    recommendations =generate_recommendations(result["missing"])

    for recommendation in recommendations:
        print(f"• {recommendation}")

