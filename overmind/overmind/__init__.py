
import sply

model_id = "default-code"
options = {
    "seed": random.randint(0, 2 << 32),
    "temperature": 0.0,
    "num_ctx": 1_000,
    }

sp = sply.sp(model_id=model_id, options=options)

from .node import node
node.sp = sp

