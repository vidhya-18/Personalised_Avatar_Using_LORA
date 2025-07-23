# 🧙‍♀️ AvatarCrafter – Personalized AI Avatar Generator

## 📌 Overview
**AvatarCrafter** is a Streamlit-based AI application that allows users to generate personalized avatars by combining a reference prompt with fine-tuned **LoRA weights** on top of the **Stable Diffusion v1.5** model.

---

## ⚙️ Features

- 🧠 **LoRA weights support** (lightweight fine-tuning over Stable Diffusion)
- ⚡ **Fast inference** using `Diffusers` + `DPMSolverMultistepScheduler`
- 🚀 **GPU acceleration** via `torch.cuda`
- 🔐 **Hugging Face Hub token** integration
- 🔁 **Modular code** with caching for efficient usage
- 🎛️ **Prompt-based avatar customization**
- 📥 **Download button** to save generated avatars
- 🖼️ *(Optional)* Image upload for future enhancement

---

## 🛠️ Tech Stack

- 🧩 [Stable Diffusion v1.5](https://huggingface.co/runwayml/stable-diffusion-v1-5)
- 🪄 LoRA fine-tuning
- 📦 [Hugging Face Hub](https://huggingface.co/vidhyavarshu/avatar-generator-weights)
- 🔗 `diffusers`, `transformers`, `safetensors`
- 📊 Streamlit for interactive frontend
- ☁️ Colab for deployment and notebook execution

---

## 🚶‍♀️ How to Use

This project uses **two Google Colab notebooks** to simplify setup and execution.

### 1️⃣ Upload LoRA Weights to Hugging Face

📓 Notebook: [LoRA Weights Upload](https://colab.research.google.com/drive/1BBSEhp_DChyPXtqADEecFSF7vRjVUpUy)

#### Steps:
1. Open the Colab notebook.
2. Click `Runtime > Run all`.
3. Enter your **Hugging Face token** when prompted.
4. The notebook uploads:
   - `lora_weights.safetensors` (U-Net)
   - *(Optional)* `lora_weights.text_encoder.safetensors`

Weights will be saved in your Hugging Face repo:  
➡️ `vidhyavarshu/avatar-generator-weights`

---

### 2️⃣ Run the Avatar Generator (Streamlit)

📓 Notebook: [Avatar Generator with Streamlit](https://colab.research.google.com/drive/1sewMBrkAmLzR2RKIcLEkZYJ0Nu-ox6TV?usp=sharing)

#### Steps:
1. Open the Colab notebook.
2. Click `Runtime > Run all`.
3. Paste your Hugging Face token when asked.
4. A **public Streamlit URL** will appear. Click to launch the app.

#### In the Streamlit App:
- Enter a prompt like:  
  `"a photo of KTN in a pilot uniform"`
- Click **Generate Avatar**
- Wait for the image to render
- Click **Download Avatar** to save it
