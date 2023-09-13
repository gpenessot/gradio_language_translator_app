import gradio as gr
from transformers import pipeline

# Load the translation pipeline from Hugging Face Transformers
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en")

# Define the translation function
def translate_text(text: str) -> str:
    """Translate text from French to English

    Args:
        text (str): french text input

    Returns:
        str: english text output
    """
    try:
        # Translate text from French to English
        translation_result = translator(text, 
                                        src_lang="fr", 
                                        tgt_lang="en")
        translated_text = translation_result[0]['translation_text']
        return translated_text
    except Exception as e:
        # Print the error for debugging
        print(f"Translation Error: {str(e)}")
        return "Translation Error"

# Create a "simple" Gradio interface
interface = gr.Interface(
    fn=translate_text,
    inputs=gr.Textbox("text", label="Enter text in French"),
    outputs='text',#gr.Textbox("text", label="Translated text in English"),
    #live=True,
    title="Language Translator",
    description="Translate French text to English using Hugging Face Transformers.",
)

# Launch the Gradio interface
interface.launch()
