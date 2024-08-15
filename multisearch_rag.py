from langchain_community.tools import WikipediaQueryRun,ArxivQueryRun,GooglePlacesTool
from langchain_community.utilities import WikipediaAPIWrapper,ArxivAPIWrapper,GooglePlacesAPIWrapper
from langchain_community.tools.google_lens import GoogleLensQueryRun
from langchain_community.utilities.google_lens import GoogleLensAPIWrapper
from langchain_googledrive.tools import GoogleDriveSearchTool
from langchain_googledrive.utilities import GoogleDriveAPIWrapper
from langchain_groq import ChatGroq
from langchain import hub
from langchain.agents import create_openai_tools_agent
from langchain.agents import AgentExecutor
import streamlit as st
import os


serp_api = os.getenv("SERP_API_KEY")
google_api = os.getenv("GOOGLECLOUD_API_KEY")



def search(query):
   
   # Wiki Tool
   wiki_wrapper = WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=200)
   wiki = WikipediaQueryRun(api_wrapper=wiki_wrapper)
   print(wiki.name)

   # Arxiv Tool
   arxiv_wrapper = ArxivAPIWrapper(top_k_results=1,doc_content_chars_max=200)
   arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)
   print(arxiv.name)

   # Google Places Tool

   places_wrapper = GooglePlacesAPIWrapper(gplaces_api_key=google_api)
   places = GooglePlacesTool(api_wrapper=places_wrapper)
   print(places.name)

   # Google lens tool

   lens_wrapper = GoogleLensAPIWrapper(serp_api_key=serp_api)
   lens = GoogleLensQueryRun(api_wrapper=lens_wrapper)
   print(lens.name)

   tools = [arxiv,places,lens,wiki]
   # LLM

   from langchain_groq import ChatGroq

   llm = ChatGroq(model="llama3-70b-8192",
               temperature=0.8)

   
   # Prompt
   prompt = hub.pull("hwchase17/openai-functions-agent")

   # Agent
   agent = create_openai_tools_agent(llm,tools,prompt)

   # Executing the Agent created
   agent_executor = AgentExecutor(agent=agent,tools=tools,verbose=True)

   response = agent_executor.invoke({"input":{query}})

   return response['output']




def main():

   st.title("Multisearch Rag App")
   st.write("Search anything you want")
   st.info("It gives you info abt the research papers, Various places,lets you search the exact image you uploaded, Lets you search through your Google Drive")

   messages = st.container()

   if query := st.chat_input("Ask a question"):
       with st.spinner("Generating response..."):
         with messages:

            st.chat_message("user").write(query)

            response = search(query)

            st.chat_message("assistant").write(response)


if __name__ == "__main__":
   main()