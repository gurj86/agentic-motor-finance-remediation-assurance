# Agentic AI Motor Finance Remediation Assurance

A portfolio demonstration of a **multi-agent assurance workflow** for UK motor-finance commission remediation.

The lead assurance agent can decide which specialist agents to call to review:

- commission evidence and data completeness;
- commission-arrangement classification, including DCA / high commission / contractual tie indicators;
- customer disclosure and complaint evidence;
- redress / methodology assumptions;
- contradictions, missing records and rationale quality; and
- relevant FCA / CONRED / CONC references for human verification.

The lead agent combines the specialist findings and recommends **Pass**, **Further Work** or **Escalate**. The final decision remains with the human reviewer.

## Why this is agentic

This is different from a fixed checklist or rule-based dashboard.

A **Lead Motor Finance Assurance Agent** receives the fictional case and decides which specialist tools are needed. It can call:

1. **Commission Evidence Agent**
2. **Arrangement Classification Agent**
3. **Disclosure & Customer Evidence Agent**
4. **Redress / Methodology Agent**
5. **Evidence Challenge Agent**
6. **Regulatory Reference Agent**

The lead agent then reconciles those outputs into one assurance recommendation.

## Important boundary

This is a personal portfolio prototype using fictional data only.

It does **not**:

- determine legal liability or unfairness;
- make final scheme-eligibility decisions;
- calculate or instruct real compensation;
- replace current FCA rules, approved firm methodology or legal advice;
- contain real customer, lender, broker or employer information; or
- replace accountable human QA / compliance judgement.

The FCA position and scheme rules can change. Regulatory references are surfaced for a human reviewer to verify against the current source.

## Model and cost

The prototype uses **GPT-6 Luna** for the lead and specialist agents to keep live API testing inexpensive while retaining function-calling and structured-output capability.

## Run locally

Requires Python 3.10+ and an OpenAI API key.

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:OPENAI_API_KEY="your-key-here"
uvicorn app:app --reload
```

Then open:

```
http://127.0.0.1:8000
```

Do **not** put an API key in this repository or client-side code.

## Portfolio positioning

> I designed a multi-agent motor-finance remediation assurance workflow. A lead agent chooses specialist reviews across commission evidence, arrangement classification, disclosure, redress methodology, evidence quality and regulatory references, then consolidates the findings for human sign-off.

Built as a non-production demonstration of agentic AI use-case design, remediation assurance and human-in-the-loop governance.
