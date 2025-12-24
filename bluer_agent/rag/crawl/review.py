from bluer_agent.rag.crawl.collect import load_binary

results = load_binary("site_text.pkl.gz")
print(len(results), list(results.keys())[:3])
