from pathlib import Path

jobs_dir = Path(__file__).parent.parent / "jobs" / "todo"
jobs_dir.mkdir(exist_ok=True, parents=True)

template = """#!/bin/bash

module load opencv
source ~/scratch/.venvs/siren/bin/activate 

python experiment_scripts/train_sdf.py \\
    --model_type=hosc \\
    --point_cloud_path=data/stanford/xyzrgb_statuette.ply \\
    --batch_size=125000 \\
    --experiment_name=hosc_a={a}_b={b} \\
    --num_epochs=1000 \\
    --a {a} \\
    --b {b} 

python experiment_scripts/test_sdf.py \\
    --model_type=hosc \\
    --batch_size=125000 \\
    --experiment_name=hosc_a={a}_b={b} \\
    --a {a} \\
    --b {b} 
"""

a_values = [0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 25.0, 50.0]
b_values = [0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 25.0, 50.0]

for a in a_values:
    for b in b_values:
        script = template.format(a=a, b=b)

        job_file = jobs_dir / f"hosc_a={a}_b={b}.sh"
        with open(job_file, "w") as f:
            f.write(script)