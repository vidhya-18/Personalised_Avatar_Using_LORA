🧙‍♀️ AvatarCrafter – Personalized AI Avatar Generator
📌 Overview
AvatarCrafter is a Streamlit-based AI application that allows users to generate personalized avatars by combining a reference prompt with fine-tuned LoRA weights over the Stable Diffusion v1.5 model.

🖼️ Upload an image (optional for future enhancement)

📝 Enter a prompt like “a photo of KTN wearing a space suit”

🪄 Generate stunning AI avatars in seconds

☁️ Weights hosted via Hugging Face (vidhyavarshu/avatar-generator-weights)

🔧 Model loaded in Colab, deployed using Streamlit

🚀 Features
🔄 LoRA weights support (compressed fine-tuning over base SD model)

🖥️ GPU acceleration via torch.cuda

🌐 Hugging Face Hub token integration

🧠 Diffusers pipeline + DPMSolverMultistepScheduler for fast inference

🧱 Modular code with caching for efficient resource usage

📥 Avatar download button after generation


🧪 How to Run the Colab Notebooks
Your project uses two Colab notebooks:

📦 LoRA Weights Upload Notebook

🎨 Avatar Generator with Streamlit

✅ Step-by-Step Instructions
🔹 STEP 1: Upload LoRA Weights to Hugging Face
📓 Notebook: LoRA Weights Upload

▶️ What it does:
Uploads your fine-tuned .safetensors files to the Hugging Face Hub under your model repo:
vidhyavarshu/avatar-generator-weights

🛠️ How to run:
Open the notebook

Click Runtime > Run all

When prompted, paste your Hugging Face token

You can get it from: https://huggingface.co/settings/tokens

This will upload:

lora_weights.safetensors (for U-Net)

(Optional) lora_weights.text_encoder.safetensors (if available)

🔹 STEP 2: Generate Avatars using Streamlit + LoRA
📓 Notebook: Avatar Generator with Streamlit

▶️ What it does:
Launches a Streamlit UI, loads LoRA weights from Hugging Face, and generates avatars from text prompts.

🛠️ How to run:
Open the notebook

Click Runtime > Run all

When prompted, enter your Hugging Face token

After all cells run, at the bottom you will see a public Streamlit URL like:

Running on public URL: https://<random-id>-<colab-name>.streamlit.app
Click the URL to open the app in a new tab

In the app:
Enter a text prompt like:
a photo of ktn in a pilot uniform

Click Generate Avatar

Wait for image generation (~20–30 sec)

Click Download Avatar to save the image
