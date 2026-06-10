from pathlib import Path 
import torch 
import shutil 
import inspect
from chai_lab.chai1 import run_inference


fasta_path = Path("input.fasta")

fasta_path.write_text()

output_dir = Path("/tmp/outputs")
if output_dir.exists():
    shutil.rmtree(output_dir)
output_dir.mkdir(exist_ok=True) 

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

cif_paths = candidates.cif_paths
agg_scores = [rd.aggregate_score.item() for rd in candidates.ranking_data]
print("CIF paths:", cif_paths) 
print("Scores:, ", agg_scores)



