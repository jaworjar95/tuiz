from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime, timezone
import identifiers

def utc_field_now(): # TODO: Could be moved to seprate file like fields.py
    return Field(default_factory=lambda: datetime.now(timezone.utc), frozen=True)

class User(BaseModel):
    id: identifiers.UserId = identifiers.new_user_id()
    created_date: datetime = utc_field_now()
    name: str

class Category(BaseModel):
    id: identifiers.CategoryId = identifiers.new_category_id()
    created_date: datetime = utc_field_now()
    name: str

class Topic(BaseModel):
    id: identifiers.TopicId = identifiers.new_topic_id()
    category_id: identifiers.CategoryId
    created_date: datetime = utc_field_now()
    name: str

class Quiz(BaseModel):
    id: identifiers.QuizId = identifiers.new_quiz_id()
    created_date: datetime = utc_field_now()
    name: str

class Question(BaseModel):
    id: identifiers.QuestionId = identifiers.new_question_id()
    category_id: identifiers.CategoryId
    topic_id: identifiers.TopicId | None = None
    created_date: datetime = utc_field_now()
    content: str

class Answer(BaseModel):
    model_config = ConfigDict(frozen=True)
    id: identifiers.AnswerId = identifiers.new_answer_id()
    question_id: identifiers.QuestionId
    created_date: datetime = utc_field_now()
    content: str

