# Notes

## Using "chat_interact.py"
  * run "./chat_interact.py --help" for command line options and defaults
  * enter "/?" for help
  * suffix input lines with a backslash to extend the input to multiple lines
  * hit Ctrl-C during generation to interrupt and return to input mode

## Dealing with gibberish output (in order of importance)
  * try a coding model - tested working with [qwen2.5-coder-14b-instruct-q8_0.gguf](https://huggingface.co/Qwen/Qwen2.5-Coder-14B-Instruct-GGUF/blob/main/qwen2.5-coder-14b-instruct-q8_0.gguf)
  * modify the prompt to show examples of proper behavior
  * try a lower temperature value
  * try an alternate seed number - restart with a new random seed, or specify a seed
  * reuse a model+prompt+seed combo that has worked in the past
  * when all else fails, Ctrl-C + edit_prompt are your friends

## Misc
  * the "prompt_file" args always have precedence over "prompt" args
  * "edit_prompt" currently leaves all prompt tempfiles intact (for later inspection)
  * the default "make_prompt" is jailbroken - modify to taste or provide a custom prompt
  * the default prompt editor is "vim" (change with the editor= option/parameters)

