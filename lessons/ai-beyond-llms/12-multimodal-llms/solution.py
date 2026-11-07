def image_tokens(width, height, patch, merge):
    patches = (width // patch) * (height // patch)
    return patches // (merge * merge)


def splice(tokens, images, marker):
    out = []
    k = 0
    for t in tokens:
        if t == marker:
            for piece in images[k]:
                out.append(piece)
            k = k + 1
        else:
            out.append(t)
    return out


print("Qwen2-VL-style, 448×448:", image_tokens(448, 448, 14, 2), "tokens")
print("LLaVA-1.5-style, 336×336:", image_tokens(336, 336, 14, 1), "tokens")
prompt = ["<user>", "What", "is", "in", "<image>", "?", "</user>"]
cat_photo = ["img0", "img1", "img2", "img3"]
print(splice(prompt, [cat_photo], "<image>"))
