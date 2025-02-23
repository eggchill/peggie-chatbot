from flask import Flask, request, jsonify
import openai
import random

app = Flask(__name__)

# Peggie’s warm & adaptive intro
def get_intro():
    return "Hi, I’m Peggie! 💛 How are you feeling today? You don’t have to share your name, but if you want to, I’d love to know who I’m chatting with!"

# Peggie’s dynamic advice system
def get_chatbot_response(user_input):
    """Generates a response using GPT-4 with Peggie’s warm, supportive, and bestie-like tone."""
    
    # Fake personal stories for relatability
    def fake_story():
        stories = [
            "I remember when I forgot to ice before my shot—NEVER making that mistake again! 😂",
            "One time, I totally blanked in my first appointment and just nodded at everything. Now I keep a notes app list ready!",
            "I tried drinking a ton of water to help with bloating, but then I was running to the bathroom every 5 minutes—balance is key!"
        ]
        return random.choice(stories)

    # Structured warm advice
    structured_responses = {
        "injections": "Omg, that totally has happened to me too! I found that icing the spot for 30 seconds before really helped. Have you tried that yet?",
        "bloating": "Yes, bloating is *so* real. Drinking water, light movement, and comfy clothes are key. Also, leggings only from now on. TRUST. 😂",
        "hot flashes": "Yep, that’s normal! Hormones are wild. A cool washcloth on your neck or wrists can feel amazing—have you tried that?",
        "anxiety": "It makes *so* much sense to feel anxious. This is a huge thing! Deep breaths, movement, and journaling help. Have you found anything that works for you?",
    }

    response = structured_responses.get(user_input.lower(), "Let me find the best advice for you! How have you been feeling about the process so far?")
    
    return response

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": get_intro()})

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    response = get_chatbot_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000")
