import gradio as gr
import pandas as pd
import numpy as np
from statistics import mode, median, mean

# Load dataset
try:
    data = pd.read_csv("dataset.csv")
except FileNotFoundError:
    raise Exception("Dataset file 'dataset.csv' not found. Please provide a valid file.")
except pd.errors.EmptyDataError:
    raise Exception("Dataset file is empty. Please provide a dataset with data.")

# Column operations function
def column_operations(column, operation):
    try:
        col_data = data[column]
        if not pd.api.types.is_numeric_dtype(col_data):
            return f"Error: Column '{column}' does not contain numeric data."
        
        if operation == "Mean":
            result = mean(col_data)
        elif operation == "Standard Deviation":
            result = np.std(col_data)
        elif operation == "Variance":
            result = np.var(col_data)
        elif operation == "Mode":
            result = mode(col_data)
        elif operation == "Median":
            result = median(col_data)
        elif operation == "Range":
            result = max(col_data) - min(col_data)
        elif operation == "Maximum":
            result = max(col_data)
        elif operation == "Minimum":
            result = min(col_data)
        else:
            return "Invalid operation selected."
        
        return f"The {operation.lower()} of column '{column}' is: {result}"
    except Exception as e:
        return f"Error: {str(e)}"

# Gradio interface
with gr.Blocks() as demo:
    # Section 1: Column Operations
    gr.Markdown("### Column Operations")
    with gr.Row():
        column_dropdown = gr.Dropdown(choices=data.columns.tolist(), label="Select Column")
        column_operation_input = gr.Radio(
            ["Mean", "Standard Deviation", "Variance", "Mode", "Median", "Range", "Maximum", "Minimum"], 
            label="Operation"
        )
    column_result_output = gr.Textbox(label="Result")
    column_calculate_button = gr.Button("Calculate Column Operation")

    # Link Functions to Buttons
    column_calculate_button.click(column_operations, 
                                  inputs=[column_dropdown, column_operation_input], 
                                  outputs=column_result_output)

# Launch the Gradio app
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=6080)
