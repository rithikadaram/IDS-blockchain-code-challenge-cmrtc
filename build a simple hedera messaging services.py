from hedera import (  
    Client,  
    Hbar,  
    TopicCreateTransaction,  
    TopicMessageSubmitTransaction,  
    TopicMessageQuery,  
)  

import datetime  
# Replace with your own Hedera testnet account ID and private key  
ACCOUNT_ID = "your-account-id"  
PRIVATE_KEY = "your-private-key"  

# Initialize the Hedera client  
client = Client.for_testnet()  
client.set_operator(ACCOUNT_ID, PRIVATE_KEY)  

def create_topic():  
    """Create a new topic on the Hedera network."""  
    transaction = TopicCreateTransaction()  
    topic_response = transaction.execute(client)  
    topic_id = topic_response.get_receipt(client).topic_id  
    return topic_id  

def send_messages(topic_id, messages):  
    """Send messages to the specified topic."""  
    for message in messages:  
        transaction = TopicMessageSubmitTransaction().set_topic_id(topic_id).set_message(message)  
        transaction.execute(client)  

def retrieve_messages(topic_id):  
    """Retrieve messages from the specified topic."""  
    messages = []  
    query = TopicMessageQuery().set_topic_id(topic_id).set_start_time(datetime.datetime.now())  

    for message in query.execute(client):  
        messages.append((message.message.decode(), message.consensus_timestamp))  
    
    return messages  

def main():  
    # Step 1: Create a new topic  
    topic_id = create_topic()  
    print(f"Topic Created: {topic_id}")  

    # Step 2: Send messages  
    messages_to_send = ["Hello, Hedera!", "Learning HCS", "Message 3"]  
    send_messages(topic_id, messages_to_send)  

    print("Messages Sent:")  
    for i, msg in enumerate(messages_to_send, start=1):  
        print(f"{i}. \"{msg}\" at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")  

    # Step 3: Retrieve messages  
    received_messages = retrieve_messages(topic_id)  

    print("\nMessages Received:")  
    for i, (msg, timestamp) in enumerate(received_messages, start=1):  
        msg_time = timestamp.to_datetime().strftime('%Y-%m-%d %H:%M:%S')  
        print(f"{i}. \"{msg}\" at {msg_time}")  

if __name__ == "__main__":  
    main()