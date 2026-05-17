from typing import NewType
from uuid import UUID, uuid4

AnswerId = NewType("AnswerId", UUID)
CategoryId = NewType("CategoryId", UUID)
QuestionAttemptId = NewType("QuestionAttemptId", UUID)
QuestionId = NewType("QuestionId", UUID)
QuizAttemptId = NewType("QuizAttemptId", UUID)
QuizId = NewType("QuizId", UUID)
TopicId = NewType("TopicId", UUID)
UserId = NewType("UserId", UUID)

def new_answer_id() -> AnswerId: return AnswerId(uuid4())
def new_category_id() -> CategoryId: return CategoryId(uuid4())
def new_question_attempt_id() -> QuestionAttemptId: return QuestionAttemptId(uuid4())
def new_question_id() -> QuestionId: return QuestionId(uuid4())
def new_quiz_attempt_id() -> QuizAttemptId: return QuizAttemptId(uuid4())
def new_quiz_id() -> QuizId: return QuizId(uuid4())
def new_topic_id() -> TopicId: return TopicId(uuid4())
def new_user_id() -> UserId: return UserId(uuid4())

