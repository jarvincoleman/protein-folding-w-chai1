import py3Dmol 
from chai_lab.chai1 import run_inference 
from chaii.py import fasta_path, rna_seq




class DrugInference:
    def __init__(self, abrv_name, id, rna_type):
        self.abrv_name = abrv_name
        self.id = id 
        self.rna_type = rna_type


        for id in input.fasta: 
            if fasta_path[id]: 
                print(id, abrv_name)
        

        rna_type = rna_seq[fasta_path]

        
        


    def classify(self, id):

        pass

    def match(self):
        pass