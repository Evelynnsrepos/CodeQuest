---
title: Checkpoint: why does a model forget?
xp: 60
---
# Checkpoint

This is the Module 1 checkpoint. It ties together tokens, the generation loop, the chat template and the context window. No new material: if a question stumps you, go back to that lesson before guessing.

**The question:** you've been chatting with a model in LM Studio for two hours. You ask about something you said at the very start, and it has no idea. Why?

## Your quest

Answer each question by setting the variable.

1. `sees_first_message`: Llama 3.1 8B is loaded with a context length of 8,192 tokens and a rolling-window overflow policy. Your chat is now 11,000 tokens long. Can the model see your first message? (`True` / `False`)
2. `why_it_forgets`: the main reason, as a letter:
   - `"a"` its weights slowly change during the chat and overwrite old information
   - `"b"` the earliest messages are no longer part of the input it is given
   - `"c"` its attention gets tired after many tokens
   - `"d"` it stores the chat in its memory, and old memories fade
3. `middle_fact`: a 100,000-token document fits in a long-context model's window, yet it misses a fact on page 40. Most likely reason, as a letter:
   - `"a"` the fact was dropped from the context
   - `"b"` models use long contexts unevenly and recall the middle worse
   - `"c"` the temperature was too low
4. `keep_instruction`: you need one rule to survive a very long chat. Where do you put it, as a letter?
   - `"a"` in the system prompt
   - `"b"` in your first message
   - `"c"` nowhere, raise the temperature instead
5. `dropped`: the context length is 4,096 tokens and the app reserves 512 of them for the reply. The system prompt is 400 tokens, followed by messages of 900, 700, 1,100, 600, 800 and 300 tokens. With a rolling window, how many messages get dropped? (A number. You may use code to work it out.)
6. `explanation`: in your own words, explain to a friend who has never heard of tokens why the model forgets. At least three sentences. Use the words *token* and *context*.

<details><summary>Open only after you pass: a model answer for question 6</summary>
The model has no memory between messages. Each time you send something, the app sends the whole conversation again, counted in tokens, which are the small pieces of text the model reads. The model can only read a fixed number of tokens at once, its context window, and the system prompt, the chat history, tool results and its own reply all have to fit in it. When the chat grows past that limit, the app drops the oldest messages so the rest fits, so the start of your chat is simply no longer in what the model is given. It can't remember what it never sees. And even within the window, very long contexts are used unevenly, so details in the middle can get missed.
</details>

## What's next

Module 2 is about running models on *your* machine: GGUF files, quantization, VRAM math for your 12 GB GPU, and LM Studio's local server.
