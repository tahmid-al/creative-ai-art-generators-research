import csv
from datasets import load_dataset

ds = load_dataset('poloclub/diffusiondb', split='train[:1000]')

with open('diffusiondb_sample.csv', 'w', newline='') as csvfile:
    fieldnames = [
        'prompt', 'seed', 'step', 'cfg', 'sampler', 
        'width', 'height', 'user_name', 'timestamp', 
        'image_nsfw', 'prompt_nsfw'
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for item in ds:
        writer.writerow({
            'prompt': item['prompt'],
            'seed': item['seed'],
            'step': item['step'],
            'cfg': item['cfg'],
            'sampler': item['sampler'],
            'width': item['width'],
            'height': item['height'],
            'user_name': item['user_name'],
            'timestamp': item['timestamp'],
            'image_nsfw': item['image_nsfw'],
            'prompt_nsfw': item['prompt_nsfw'],
        })