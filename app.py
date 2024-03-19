# Bring in deps
import os
from apikey import apikey
from PyPDF2 import PdfReader
import streamlit as st
import re
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper

os.environ['OPENAI_API_KEY'] = apikey

# Function to extract author information from text
def extract_author_info(text):
    # Define a regular expression pattern to match author names and affiliations
    pattern = r"Author(s)?:\s*(.*?)\s*Affiliation(s)?:\s*(.*?)\s*Abstract"  # Modify as per your text structure

    # Search for matches in the text
    match = re.search(pattern, text, re.DOTALL)

    # Extract author names and affiliations
    if match:
        authors = match.group(2).strip()
        affiliations = match.group(4).strip()
        return authors, affiliations
    else:
        return "Author information not found", ""

import streamlit as st

import streamlit as st
from PyPDF2 import PdfFileReader
# Add custom CSS for background color
# Add custom CSS for background image



# Main page content
st.title('🔬🔗 PaperDigest')
st.markdown("<p style='color: blue; font-style: italic;'>Digesting Research, One Paper at a Time.</p>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload your research paper (PDF)", type="pdf")
if uploaded_file:
    # Read PDF file and extract text
    pdf_text = ""
    pdf_reader = PdfReader(uploaded_file)
    for page_num in range(len(pdf_reader.pages) ):
        page = pdf_reader.pages[page_num] 
        pdf_text += page.extract_text()

    # Prompt templates
    script_template = PromptTemplate(
        input_variables=['research_text'],
        template='summarize the given research paper: {research_text}'
    )

    # Memory
    script_memory = ConversationBufferMemory(input_key='research_text', memory_key='chat_history')

    # Llms
    llm = OpenAI(temperature=0.9)
    script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key='script',
                            memory=script_memory)

    # Show stuff to the screen if there's a prompt
    if st.button("Summarize 📝✨"):
        summary = script_chain.run(research_text=pdf_text)
        st.write("Summary:")
        st.write(summary)

# Sidebar content
st.sidebar.title("*Curious for more?*")

if st.sidebar.button("Key Findings🔑🔍"):
   # Prompt templates
    key_findings_template = PromptTemplate(
        input_variables=['research_text'],
        template='Provide key findings based on the given research paper: {research_text}'
    )

    # Memory
    key_findings_memory = ConversationBufferMemory(input_key='research_text', memory_key='chat_history')

    # Llms
    llm = OpenAI(temperature=0.9)
    key_findings_chain = LLMChain(llm=llm, prompt=key_findings_template, verbose=True, output_key='key_findings',
                            memory=key_findings_memory)

    if uploaded_file:
        key_findings = key_findings_chain.run(research_text=pdf_text)
        st.write("Key Findings:")
        st.write(key_findings)
    else:
        st.write("Upload a research paper to generate key findings.")

if st.sidebar.button("Methodology 📊🔬"):
    # Prompt templates
    methodology_template = PromptTemplate(
        input_variables=['research_text'],
        template='Explain the methodology used in the research paper: {research_text}'
    )

    # Memory
    methodology_memory = ConversationBufferMemory(input_key='research_text', memory_key='chat_history')

    # Llms
    llm = OpenAI(temperature=0.9)
    methodology_chain = LLMChain(llm=llm, prompt=methodology_template, verbose=True, output_key='methodology',
                            memory=methodology_memory)

    if uploaded_file:
        methodology = methodology_chain.run(research_text=pdf_text)
        st.write("Methodology:")
        st.write(methodology)
    else:
        st.write("Upload a research paper to generate methodology explanation.")

if st.sidebar.button("Results 📈💡"):
    # Prompt templates
    results_template = PromptTemplate(
        input_variables=['research_text'],
        template='Present the results obtained from the research paper: {research_text}'
    )

    # Memory
    results_memory = ConversationBufferMemory(input_key='research_text', memory_key='chat_history')

    # Llms
    llm = OpenAI(temperature=0.9)
    results_chain = LLMChain(llm=llm, prompt=results_template, verbose=True, output_key='results',
                            memory=results_memory)

    if uploaded_file:
        results = results_chain.run(research_text=pdf_text)
        st.write("Results:")
        st.write(results)
    else:
        st.write("Upload a research paper to generate results presentation.")

if st.sidebar.button("Conclusion 🏁📝"):
    # Prompt templates
    conclusion_template = PromptTemplate(
        input_variables=['research_text'],
        template='Summarize the conclusion drawn from the research paper: {research_text}'
    )

    # Memory
    conclusion_memory = ConversationBufferMemory(input_key='research_text', memory_key='chat_history')

    # Llms
    llm = OpenAI(temperature=0.9)
    conclusion_chain = LLMChain(llm=llm, prompt=conclusion_template, verbose=True, output_key='conclusion',
                            memory=conclusion_memory)

    if uploaded_file:
        conclusion = conclusion_chain.run(research_text=pdf_text)
        st.write("Conclusion:")
        st.write(conclusion)
    else:
        st.write("Upload a research paper to generate conclusion summary.")



