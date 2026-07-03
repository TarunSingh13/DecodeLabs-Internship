from responses import responses
from datetime import datetime

# Ask user name
user_name = input("Enter your name: ").strip().title()

# Message Counter
message_count = 0

print("=" * 55)
print(f"🤖 Welcome {user_name}!")
print("DecodeBot - Rule Based AI Chatbot")
print("Type 'help' to see available commands.")
print("Type 'exit' to end the chat.")
print("=" * 55)

# Open chat history file
history = open("chat_history.txt", "a", encoding="utf-8")

history.write("\n")
history.write("=" * 50 + "\n")
history.write(f"New Chat Session : {datetime.now()}\n")
history.write("=" * 50 + "\n")

while True:

    user_input = input(f"\n{user_name}: ").lower().strip()

    message_count += 1

    history.write(f"{user_name}: {user_input}\n")

    if user_input == "exit":

        print("\nDecodeBot: Thank you for chatting! 👋")
        print("\nSession Summary")
        print("----------------")
        print(f"Total Messages : {message_count}")

        history.write("Session Ended\n")
        history.close()

        break

    elif user_input == "time":

        current_time = datetime.now().strftime("%I:%M:%S %p")
        response = f"Current Time : {current_time}"

    elif user_input == "date":

        current_date = datetime.now().strftime("%d-%m-%Y")
        response = f"Today's Date : {current_date}"

    elif user_input in responses:

        response = responses[user_input]

    else:

        response = "Sorry! I don't understand that command."

    print("DecodeBot:", response)

    history.write(f"DecodeBot: {response}\n")