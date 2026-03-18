def pretty_print(results):
    for i, r in enumerate(results):
        print(f"\nClause {i+1}")
        print("Risks:", r["risks"])
        print("Missing:", r["missing"])
        print("Severity:", r["severity"])