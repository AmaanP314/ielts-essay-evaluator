import streamlit as st
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain.chains import LLMChain

st.set_page_config(
    page_title="IELTS Essay Evaluator",
    page_icon="📝",
    layout="wide"
)

st.title("IELTS Writing Task 2 Evaluator")
st.markdown("""
This application evaluates IELTS Writing Task 2 essays based on official IELTS criteria.
Enter the essay prompt and your essay to receive a detailed evaluation.
""")

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

if st.sidebar.button("Load Example"):
    st.session_state.essay_prompt = "Some people believe that the purpose of education should be to help individuals become useful members of society. Others say education should help individuals achieve their ambitions. Discuss both views and give your opinion."
    st.session_state.essay_text = """
Education is a powerful tool that shapes not only the future of individuals but also the development of society. While some argue that the primary goal of education should be to produce responsible and productive citizens, others contend that it should help individuals pursue their personal ambitions. This essay will discuss both perspectives before offering a reasoned opinion.

On one hand, proponents of the view that education should help individuals become useful members of society emphasize the role of education in preparing people for the workforce and instilling a sense of responsibility. By learning subjects that are relevant to societal needs, such as science, technology, engineering, and mathematics (STEM), individuals can contribute to economic growth and innovation. For instance, doctors, engineers, and teachers play crucial roles in maintaining the well-being and progress of society. Additionally, education can foster social values, such as respect for others, teamwork, and civic duty, which are vital for creating cohesive communities. In this sense, education is seen as a means of equipping individuals with the skills and knowledge needed to contribute to the public good.

On the other hand, those who believe that education should help individuals achieve their personal ambitions argue that the primary purpose of education is self-fulfillment and the pursuit of personal goals. According to this view, education provides individuals with the tools to explore their interests, discover their talents, and ultimately find careers that align with their passions. For example, a student who dreams of becoming an artist or a musician should be encouraged to study the subjects and skills that will help them succeed in their chosen field, even if these disciplines do not directly serve societal needs. Furthermore, education can serve as a platform for personal growth and empowerment, helping individuals to develop confidence and achieve a sense of purpose in life. The notion that everyone has the right to follow their dreams is central to this perspective.

In my opinion, while both views are valid, the most effective education system should strike a balance between helping individuals achieve their ambitions and preparing them to be productive members of society. Education should not solely focus on societal needs, as it risks stifling individual creativity and personal fulfillment. At the same time, it cannot be purely centered on personal goals, as this would overlook the broader responsibilities that individuals have towards their communities. A well-rounded education system can offer both opportunities for personal development and training in skills that are beneficial to society.

In conclusion, the debate about the purpose of education hinges on the balance between personal aspirations and societal contribution. Although both perspectives have merit, I believe that a harmonious blend of both approaches is essential for fostering well-rounded individuals who can achieve their personal goals while also making meaningful contributions to society.
"""
prompt_value = st.session_state.get("essay_prompt", "")
essay_value = st.session_state.get("essay_text", "")

with st.form("essay_form"):
    essay_prompt = st.text_area("Enter the Essay Prompt", value=prompt_value,placeholder="e.g., Some people think the best way to reduce crime is to give longer prison sentences. Others believe there are better alternatives. Discuss both views and give your opinion.", height=100)
    essay_text = st.text_area("Enter Your Essay", value=essay_value, placeholder="Write your essay here...", height=300)
    
    submitted = st.form_submit_button("Evaluate Essay")

def evaluate_essay(essay_prompt, essay_text):
    try:
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash-exp",
            google_api_key=GOOGLE_API_KEY
        )
        
        band_score = ResponseSchema(
            name="band_score",
            description="Overall band score of the essay (a number, e.g., 7.5)."
        )
        task_response = ResponseSchema(
            name="task_response",
            description=(
                "An object with two keys: 'score' (a numerical string, e.g. '3.0') and 'comment' (a detailed explanation). "
                "Return this as nested JSON. For example: {\"score\": \"3.0\", \"comment\": \"Detailed comment here.\"}"
            )
        )
        coherence_and_cohesion = ResponseSchema(
            name="coherence_and_cohesion",
            description=(
                "An object with two keys: 'score' (a numerical string, e.g. '6.0') and 'comment' (a detailed explanation). "
                "Return this as nested JSON. For example: {\"score\": \"6.0\", \"comment\": \"Detailed comment here.\"}"
            )
        )
        lexical_resource = ResponseSchema(
            name="lexical_resource",
            description=(
                "An object with two keys: 'score' (a numerical string, e.g. '6.0') and 'comment' (a detailed explanation). "
                "Return this as nested JSON. For example: {\"score\": \"6.0\", \"comment\": \"Detailed comment here.\"}"
            )
        )
        grammatical_range_and_accuracy = ResponseSchema(
            name="grammatical_range_and_accuracy",
            description=(
                "An object with two keys: 'score' (a numerical string, e.g. '7.0') and 'comment' (a detailed explanation). "
                "Return this as nested JSON. For example: {\"score\": \"7.0\", \"comment\": \"Detailed comment here.\"}"
            )
        )
        
        schemas = [
            band_score,
            task_response,
            coherence_and_cohesion,
            lexical_resource,
            grammatical_range_and_accuracy,
        ]
        
        structured_output_parser = StructuredOutputParser.from_response_schemas(schemas)
        format_instructions = structured_output_parser.get_format_instructions()
        
        prompt = PromptTemplate(
            template=(
                "You are an IELTS Writing Task 2 evaluator. Below is the exam prompt followed by a candidate's essay. "
                "Evaluate the essay based on how well it responds to the exam prompt and the IELTS evaluation metrics. "
                "Provide an overall band score and detailed analysis on the following dimensions:\n\n"
                "1. task_response\n2. coherence_and_cohesion\n3. lexical_resource\n4. grammatical_range_and_accuracy\n\n"
                "For each metric, return a nested JSON object with two keys: 'score' and 'comment'.\n\n"
                "Make sure to evaluate the exam prompt and essay critically"
                "Exam Prompt:\n{essay_prompt}\n\n"
                "Essay:\n{essay}\n\n"
                "Format your response exactly as JSON following these instructions:\n\n"
                "{format_instructions}\n\n"
                "Do not include any additional text or explanation."
            ),
            input_variables=["essay_prompt", "essay"],
            partial_variables={"format_instructions": format_instructions}
        )
        
        chain = LLMChain(llm=llm, prompt=prompt)
        result = chain.run(essay_prompt=essay_prompt, essay=essay_text)
        
        structured_result = structured_output_parser.parse(result)
        return structured_result
    
    except Exception as e:
        return {"error": str(e)}

