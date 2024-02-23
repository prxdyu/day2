import os 
from pathlib import Path

list_of_files=[".github/workflow/.gitkeep",
               "src/__init__.py",
               "src/components/__init__.py",
               "src/componens/data_ingestion.py",
               "src/components/data_transformation.py",
               "src/components/model_training.py",
               "src/components/model_evaluation.py",
               "src/pipeline/__init__.py",
               "src/pipeline/training_pipeline.py",
               "src/pipeline/prediction_pipeline.py",
               "src/utils/utils.py",
               "src/logger/logging.py",
               "src/exception/exception.py"
               "tests/unit/__init.py",
               "teest/intergration/__init__.py",
               "init_setup.sh",
               "requirements.txt",
               "requirements_dev.txt",
               "setup.py",
               "setup.config",
               "pyproject.toml",
               "tox.ini",
               "experiment/experiment.ipynb"]

# Iterate over the list and create the directories and files
for file_path in list_of_files:
    # Use Path to create directories if they don't exist
    directory = os.path.dirname(file_path)
    if directory:
        Path(directory).mkdir(parents=True, exist_ok=True)
    # Create the file
    open(file_path, 'a').close()