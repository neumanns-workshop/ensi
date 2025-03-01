from pydantic import BaseModel, Field
from typing import List, Optional, Literal


# Symbolic Representation of Dream Elements
class SymbolicElement(BaseModel):
    name: str = Field(..., description="Name of the symbolic element (e.g., lion, fire, reed).")
    meaning: str = Field(..., description="The meaning or interpretation of the symbol.")
    category: Optional[Literal["Animal", "Object", "Action", "Plant", "Other"]] = Field(
        None, description="Category of the symbol."
    )
    associated_deities: Optional[List[str]] = Field(None, description="Deities or spirits associated with the symbol.")
    source: Optional[str] = Field(None, description="Textual or historical source of the symbol's meaning.")
    notes: Optional[str] = Field(None, description="Additional context or interpretation of the symbol.")


# Objects Used in Rituals or Prevention
class RitualObject(BaseModel):
    name: str = Field(..., description="Name of the ritual object (e.g., reed, clay lump, Pazuzu amulet).")
    type: Literal[
        "Protective", "Transfer", "Cleansing", "Offering", "Symbolic Tool", "Boundary"
    ] = Field(..., description="Functional role of the object in rituals.")
    usage: List[str] = Field(..., description="Instructions on how the object is used in rituals or preventive measures.")
    materials: Optional[List[str]] = Field(None, description="Materials used to make or prepare the object.")
    associated_deities: Optional[List[str]] = Field(None, description="Deities or spirits linked to the object.")
    source: Optional[str] = Field(None, description="Source or textual reference for the object's use.")
    notes: Optional[str] = Field(None, description="Additional observations or variations in its use.")


# Verbal Components
class Incantation(BaseModel):
    text: str = Field(..., description="The full text of the incantation.")
    purpose: Optional[str] = Field(None, description="Purpose or intent of the incantation (e.g., cleansing, affirmation).")
    source: Optional[str] = Field(None, description="Source text or origin of the incantation.")
    notes: Optional[str] = Field(None, description="Additional observations or cultural context.")


class Conjuration(BaseModel):
    text: str = Field(..., description="The full text of the conjuration.")
    deities_invoked: Optional[List[str]] = Field(None, description="Deities or spirits addressed in the conjuration.")
    purpose: Optional[str] = Field(None, description="Purpose of the conjuration.")
    source: Optional[str] = Field(None, description="Source or textual origin of the conjuration.")
    notes: Optional[str] = Field(None, description="Additional observations or details.")


class Invocation(BaseModel):
    targets: List[str] = Field(..., description="Deities, spirits, or entities being invoked.")
    text: str = Field(..., description="The exact wording of the invocation.")
    purpose: Optional[str] = Field(None, description="Intent behind the invocation (e.g., protection, petition).")
    source: Optional[str] = Field(None, description="The source of the invocation.")
    notes: Optional[str] = Field(None, description="Additional cultural or contextual information.")


# Actions Taken in a Ritual
class RitualAction(BaseModel):
    description: str = Field(..., description="Description of the ritual.")
    steps: List[str] = Field(..., description="Step-by-step instructions for performing the ritual.")
    materials: Optional[List[str]] = Field(None, description="Objects or resources needed for the ritual.")
    source: Optional[str] = Field(None, description="Source or text documenting the ritual.")


# Ritual Structure
class Ritual(BaseModel):
    type: str = Field(..., description="The classification of the ritual (e.g., Type A, Type G).")
    title: Optional[str] = Field(None, description="A brief title or purpose of the ritual.")
    actions: RitualAction = Field(..., description="Actions and steps of the ritual.")
    incantations: Optional[List[Incantation]] = Field(None, description="List of incantations used.")
    conjurations: Optional[List[Conjuration]] = Field(None, description="List of conjurations included.")
    invocations: Optional[List[Invocation]] = Field(None, description="Specific invocations to entities.")
    objects: Optional[List[RitualObject]] = Field(None, description="Ritual objects used in the ceremony.")
    preventive_measures: Optional[List[RitualObject]] = Field(
        None, description="Objects or steps to prevent recurrence of bad dreams."
    )
    source: Optional[str] = Field(None, description="Textual or historical source for the ritual.")
    cultural_notes: Optional[str] = Field(None, description="Additional contextual information.")


# Interpretation of the Dream
class Interpretation(BaseModel):
    description: str = Field(..., description="Content or events of the dream.")
    symbols: List[SymbolicElement] = Field(..., description="Symbols identified and their interpretations.")
    severity: Literal["Minor", "Moderate", "Severe", "Critical"] = Field(
        ..., description="The assessed severity of the dream."
    )
    summary: str = Field(..., description="Summary interpretation of the dream's meaning.")
    source: Optional[str] = Field(None, description="The source of the interpretation rules or references.")


# Final Recommendation for the Dreamer
class Recommendation(BaseModel):
    interpretation: Interpretation = Field(..., description="The analyzed interpretation of the dream.")
    ritual: Ritual = Field(..., description="The recommended ritual to address the dream.")
    preventive_measures: Optional[List[RitualObject]] = Field(
        None, description="Suggestions for preventing bad dreams in the future."
    )
    invocations: Optional[List[Invocation]] = Field(None, description="Invocations to deities or spirits for protection.")
    user_notes: Optional[str] = Field(None, description="Personalized notes or adjustments for the dreamer.")
    source: Optional[str] = Field(None, description="The origin or compilation source for the recommendation.")
