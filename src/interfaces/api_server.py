"""
API Server

Provides:
- external API interfaces
- recursive interaction endpoints
- ecosystem interoperability
- operational telemetry access
"""

from fastapi import APIRouter
from pydantic import BaseModel

from src.axios_core.core_engine import AxiosCore
from src.utils.logger import setup_logger

# --------------------------------------------------
# Initialize Logger
# --------------------------------------------------

logger = setup_logger()

# --------------------------------------------------
# Router Initialization
# --------------------------------------------------

router = APIRouter()

# --------------------------------------------------
# AXIOS CORE Initialization
# --------------------------------------------------

axios_core = AxiosCore()

# --------------------------------------------------
# Request Models
# --------------------------------------------------

class PromptRequest(BaseModel):

    prompt: str


class HealthResponse(BaseModel):

    system: str
    status: str
    version: str


# --------------------------------------------------
# Health Endpoint
# --------------------------------------------------

@router.get(
    "/health",
    response_model=HealthResponse
)
async def health_check():
    """
    System health check endpoint.
    """

    logger.info(
        "Health check requested."
    )

    return {
        "system": "AXIOS OS",
        "status": "operational",
        "version": "0.1.0"
    }

# --------------------------------------------------
# Recursive Processing Endpoint
# --------------------------------------------------

@router.post("/process")
async def process_prompt(
    request: PromptRequest
):
    """
    Main recursive reasoning endpoint.
    """

    logger.info(
        f"Processing API prompt: "
        f"{request.prompt}"
    )

    result = axios_core.process(
        request.prompt
    )

    return result

# --------------------------------------------------
# System Telemetry Endpoint
# --------------------------------------------------

@router.get("/telemetry")
async def telemetry():
    """
    Retrieve operational telemetry snapshot.
    """

    logger.info(
        "Telemetry snapshot requested."
    )

    return {
        "system_state": "operational",
        "recursive_stability": "stable",
        "constraint_state": "stable",
        "coherence_status": "within_bounds"
    }

# --------------------------------------------------
# Recursive Reflection Endpoint
# --------------------------------------------------

@router.get("/reflection")
async def reflection_state():
    """
    Retrieve recursive reflection state.
    """

    logger.info(
        "Reflection state requested."
    )

    return {
        "reflection_state": (
            "stable_recursive_alignment"
        ),
        "meta_governance_state": "stable",
        "epistemic_integrity": "stable"
    }
