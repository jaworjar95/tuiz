from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime, timezone
from .identifiers import (
    CategoryId, TopicId, QuestionId,
    UserIdDefault, CategoryIdDefault, TopicIdDefault, QuizIdDefault, QuestionIdDefault, AnswerIdDefault
  )

def utc_field_now(): # TODO: Could be moved to seprate file like fields.py
    return Field(default_factory=lambda: datetime.now(timezone.utc))

class User(BaseModel):
    id: UserIdDefault
    created_date: datetime = utc_field_now()
    name: str

class Category(BaseModel):
    id: CategoryIdDefault
    created_date: datetime = utc_field_now()
    name: str

class Topic(BaseModel):
    id: TopicIdDefault
    category_id: CategoryId
    created_date: datetime = utc_field_now()
    name: str

class Quiz(BaseModel):
    id: QuizIdDefault
    created_date: datetime = utc_field_now()
    name: str

class Question(BaseModel):
    id: QuestionIdDefault
    category_id: CategoryId
    topic_id: TopicId | None = None
    created_date: datetime = utc_field_now()
    content: str

class Answer(BaseModel):
    model_config = ConfigDict(frozen=True)
    id: AnswerIdDefault
    question_id: QuestionId
    created_date: datetime = utc_field_now()
    content: str

