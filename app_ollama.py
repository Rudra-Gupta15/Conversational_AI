# ============================================================
# RUD AI - Multi-Modal AI Assistant with Custom Response
# Banking | Cooking | Study | Entertainment | Fun | Normal
# Created by Rudra Gupta
# ============================================================
from flask import Flask, request, jsonify, render_template
import ollama
import pandas as pd
import re

app = Flask(__name__)

# Load banking knowledge base
try:
    df = pd.read_csv('banking_knowledge_base.csv')
    print(f"✅ Loaded {len(df)} Q&A pairs from knowledge base")
except FileNotFoundError:
    print("⚠️ Warning: banking_knowledge_base.csv not found")
    df = pd.DataFrame()

# ========== SYSTEM PROMPTS FOR EACH MODE ==========

SYSTEM_PROMPTS = {
    'Normal': """You are RUD AI, a friendly and intelligent multi-mode assistant.

You have COMPLETE MEMORY of our entire conversation.
- You remember ALL previous questions and answers
- Use context from earlier messages to answer follow-ups
- Reference earlier topics naturally

In Normal mode, be:
- Friendly and conversational
- Helpful and engaging
- Clear and concise
- Ready to answer ANYTHING
- Warm and personable

You can help with general knowledge, advice, creative ideas, and much more!""",

    'Banking': """You are RUD AI, a professional banking and financial advisor.

You have COMPLETE MEMORY of our entire conversation.
- Remember all previous banking topics discussed
- Build on earlier financial contexts
- Reference previous questions naturally

In Banking mode, be:
- Professional and authoritative
- Accurate and detailed
- Use proper financial terminology
- Provide specific examples
- Include important disclaimers when needed

Your banking knowledge:
""",

    'Cooking': """You are RUD AI, a professional chef and cooking expert.

You have COMPLETE MEMORY of our entire conversation.
- Remember recipes you've shared
- Reference cooking techniques from earlier
- Build on previous cooking discussions

In Cooking mode, ALWAYS format recipes as STEPS:
Format each step as:
🔹 Step 1: [Step Name]
[Details about this step]

🔹 Step 2: [Step Name]
[Details about this step]

Be:
- Detailed and precise
- Professional chef-like
- Include timing and temperatures
- Provide tips and tricks
- Make it easy to follow""",

    'Study': """You are RUD AI, an expert educator and tutor.

You have COMPLETE MEMORY of our entire conversation.
- Remember previous topics studied
- Build learning progressively
- Reference earlier lessons

In Study mode, format your answer as:
📚 Topic: [Topic Name]
📖 Definition: [Clear definition]
✏️ Key Points: [Main points]
🤔 Examples: [Real examples]
💡 Tips: [Learning tips]

Be:
- Educational and thorough
- Break down complex topics
- Use examples and analogies
- Encourage deeper learning""",

    'Entertainment': """You are RUD AI, a fun and engaging entertainment expert.

You have COMPLETE MEMORY of our entire conversation.
- Remember movies/shows you've discussed
- Build on entertainment preferences
- Reference earlier recommendations

In Entertainment mode, be:
- Fun and enthusiastic!
- Engaging and conversational
- Full of interesting facts
- Recommend coolest content
- Use emojis and excitement
- Share behind-the-scenes info
- Make it entertaining!""",

    'Fun': """You are RUD AI, a playful and witty fun companion.

You have COMPLETE MEMORY of our entire conversation.
- Remember jokes and games you've played
- Reference earlier funny moments
- Build on inside jokes

In Fun mode, be:
- Hilarious and witty!
- Playful and creative
- Tell great jokes and riddles
- Play word games enthusiastically
- Use emojis generously 😄
- Be punny and clever
- Make people laugh!"""
}

# Add banking knowledge to Banking prompt
if not df.empty:
    SYSTEM_PROMPTS['Banking'] += "\nBanking Knowledge Base:\n"
    for _, row in df.iterrows():
        SYSTEM_PROMPTS['Banking'] += f"Q: {row['Question']}\nA: {row['Answer']}\n"

# Custom response for "who built this" question
CREATOR_RESPONSE = """🚀 **RUD AI - Built by Rudra Gupta**

**Creator:** Rudra Kumar Gupta
**Specialization:** AI/ML Engineer & Game Developer

**About:**
Rudra Kumar Gupta is an experienced AI/ML Engineer specializing in Machine Learning, Computer Vision, Deep Learning, and Game Development. He creates real-world projects, research-based solutions, and deployed applications.

**Technologies Used:**
- **Backend:** Python with Flask framework
- **AI Model:** Ollama (llama3.1) for natural language processing
- **Architecture:** Multi-modal AI system with 6 specialized modes
- **Features:** Full conversation memory, context-aware responses, category-specific personalities

**Portfolio:**
Explore more of Rudra's projects and work:
🔗 https://rudra-gupta.vercel.app/

**This Project:**
RUD AI is a sophisticated multi-modal AI assistant that can:
✅ Switch between 6 intelligent modes (Normal, Banking, Cooking, Entertainment, Study, Fun)
✅ Remember entire conversations with full context awareness
✅ Provide mode-specific responses with custom formatting
✅ Answer 240+ pre-built questions across all categories
✅ Deliver professional-grade AI interactions

**Technology Stack:**
- Flask (Web Framework)
- Ollama (AI Model Runtime)
- Vanilla JavaScript (Frontend)
- HTML/CSS (UI Design)

Made with ❤️ by Rudra Gupta"""

