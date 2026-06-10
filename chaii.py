from pathlib import Path 
import shutil 
from chai_lab.chai1 import run_inference
import subprocess
import py3Dmol

fasta_path = Path("input.fasta")


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

cif_text = open("outputs/pred.model_idx_0_cif").read()

view = py3Dmol.view(width=800, height=600)
view.addModel(cif_text, "cif")
view.setStyle({"cartoon":{"color":"spectrum"}})
view.zoomTo() 
view.show()
cif_paths = candidates.cif_paths
agg_scores = [rd.aggregate_score.item() for rd in candidates.ranking_data]
print("CIF paths:", cif_paths) 
print("Scores:, ", agg_scores)



