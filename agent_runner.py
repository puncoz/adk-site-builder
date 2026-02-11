import asyncio

from dotenv import load_dotenv
from google.adk import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part

from agents.multi_step_site_builder_agent.agent import root_agent
from utils.print_json import print_json_response

load_dotenv()

# --- 1. setting up identifies (constants) ---
# we define constant text variables to identify our application and conversation
APP_NAME = "adk_website_builder"
USER_ID = "user_123456"
# unique id for this entire chat session
SESSION_ID = "session_chat_loop__1"


# --- 2. main chat loop function ---
# this async function will set everything up once, then loop to allow for continuous chat
async def chat_loop():
    """
    Initialize the agent and session, then enters a loop to continuously accept
    user queries and provide agent responses.
    """
    print("Agent chat session started!")
    print("Type 'quit', 'exit', or ':q' to end the session.\n")

    # === SETUP (done once) ===
    # session service stores the conversation history (memory)
    session_service = InMemorySessionService()

    # we create session object that will be used for the entire chat
    session = await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID
    )

    # Runner is the engine that executes agent's logic
    runner = Runner(
        agent=root_agent,
        app_name=APP_NAME,
        session_service=session_service
    )

    # === INTERACTIVE LOOP ===
    # this `while True` loop will run indefinitely until user decides to quit
    while True:
        # prompt user for their next message
        user_input = input("Enter your query: ")

        # check if user wants to exit the chat
        # .lower() makes the text lowercase so "Quit" or "QUIT" also work
        if user_input.lower() in ["quit", "exit", ":q"]:
            print("Ending chat session. Goodbye!")
            break

        # --- Agent Interaction ---
        # format user's input into the structure that agent understands
        message = Content(
            role="user",
            parts=[
                Part(text=user_input)
            ]
        )

        # runner.run_async() method sends message and gets a stream of events back
        # because we are using the SAME runner and session IDs each time, agent remembers
        # the previous parts of the conversation
        events = runner.run_async(
            user_id=USER_ID,
            session_id=SESSION_ID,
            new_message=message
        )

        # --- Process the Event Stream ---
        # we loop through the agent's "thinking steps" (events) to find the final answer
        final_response = ""
        event_counter = 0
        async for event in events:
            event_counter += 1

            # print each event as it comes in, with a title for clarity
            # this helps us see the agent's thought process step-by-step
            print_json_response(event, f"============== Event #{event_counter} ================")

            if hasattr(event, "author") and event.author == "website_coder_agent":
                if event.is_final_response():
                    # if event is a final response, we extract the text
                    # this is agent's final answer to the user's query
                    final_response = event.content.parts[0].text

                    # print a clean separation for the agent's response
                    print(f"\nAgent Response:\n-----------------------------------\n{final_response}\n")
                    break


# --- 3. starting the program ---
# this is the entry point that runs our chat loops
if __name__ == "__main__":
    asyncio.run(chat_loop())
