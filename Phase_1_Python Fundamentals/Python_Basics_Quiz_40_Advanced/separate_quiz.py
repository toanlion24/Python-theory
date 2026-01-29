import json
import re
import os

# Read the original notebook
with open('../Python_Basics_Quiz_40_Advanced_Questions.ipynb', 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# Initialize lists for questions and answers
questions_cells = [notebook['cells'][0]]  # Keep the header
answers_cells = [{
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "# Python Basics Quiz - 40 Advanced Questions - Answer Key\n",
        "\n",
        "**Answer Key** - Correct answers for all 40 advanced questions\n",
        "\n",
        "This notebook contains the correct answers for all questions in the quiz.\n",
        "\n",
        "**Instructions:**\n",
        "- Review your answers after completing the quiz\n",
        "- Each answer includes the correct option and explanation\n",
        "\n",
        "---\n"
    ]
}]

# Process cells to separate questions and answers
question_num = 0
current_question_cells = []
current_answer_cells = []

for i, cell in enumerate(notebook['cells'][1:], 1):  # Skip header
    source_text = ''.join(cell['source']) if cell['source'] else ''
    
    if cell['cell_type'] == 'markdown':
        # Check if it's a question header
        if '## Question' in source_text and ':' in source_text:
            # Save previous question if exists
            if current_question_cells:
                questions_cells.extend(current_question_cells)
            if current_answer_cells:
                answers_cells.extend(current_answer_cells)
            
            # Start new question
            current_question_cells = [cell]
            current_answer_cells = []
            
            # Extract question number
            match = re.search(r'## Question (\d+)', source_text)
            if match:
                question_num = int(match.group(1))
        
        # Check if it contains answer options and correct answer
        elif '**Correct Answer:' in source_text:
            # Split into question part (options) and answer part
            parts = source_text.split('**Correct Answer:')
            if len(parts) == 2:
                # Question part: everything before "**Correct Answer:"
                question_part = parts[0].strip()
                # Answer part: the correct answer
                answer_text = parts[1].strip()
                
                # Add options to question cells (without the answer)
                question_cell = {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [question_part + "\n\n---\n"]
                }
                current_question_cells.append(question_cell)
                
                # Add answer to answer cells
                answer_cell = {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        f"## Question {question_num} - Answer\n",
                        "\n",
                        f"**Correct Answer: {answer_text}**\n",
                        "\n",
                        "---\n"
                    ]
                }
                current_answer_cells.append(answer_cell)
            else:
                current_question_cells.append(cell)
        else:
            # Regular markdown cell (theory, explanation, etc.)
            current_question_cells.append(cell)
    
    elif cell['cell_type'] == 'code':
        # Code cells go to both questions and answers
        current_question_cells.append(cell)
        current_answer_cells.append(cell)

# Add the last question/answer sets
if current_question_cells:
    questions_cells.extend(current_question_cells)
if current_answer_cells:
    answers_cells.extend(current_answer_cells)

# Add end message to questions
questions_cells.append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "## End of Quiz\n",
        "\n",
        "You have completed all 40 questions!\n",
        "\n",
        "Check your answers using the Answer Key notebook.\n",
        "\n",
        "---\n"
    ]
})

# Create questions notebook
questions_notebook = {
    "cells": questions_cells,
    "metadata": notebook['metadata'],
    "nbformat": notebook['nbformat'],
    "nbformat_minor": notebook['nbformat_minor']
}

# Create answers notebook
answers_notebook = {
    "cells": answers_cells,
    "metadata": notebook['metadata'],
    "nbformat": notebook['nbformat'],
    "nbformat_minor": notebook['nbformat_minor']
}

# Write questions notebook
with open('Python_Basics_Quiz_40_Advanced_Questions_ONLY.ipynb', 'w', encoding='utf-8') as f:
    json.dump(questions_notebook, f, indent=2, ensure_ascii=False)

# Write answers notebook
with open('Python_Basics_Quiz_40_Advanced_Answers.ipynb', 'w', encoding='utf-8') as f:
    json.dump(answers_notebook, f, indent=2, ensure_ascii=False)

# Copy original notebook to folder
import shutil
shutil.copy('../Python_Basics_Quiz_40_Advanced_Questions.ipynb', 
            'Python_Basics_Quiz_40_Advanced_Questions.ipynb')

print("Successfully created:")
print("1. Python_Basics_Quiz_40_Advanced_Questions_ONLY.ipynb (Questions without answers)")
print("2. Python_Basics_Quiz_40_Advanced_Answers.ipynb (Answers only)")
print("3. Python_Basics_Quiz_40_Advanced_Questions.ipynb (Original with both)")
