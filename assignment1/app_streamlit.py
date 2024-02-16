# https://pandas.pydata.org
# https://pypi.org/project/altair/
# https://docs.streamlit.io/library/api-reference/data/st.table
# https://docs.streamlit.io/library/api-reference/charts/st.altair_chart

from collections import Counter
from operator import itemgetter

import streamlit as st
import pandas as pd
import altair as alt

import ner

# import graphviz for graphing dependencies
from graphviz import Digraph



example = (
        "When Sebastian Thrun started working on self-driving cars at "
        "Google in 2007, few people outside of the company took him "
        "seriously. “I can tell you very senior CEOs of major American "
        "car companies would shake my hand and turn away because I wasn't "
        "worth talking to,” said Thrun, in an interview with Recode earlier "
        "this week.")


example2 = ("Sebastian Thrun worked at Google in 2007.")


Myview = st.sidebar.radio("Select View", ["Entity", "Dependencies"])

#View for Entity
if Myview == "Entity":
    # st.set_page_config(layout='wide')
    st.markdown('## spaCy Named Entity Recognition')
    text = st.text_area('Text to process', value=example2, height=100)

    doc = ner.SpacyDocument(text)

    entities = doc.get_entities()
    tokens = doc.get_tokens()
    counter = Counter(tokens)
    words = list(sorted(counter.most_common(30)))

    
    chart = pd.DataFrame({
        'frequency': [w[1] for w in words],
        'word': [w[0] for w in words]})

    
    bar_chart = alt.Chart(chart).mark_bar().encode(x='word', y='frequency')

    st.markdown(f'Total number of tokens: {len(tokens)}<br/>'
                f'Total number of types: {len(counter)}', unsafe_allow_html=True)

    #split to two tabs
    tab1, tab2 = st.tabs(["table", "chart"])

    with tab1:
        st.table(entities)
    with tab2:
        st.altair_chart(bar_chart)


#View for Dependencies
elif Myview == "Dependencies":


    st.markdown('## spaCy visualization')
    text = st.text_area('Text to process', value=example2, height=100)

    doc = ner.SpacyDocument(text)

    dependencies = doc.get_dependency_parse()
    tokens = doc.get_tokens()
    counter = Counter(tokens)
    words = list(sorted(counter.most_common(30)))

    
    #Revise the dependencies data so it can be printed as the sample shows
    def dependency_graph(dependency_parse):
        dot = Digraph()
        
        
        nodes = {}
        for i, dep in enumerate(dependency_parse):
            node_label = f"{dep['text']}_{i}"
            nodes[dep['text'], i] = node_label
            dot.node(node_label, f"{dep['text']}")
            

        for i, dep in enumerate(dependency_parse):
            child_label = nodes[dep['text'], i]

            #Add root edge if the node is root node
            if dep['dep'] == 'ROOT':
                dot.edge(child_label, child_label, label="root")
            else:
                for j, head in enumerate(dependency_parse):
                    if dep['head_text'] == head['text']:
                        head_label = nodes[head['text'], j]
                        dot.edge(head_label, child_label, label=dep['dep'])
                        break
        
        return dot

    dot = dependency_graph(dependencies)

   
    #split to two tabs
    tab1, tab2 = st.tabs(["table", "graph"])

    with tab1:
        st.table(dependencies)
    with tab2:
        st.graphviz_chart(dot.source)
        
    



    

