KINDS = {
    "predict a flat's rent from its size and district, using past listings": "supervised",
    "group songs into styles nobody has named yet": "unsupervised",
    "pretrain an LLM on web text": "self-supervised",
    "teach a robot arm to stack blocks by trial and error": "reinforcement",
    "label X-ray images as healthy or not, from doctor-labelled examples": "supervised",
}

for task, kind in KINDS.items():
    print(f"{kind or '?':16} {task}")
