import json

class question_reader():
    def __init__(self):   
        self.questions_info = {}
    
    def read_json_file():
        with open('qload.txt') as json_file:
            questions_info = json.load(json_file)
        return questions_info

    def get_next_question_id(self,current_id):
        return (current_id + 1)

    def read_json_file_next_qid(question_id):
        with open('qload.txt') as json_file:
            questions_info = json.load(json_file)
            xkey = get_next_question_id(question_id)
        return questions_info[xkey]

