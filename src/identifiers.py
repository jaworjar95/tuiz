from typing import NewType
from uuid import UUID, uuid4

UserId = NewType("UserId", UUID)
CategoryId = NewType("CategoryId", UUID)
TopicId = NewType("TopicId", UUID)
QuizId = NewType("QuizId", UUID)
QuestionId = NewType("QuestionId", UUID)
ChoiceId = NewType("ChoiceId", UUID)

def new_user_id() -> UserId: return UserId(uuid4())
def new_category_id() -> CategoryId: return CategoryId(uuid4())
def new_topic_id() -> TopicId: return TopicId(uuid4())
def new_question_id() -> QuestionId: return QuestionId(uuid4())
def new_quiz_id() -> QuizId: return QuizId(uuid4())
def new_choice_id() -> ChoiceId: return ChoiceId(uuid4())
