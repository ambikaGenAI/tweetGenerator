from langchain import prompts
from langchain import chains
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import streamlit as st
os.environ['GOOGLE_API_KEY']=st.secrets["GOOGLE_API_KEY"]

tweet_template="Give me {number} of tweets on topic {topic}"
tweet_prompt_template=prompts.PromptTemplate(input_variables={"number","topic"},template=tweet_template)

googlemodel=ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest")
tweet_chain=tweet_prompt_template | googlemodel

st.set_page_config(page_title="Tweet Generator")
st.header("Tweet Generator")
st.subheader("Generates tweets as per required number")

Topic= st.text_input("topic")
Number_of_Tweets=st.number_input("number of tweets",min_value=1,max_value=10,value=1,step=1)

if(st.button("Generate")):
    tweets=tweet_chain.invoke({"number":Number_of_Tweets,"topic":Topic})
    st.write(tweets.content)