if st.sidebar.button("References 📚🔖"):
    # Prompt templates
    references_template = PromptTemplate(
        input_variables=['research_text'],
        template='List the references cited in the research paper: {research_text}'
    )

    # Memory
    references_memory = ConversationBufferMemory(input_key='research_text', memory_key='chat_history')

    # Llms
    llm = OpenAI(temperature=0.9)
    references_chain = LLMChain(llm=llm, prompt=references_template, verbose=True, output_key='references',
                            memory=references_memory)

    if uploaded_file:
        references = references_chain.run(research_text=pdf_text)
        st.write("References:")
        st.write(references)
    else:
        st.write("Upload a research paper to generate references list.")


if st.sidebar.button("Limitations ⚠️🚫"):
    # Prompt templates
    limitations_template = PromptTemplate(
        input_variables=['research_text'],
        template='Identify the limitations of the research paper: {research_text}'
    )

    # Memory
    limitations_memory = ConversationBufferMemory(input_key='research_text', memory_key='chat_history')

    # Llms
    llm = OpenAI(temperature=0.9)
    limitations_chain = LLMChain(llm=llm, prompt=limitations_template, verbose=True, output_key='limitations',
                            memory=limitations_memory)

    if uploaded_file:
        limitations = limitations_chain.run(research_text=pdf_text)
        st.write("Limitations:")
        st.write(limitations)
    else:
        st.write("Upload a research paper to identify its limitations.")


if st.sidebar.button("Future Work 🚀🔮"):
    # Prompt templates
    future_work_template = PromptTemplate(
        input_variables=['research_text'],
        template='Discuss potential future directions or work based on the research paper: {research_text}'
    )

    # Memory
    future_work_memory = ConversationBufferMemory(input_key='research_text', memory_key='chat_history')

    # Llms
    llm = OpenAI(temperature=0.9)
    future_work_chain = LLMChain(llm=llm, prompt=future_work_template, verbose=True, output_key='future_work',
                            memory=future_work_memory)

    if uploaded_file:
        future_work = future_work_chain.run(research_text=pdf_text)
        st.write("Future Work:")
        st.write(future_work)
    else:
        st.write("Upload a research paper to discuss potential future work.")



if st.sidebar.button("Lit Review 📚🔍"):
    # Prompt templates
    lit_review_template = PromptTemplate(
        input_variables=['research_text'],
        template='Conduct a literature review based on the research paper: {research_text}'
    )

    # Memory
    lit_review_memory = ConversationBufferMemory(input_key='research_text', memory_key='chat_history')

    # Llms
    llm = OpenAI(temperature=0.9)
    lit_review_chain = LLMChain(llm=llm, prompt=lit_review_template, verbose=True, output_key='lit_review',
                            memory=lit_review_memory)

    if uploaded_file:
        lit_review = lit_review_chain.run(research_text=pdf_text)
        st.write("Literature Review:")
        st.write(lit_review)
    else:
        st.write("Upload a research paper to conduct a literature review.")


if st.sidebar.button("Visualizations 📊🖼️"):
    # Prompt templates
    visualizations_template = PromptTemplate(
        input_variables=['research_text'],
        template='Generate visualizations based on the data presented in the research paper: {research_text}'
    )

    # Memory
    visualizations_memory = ConversationBufferMemory(input_key='research_text', memory_key='chat_history')

    # Llms
    llm = OpenAI(temperature=0.9)
    visualizations_chain = LLMChain(llm=llm, prompt=visualizations_template, verbose=True, output_key='visualizations',
                            memory=visualizations_memory)

    if uploaded_file:
        visualizations = visualizations_chain.run(research_text=pdf_text)
        st.write("Visualizations:")
        st.write(visualizations)
    else:
        st.write("Upload a research paper to generate visualizations.")


if st.sidebar.button("Author Background 👤📚"):
    # Prompt templates
    author_background_template = PromptTemplate(
        input_variables=['research_text'],
        template='Provide background information about the author(s) of the research paper: {research_text}'
    )

    # Memory
    author_background_memory = ConversationBufferMemory(input_key='research_text', memory_key='chat_history')

    # Llms
    llm = OpenAI(temperature=0.9)
    author_background_chain = LLMChain(llm=llm, prompt=author_background_template, verbose=True, output_key='author_background',
                            memory=author_background_memory)

    if uploaded_file:
        author_background = author_background_chain.run(research_text=pdf_text)
        st.write("Author Background:")
        st.write(author_background)
    else:
        st.write("Upload a research paper to provide background information about the author(s).")

st.sidebar.write("<p style='text-align:center;'>made with 💙 by Advika Thakur</p>", unsafe_allow_html=True)
