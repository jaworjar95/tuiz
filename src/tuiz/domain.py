from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime, timezone
from .identifiers import (
      UserId, CategoryId, TopicId, QuizId, QuestionId, AnswerId,
      new_user_id, new_category_id, new_topic_id,
      new_quiz_id, new_question_id, new_answer_id,
  )

def utc_field_now(): # TODO: Could be moved to seprate file like fields.py
    return Field(default_factory=lambda: datetime.now(timezone.utc), frozen=True)

class User(BaseModel):
    id: UserId = Field(default_factory=new_user_id)
    created_date: datetime = utc_field_now()
    name: str

class Category(BaseModel):
    id: CategoryId = Field(default_factory=new_category_id)
    created_date: datetime = utc_field_now()
    name: str

class Topic(BaseModel):
    id: TopicId = Field(default_factory=new_topic_id)
    category_id: CategoryId
    created_date: datetime = utc_field_now()
    name: str

class Quiz(BaseModel):
    id: QuizId = Field(default_factory=new_quiz_id)
    created_date: datetime = utc_field_now()
    name: str

class Question(BaseModel):
    id: QuestionId = Field(default_factory=new_question_id)
    category_id: CategoryId
    topic_id: TopicId | None = None
    created_date: datetime = utc_field_now()
    content: str

class Answer(BaseModel):
    model_config = ConfigDict(frozen=True)
    id: AnswerId = Field(default_factory=new_answer_id)
    question_id: QuestionId
    created_date: datetime = utc_field_now()
    content: str

