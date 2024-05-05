import streamlit as st
import requests
from pytube import YouTube
import os
from twelvelabs.models.task import Task

# Streamlit interface setup
st.title('12 Labs - Interview Insight Analyzer')

from twelvelabs import TwelveLabs

client = TwelveLabs(api_key=os.environ.get('TL_API_KEY'))

# Creating tabs, 
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Project Description", "Video Uploader", "Video Analyzer", "Unique Value Add", "Thanks Team"])

with tab1:
    st.header("Project Description")
    st.write("The automatic video interview analyzer project leverages AI to streamline recruitment by objectively assessing video interviews. This tool evaluates responses and non-verbal cues, ensuring a fair and efficient process. It enhances candidate experience with immediate feedback and integrates smoothly with HR systems, optimizing hiring practices.")
    image_path = 'data/interview.png'
    # Display the image
    st.image(image_path, caption='Project Flow Diagram')
    # Add more components as needed

with tab2:

    from pytube import YouTube
    
    # Function to download YouTube video
    def download_youtube_video(url):
        yt = YouTube(url)
        stream = yt.streams.filter(file_extension='mp4').first()
        video = stream.download()
        return video
    
    st.header('Video Upload and Processing (To Do)')
    
    # Setup your Twelve Labs client
    # Assuming 'client' is set up here (use your actual client initialization)
    # client = TwelveLabsClient(api_key="your_api_key")
    
    # Container for video input
    with st.container():
        st.write("Video Input")
        video_file = st.file_uploader("Upload a video file", type=["mp4", "avi"])
        youtube_url = st.text_input("Or paste a YouTube URL here:")
    
    # Container for video processing output
    with st.container():
        st.write("Video Processing")
    
        if st.button("Process Video"):
            st.warning('This feature is under construction and will be developed in a future project.')



with tab3:

    st.header("Video Analyzer")
    st.write("Choose the number of issues you like to examine, and get feedback on how to improve for your next job interview.")
    
    # Creating two columns for layout
    col1, col2 = st.columns(2)
    
    # Embedding YouTube video directly in the left column
    with col1:
        youtube_url = "https://www.youtube.com/watch?v=Uo0KjdDJr1c"
        st.video(youtube_url)
    
    # Using the right column for prompt modification and response
    with col2:
        # Input for modifying the prompt
        prompt = st.text_input("Enter your prompt:", 
                               "list the top 4 job interview mistakes and how to improve")
        
        # Slider to adjust the number in the prompt
        number = st.slider("Select the number of top mistakes:", min_value=1, max_value=10, value=4)
        
        # Update the prompt with the chosen number
        updated_prompt = prompt.replace("4", str(number))
        
        # Button to send the request
        if st.button("Summarize Video"):
            BASE_URL = "https://api.twelvelabs.io/v1.2"
            api_key = "tlk_3CPMVGM0ZPTKNT2TKQ3Y62TA7ZY9"
            data = {
                "video_id": "6636cf7fd1cd5a287c957cf5",
                "type": "summary",
                "prompt": updated_prompt
            }
        
            # Send the request
            response = requests.post(f"{BASE_URL}/summarize", json=data, headers={"x-api-key": api_key})
            
            # Check if the response is successful
            if response.status_code == 200:
                st.text_area("Summary:", response.json()['summary'], height=300)
            else:
                st.error("Failed to fetch summary: " + response.text)
    
    # Run this script using the following command:
    # streamlit run your_script_name.py

with tab4:
    st.header("Top 20 - Unique Value Add")
    import streamlit as st
    
    # List of items
    items = [
        "Standardization and Fairness: Ensuring every candidate is treated equally improves legal compliance and internal fairness.",
        "Improved Hiring Decisions: Objective, data-driven assessments lead to better hires, directly impacting organizational performance.",
        "Time and Cost Efficiency: Reducing the time and resources required for hiring processes translates directly into cost savings.",
        "Scalability: Ability to handle a high volume of interviews efficiently supports rapid scaling, critical for growth phases.",
        "Integration with HR Systems: Streamlining recruitment into broader HR workflows enhances overall HR efficiency.",
        "Predictive Analytics: Advanced analytics can forecast candidate success, improving long-term job fit and satisfaction.",
        "Enhanced Candidate Experience: Providing immediate feedback can enhance reputation and attract quality candidates.",
        "Remote Hiring Efficiency: Facilitates global talent acquisition, crucial for companies with a diverse geographic footprint.",
        "Accessibility and Inclusiveness: Opens up opportunities for a wider pool of candidates, enhancing diversity.",
        "Security and Privacy Compliance: Ensures handling of personal data safely and legally, protecting the company and candidate.",
        "Data-Driven Insights: Offers deep insights into candidate behaviors, refining hiring criteria and outcomes.",
        "Reduced Interviewer Bias: Minimizes human bias, directly contributing to a more diverse and innovative workforce.",
        "Competitive Advantage: Attracting top talent by using cutting-edge technology enhances a company's market positioning.",
        "Reduced Administrative Load: Automates tasks such as scheduling, increasing operational efficiency.",
        "Continuous Improvement Loop: The system's ability to learn and adapt from each interview boosts long-term effectiveness.",
        "Dynamic Questioning: Adapting questions in real-time ensures more relevant and revealing candidate responses.",
        "Documentation and Review: Facilitates compliance and quality control in hiring processes.",
        "AI-Driven Role Matching: Optimizes talent distribution within the organization by matching candidates to suitable roles.",
        "Enhanced Employer Branding: Advances the company's image as innovative and candidate-focused.",
        "Speed of Process: Accelerates the recruitment cycle, reducing downtime and improving responsiveness to staffing needs."
    ]
    
    # Displaying items with numbering in a Streamlit text area
    st.text_area("List of Items", "\n".join([f"{i+1}. {item}" for i, item in enumerate(items)]), height=600)

with tab5:
    st.header("Thanks to the Team")
    st.write("This tool isn’t just a testament to our technical capabilities—it’s a step forward in transforming how the world approaches recruitment. Thanks to your efforts, we are on the path to making recruitment processes more efficient, fair, and insightful, which will ultimately benefit countless individuals and organizations.")
    image_path = 'data/interview2.png'

    # Display the image
    st.image(image_path, caption='Our Team')
    # Add more components as needed