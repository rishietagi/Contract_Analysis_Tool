from llm import call_llm


REVIEW_SECTIONS = [
    "Scope",
    "Duration",
    "Deliverables",
    "Location / Geographical Scope",
    "Timelines",
    "Technical Architecture",
    "Scope Assumptions and Exclusions",
    "Service Level Agreements (SLAs)",
    "Project Structure, Roles and Responsibilities",
    "Handling Changes to Baseline",
    "Commercial Model",
    "Billing Model",
    "Overhead Expenses",
    "Incentives / Disincentives",
    "Procurement and Licensing Model",
    "Operations Model",
    "Acceptance Criteria",
    "Performance Criteria",
    "Discretionary Hours / Development Effort",
    "Minimum Skill Set",
    "Resource Deployment / Replacement Guidelines",
    "Subcontracting / Consortium Guidelines",
    "Handholding Support (Post Go-Live)",
    "Ongoing Operations Support",
    "Technical SOPs and Training to Ops Team",
    "Training and Awareness of End Users",
    "Intellectual Property and Source Code Ownership",
    "Requirements / Support from Client",
    "Governance and Reporting",
    "Contract Exit Mechanism",
    "Payment Terms",
    "Non-Functional Requirements"
]



def generate_contract_review(notes):

    sections = "\n".join(
        f"{i+1}. {section}"
        for i, section in enumerate(REVIEW_SECTIONS)
    )

    prompt = f"""
You are a contract review assistant.

Generate a contract review following this structure:

{sections}

For EACH section include:

Status: Covered / Partially Covered / Not Covered / NA
Impact: Low / Medium / High / NA
Key Points:
Remarks:

Notes:
{notes}
"""

    return call_llm(prompt)