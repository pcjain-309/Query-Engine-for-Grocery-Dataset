import pinecone
from flask import jsonify
from langchain.llms import Cohere
from langchain.vectorstores import Pinecone
from langchain.embeddings import CohereEmbeddings
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

pinecone.init(
    api_key="97cfdfb9-96fd-4011-93d7-44a2787cb9d8",
    environment="gcp-starter"
)

index_name = "chaabi"

index = pinecone.Index(index_name=index_name)


template = """Question: {question}
Answer: Let's think step by step."""
prompt = PromptTemplate(template=template, input_variables=["question"])

def similarDocs(query, docsearch) :
    docs = docsearch.similarity_search(query)
    return docs

def get_answer(api_key, query):
    llm = Cohere(cohere_api_key= api_key)
    embedder = CohereEmbeddings(cohere_api_key= api_key)
    docsearch = Pinecone.from_existing_index(index_name, embedder)

    similar_docs = similarDocs(query, docsearch)
    product_list = []

    for i, doc in enumerate(similar_docs):
        product_desc = doc.page_content
        lines = product_desc.split('\n')

        index = lines[0].split('.')[0].strip()
        product = lines[1].strip()
        category = lines[2].strip()
        sub_category = lines[3].strip()
        brand = lines[4].strip()
        sale_price = float(lines[5])
        market_price = float(lines[6])
        product_type = lines[7].strip()
        rating = float(lines[8])
        description = "\n".join(lines[9:]).strip()

        product_dict = {
            "index": index,
            "product": product,
            "category": category,
            "sub_category": sub_category,
            "brand": brand,
            "sale_price": sale_price,
            "market_price": market_price,
            "type": product_type,
            "rating": rating,
            "description": description
        }

        product_list.append(product_dict)

    print(product_list)
    json_data = jsonify(product_list)
    return json_data

    # chain = LLMChain(llm=llm, prompt=prompt)
    # answer = chain.run(input_documents=similar_docs, question=query)
    # return  answer

