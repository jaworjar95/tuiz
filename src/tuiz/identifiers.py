from typing import NewType, Annotated
from pydantic import Field
from uuid import UUID, uuid4

UserId = NewType("UserId", UUID)
CategoryId = NewType("CategoryId", UUID)
TopicId = NewType("TopicId", UUID)
QuizId = NewType("QuizId", UUID)
QuestionId = NewType("QuestionId", UUID)
AnswerId = NewType("AnswerId", UUID)

def new_user_id() -> UserId: return UserId(uuid4())
def new_category_id() -> CategoryId: return CategoryId(uuid4())
def new_topic_id() -> TopicId: return TopicId(uuid4())
def new_question_id() -> QuestionId: return QuestionId(uuid4())
def new_quiz_id() -> QuizId: return QuizId(uuid4())
def new_answer_id() -> AnswerId: return AnswerId(uuid4())

# Self-defaulting type aliases
UserIdDefault     = Annotated[UserId,     Field(default_factory=new_user_id)]
CategoryIdDefault = Annotated[CategoryId, Field(default_factory=new_category_id)]
TopicIdDefault    = Annotated[TopicId,    Field(default_factory=new_topic_id)]
QuizIdDefault     = Annotated[QuizId,     Field(default_factory=new_quiz_id)]
QuestionIdDefault = Annotated[QuestionId, Field(default_factory=new_question_id)]
AnswerIdDefult   = Annotated[AnswerId,   Field(default_factory=new_answer_id)]

