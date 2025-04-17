import os
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from dotenv import load_dotenv


# Define input schema for the tool
load_dotenv()
# Initialize Tavily search tool
search = TavilySearchResults(max_results=2)
tools = [search]

# Initialize chat model
model = init_chat_model("gpt-4o", model_provider="openai")

# Create a React agent with memory
memory = MemorySaver()
agent_executor = create_react_agent(model, tools, checkpointer=memory)

# Set up configuration for memory persistence
config = {"configurable": {"thread_id": "abc123"}}


def main():
    print("Welcome to the chatbot! Type 'quit' to exit.")
    print("-" * 50)

    conversation_active = True
    while conversation_active:
        # Get user input
        user_input = input("\nYou: ")

        # Check if user wants to quit
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("\nGoodbye!")
            conversation_active = False
            continue

        print("\nBot is thinking...")

        # Process the user message through the agent
        response = agent_executor.invoke(
            {"messages": [HumanMessage(content=user_input)]},
            config
        )

        # Extract and print the assistant's response
        print("\nBot:", end=" ")
        assistant_message = response["messages"][-1]
        print(assistant_message.content)


if __name__ == "__main__":
    main()