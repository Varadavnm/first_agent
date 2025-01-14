
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")






# Function to interact with LLM
def generate_web_code(prompt):
    """
    Generate HTML and CSS code based on the user's design request using an LLM.
    """
    try:
        openai.api_key = os.getenv("OPENAI_API_KEY")  # Replace with your OpenAI key or set it in environment variables
        
        response = openai.Completion.create(
            engine="text-davinci-003",  # Replace with your preferred LLM engine
            prompt=prompt,
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error generating code: {e}")
        return None

# Interactive agent
def interactive_design_agent():
    """
    Interactive agent to generate web designs based on user input.
    """
    print("Welcome to the Interactive Web Design Generator!")
    print("Describe the web page design you want. (e.g., 'A Google-like search page with a logo and a centered search bar')")
    
    user_request = input("Your design request: ")
    
    # Define LLM prompt
    llm_prompt = f"""
    Generate HTML and CSS code for the following web design request:
    {user_request}
    
    Ensure that the code is simple, well-formatted, and includes both the HTML and CSS parts. The CSS should be embedded in a <style> block within the HTML file.
    """
    
    print("\nGenerating your design...\n")
    generated_code = generate_web_code(llm_prompt)
    
    if generated_code:
        # Save the code to a file
        output_file = "generated_design.html"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(generated_code)
        print(f"Design generated successfully! Saved to {output_file}")
        print("Preview the file in a browser.")
    else:
        print("Failed to generate the design. Please try again.")

# Example usage
if __name__ == "__main__":
    interactive_design_agent()
