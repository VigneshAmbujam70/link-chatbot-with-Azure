import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Get environment variables
api_key = os.environ.get("MicrosoftAPIKey")
endpoint = os.environ.get("MicrosoftAIServiceEndpoint")

if not api_key or not endpoint:
    print("Error: Environment variables not set.")
    exit()

# Create Azure client
credential = AzureKeyCredential(api_key)
text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=credential)

def analyze_sentiment(text):
    response = text_analytics_client.analyze_sentiment(documents=[text])[0]
    sentiment = response.sentiment
    scores = response.confidence_scores
    return sentiment, scores

def show_capabilities():
    return """
I can:
- Greet you
- Analyze sentiment using Azure AI
- Handle invalid input
- Show my capabilities
Type 'exit' to quit.
"""

def chatbot():
    print("Azure AI Sentiment Chatbot")
    print("Type 'help' to see capabilities.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break

        if not user_input.strip():
            print("Bot: Please enter valid text.")
            continue

        if user_input.lower() == "help":
            print(show_capabilities())
            continue

        if user_input.lower() in ["hi", "hello"]:
            print("Bot: Hello! How are you feeling today?")
            continue

        sentiment, scores = analyze_sentiment(user_input)

        print(f"Bot: Sentiment detected: {sentiment}")
        print(f"Positive: {scores.positive:.2f}")
        print(f"Neutral: {scores.neutral:.2f}")
        print(f"Negative: {scores.negative:.2f}")
        print("-" * 40)

if __name__ == "__main__":
    chatbot()
