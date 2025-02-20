# The Overmind
#### _an experiment in abstract LLM control using the SPLY library_

## Table of Contents

- [Example usage](#example-usage)
- [Environment variables](#environment-variables)

## Example usage
```python
>>> import overmind
>>> n = overmind.node("n", "a primary node connected to the Overmind")
>>> jane = n.node("jane", "a lady named Jane, age 25.")
>>> jane["name"]
"Jane"
>>> n("infer the meaning of a 'realism' property (i.e. jane[\"realism\"]) and return it")
"Realism in this context refers to the degree to which Jane's characteristics and behaviors align with real-world human traits and experiences. It encompasses factors such as her emotional depth, cognitive abilities, and interactions within the environment. A higher realism value indicates that Jane exhibits more authentic and relatable human-like qualities."
>>> jane["realism"] = "very human-like"
>>> jane["IQ"] = "120.0"
>>> user = n.node("user", "a reference to myself, a man named John")
>>> jane["master"] = "user"
>>> jane("how are you feeling today?")
"Hello John! I'm doing well, thank you for asking. How about yourself?"
>>> sue = n.node("sue", "Sue - a copy of Jane with various personal properties randomly changed by up to 20%")
>>> sue["master"] = "user"
>>> g = n.node("g", "an uninitialized node group")
>>> g["members"] = ['jane', 'sue']
>>> room = n.node("room", "a large and luxurious living room")
>>> user["location"] = "room"
>>> g["location"] = "room"
>>> n("add some items to the living room that Jane and Sue would like")
>>> g("how do you like the room?")
```

## Environment variables
  * $overmind_model_id: ollama model to load
  * $overmind_seed: psuedo-random number generator seed for ollama
  * $overmind_temp: temperature setting for ollama
  * $overmind_num_ctx: context size for ollama
  * $overmind_show: if "True", show otherwise hidden generation for debugging

