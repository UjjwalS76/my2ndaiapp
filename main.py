from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import streamlit as st

# Initialize model
pplx_model = ChatOpenAI(
    model="llama-3.1-sonar-small-128k-online",
    openai_api_key='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',
    openai_api_base="https://api.perplexity.ai"
)

# Define template
app_template = """You are an intelligent Management Consultant. Write in detail about this topic:{topic};making sure that information should as latest of max {recency} years old only from 2025, i want you to write in bullet format starting with bold subheading followed by : explanation in max 2 lines
like this:
{topic}:
1. (in bold): (explantion)
2. (in bold): (explantion)  
3. (in bold): (explantion)
4. (in bold): (explantion)
"""

# Create prompt and chain
app_prompt = PromptTemplate(template=app_template, input_variables=["topic", "recency"])
app_chain = LLMChain(llm=pplx_model, prompt=app_prompt)  # Changed from using | operator

# Streamlit interface
st.header("Complexity Researcher")
topic = st.text_input("Enter the topic you want to research")
recency = st.slider("How recent do you want the information to be (in years)?", min_value=1, max_value=10, value=5)

if st.button("Generate"):
    try:
        answer = app_chain.invoke({"topic": topic, "recency": recency})
        st.write(answer['text'])  # Changed from answer.content to answer['text']
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
