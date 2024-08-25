from nltk.chat.util import Chat, reflections
from flask import Flask, render_template, request

app = Flask(__name__)

def simple_chatbot(user_query):
    if user_query == "What was Apple's total revenue in 2022?":
        return "Apple's total revenue in 2022 was approximately $383.29 billion."
    elif user_query == "How has Tesla's net income changed in 2022?":
        return "Tesla's net income grew by 123.02% in 2022."
    elif user_query == "What is Microsoft's total revenue growth in 2023?":
        return "Microsoft's total revenue growth in 2023 was 6.88%."
    elif user_query == "What was Tesla's total revenue growth in 2022?":
        return "Tesla's total revenue growth in 2022 was 51.35%."
    elif user_query == "How has Apple's net income changed in 2023?":
        return "Apple's net income decreased by 2.81% in 2023."
    elif user_query == "What was Microsoft's net income growth in 2022?":
        return "Microsoft's net income grew by 18.72% in 2022."
    elif user_query == "What was Apple's total revenue growth in 2023?":
        return "Apple's total revenue decreased by 2.80% in 2023."
    elif user_query == "How has Tesla's net income changed in 2023?":
        return "Tesla's net income increased by 18.96% in 2023."
    elif user_query == "What is Microsoft's net income growth in 2023?":
        return "Microsoft's net income decreased by 0.52% in 2023."
    else:
        return "Sorry, I can only provide information on predefined queries."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_query = request.args.get("msg")
    response = simple_chatbot(user_query)
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)