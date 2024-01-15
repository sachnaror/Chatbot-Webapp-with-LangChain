import os

from langchain.chains import ConversationChain
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory

os.environ['OPENAI_API_KEY'] = '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'

model = OpenAI(temperature=0)
chain = ConversationChain(llm=model,
                          memory=ConversationBufferMemory(),
                          verbose=True)

print(chain.predict(input="Can You tell me something about vector database ?"))
