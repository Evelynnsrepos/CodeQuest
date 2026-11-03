KINDS = {
    "predict a flat's rent from its size and district, using past listings": "",
    "group songs into styles nobody has named yet": "",
    "pretrain an LLM on web text": "",
    "teach a robot arm to stack blocks by trial and error": "",
    "label X-ray images as healthy or not, from doctor-labelled examples": "",
}

for task, kind in KINDS.items():
    print(f"{kind or '?':16} {task}")
