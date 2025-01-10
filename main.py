pip install langchain-openai  streamlit
import os 
os.environ["OPENAI_API_KEY"]= st.secrets['OPENAI_API_KEY']

from langchain_openai import ChatOpenAI
pplx_model=ChatOpenAI(model="llama-3.1-sonar-small-128k-online",
                      openai_api_base="https://api.perplexity.ai"
)
from langchain import PromptTemplate

app_template="""You are an intelligent Management Consultant. Write in detail about this topic:{topic};making sure that information should as latest of max {recency} years old only from 2025, i want you to write in bullet format starting with bold subheading followed by : explanation in max 2 lines
like this:
{topic}:
1. (in bold): (explantion)
2. (in bold): (explantion)  
3. (in bold): (explantion)
4. (in bold): (explantion)
..
"""

app_prompt=PromptTemplate(template=app_template,input_variables=["topic","recency"])

from langchain import LLMChain

app_chain= app_prompt | pplx_model

import streamlit as st

st.header("Complexity Researcher")

topic=st.text_input("Enter the topic you want to research")
recency=st.slider("How recent do you want the information to be (in years)?",min_value=1,max_value=10,value=5)
if st.button("Generate"):
    answer=app_chain.invoke({"topic":topic,"recency":recency})
    st.write(answer.content)