if submitted:
    if not essay_prompt or not essay_text:
        st.error("Please enter both the essay prompt and your essay.")
    else:
        with st.spinner("Evaluating your essay..."):
            results = evaluate_essay(essay_prompt, essay_text)
            st.session_state.results = results
        
        if "error" in st.session_state.results:
            st.error(f"Error: {st.session_state.results['error']}")
        else:
            st.success("Evaluation complete!")

def parse_metric(metric):
    if isinstance(metric, str):
        try:
            return json.loads(metric)
        except json.JSONDecodeError:
            return metric
    return metric

if hasattr(st.session_state, 'results') and "error" not in st.session_state.results:
    results = st.session_state.results
    for key in ['task_response', 'coherence_and_cohesion', 'lexical_resource', 'grammatical_range_and_accuracy']:
        if key in results:
            results[key] = parse_metric(results[key])

    st.markdown("### Overall Evaluation")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.markdown(
            f"""
            <div style="padding: 20px; border-radius: 10px; border: 1px solid #ddd; text-align: center; background-color: #262730;">
                <h1 style="font-size: 48px; color: #1e88e5;">{results['band_score']}</h1>
                <p style="font-size: 18px;">Overall Band Score</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    st.markdown("### Detailed Criteria Analysis")
    tab1, tab2, tab3, tab4 = st.tabs([
        "Task Response", 
        "Coherence & Cohesion", 
        "Lexical Resource", 
        "Grammatical Range & Accuracy"
    ])
    
    with tab1:
        tr = results['task_response']
        st.markdown(f"**Score:** {tr['score']}")
        st.markdown(f"**Comments:** {tr['comment']}")
    
    with tab2:
        cc = results['coherence_and_cohesion']
        st.markdown(f"**Score:** {cc['score']}")
        st.markdown(f"**Comments:** {cc['comment']}")
    
    with tab3:
        lr = results['lexical_resource']
        st.markdown(f"**Score:** {lr['score']}")
        st.markdown(f"**Comments:** {lr['comment']}")
    
    with tab4:
        gr = results['grammatical_range_and_accuracy']
        st.markdown(f"**Score:** {gr['score']}")
        st.markdown(f"**Comments:** {gr['comment']}")
    
    st.markdown("### Score Visualization")
    
    categories = ['Task Response', 'Coherence & Cohesion', 'Lexical Resource', 'Grammar']
    scores = [
        float(results['task_response']['score']), 
        float(results['coherence_and_cohesion']['score']),
        float(results['lexical_resource']['score']),
        float(results['grammatical_range_and_accuracy']['score'])
    ]
    
    plt.style.use('dark_background') 
    sns.set_style('dark')
    fig, ax = plt.subplots(figsize=(10, 6), facecolor='#262730')
    ax.set_facecolor('#262730')
    bars = ax.bar(categories, scores, color=['#5d76cb', '#546ab7', '#4a5ea2', '#41538e'])
    
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.1, f'{height}',
                ha='center', va='bottom', color='white')
    
    ax.set_ylim(0, 10)
    ax.set_ylabel('Score', color='white', fontweight='bold')
    ax.set_title('IELTS Writing Task 2 Scores by Category', color='white', fontweight='bold')
    ax.axhline(y=float(results['band_score']), color='red', linestyle='--', label=f'Overall: {results["band_score"]}')
    ax.tick_params(axis='x', rotation=0, labelcolor='white')
    ax.tick_params(axis='y', labelcolor='white')
    ax.legend()
    st.pyplot(fig)
    
    st.markdown("### Export Results")
    export_data = {
        "evaluation_date": str(pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')),
        "essay_prompt": essay_prompt,
        "essay_text": essay_text,
        "results": results
    }
    
    json_results = json.dumps(export_data, indent=4)
    st.download_button(
        label="Download Evaluation as JSON",
        data=json_results,
        file_name=f"ielts_evaluation_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.json",
        mime="application/json"
    )

with st.sidebar:
    st.markdown("## About")
    st.markdown("""
    This application uses AI to evaluate IELTS Writing Task 2 essays based on the official IELTS marking criteria:
    
    * Task Response
    * Coherence and Cohesion
    * Lexical Resource
    * Grammatical Range and Accuracy
    
    The evaluation provides scores on a scale of 1-9 for each criterion, as well as an overall band score.
    """)
    
    st.markdown("## Tips for IELTS Writing")
    st.markdown("""
    * Read the prompt carefully
    * Plan your essay before writing
    * Use a clear structure with introduction, body paragraphs, and conclusion
    * Develop your ideas with examples
    * Use a range of vocabulary and grammatical structures
    * Aim for at least 250 words
    * Proofread your work
    """)

st.markdown("---")
st.markdown("""
<div style="text-align: center;">
    <p>IELTS Essay Evaluator</p>
</div>
""", unsafe_allow_html=True)