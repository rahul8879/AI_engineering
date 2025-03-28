import os
from dotenv import load_dotenv
from autogen import ConversableAgent
#load the .env : 
load_dotenv(r'C:\Users\Rahul\Documents\FREELANCING\1.AppliedSkil\Gen_AI_learning\.env')
model = "gpt-3.5-turbo"
llm_config = {
    "model":model,
    "api_key":os.environ.get("OPENAI_API_KEY"),

}

agent = ConversableAgent(name='chatbot',
                         llm_config=llm_config,
                         code_execution_config=False,
                         human_input_mode="NEVER")

response = agent.generate_reply(messages=[{"role":"system","content": " Hello, how are you"}])