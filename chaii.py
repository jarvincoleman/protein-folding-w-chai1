from pathlib import Path 
import shutil 
import subprocess
subprocess.run(["pip", "install", "py3Dmol", "-q"], check=True)
import py3Dmol
from chai_lab.chai1 import run_inference





fasta_path = Path("/kaggle/working/protein-folding-w-chai1/input.fasta")


output_dir = Path("/kaggle/working/outputs")
if output_dir.exists():
    shutil.rmtree(output_dir)
output_dir.mkdir(exist_ok=True) 


candidates = run_inference(
    fasta_file = fasta_path, 
    output_dir = output_dir,
    num_trunk_recycles=3,
    num_diffn_timesteps=200, 
    num_diffn_samples=1, 
    seed=42, 
    device = "cuda",
    use_esm_embeddings=True, 
)


rna_seq = run_inference(
    fasta_file = fasta_path, 
    output_dir = output_dir,
)


cif_paths = candidates.cif_paths
cif_text = open(cif_paths[0]).read() 
agg_scores = [rd.aggregate_score.item() for rd in candidates.ranking_data]
print("CIF paths:", cif_paths) 
print("Scores:, ", agg_scores)

