import openai

# OpenAI API 키 설정

# 파인 튜닝된 모델의 ID
fine_tuned_model_id = 'ft:gpt-3.5-turbo-0125:personal::9wAN8XY4'

# 대화 이력을 저장할 리스트 초기화
conversation_history = [
    {"role": "system", "content": "Marv is a friendly and humorous chatbot for a cafe."}
]
#ssdfsf
def continue_conversation(user_input):
    # 사용자의 입력을 대화 이력에 추가
    conversation_history.append({"role": "user", "content": user_input})

    # 모델에게 대화 이력을 전달하고 응답 생성
    response = openai.ChatCompletion.create(
        model=fine_tuned_model_id,
        messages=conversation_history
    )
    
    # 모델의 응답을 대화 이력에 추가
    assistant_message = response['choices'][0]['message']['content']
    conversation_history.append({"role": "assistant", "content": assistant_message})

    # 모델의 응답 출력
    return assistant_message

