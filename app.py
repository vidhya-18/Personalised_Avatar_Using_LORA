import streamlit as st
from diffusers import StableDiffusionPipeline
from safetensors.torch import load_file
import torch
from PIL import Image
import os

import os
from huggingface_hub import login

hf_token = os.getenv("HF_TOKEN")
if hf_token:
    login(token=hf_token)

from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
# Paths
UNET_PATH = "lora_weights.safetensors"
TEXT_ENCODER_PATH = "lora_weights.text_encoder.safetensors"
MODEL_NAME = "runwayml/stable-diffusion-v1-5"
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Load the model
@st.cache_resource
def load_pipeline():
    st.write("⏳ Loading base model...")
    pipe = StableDiffusionPipeline.from_pretrained(
        MODEL_NAME,
        torch_dtype=torch.float16 if DEVICE == "cuda" else torch.float32,
        scheduler=DPMSolverMultistepScheduler.from_pretrained(MODEL_NAME, subfolder="scheduler")
    ).to(DEVICE)

    st.write("🔁 Loading LoRA weights...")
    pipe.load_lora_weights("vidhyavarshu/avatar-generator-weights", weight_name="lora_weights.safetensors")
    pipe.load_lora_weights("vidhyavarshu/avatar-generator-weights", weight_name="lora_weights.text_encoder.safetensors")

    st.write("✅ Pipeline loaded successfully.")
    return pipe

# Streamlit UI
st.title("🧙 AvatarCrafter")
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("Bring your imagination to life! Upload an image and enter a prompt to craft your personalized AI avatar.")


uploaded_file = st.file_uploader("Upload a reference image", type=["jpg", "jpeg", "png"])
st.markdown("<br>", unsafe_allow_html=True)
prompt = st.text_input("Enter your prompt", value="a photo of ktn wearing a space suit")


GUIDANCE = 7.5  # Fixed for optimal results

if st.button("Generate Avatar") and prompt:
    with st.spinner("Generating avatar..."):
        pipe = load_pipeline()
        image = pipe(prompt, num_inference_steps=30, guidance_scale=GUIDANCE).images[0]
        image.save("generated_avatar.png")
        st.image(image, caption="🎨 Generated Avatar")
        with open(image_path, "rb") as f:
            st.download_button("📥 Download Avatar", f, "avatar.png", "image/png")
