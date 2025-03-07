# Notes

## Using "sply_chat_interact.py"
  * Run "sply_chat_interact.py --help" for command line options and defaults
  * Enter "/h" for help
  * Hit Ctrl-C to interrupt generation and enter input mode

## Tested working models
  * [qwen2.5-coder-14b-instruct-q8_0.gguf](https://huggingface.co/Qwen/Qwen2.5-Coder-14B-Instruct-GGUF/blob/main/qwen2.5-coder-14b-instruct-q8_0.gguf)
    - Base-line for testing

## Mostly-working models
  * [phi-4-abliterated.Q8_0.gguf](https://huggingface.co/mradermacher/phi-4-abliterated-GGUF/blob/main/phi-4-abliterated.Q8_0.gguf)
    - Occasionally generates high-strangeness like multiple string results ('this''that'), markdown block-quotes, or comments
  * [Qwen2.5-Coder-7B-Instruct-abliterated-Q8_0.gguf](https://huggingface.co/bartowski/Qwen2.5-Coder-7B-Instruct-abliterated-GGUF/blob/main/Qwen2.5-Coder-7B-Instruct-abliterated-Q8_0.gguf)
    - fails [sp_pow.py](examples/sp_pow.py)
  * [ibm-granite_granite-3.2-8b-instruct-Q8_0.gguf](https://huggingface.co/bartowski/ibm-granite_granite-3.2-8b-instruct-GGUF/blob/main/ibm-granite_granite-3.2-8b-instruct-Q8_0.gguf)
    - fails [sp_pow.py](examples/sp_pow.py)
  * [c4ai-command-r7b-12-2024-Q8_0.gguf](https://huggingface.co/bartowski/c4ai-command-r7b-12-2024-GGUF/blob/main/c4ai-command-r7b-12-2024-Q8_0.gguf)
    - fails [sp_pow.py](examples/sp_pow.py)
  * [arcee-ai_Arcee-Blitz-IQ4_NL.gguf](https://huggingface.co/bartowski/arcee-ai_Arcee-Blitz-GGUF/blob/main/arcee-ai_Arcee-Blitz-IQ4_NL.gguf)
    - fails [sp_pow.py](examples/sp_pow.py)
  * [Captain-Eris-Diogenes_Twilight-V0.420-12B-Q6_K_L.gguf](https://huggingface.co/bartowski/Captain-Eris-Diogenes_Twilight-V0.420-12B-GGUF/blob/main/Captain-Eris-Diogenes_Twilight-V0.420-12B-Q6_K_L.gguf)
    - fails [sp_pow.py](examples/sp_pow.py)
  * [huihui-ai_Mistral-Small-24B-Instruct-2501-abliterated-IQ4_XS.gguf](https://huggingface.co/bartowski/huihui-ai_Mistral-Small-24B-Instruct-2501-abliterated-GGUF/blob/main/huihui-ai_Mistral-Small-24B-Instruct-2501-abliterated-IQ4_XS.gguf)
    - fails [sp_pow.py](examples/sp_pow.py)

## Non-working models
  * [Mistral-Small-24B-Instruct-2501-Q5_K_M.gguf](https://huggingface.co/bartowski/Mistral-Small-24B-Instruct-2501-GGUF/blob/main/Mistral-Small-24B-Instruct-2501-Q5_K_M.gguf)
    - Generates _a lot_ of simulated python errors
  * [qihoo360_TinyR1-32B-Preview-v0.1-Q6_K.gguf](https://huggingface.co/bartowski/qihoo360_TinyR1-32B-Preview-v0.1-GGUF/blob/main/qihoo360_TinyR1-32B-Preview-v0.1-Q6_K.gguf)
    - Generates _a lot_ of simulated python errors

## Dealing with gibberish output
  * Try a different model - see the [tested working models list](#tested-working-models). Note that "chain of thought reasoning" models aren't well suited as they generate a lot of extraneous output
  * Modify the prompt to show examples of expected behavior
  * Try a lower temperature value
  * Try an alternate seed number
  * Reuse a model/prompt/seed combo that has worked in the past
  * When all else fails, Ctrl-C + "edit_prompt()" are your friends

## Misc
  * The default prompt editor is "vim -b" - customize with the "editor=" options and parameters
  * "prompt_file=" args always have precedence over "prompt=" args
  * "edit_prompt" currently leaves prompt tempfiles intact (for manual review)
  * "make_prompt" is jailbroken - modify to taste, or provide a custom prompt
  * sp passes some alternate default params to chat - see [sply/sp.py](sply/sp.py)

