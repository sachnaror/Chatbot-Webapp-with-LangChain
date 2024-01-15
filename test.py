


import os

from langchain.chains import ConversationChain
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain_community.llms import OpenAI

os.environ['OPENAI_API_KEY'] = 'sk-7LWn4p9jQQoo5dgAwLAsT3BlbkFJ2N625TTPBmEQMVjqT'

model = OpenAI(temperature=0)
chain = ConversationChain(llm=model,
                          verbose=True,lseek(fd, pos, how)
                          memory=ConversationBufferMemory()
                          )

print(chain.predict(input="Can You tell me something about vector database ?"))



--------------------------------------------




from langchain.llms import OpenAI
import os

os.environ['OPENAI_API_KEY'] = 'Enter your openAI API key'
model = OpenAI(temperature=0.6)

prompt = model("Tell me a joke")

print(prompt)


--------------------------------------------



from langchain import PromptTemplate

template = "{name} is my favourite course at GFG"

prompt = PromptTemplate(
	input_variables=["name"],
	template=template,
)

example = prompt.format(name="Data Structures and Algorithms")

print(example)




--------------------------------------------

import streamlit as st
st.title('Sachin o sachin ')
input_text = st.text_input('Enter Your Text: ')
from langchain.prompts import PromptTemplate
title_template = PromptTemplate(
	input_variables = ['concept'],
	template='Give me a youtube video title about {concept}'
)
script_template = PromptTemplate(
	input_variables = ['title', 'wikipedia_research'],
	template='''Give me an attractive youtube video script based on the title Vector database while making use of the information and knowledge obtained from the Wikipedia research:{wikipedia_research}'''
)


--------------------------------------------

wikipedia = WikipediaAPIWrapper()
if input_text:
	title = chainT.run(input_text)
	wikipedia_research = wikipedia.run(input_text)
	script = chainS.run(title=title, wikipedia_research=wiki_research)
	st.write(title)
	st.write(script)
	with st.expander('Wikipedia-based exploration: '):
		st.info(wiki_research)



--------------------------------------------


import os
os.environ['OPENAI_API_KEY'] = "Enter the api key"

import streamlit as st
# Set the title using StreamLit
st.title(' Sachin o Sachin')
input_text = st.text_input('Enter Your Text: ')


from langchain.prompts import PromptTemplate
# setting up the prompt templates
title_template = PromptTemplate(
	input_variables = ['concept'],
	template='Give me a youtube video title about {concept}'
)

script_template = PromptTemplate(
	input_variables = ['title', 'wikipedia_research'],
	template='''Give me an attractive youtube video script based on the LLM model in AI
	while making use of the information and knowledge obtained from the Wikipedia research:{wikipedia_research}'''
)


from langchain.memory import ConversationBufferMemory
# Using the ConversationBufferMemory to can be used to store a history of the conversation between the user and the language model.
# This information can be used to improve the language model's understanding of the user's intent, and to generate more relevant and coherent responses.

memoryT = ConversationBufferMemory(input_key='concept', memory_key='chat_history')
memoryS = ConversationBufferMemory(input_key='title', memory_key='chat_history')


from langchain.llms import OpenAI
# Importing the large language model OpenAI via langchain
model = OpenAI(temperature=0.6)

from langchain.chains import LLMChain
chainT = LLMChain(llm=model, prompt=title_template, verbose=True, output_key='title', memory=memoryT)
chainS = LLMChain(llm=model, prompt=script_template, verbose=True, output_key='script', memory=memoryS)


from langchain.utilities import WikipediaAPIWrapper
wikipedia = WikipediaAPIWrapper()

# Display the output if the the user gives an input
if input_text:
	title = chainT.run(input_text)
	wikipedia_research = wikipedia.run(input_text)
	script = chainS.run(title=title, wikipedia_research=wikipedia_research)

	st.write(title)
	st.write(script)

	with st.expander('Wikipedia-based exploration: '):
		st.info(wikipedia_research)


--------------------------------------------
