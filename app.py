import torch
import gradio as gr
from transformers import pipeline
from diffusers import StableDiffusionPipeline

# Load Whisper Tiny (Fast Speech-to-Text)
stt_pipeline = pipeline("automatic-speech-recognition", model="openai/whisper-tiny")

# Load a high-quality photorealistic model
model_id = "dreamlike-art/dreamlike-photoreal-2.0"
image_pipeline = StableDiffusionPipeline.from_pretrained(
    model_id, 
    torch_dtype=torch.float16  # Faster inference
)

# Optimize VRAM usage
image_pipeline.to("cuda" if torch.cuda.is_available() else "cpu")
image_pipeline.enable_attention_slicing()
image_pipeline.enable_vae_slicing()
image_pipeline.enable_model_cpu_offload()

def audio_to_image(audio_file):
    """Convert voice input to text and generate a high-quality realistic image."""
    transcription = stt_pipeline(audio_file)["text"]
    print("Transcription:", transcription)  # Debugging: Check if STT is working

    if not transcription.strip():
        return "No valid text detected. Try speaking more clearly."

    # Generate a high-quality photorealistic image
    image = image_pipeline(
        prompt=transcription, 
        width=768, height=768,  # Increase resolution for realism
        num_inference_steps=25,  # More steps = better quality
        guidance_scale=7.5  # Improves prompt adherence
    ).images[0]

    return image

# Gradio UI
app = gr.Interface(
    fn=audio_to_image,
    inputs=gr.Audio(type="filepath"),
    outputs=gr.Image(),
    title="Realistic Audio2Art",
    description="Speak a prompt and get a high-quality, photorealistic AI-generated image!"
)

app.launch()