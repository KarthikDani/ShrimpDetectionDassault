import os
import subprocess

# Define the path to your .ipynb file
notebook_path = "/Users/karthik/Desktop/Others/Other 1/ShrimpDetection/test_fish_yolo_model.ipynb"
base_filename = os.path.basename(notebook_path).split(".")[0]
markdown_path = os.path.join(os.path.dirname(notebook_path), base_filename + ".md")
pdf_output_path = os.path.join(os.path.dirname(notebook_path), base_filename + ".pdf")

metadata = {
    "title": "Visualizing YOLOv8 Fish Detection Results and Creating Annotated Videos",
    "author": "Karthik M Dani",
    "date": "2024-08-23",
    # "abstract": "This report presents a comprehensive analysis of carbon yield dynamics in Escherichia coli using metabolic modeling techniques. The production envelope of oxygen uptake rate versus carbon yield maximum for D-glucose exchange is analyzed and visualized using Python-based libraries such as COBRApy, seaborn, and sympy. The quadratic model fitting of the production data is performed to understand the underlying kinetics. Furthermore, the Laplace transform of the fitted quadratic model is computed, and a Bode plot is generated to visualize the frequency response of the system. This study highlights the integration of metabolic modeling with control theory to gain insights into the metabolic behavior of E. coli under varying oxygen uptake conditions.",
    #"subtitle": "Process of constructing CSMs for epithelial and mesenchymal states with GSMM package using iMAT algorithm.",
    #"keywords": "Genome Scale Metabolic Modeling",
    #"thanks": "*",
    "email": "karthik.ml22@bmsce.ac.in",
    "institute": "BMS College of Engineering, Bangalore"
}

# try:
#     subprocess.run(['jupyter', 'nbconvert', '--to', 'markdown', #'--TagRemovePreprocessor.enabled=True', '--TagRemovePreprocessor.remove_cell_tags="exclude-output', 
#                     notebook_path], check=True)
#     print(f"Converted notebook to Markdown: {markdown_path}")
    
# except subprocess.CalledProcessError as e:
#     print(f"Error during Markdown conversion: {e}")
#     exit(1)

pandoc_command = ["pandoc", notebook_path, "-o", pdf_output_path]

for key, value in metadata.items():
    pandoc_command.append(f"--metadata={key}={value}")

# Convert the Markdown file to PDF using pandoc
try:
    subprocess.run(pandoc_command, check=True)
    print(f"Successfully converted Markdown to PDF: {pdf_output_path}")
except subprocess.CalledProcessError as e:
    print(f"Error during PDF conversion: {e}")
    print(f"Error during PDF conversion: {e}")

# Clean up intermediate files if needed
# os.remove(markdown_path)
