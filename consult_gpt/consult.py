from django.http import JsonResponse
import openai

def chat_with_gpt(request):
    user_input = request.GET.get('user_input')

    if not user_input:
        return JsonResponse({"response": "Поле вводу не може бути порожнім"})

    openai.api_key = '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'  # Зберігайте ключ в змінній оточення

    messages = [{"role": "user", "content": user_input}]
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=messages,
                                            temperature=0.5,
                                            max_tokens=1000)

    chat_response = response['choices'][0]['message']['content']

    return JsonResponse({"response": chat_response})


from django.shortcuts import render

def consult(request):
    return render(request, 'consult.html')
