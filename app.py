import gradio as gr

# --- Selection Sort Function ---
def selection_sort_steps(arr):
    steps = ""
    n = len(arr)

    for i in range(n):
        min_index = i

        steps += f"\nStep {i+1}:\n"
        steps += f"Starting from index {i}, current list: {arr}\n"
        
        for j in range(i + 1, n):
            steps += f"Comparing {arr[j]} with current min {arr[min_index]}\n"
            if arr[j] < arr[min_index]:
                min_index = j
                steps += f"New minimum found: {arr[min_index]} at index {min_index}\n"

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            steps += f"Swapping {arr[min_index]} and {arr[i]}\n"
        else:
            steps += "No swap needed this round\n"

        steps += f"List after step {i+1}: {arr}\n"
    
    return arr, steps

# --- Function Gradio will call ---
def run_selection_sort(user_input):
    try:
        arr = [int(x.strip()) for x in user_input.split(",")]
    except:
        return "Error: Please enter numbers separated by commas."

    original = arr.copy()
    sorted_arr, steps = selection_sort_steps(arr)

    result = (
        f"Original List: {original}\n"
        f"Sorted List: {sorted_arr}\n\n"
        f"--- Selection Sort Steps ---\n"
        f"{steps}"
    )

    return result

# --- Gradio UI ---
demo = gr.Interface(
    fn=run_selection_sort,
    inputs=gr.Textbox(label="Enter numbers separated by commas (ex: 5, 2, 9, 1)"),
    outputs=gr.Textbox(label="Selection Sort Steps"),
    title="Selection Sort Visualizer",
    description="A simple step-by-step demonstration of Selection Sort."
)

if __name__ == "__main__":
    demo.launch()
