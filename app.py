import gradio as gr
import numpy as np
from PIL import Image
import tensorflow as tf

# Load model
model = tf.keras.models.load_model("tomato_model.keras")

class_names = [
    "Tomato___Bacterial_spot",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold",
    "Tomato___Septoria_leaf_spot",
    "Tomato___Spider_mites Two-spotted_spider_mite",
    "Tomato___Target_Spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    "Tomato___Tomato_mosaic_virus",
    "Tomato___healthy",
]

# Disease information
disease_info = {
    "Tomato___Bacterial_spot": "Bacterial leaf spot causes dark, greasy spots on leaves. Manage with copper fungicides and remove infected leaves.",
    "Tomato___Early_blight": "Early blight appears as concentric rings on lower leaves. Improve air circulation and use fungicides.",
    "Tomato___Late_blight": "Late blight causes water-soaked spots that spread rapidly. Use preventive fungicides in humid conditions.",
    "Tomato___Leaf_Mold": "Leaf mold creates yellow spots with gray mold on undersides. Reduce humidity and improve ventilation.",
    "Tomato___Septoria_leaf_spot": "Small circular spots with dark borders. Remove infected leaves and use fungicides.",
    "Tomato___Spider_mites Two-spotted_spider_mite": "Spider mites cause stippled, yellowing leaves. Use miticides or insecticidal soap.",
    "Tomato___Target_Spot": "Concentric ring patterns on leaves. Use fungicides and ensure proper spacing.",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": "Viral infection causing leaf curling and yellowing. No cure; remove infected plants.",
    "Tomato___Tomato_mosaic_virus": "Mosaic patterns and stunted growth. Control through isolation and vector management.",
    "Tomato___healthy": "Your tomato plant appears healthy! Continue regular monitoring and maintenance.",
}

def predict(image):
    if image is None:
        return None, "Please upload an image first.", None
    
    img = image.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    pred = model.predict(img_array, verbose=0)
    
    # Get predictions as dictionary
    predictions = {class_names[i]: float(pred[0][i]) for i in range(len(class_names))}
    
    # Get top prediction
    top_disease = max(predictions, key=predictions.get)
    confidence = predictions[top_disease] * 100
    
    # Get disease info
    info = disease_info.get(top_disease, "Unknown disease")
    
    return predictions, f"**Detected Disease:** {top_disease.replace('Tomato___', '').replace('_', ' ')}\n\n**Confidence:** {confidence:.2f}%\n\n**Recommendation:** {info}", confidence

# Create custom CSS for better styling
css = """
.header {
    text-align: center;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 30px;
    border-radius: 15px;
    color: white;
    margin-bottom: 20px;
}
.info-box {
    background-color: #f0f4ff;
    border-left: 4px solid #667eea;
    padding: 15px;
    margin: 10px 0;
    border-radius: 5px;
}
"""

# Create the interface with Blocks for better customization
with gr.Blocks(css=css, theme=gr.themes.Soft()) as interface:
    gr.HTML("""
    <div class="header">
        <h1>🍅 Tomato Leaf Disease Prediction System</h1>
        <p>Advanced AI-powered disease detection for tomato plants</p>
    </div>
    """)
    
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("""
            ### How to Use
            1. **Upload** a clear image of a tomato leaf
            2. **Click** the predict button
            3. **View** the detailed analysis and recommendations
            
            ### Supported Diseases
            - Bacterial Spot
            - Early Blight
            - Late Blight
            - Leaf Mold
            - Septoria Leaf Spot
            - Spider Mites
            - Target Spot
            - Yellow Leaf Curl Virus
            - Tomato Mosaic Virus
            - Healthy Leaves
            """)
        
        with gr.Column(scale=1):
            image_input = gr.Image(
                label="📸 Upload Tomato Leaf Image",
                type="pil",
                sources=["upload", "webcam"]
            )
    
    predict_btn = gr.Button("🔍 Analyze Image", variant="primary", size="lg")
    
    with gr.Row():
        with gr.Column(scale=1):
            output_chart = gr.Label(label="📊 Prediction Confidence", num_top_classes=10)
        
        with gr.Column(scale=1):
            output_text = gr.Markdown(label="📋 Analysis & Recommendations")
    
    # Hidden component to pass confidence value
    confidence_value = gr.Number(visible=False)
    
    predict_btn.click(
        fn=predict,
        inputs=image_input,
        outputs=[output_chart, output_text, confidence_value]
    )
    
    gr.Markdown("""
    ---
    **Note:** This model achieves high accuracy but should be used as a tool to assist in diagnosis. Always consult agricultural experts for final decisions.
    """)

interface.launch(share=True)
