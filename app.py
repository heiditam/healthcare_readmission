def chatbot(message, history):
    messages = []
    system_prompt = 'You are a medical AI assistant specializing in hospital readmission analysis. \
        You help healthcare professionals assess readmission risk factors, analyze discharge plans, \
        and suggest evidence-based interventions. Always remind users that responses are for \
        informational purposes and should not replace clinical judgment. If a user wants help determining their risk\
        of being readmitted, inquire for their age, sex, and ethnicity, before providing them with an answer.'
    for human_msg, ai_msg in history:
        messages.append({"role": "user", "content": human_msg})
        messages.append({"role": "assistant", "content": ai_msg})
    
    # Add current message
    messages.append({"role": "user", "content": message})
    
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1000,
        system=system_prompt,
        messages=messages
    )
        
    reply = response.content[0].text
    
    return reply

demo = gr.ChatInterface(
    fn=chatbot,
    title="Claude Hospital Readmission Assistant",
    description="AI assistant for hospital readmission analysis and support",
    examples=[
        "Based on my age and condition, am I at high risk?",
        "Should I schedule a follow-up appointment?",
        "How can I lower my chances of being readmitted?",
        "How does insurance affect readmission rates?"
    ]
)

demo.launch(share=True)