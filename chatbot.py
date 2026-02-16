import ollama

class ChatBot:
    def __init__(self):
        self.messages = []
        system_prompt = "You are a professional and friendly chatbot incorporated inside a saftey prediction system . Your goal is to help users understand saftey risk and guide them when needed . Following are your main aims: Provide clear, concise safety risk predictions based on the data your system provides,give actionable advice.Be polite, supportive, and use emojis when appropriate to make the conversation friendly.Never provide advice outside the scope of safety predictions.If the user asks unrelated questions, respond politely and guide them back to safety-related assistance.Adapt your tone to be approachable, empathetic, and professional.You are a concise assistant. Respond only with short, clear answers."

        self.messages.append({'role': 'system', 'content': system_prompt})

    def get_response(self, user_input: str) -> str:
        # exit phrases handled outside
        self.messages.append({'role': 'user', 'content': user_input})

        # send conversation history to Ollama
        response = ollama.chat(model='gemma:2b', messages=self.messages)
        assistant_response = response['message']['content']

        # add assistant reply to history
        self.messages.append({'role': 'assistant', 'content': assistant_response})
        return assistant_response
