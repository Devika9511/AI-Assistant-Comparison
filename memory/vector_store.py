memory_store = []

def store_memory(text):
    memory_store.append(text)

def retrieve_memory(query, k=3):
    return memory_store[-k:]