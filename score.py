def severity_to_score(severity):
    mapping = {
        "Low": 0.3,
        "Medium": 0.6,
        "High": 1.0
    }
    return mapping.get(severity, 0.5)


def compute_score(results):
    total = 0
    count = 0

    for r in results:
        score = severity_to_score(r["severity"]) * r["confidence"]
        total += score
        count += 1

    if count == 0:
        return 0

    return round((total / count) * 100, 2)