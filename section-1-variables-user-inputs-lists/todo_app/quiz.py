import json

with open('files/questions.json') as file:
    questions = json.load(file)

correct = 0
for item in questions:
    print(item['question'])
    options = item['options']

    for i, option in enumerate(options):
        print(f"\t {i+1}) {option}")

    answer = input(f"Answer (1-{len(options)}): ")
    answer_index = int(answer) - 1

    if answer_index == item['answer']:
        correct += 1

print(f"Result: {correct}/{len(questions)}")