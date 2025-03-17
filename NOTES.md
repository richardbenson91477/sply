# Notes

## Table of Contents

- [Using "sply_chat_interact.py"](#using-sply_chat_interactpy)
- [Tested models](#tested-models)
- [Dealing with incorrect output](#dealing-with-incorrect-output)
- [Misc](#misc)

## Using "sply_chat_interact.py"
  * Run "sply_chat_interact.py --help" for command line options and defaults
  * Enter "/h" at the input prompt ("> ") for help
  * Hit Ctrl-C to interrupt generation and enter input mode

## Tested models
  * qwen2.5-coder-14b-*-q*.gguf
    - base-line for testing
  * TODO: semi-automated test logs for various models (coming soon)

## Dealing with incorrect output
  * Try a different model - see the [tested models list](#tested-models)
  * Modify the prompt to show examples of expected behavior
  * Try a lower temperature value
  * Try an alternate seed number
  * Reuse a working model/prompt/seed combo
  * When all else fails, Ctrl-C + "edit_prompt()" are your friends

## Misc
  * The default prompt editor is "vim -b" - customize with the "editor=" options and parameters
  * "prompt_file=" args always have precedence over "prompt=" args
  * "edit_prompt" currently leaves prompt tempfiles intact (for manual review)
  * "make_prompt" is jailbroken - modify to taste, or provide a custom prompt

