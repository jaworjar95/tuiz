from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime, timezone
from .identifiers import (
    CategoryId, TopicId, QuestionId,
    UserIdField, CategoryIdField, TopicIdField, QuizIdField, QuestionIdField, AnswerIdField
  )

def utc_field_now(): # TODO: Could be moved to seprate file like fields.py
    return Field(default_factory=lambda: datetime.now(timezone.utc), frozen=True)

class User(BaseModel):
    id: UserIdField
    created_date: datetime = utc_field_now()
    name: str

class Category(BaseModel):
    id: CategoryIdField
    created_date: datetime = utc_field_now()
    name: str

class Topic(BaseModel):
    id: TopicIdField
    category_id: CategoryIdField
    created_date: datetime = utc_field_now()
    name: str

class Quiz(BaseModel):
    id: QuizIdField
    created_date: datetime = utc_field_now()
    name: str

class Question(BaseModel):
    id: QuestionIdField
    category_id: CategoryId
    topic_id: TopicId | None = None
    created_date: datetime = utc_field_now()
    content: str

class Answer(BaseModel):
    model_config = ConfigDict(frozen=True)
    id: AnswerIdField
    question_id: QuestionId
    created_date: datetime = utc_field_now()
    content: str

