from tuitor.domain import User, Category, Topic, Question, Answer

def main():
    user = User(name="Jarek")
    category = Category(name="History")
    topic = Topic(category_id=category.id, name="WW1")
    question = Question(category_id=category.id, topic_id=topic.id, content="Who won the World War I?")
    answer = Answer(content="France", attempt_number=1)
    
    print(f"User with id {user.id} will now answer question with id {question.id}")
    print(f"The first question is: {question.content}")
    print(f"The only correct answer is: {answer.content}")

if __name__ == "__main__":
    main()
