from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime, timezone
from .identifiers import (
    CategoryId, TopicId, UserId, QuizId, QuestionId, QuestionAttemptId, QuizAttemptId,
    new_user_id, new_category_id, new_topic_id, new_quiz_id, new_question_id, new_question_attempt_id, new_quiz_attempt_id,
)

class User(BaseModel):
    id: UserId = Field(default_factory=new_user_id)
    name: str

class Category(BaseModel):
    id: CategoryId = Field(default_factory=new_category_id)
    name: str

class Topic(BaseModel):
    id: TopicId = Field(default_factory=new_topic_id)
    category_id: CategoryId
    name: str

class Quiz(BaseModel):
    id: QuizId = Field(default_factory=new_quiz_id)
    name: str

class Question(BaseModel):
    id: QuestionId = Field(default_factory=new_question_id)
    category_id: CategoryId
    topic_id: TopicId | None = None
    content: str

class Evaluation(BaseModel):
    model_config = ConfigDict(frozen=True)
    rating: int
    content: str
    hint: str

class Answer(BaseModel):
    model_config = ConfigDict(frozen=True)
    content: str


class QuestionAttempt(BaseModel):
    id: QuestionAttemptId = Field(default_factory=new_question_attempt_id)
    question_id: QuestionId
    answers: list[Answer] = []


class QuizAttempt(BaseModel):
    id: QuizAttemptId = Field(default_factory=new_quiz_attempt_id)
    quiz_id: QuizId
    user_id: UserId
    question_attempts: list[QuestionAttempt] = []

