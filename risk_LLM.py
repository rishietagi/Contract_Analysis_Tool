import json
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.1:8b"   # or whatever you pulled


def analyze_clause(clause, retrieved_buckets):
    prompt = f"""
You are a Tech M&A risk analyst.

Clause:
{clause}

Relevant Knowledge:
{json.dumps(retrieved_buckets, indent=2)}

Tasks:
1. Identify explicit risks
2. Identify implicit risks
3. Identify missing protections
4. Identify anomalies (even beyond given knowledge)
5. Assign severity (Low/Medium/High)
6. Give confidence (0-1)

Return STRICT JSON ONLY:
{{
  "risks": [],
  "missing": [],
  "anomalies": [],
  "severity": "",
  "confidence": 0.0
}}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.2
            }
        }
    )

    output = response.json()["response"]

    # ⚠️ IMPORTANT: clean output (llama sometimes adds text)
    try:
        start = output.find("{")
        end = output.rfind("}") + 1
        json_str = output[start:end]
        return json.loads(json_str)
    except:
        print("❌ Failed to parse LLM output")
        print(output)
        return {
            "risks": [],
            "missing": [],
            "anomalies": [],
            "severity": "Low",
            "confidence": 0.5
        }