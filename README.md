# Audio2art-Future-Forge-
Audio2Art: Convert Voice Prompts into High-Quality Photorealistic Images

Description

Audio2Art is an innovative AI project that converts voice prompts into photorealistic images. By combining Whisper for automatic speech recognition (ASR) and Stable Diffusion for image generation, Audio2Art allows users to simply speak a prompt and receive a high-resolution, realistic image.

Features

Voice-to-Text (STT): Transcribes spoken words into text using Whisper.

Photorealistic Image Generation: Uses Stable Diffusion to generate high-quality images based on voice prompts.

Optimized for Performance: Utilizes techniques such as attention slicing and CPU offloading to optimize VRAM usage and speed up generation.

Gradio Interface: Provides a simple, easy-to-use interface for users to interact with the AI.



---

How It Works

1. Speech-to-Text: The user speaks a prompt (e.g., "a sunset over the ocean"). The audio is transcribed into text using the Whisper Tiny model.


2. Image Generation: The transcribed text is passed to the Stable Diffusion model, which generates a corresponding photorealistic image.


3. Gradio Interface: A Gradio UI allows users to upload audio or speak directly into the microphone, triggering the image generation process.




---

Installation & Requirements

To run Audio2Art, you'll need to install the following dependencies:

Python 3.7+

PyTorch (with CUDA support for GPU acceleration)

Hugging Face Transformers

Diffusers

Gradio


Install Dependencies

You can install the required libraries by running the following command:

pip install torch torchvision gradio transformers diffusers

Ensure you have CUDA installed if you're using GPU for faster processing. If you're on CPU, the system will automatically adjust.


---

How to Run

Step 1: Clone the Repository

Clone the repository containing the code:

git clone https://github.com/your-username/Audio2Art.git
cd Audio2Art

Step 2: Install the Dependencies

After cloning, install all the required Python packages:

pip install -r requirements.txt

Step 3: Run the Script

Run the app.py script:

python app.py

Step 4: Use the Gradio Interface

Once the script is running, the Gradio interface will open. You can speak a prompt directly into the microphone, or upload an audio file for transcription. The AI will generate an image based on your voice prompt.


---

Example Usage

Input: "A beautiful sunset over the ocean with a calm beach."

Output: A high-quality, photorealistic image of a sunset over the ocean.



---

Optimizations

This version of the project comes with several optimizations for faster image generation:

VRAM Optimization: Uses techniques like attention slicing, model CPU offload, and vae slicing to minimize VRAM usage.

Higher Resolution: Generates images at a resolution of 768x768 for better detail.



---

Future Improvements

Real-time Voice Processing: Optimizing the system to generate images instantly after voice input.

Increased Image Quality: Experiment with even higher resolutions or more inference steps for greater detail.

Customization: Allow users to customize certain aspects of the image (e.g., color palette, lighting, etc.
