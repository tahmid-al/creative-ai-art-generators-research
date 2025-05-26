


# Creative AI Art Generators Research

A research project exploring and benchmarking generative AI art models, including Stable Diffusion and DALL-E. This repository contains app code, data scripts, analysis notebooks, and research documents for evaluating image generation models.

## Project Structure

```
creative-ai-art-generators-research/
├── app/                 # App source code
│   └── demo_app.py
├── data/                # Dataset scripts and raw data
├── images/              # Project images and visualizations
├── notebooks/           # Jupyter Notebooks for exploratory analysis and benchmarking
├── research/            # Research documents, literature reviews, and ethics discussions
├── diffusiondb_sample.csv  # Sample data
├── LICENSE
├── README.md
└── requirements.txt
```

## Installation

```bash
# Clone the repository
git clone https://github.com/tahmid-al/creative-ai-art-generators-research.git
cd creative-ai-art-generators-research

# Create and activate a Python environment (example: conda)
conda create -n aiart_env python=3.10
conda activate aiart_env

# Install required packages
pip install -r requirements.txt
```

## Example Usage

```python
from diffusers import StableDiffusionPipeline
import torch

device = "mps" if torch.backends.mps.is_available() else "cpu"
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
pipe = pipe.to(device)

prompt = "A futuristic city at sunset, concept art, vibrant colors"
image = pipe(prompt, height=256, width=256).images[0]
image.show()
```

## Notebooks

- `notebooks/artgen_api_benchmark.ipynb`: Benchmarking API image generation.
- `notebooks/exploratory_analysis.ipynb`: Data exploration and prompt analysis.

## Research

- `research/literature_review.md`
- `research/model_comparison.md`
- `research/ethics_discussion.md`

## License

This project is licensed under the MIT License.
