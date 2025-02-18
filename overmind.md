# The Overmind
#### _an experiment in abstract LLM control using the SPLY library_

## Table of Contents

- [Example usage](#example-usage)
- [Environment variables](#environment-variables)

## Example usage
```python
>>> import overmind
>>> n = overmind.node("n", "a primary node connected to the Overmind")
>>> jane = n.node("jane", "an intelligent being named Jane, female gender, age 25.")
>>> jane["name"]
"'Jane'"
>>> n("infer the meaning of a 'realism' property of the jane object and describe it to me")
"'Realism is a property that indicates how closely Jane\'s characteristics align with real-world human traits.'"
>>> jane["realism"] = "very high"
>>> jane["IQ"] = "120.0"
>>> user = n.node("user", "a reference to myself, a man named John")
>>> jane["master"] = "user"
>>> jane("how are you feeling today?")
"'Jane: I\'m feeilng great, John!'"
>>> sue = n.node("sue", "Sue - a copy of Jane with various personal properties randomly changed by up to 20%")
>>> sue["master"] = "user"
>>> g = n.node("g", "an empty group that I can communicate with")
>>> g["members"] = ["jane", "sue"]
>>> room = n.node("room", "a large and luxurious living room")
>>> user["location"] = "room"
>>> g["location"] = "room"
>>> n("add some items to the living room that Jane and Sue would like")
"'OK'"
>>> g("how do you like the room?")
```

## Environment variables
  * $overmind_model_id: ollama model to load
  * $overmind_seed: psuedo-random number generator seed for ollama
  * $overmind_temp: temperature setting for ollama
  * $overmind_num_ctx: context size for ollama
  * $overmind_show: if "True", show otherwise hidden generation for debugging

