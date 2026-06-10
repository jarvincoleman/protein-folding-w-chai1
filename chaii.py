from pathlib import Path 
import torch 
from chai_lab.chai1 import run_inference

import inspect
from chai_lab.chai1 import run_inference
print(inspect.signature(run_inference))





Path("outputs").mkdir(exist_ok=True) 

candidates = run_inference(
    fasta_file = Path("input.fasta"), 
    output_dir = Path("outputs"),
    num_trunk_recycles=3,
    num_diffn_timesteps=200, 
    num_diffn_samples=1, 
    seed=42, 
    device = "cuda",
    use_esm_embeddings=True, 
)

print(candidates)

