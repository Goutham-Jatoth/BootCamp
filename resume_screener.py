import json

result = {
    "match_score": 8,
    "strengths": [
        "Python Knowledge",
        "SQL Skills",
        "Good Projects"
    ],
    "gaps": [
        "No Django Experience",
        "No REST API Experience"
    ],
    "recommendation": "Moderate Fit",
    "summary": "Candidate matches most requirements."
}

print(json.dumps(result, indent=4))