import numpy as np
import torch
pd_, li, tf, npr = ns.get("pick_device"), ns.get("linear"), ns.get("to_float_tensor"), ns.get("n_params")
assert pd_ and li and tf and npr, "Keep pick_device, linear, to_float_tensor and n_params."
want = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
assert pd_() == want, f"pick_device() should be {want!r} on this computer."
x = torch.tensor([[1.0, 2.0, 3.0]]); W = torch.ones(2, 3); b = torch.tensor([0.5, -0.5])
assert torch.allclose(li(x, W, b), torch.tensor([[6.5, 5.5]])), "linear: x @ W.T + b."
lay = torch.nn.Linear(3, 2)
assert torch.allclose(li(x, lay.weight, lay.bias), lay(x)), "linear should match torch.nn.Linear."
t = tf(np.arange(3))
assert isinstance(t, torch.Tensor) and t.dtype == torch.float32, "to_float_tensor: a float32 tensor."
assert npr([(4, 3), (4,)]) == 16 and npr([(768, 768), (768,)]) == 590592, "n_params: multiply each shape, add them up."
