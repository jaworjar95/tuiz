from tuitor.domain import Answer, Category, Question, Topic, User, Evaluation
from pydantic import ValidationError
import pytest

@pytest.fixture
def category():
    return Category(name="History")

@pytest.fixture
def topic(category):
    return Topic(category_id=category.id, name="WW1")

@pytest.fixture
def question(category, topic):
    return Question(category_id=category.id, topic_id=topic.id, content="Who won the World War I?")

@pytest.fixture
def answer(question):
    return Answer(content="France", attempt_number=1)

def test_answer_is_immutable(answer):
    with pytest.raises(ValidationError):
        answer.content = "Germany"

def test_user_have_unique_ids():
    user1 = User(name="Jan")
    user2 = User(name="John")
    assert user1.id != user2.id

def test_evaluation_ranking_is_within_boundaries():
    with pytest.raises(ValidationError):
        eval = Evaluation(content="Got it SOOOO right", rating=11)
        eval = Evaluation(content="Got it SOOOO wrong", rating=0)

