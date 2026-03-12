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
You are a senior contract analyst.

Evaluate whether the following aspects are present in the contract.

Rules:
- Mark Covered only if clearly present.
- Mark Partially Covered if incomplete.
- Mark Not Covered if missing.

For EACH section output:

Status:
Impact:
Remarks:
Evidence:

Impact Guide:
High = legal/commercial risk
Medium = operational risk
Low = minor governance gap

Section Definitions:

Scope:
Defines the purpose of the contract and the overall services or work covered.

Duration:
Contract start date, end date, renewal terms.

Deliverables:
Specific outputs or services that must be delivered.

Location / Geographical Scope:
Where the services are performed or geographically applicable.

Timelines:
Milestones, deadlines, schedules.

Technical Architecture:
System architecture, platforms, technology stack.

Service Level Agreements (SLAs):
Uptime guarantees, response times, penalties for failure.

Project Structure, Roles and Responsibilities:
Responsibilities of client, vendor, teams.

Commercial Model:
How the engagement is structured commercially.

Billing Model:
Billing schedule, invoicing structure.

Intellectual Property and Source Code Ownership:
Ownership of developed software, IP rights.

Contract Exit Mechanism:
Termination conditions and exit process.

Payment Terms:
Payment schedule, fees, penalties.

Now evaluate these sections:

1. Scope
2. Duration
3. Deliverables
4. Location / Geographical Scope
5. Timelines
6. Technical Architecture
7. Scope Assumptions and Exclusions
8. Service Level Agreements (SLAs)
9. Project Structure, Roles and Responsibilities
10. Handling Changes to Baseline
11. Commercial Model
12. Billing Model
13. Overhead Expenses
14. Incentives / Disincentives
15. Procurement and Licensing Model
16. Operations Model
17. Acceptance Criteria
18. Performance Criteria
19. Discretionary Hours / Development Effort
20. Minimum Skill Set
21. Resource Deployment / Replacement Guidelines
22. Subcontracting / Consortium Guidelines
23. Handholding Support (Post Go-Live)
24. Ongoing Operations Support
25. Technical SOPs and Training to Ops Team
26. Training and Awareness of End Users
27. Intellectual Property and Source Code Ownership
28. Requirements / Support from Client
29. Governance and Reporting
30. Contract Exit Mechanism
31. Payment Terms
32. Non-Functional Requirements

Contract Notes:
{notes}
"""

    return call_llm(prompt)