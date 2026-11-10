---
title: Checkpoint: why does a model forget?
minutes: 30
xp: 60
hint: Question 1: 11,000 tokens is more than 8,192, so the oldest messages were dropped. Can it see the first one?
hint: Question 5: the window for the input is 4,096 - 512 = 3,584 tokens. Add up the system prompt and messages, and drop from the oldest until it fits.
hint: Question 6: the text goes between the three quotes, on its own lines. Write at least three sentences with the words token and context.
---
# Checkpoint

⏱️ About 30 minutes

This is the Module 1 checkpoint. It ties together tokens, the generation loop, the chat template and the context window. No new material: if a question stumps you, go back to that lesson before guessing.

**The question:** you've been chatting with a model in LM Studio for two hours. You ask about something you said at the very start, and it has no idea. Why?

## 🐍 How to answer

Each answer is one line in the editor: the name, `=`, then your answer.

| Kind of answer | Write it like | Notes |
|---|---|---|
| yes / no | `sees_first_message = False` | `True` or `False`, no quotes |
| a letter | `why_it_forgets = "b"` | the letter **in quotes** |
| a number | `dropped = 3` | no quotes |
| a longer text | between the `"""` and `"""` | three quotes start and end a text that can have many lines |

### 👀 Worked example for question 5 (other numbers)

The context length is 2,000 tokens and 500 are reserved for the reply. The system prompt is 300 tokens, followed by messages of 600, 400, 700 and 200.

1. Room for the input: 2,000 − 500 = **1,500** tokens.
2. Everything now: 300 + 600 + 400 + 700 + 200 = **2,200**. Too much.
3. Drop the oldest message (not the system prompt!): 2,200 − 600 = **1,600**. Still more than 1,500.
4. Drop the next oldest: 1,600 − 400 = **1,200**. Fits.
5. Two messages were dropped, so the answer would be `2`.

Do the same with the numbers in question 5. Or use your `rolling_window` from lesson 13: copy it into the editor and print `len(chat) - len(rolling_window(chat, 4096 - 512))`.

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
