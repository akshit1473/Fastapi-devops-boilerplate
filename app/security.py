import re
from fastapi import HTTPException, status

# Known prompt-override and jailbreak signatures
INJECTION_PATTERNS = [
    r"(?i)ignore\s+previous\s+instructions",
    r"(?i)system\s*:\s*you\s+are",
    r"(?i)disregard\s+all\s+prior",
    r"(?i)you\s+are\s+now\s+a\s+DAN",
    r"(?i)drop\s+table",  # Basic SQLi defense
]

def sanitize_input_prompt(prompt: str) -> str:
    """Scans incoming text for malicious prompt injection signatures."""
    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, prompt):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Security Violation: Malicious or prompt-override pattern detected."
            )
    return prompt
