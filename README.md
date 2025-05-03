# IELTS Writing Task 2 Evaluator

## Overview

The IELTS Writing Task 2 Evaluator is an AI-powered application designed to assess IELTS Writing Task 2 essays based on official IELTS scoring criteria. It provides detailed evaluations for each criterion including Task Response, Coherence and Cohesion, Lexical Resource, and Grammatical Range and Accuracy. After submission, users receive an overall band score and a breakdown of their essay’s strengths and weaknesses, alongside visualizations and the ability to export the results.

## Features

* **Essay Evaluation**: Automatically evaluates essays against the four IELTS Writing Task 2 criteria:

  * **Task Response**: How well the essay addresses the prompt.
  * **Coherence and Cohesion**: Structure, clarity, and logical flow.
  * **Lexical Resource**: Vocabulary usage and range.
  * **Grammatical Range and Accuracy**: Grammar usage and complexity.

* **Band Score Calculation**: Each criterion is assigned a score between 1 and 9, and an overall band score is calculated based on the evaluations.

* **Visualization**: Displays a bar chart showing the scores for each criterion, with a line for the overall band score.

* **Results Export**: The evaluation results can be downloaded as a JSON file for future reference or analysis.

* **Example Essay**: Load a pre-filled example essay to test the application’s functionality.

* **Helpful Tips**: Provides tips on how to improve your IELTS Writing score.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/ielts-essay-evaluator.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Google API key. This application requires a Google API key for the integration with `langchain_google_genai`:

   * Go to [Google Cloud Console](https://console.cloud.google.com/).
   * Enable the appropriate API (e.g., Gemini).
   * Create an API key and store it as an environment variable:

     ```bash
     export GOOGLE_API_KEY="your_google_api_key"
     ```

---

## Usage

1. **Running the Application:**
   Start the application with Streamlit:

   ```bash
   streamlit run app.py
   ```

2. **Interface:**

   * **Essay Prompt**: Enter the IELTS Writing Task 2 prompt.
   * **Essay Text**: Write or paste your essay in the text box.
   * **Submit**: Click the "Evaluate Essay" button to submit your essay for evaluation.

3. **Evaluation Process**:
   After submitting, the AI evaluates the essay and provides:

   * **Overall Band Score**: The total score for your essay.
   * **Detailed Evaluation**: A breakdown for each IELTS criterion, including a score and a detailed comment.
   * **Visuals**: A bar chart displaying your scores for each criterion.
   * **Download**: A JSON file with the detailed evaluation results.

4. **Sidebar Features**:

   * **About**: Information about the application.
   * **IELTS Writing Tips**: Tips for improving your IELTS Writing Task 2 performance.
   * **Example Essay**: Load an example essay for evaluation.

---

## Evaluation Criteria

Each essay is evaluated based on the following official IELTS criteria:

* **Task Response**: This criterion assesses how well you address the prompt, present a clear position, and develop a well-supported argument.

* **Coherence and Cohesion**: This measures how logically ideas are presented, the overall structure of your essay, and how well ideas are connected.

* **Lexical Resource**: This evaluates the range and accuracy of vocabulary used in your essay.

* **Grammatical Range and Accuracy**: This measures the complexity and accuracy of the grammar used in the essay.

The system will give a score for each of these categories, followed by detailed comments on what was done well and what could be improved.

---

## Example Output

### Example Essay:

**Essay Prompt:**

```
Some people believe that the purpose of education should be to help individuals become useful members of society. Others say education should help individuals achieve their ambitions. Discuss both views and give your opinion.
```

**Essay Text:**

```
Education is a powerful tool that shapes not only the future of individuals but also the development of society. While some argue that the primary goal of education should be to produce responsible and productive citizens, others contend that it should help individuals pursue their personal ambitions. This essay will discuss both perspectives before offering a reasoned opinion.

On one hand, proponents of the view that education should help individuals become useful members of society emphasize the role of education in preparing people for the workforce and instilling a sense of responsibility. By learning subjects that are relevant to societal needs, such as science, technology, engineering, and mathematics (STEM), individuals can contribute to economic growth and innovation. For instance, doctors, engineers, and teachers play crucial roles in maintaining the well-being and progress of society. Additionally, education can foster social values, such as respect for others, teamwork, and civic duty, which are vital for creating cohesive communities. In this sense, education is seen as a means of equipping individuals with the skills and knowledge needed to contribute to the public good.

On the other hand, those who believe that education should help individuals achieve their personal ambitions argue that the primary purpose of education is self-fulfillment and the pursuit of personal goals. According to this view, education provides individuals with the tools to explore their interests, discover their talents, and ultimately find careers that align with their passions. For example, a student who dreams of becoming an artist or a musician should be encouraged to study the subjects and skills that will help them succeed in their chosen field, even if these disciplines do not directly serve societal needs. Furthermore, education can serve as a platform for personal growth and empowerment, helping individuals to develop confidence and achieve a sense of purpose in life. The notion that everyone has the right to follow their dreams is central to this perspective.

In my opinion, while both views are valid, the most effective education system should strike a balance between helping individuals achieve their ambitions and preparing them to be productive members of society. Education should not solely focus on societal needs, as it risks stifling individual creativity and personal fulfillment. At the same time, it cannot be purely centered on personal goals, as this would overlook the broader responsibilities that individuals have towards their communities. A well-rounded education system can offer both opportunities for personal development and training in skills that are beneficial to society.

In conclusion, the debate about the purpose of education hinges on the balance between personal aspirations and societal contribution. Although both perspectives have merit, I believe that a harmonious blend of both approaches is essential for fostering well-rounded individuals who can achieve their personal goals while also making meaningful contributions to society.
```

**Evaluation Output**:

* **Overall Band Score**: 7.0
* **Detailed Criteria Analysis**:

  * **Task Response**: Score: 7.0, Comment: The essay addresses both views thoroughly and offers a balanced perspective.
  * **Coherence and Cohesion**: Score: 7.0, Comment: The essay is well-structured, but the transitions between ideas could be smoother.
  * **Lexical Resource**: Score: 7.0, Comment: The vocabulary used is appropriate, with a good range and some academic phrases.
  * **Grammatical Range and Accuracy**: Score: 7.0, Comment: There are some minor grammatical errors, but sentence structures are varied and complex.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

This project uses the `langchain_google_genai` library for text generation, and `Streamlit` for building the web interface. Special thanks to the developers of these libraries for providing the tools to create this application.

---

## Contact

For any issues, suggestions, or contributions, feel free to open an issue or create a pull request.
