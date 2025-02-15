# [SPLY - **S**imulated **P**ython **L**ink librar**Y**](https://github.com/richardbenson91477/sply)
#### _a bridge between real and simulated python interpreters_

## requirements
  * the [Ollama Python Library](https://pypi.org/project/ollama/) (https://pypi.org/project/ollama/)

## example usage
```python
>>> import sply
>>> sp = sply.sp(model_id="default-code") # create a simulated python interpreter
>>> y = 1
>>> sp.runcode(f"y = {y} + 1") # set y in simulated python to realish y + 1
''
>>> y = int(sp.runcode("y")) # set realish y's value to the simulated y's value
>>> y
2
>>> 
```

## chat_interact.py usage
  * run "./chat_interact.py --help" for command line options and defaults
  * enter /? for help
  * suffix input lines with a backslash to extend the input to multiple lines
  * hit Ctrl-C during generation to interrupt and return to input mode

## issues with gibberish
  * try a lower temperature value
  * try a coding model (tested working on qwen2.5-coder-14b-instruct-q8_0.gguf)
  * Ctrl-C is your friend!

## credits
an [richardbenson91477](https://www.deviantart.com/richardbenson91477) artistic expression

available under GPLv3: see [LICENSE](https://github.com/richardbenson91477/sply/blob/main/LICENSE)

