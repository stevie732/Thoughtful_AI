import gradio as gr

thoughtful_ai_data = {
  "questions": [
    {"question": "What is Thoughtful AI?", "answer": "Thoughtful AI is an AI support agent."},
    {"question": "How does Thoughtful AI work?", "answer": "Thoughtful AI uses machine learning to provide answers."}
  ]
}

def thoughtful_ai(user_input):
  user_input = user_input.lower()

  for qa_pair in thoughtful_ai_data["questions"]:
    if user_input in qa_pair["question"].lower():
      return qa_pair["answer"]

  return "I'm sorry, I don't have information on that. Please contact Thoughtful AI support for further assistance."

def chat(user_input, history):
  history = history or []
  response = thoughtful_ai(user_input)
  history.append((user_input, response))
  return history, history

interface = gr.Interface(
  fn=chat,
  inputs=["text", "state"],
  outputs=["chatbot", "state"],
  live=True,
  title="Thoughtful AI Support Agent",
  description="Ask me anything about Thoughtful AI!"
)

interface.launch(share=True)