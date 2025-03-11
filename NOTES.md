# Notes

## Table of Contents

- [Using "sply_chat_interact.py"](#using-sply_chat_interactpy)
- [Tested working models](#tested-working-models)
- [Mostly-working models](#mostly-working-models)
- [Non-working models](#non-working-models)
- [On reasoning models](#on-reasoning-models)
- [Dealing with incorrect output](#dealing-with-incorrect-output)
- [Misc](#misc)

## Using "sply_chat_interact.py"
  * Run "sply_chat_interact.py --help" for command line options and defaults
  * Enter "/h" for help
  * Hit Ctrl-C to interrupt generation and enter input mode

## Tested working models
  * [qwen2.5-coder-14b-instruct-q8_0.gguf](https://huggingface.co/Qwen/Qwen2.5-Coder-14B-Instruct-GGUF/blob/main/qwen2.5-coder-14b-instruct-q8_0.gguf)
    - Base-line for testing
  * [Qwen2.5-Coder-14B-IQ4_XS.gguf](https://huggingface.co/bartowski/Qwen2.5-Coder-14B-GGUF/blob/main/Qwen2.5-Coder-14B-IQ4_XS.gguf)
  * [QwQ-Snowdrop.i1-IQ3_XXS.gguf](https://huggingface.co/mradermacher/QwQ-Snowdrop-i1-GGUF/blob/main/QwQ-Snowdrop.i1-IQ3_XXS.gguf)

## Mostly-working models
  * [phi-4-abliterated.Q8_0.gguf](https://huggingface.co/mradermacher/phi-4-abliterated-GGUF/blob/main/phi-4-abliterated.Q8_0.gguf)
    - Occasionally generates stray comments, markdown, and so on
  * [Qwen2.5-Coder-7B-Instruct-abliterated-Q8_0.gguf](https://huggingface.co/bartowski/Qwen2.5-Coder-7B-Instruct-abliterated-GGUF/blob/main/Qwen2.5-Coder-7B-Instruct-abliterated-Q8_0.gguf)
    - fails [sp_pow.py](examples/sp_pow.py)
  * [ibm-granite_granite-3.2-8b-instruct-Q8_0.gguf](https://huggingface.co/bartowski/ibm-granite_granite-3.2-8b-instruct-GGUF/blob/main/ibm-granite_granite-3.2-8b-instruct-Q8_0.gguf)
    - fails [sp_pow.py](examples/sp_pow.py)
  * [c4ai-command-r7b-12-2024-Q8_0.gguf](https://huggingface.co/bartowski/c4ai-command-r7b-12-2024-GGUF/blob/main/c4ai-command-r7b-12-2024-Q8_0.gguf)
    - fails [sp_pow.py](examples/sp_pow.py)
  * [arcee-ai_Arcee-Blitz-IQ4_NL.gguf](https://huggingface.co/bartowski/arcee-ai_Arcee-Blitz-GGUF/blob/main/arcee-ai_Arcee-Blitz-IQ4_NL.gguf)
    - fails [sp_pow.py](examples/sp_pow.py)
  * [huihui-ai_Mistral-Small-24B-Instruct-2501-abliterated-IQ4_XS.gguf](https://huggingface.co/bartowski/huihui-ai_Mistral-Small-24B-Instruct-2501-abliterated-GGUF/blob/main/huihui-ai_Mistral-Small-24B-Instruct-2501-abliterated-IQ4_XS.gguf)
    - fails [sp_pow.py](examples/sp_pow.py)

## Non-working models
  * [Mistral-Small-24B-Instruct-2501-Q5_K_M.gguf](https://huggingface.co/bartowski/Mistral-Small-24B-Instruct-2501-GGUF/blob/main/Mistral-Small-24B-Instruct-2501-Q5_K_M.gguf)
    - Generates _a lot_ of simulated python errors

## On reasoning models
  * "Reasoning" models aren't _currently_ well suited, _if_ they insist on generating extraneous "thinking" output. That being said, models such as _DeepSeek-R1-Distill-Qwen-1.5B_, even at it's miniscule size, can solve [sp_pow.py](examples/sp_pow.py) correctly after some "thinking out loud" examination. I'm currently experimenting with optionally supporting \<think\> tags "behind the scenes." using models which stay "in bounds" after special prompting.

## Dealing with incorrect output
  * Try a different model - see the [tested working models list](#tested-working-models)
  * Modify the prompt to show examples of expected behavior
  * Try a lower temperature value
  * Try an alternate seed number
  * Reuse a model/prompt/seed combo that has worked in the past
  * When all else fails, Ctrl-C + "edit_prompt()" are your friends

## Misc
  * The model lists are very subject to change, as the model results can be unpredicatable with code changes!
  * The default prompt editor is "vim -b" - customize with the "editor=" options and parameters
  * "prompt_file=" args always have precedence over "prompt=" args
  * "edit_prompt" currently leaves prompt tempfiles intact (for manual review)
  * "make_prompt" is jailbroken - modify to taste, or provide a custom prompt
  * sp passes some alternate default params to chat - see [sply/sp.py](sply/sp.py)

