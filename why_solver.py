# The Why Theory AI Tool

def why_theory_solver(problem_input):
    # Step 1: Categorize Problem
    category = categorize_problem(problem_input)
    
    # Step 2: Initialize Why Layers
    why_layers = []
    current_reason = analyze_problem(problem_input)
    
    # Step 3: Loop through "Why?" layering
    for i in range(5):  # configurable depth
        why_layers.append(current_reason)
        
        if is_root_cause(current_reason):
            break
        else:
            current_reason = ask_why(current_reason)
    
    # Step 4: Decision Branch
    if is_controllable(current_reason):
        output_type = "Solution"
        output_message = generate_solution(current_reason)
    else:
        output_type = "Reason"
        output_message = f"This happens because {current_reason}"
    
    # Step 5: Format Output
    return {
        "Problem": problem_input,
        "Category": category,
        "Why Layers": why_layers,
        "Output Type": output_type,
        "Output Message": output_message,
        "Powered By": "The Why Theory™"
    }


# Helper Functions (simplified)
def categorize_problem(problem_input):
    # Basic keyword matching or AI classification
    if "sell" in problem_input or "traffic" in problem_input:
        return "Business/Practical"
    elif "growth" in problem_input or "brand" in problem_input:
        return "Strategic"
    else:
        return "General"

def analyze_problem(problem_input):
    # First diagnostic step
    return "Traffic is low"

def ask_why(reason):
    # Example chain
    if reason == "Traffic is low":
        return "SEO keywords not optimized"
    elif reason == "SEO keywords not optimized":
        return "Titles are generic"
    else:
        return "External market saturation"

def is_root_cause(reason):
    return reason in ["Titles are generic", "External market saturation"]

def is_controllable(reason):
    return reason not in ["External market saturation"]

def generate_solution(reason):
    if reason == "Titles are generic":
        return "Optimize titles with buyer-focused keywords."
    else:
        return "Experiment with alternative strategies."