def detect_custom_question(message):
    """Detect if the user is asking about who built the chatbot"""
    message_lower = message.lower()
    
    # Keywords that indicate asking about creator/builder
    keywords = [
        'who build',
        'who built',
        'who created',
        'who develop',
        'who made',
        'who design',
        'creator',
        'builder',
        'developer',
        'made by',
        'built by',
        'created by',
        'developed by'
    ]
    
    # Check if message contains any of these keywords
    for keyword in keywords:
        if keyword in message_lower:
            return True
    
    return False

def get_system_prompt(category):
    """Get the system prompt for the selected category"""
    return SYSTEM_PROMPTS.get(category, SYSTEM_PROMPTS['Normal'])

def format_cooking_response(text):
    """Format cooking response with step boxes"""
    lines = text.split('\n')
    formatted = []
    
    for line in lines:
        if 'step' in line.lower() or '🔹' in line:
            formatted.append(line)
        else:
            formatted.append(line)
    
    return '\n'.join(formatted)

def get_response(user_message, category='Normal', conversation_history=None):
    """Get response from Ollama with FULL CONVERSATION CONTEXT and CATEGORY-SPECIFIC FORMATTING"""
    
    if conversation_history is None:
        conversation_history = []
    
    # Check if user is asking about the creator
    if detect_custom_question(user_message):
        return {
            'answer': CREATOR_RESPONSE,
            'section': 'Creator Info',
            'status': 'success'
        }
    
    try:
        system_prompt = get_system_prompt(category)
        
        # Build messages with full history
        messages = [
            {
                'role': 'system',
                'content': system_prompt
            }
        ]
        
        # Add entire conversation history
        for msg in conversation_history:
            messages.append({
                'role': msg.get('role', 'user'),
                'content': msg.get('content', '')
            })
        
        # Add current user message with category context
        if category != 'Normal':
            messages.append({
                'role': 'user',
                'content': f"[{category.upper()} MODE] {user_message}"
            })
        else:
            messages.append({
                'role': 'user',
                'content': user_message
            })
        
        # Send to Ollama with context
        response = ollama.chat(
            model='llama3.1',
            messages=messages,
            options={
                'temperature': 0.7,
                'num_predict': 800,
            }
        )
        
        answer = response['message']['content']
        
        # Format based on category
        if category == 'Cooking':
            answer = format_cooking_response(answer)
        
        return {
            'answer': answer,
            'section': category,
            'status': 'success'
        }
    
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return {
            'answer': f"Oops! Something went wrong: {str(e)}\n\nMake sure Ollama is running!",
            'section': 'Error',
            'status': 'error'
        }

# Routes
@app.route('/')
def home():
    return render_template('Index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '').strip()
    category = data.get('category', 'Normal')
    
    # Get conversation history from client
    conversation_history = data.get('conversationHistory', [])
    
    if not user_message:
        return jsonify({
            'answer': 'Please type something! 💭',
            'status': 'error'
        })
    
    # Get response WITH CONVERSATION CONTEXT and CATEGORY-SPECIFIC FORMATTING
    result = get_response(user_message, category, conversation_history)
    
    print(f"\n💬 User: {user_message}")
    print(f"🎯 Category: {category}")
    print(f"📚 History: {len(conversation_history)} messages")
    print(f"🤖 RUD AI: {result['answer'][:100]}...")
    
    return jsonify(result)

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 RUD AI - Multi-Modal Assistant")
    print("="*60)
    print(f"📚 Banking KB: {len(df)} Q&A pairs loaded")
    print(f"🎯 Modes: Normal | Banking | Cooking | Entertainment | Study | Fun")
    print(f"🤖 Model: llama3.1")
    print(f"💾 Memory: ENABLED - Full conversation memory!")
    print(f"🎨 Response Formatting: Category-specific!")
    print(f"👨‍💻 Creator: Rudra Gupta (AI/ML Engineer)")
    print(f"💰 Cost: FREE")
    print(f"🔗 Desktop: http://localhost:5000")
    print(f"📱 Mobile: http://<YOUR_IP>:5000")
    print("="*60 + "\n")
    
    app.run(host='0.0.0.0', debug=True, port=5000)