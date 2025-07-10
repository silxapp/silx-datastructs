from pydantic import BaseModel
from datetime import date
from typing import Optional, Any

from .article import Author
from .dag import ProbabilityStatement


class Publication(BaseModel):
    citation: str
    context: str
    pmid: Optional[str]


class StudyInfo(BaseModel):
    title: str
    brief_description: str
    detailed_description: str
    study_date: date
    study_type: str
    phase: str
    status: str
    countries: list[str]
    enrollment: Optional[int] = None
    short_title: Optional[str] = None
    abstract: Optional[str] = None
    sponsor: Optional[str] = None
    n_arms: int = 1
    references: Optional[list[Publication]] = None


class StudySponsor(BaseModel):
    name: str
    status: str
    agency_class: str


class StudyDesign(BaseModel):
    allocation: Optional[str]
    intervention_model: Optional[str]
    observation_model: Optional[str]
    purpose: Optional[str]
    masking: Optional[str]


class PaperIR(BaseModel):
    id: str
    study_info: StudyInfo
    study_design: StudyDesign
    authors: list[Author]
    sponsors: list[StudySponsor]
    source_index: list[Any]
    dag: list[ProbabilityStatement]
