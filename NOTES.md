# Notes

## Using "chat_interact.py"
  * run "./chat_interact.py --help" for command line options and defaults
  * enter "/?" for help
  * suffix input lines with a backslash to extend the input to multiple lines
  * hit Ctrl-C during generation to interrupt and return to input mode

## Dealing with gibberish
  * try a lower temperature value
  * try a coding model (tested working on qwen2.5-coder-14b-instruct-q8_0.gguf)
  * Ctrl-C + edit_prompt are your friends

## Misc
  * the "prompt_file" args always have precedence over "prompt" args
  * "edit_prompt" currently leaves all prompt tempfiles intact (for later inspection)
  * the default "make_prompt" is jailbroken - modify to taste or provide a custom prompt
  * the default prompt editor is "vim" (change with the editor= option/parameters)


