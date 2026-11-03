def image_tokens(width, height, patch, merge):
    return 0


def splice(tokens, images, marker):
    return tokens


print("Qwen2-VL-style, 448×448:", image_tokens(448, 448, 14, 2), "tokens")
print("LLaVA-1.5-style, 336×336:", image_tokens(336, 336, 14, 1), "tokens")
prompt = ["<user>", "What", "is", "in", "<image>", "?", "</user>"]
cat_photo = ["img0", "img1", "img2", "img3"]
print(splice(prompt, [cat_photo], "<image>"))
