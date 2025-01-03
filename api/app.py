from langflow.load import run_flow_from_json
TWEAKS = {
  "ChatInput-w7erC": {
    "files": "",
    "background_color": "",
    "chat_icon": "",
    "input_value": "give me insights on reels",
    "sender": "User",
    "sender_name": "User",
    "session_id": "",
    "should_store_message": True,
    "text_color": ""
  },
  "File-EdFel": {
    "path": "Updated_Social_Media_Data_with_Total_Engagement.csv",
    "concurrency_multithreading": 4,
    "silent_errors": False,
    "use_multithreading": False
  },
  "SplitText-8XZ2r": {
    "chunk_overlap": 200,
    "chunk_size": 1000,
    "separator": "\n"
  },
  "AstraDB-XZAmC": {
    "advanced_search_filter": "{}",
    "api_endpoint": "ASTRA_DB_API_ENDPOINT",
    "batch_size": None,
    "bulk_delete_concurrency": None,
    "bulk_insert_batch_concurrency": None,
    "bulk_insert_overwrite_concurrency": None,
    "collection_indexing_policy": "",
    "collection_name": "collection_latest",
    "embedding_choice": "Embedding Model",
    "keyspace": "",
    "metadata_indexing_exclude": "",
    "metadata_indexing_include": "",
    "metric": "cosine",
    "number_of_results": 4,
    "pre_delete_collection": False,
    "search_filter": {},
    "search_input": "",
    "search_score_threshold": 0,
    "search_type": "Similarity",
    "setup_mode": "Sync",
    "token": "ASTRA_DB_APPLICATION_TOKEN"
  },
  "Google Generative AI Embeddings-YpPQW": {
    "api_key": "GOOGLE_API_KEY",
    "model_name": "models/text-embedding-004"
  },
  "Prompt-HTpAF": {
    "template": "{context}.\nFrom the above context calculate all the required metric  and generate insights  percentage based by comparing with different post types based on users question.\n{question}",
    "context": "",
    "question": ""
  },
  "AstraDB-sv6vK": {
    "advanced_search_filter": "{}",
    "api_endpoint": "ASTRA_DB_API_ENDPOINT",
    "batch_size": None,
    "bulk_delete_concurrency": None,
    "bulk_insert_batch_concurrency": None,
    "bulk_insert_overwrite_concurrency": None,
    "collection_indexing_policy": "",
    "collection_name": "collection_latest",
    "embedding_choice": "Embedding Model",
    "keyspace": "",
    "metadata_indexing_exclude": "",
    "metadata_indexing_include": "",
    "metric": "cosine",
    "number_of_results": 4,
    "pre_delete_collection": False,
    "search_filter": {},
    "search_input": "",
    "search_score_threshold": 0,
    "search_type": "Similarity",
    "setup_mode": "Sync",
    "token": "ASTRA_DB_APPLICATION_TOKEN"
  },
  "Google Generative AI Embeddings-pmhlg": {
    "api_key": "GOOGLE_API_KEY",
    "model_name": "models/text-embedding-004"
  },
  "ParseData-EnYIW": {
    "sep": "\n",
    "template": "{text}"
  },
  "GoogleGenerativeAIModel-9FoAi": {
    "google_api_key": "GOOGLE_API_KEY",
    "input_value": "",
    "max_output_tokens": 700,
    "model": "gemini-1.5-pro",
    "n": None,
    "stream": False,
    "system_message": "keep the answer short give only insights based on percentages",
    "temperature": 0.1,
    "top_k": None,
    "top_p": None
  },
  "ChatOutput-gm65H": {
    "background_color": "",
    "chat_icon": "",
    "data_template": "{text}",
    "input_value": "",
    "sender": "Machine",
    "sender_name": "AI",
    "session_id": "",
    "should_store_message": True,
    "text_color": ""
  }
}

result = run_flow_from_json(flow="prototype.json",
                            session_id="", # provide a session id if you want to use session state
                            fallback_to_env_vars=True, # False by default
                            tweaks=TWEAKS)