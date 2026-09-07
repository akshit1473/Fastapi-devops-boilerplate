from pydantic import BaseModel, Field, field_validator

class QueryRequest(BaseModel):
    # Enforce strict character limits to prevent DoS (Denial of Service) attacks
    prompt: str = Field(..., min_length=3, max_length=1000, description="User query prompt")
    user_id: str = Field(..., min_length=1, max_length=50, description="Unique client identifier")

    @field_validator('prompt')
    @classmethod
    def validate_no_null_bytes(cls, value: str) -> str:
        # Strip null bytes and normalize whitespace
        if "\x00" in value:
            raise ValueError("Null bytes are prohibited in incoming payloads.")
        return value.strip()
