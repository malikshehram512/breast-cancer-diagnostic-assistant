import gradio as gr
import joblib
import numpy as np

# Load the model
# Make sure model.joblib is uploaded to your Space!
try:
    model = joblib.load('model.joblib')
except:
    model = None

def predict(radius, texture, perimeter, area, smoothness):
    if model is None:
        return "Model file not found. Please upload model.joblib"
    
    # Prepare input
    input_features = np.array([[radius, texture, perimeter, area, smoothness]])
    prediction = model.predict(input_features)[0]
    
    # 0 = Malignant, 1 = Benign (Standard for this dataset)
    label = "Benign (Non-Cancerous)" if prediction == 1 else "Malignant (Cancerous)"
    color = "#28a745" if prediction == 1 else "#dc3545"
    
    return f"""
    <div style="text-align: center; padding: 20px; border-radius: 10px; background-color: {color}; color: white;">
        <h2 style="margin: 0;">Result: {label}</h2>
    </div>
    """

# Professional UI Design
with gr.Blocks(theme=gr.themes.Soft(primary_hue="blue")) as demo:
    gr.Markdown(
        """
        # 🏥 Breast Cancer Diagnostic Assistant
        ### AI-Powered Screening Tool (Naive Bayes)
        Enter the clinical measurements below to get an instant diagnostic prediction.
        """
    )
    
    with gr.Row():
        with gr.Column():
            gr.Markdown("### Input Measurements")
            radius = gr.Slider(5, 30, value=14, label="Mean Radius")
            texture = gr.Slider(5, 40, value=19, label="Mean Texture")
            perimeter = gr.Slider(40, 200, value=91, label="Mean Perimeter")
            area = gr.Slider(100, 2500, value=650, label="Mean Area")
            smoothness = gr.Slider(0.05, 0.25, value=0.1, label="Mean Smoothness")
            btn = gr.Button("Run Diagnostic Analysis", variant="primary")
            
        with gr.Column():
            gr.Markdown("### Analysis Output")
            output = gr.HTML("<div style='text-align: center; padding: 40px; border: 2px dashed #ccc;'>Result will appear here...</div>")

    btn.click(predict, inputs=[radius, texture, perimeter, area, smoothness], outputs=output)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)