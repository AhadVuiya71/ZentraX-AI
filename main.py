import os
import threading
import webbrowser
import time
import requests # এআই ইমেজ ডাউনলোডের জন্য
from flask import Flask, send_from_directory, request, jsonify
from colorama import Fore, Style, init

# ১. সেটিংস ও ডিরেক্টরি
init(autoreset=True)
app = Flask(__name__)
PORTFOLIO_DIR = "my_designs"

if not os.path.exists(PORTFOLIO_DIR):
    os.makedirs(PORTFOLIO_DIR)

# ২. Generative AI Design Engine (v6.0 Special)
def generate_ai_design():
    print(Fore.MAGENTA + "\n" + "="*40)
    print(Fore.WHITE + "       ZENTRAX AI DESIGNER (v6.0)       ")
    print(Fore.MAGENTA + "="*40)
    
    prompt = input(Fore.CYAN + "আপনি কী ধরণের ডিজাইন চান? (বিস্তারিত লিখুন): ")
    if not prompt: return
    
    print(Fore.YELLOW + "⌛ ZentraX আপনার ডিজাইনটি জেনারেট করছে... দয়া করে অপেক্ষা করুন।")
    
    # Pollinations AI API (Free & No API Key)
    encoded_prompt = prompt.replace(" ", "%20")
    image_url = f"https://pollinations.ai/p/{encoded_prompt}?width=1024&height=1024&model=flux"
    
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            file_name = f"ai_design_{int(time.time())}.jpg"
            file_path = os.path.join(PORTFOLIO_DIR, file_name)
            
            with open(file_path, 'wb') as f:
                f.write(response.content)
            
            print(Fore.GREEN + f"✅ ডিজাইন সফলভাবে তৈরি হয়েছে: {file_name}")
            print(Fore.BLUE + "এটি আপনার ড্যাশবোর্ড গ্যালারিতে যোগ করা হয়েছে।")
        else:
            print(Fore.RED + "❌ সার্ভার থেকে ইমেজ পাওয়া যায়নি।")
    except Exception as e:
        print(Fore.RED + f"❌ সমস্যা হয়েছে: {e}")

# ৩. ড্যাশবোর্ড ও গ্যালারি
@app.route('/designs/<filename>')
def serve_design(filename):
    return send_from_directory(PORTFOLIO_DIR, filename)

@app.route('/')
def dashboard():
    files = [f for f in os.listdir(PORTFOLIO_DIR) if f.endswith(('.png', '.jpg', '.jpeg'))]
    img_tags = "".join([f'<div style="margin:10px; display:inline-block;"><img src="/designs/{f}" style="width:250px; border-radius:10px; border:2px solid #00ff88; box-shadow: 0 0 10px #00ff88;"><p style="color:#fff;">{f}</p></div>' for f in files])
    
    return f"""
    <body style="background:#0a192f; color:#00d4ff; text-align:center; font-family:sans-serif; padding:20px;">
        <h1 style="text-shadow: 0 0 15px #00ff88;">ZENTRAX v6.0 AI COMMANDER</h1>
        <p>Founder: Khan Ahad</p>
        <div style="background:rgba(17, 34, 64, 0.9); padding:20px; border-radius:15px; margin:20px; border:1px solid #00d4ff;">
            <h3>Live AI Portfolio Gallery</h3>
            <div style="overflow-x:auto; white-space:nowrap; padding:10px;">
                {img_tags if img_tags else "<p>কোনো ডিজাইন এখনো তৈরি হয়নি।</p>"}
            </div>
        </div>
        <p style="color:#666;">Refreshed at: {time.ctime()}</p>
    </body>
    """

# ৪. মেইন সিস্টেম কন্ট্রোল
def run_zentrax():
    print(Fore.RED + Style.BRIGHT + "\n[SECURITY] Master Key Required.")
    if input(Fore.YELLOW + "মাস্টার কী: ") == "admin123":
        print(Fore.GREEN + "✅ ZentraX v6.0 ইঞ্জিন অনলাইন।")
        while True:
            print(Fore.CYAN + "\n" + "-"*30)
            print(" ১. ড্যাশবোর্ড ওপেন করুন\n ২. AI দিয়ে নতুন ডিজাইন করুন (Generative)\n ৩. এক্সিট")
            print("-"*30)
            cmd = input(Fore.WHITE + "কমান্ড: ")
            
            if cmd == '১': webbrowser.open("http://127.0.0.1:5000")
            elif cmd == '২': generate_ai_design()
            elif cmd == '৩': os._exit(0)

if __name__ == "__main__":
    # ক্লাউড ফ্রেন্ডলি পোর্ট সেটিংস
    port = int(os.environ.get("PORT", 5000))
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=port), daemon=True).start()
    run_zentrax()
    # তোমার পোর্টফোলিও গ্যালারির ইমেজ লিঙ্কগুলো এখানে দাও
portfolio_items = [
    {"title": "Branding Logo", "url": "https://i.ibb.co/example1.jpg"},
    {"title": "Social Media Banner", "url": "https://i.ibb.co/example2.jpg"},
    {"title": "AI Artwork", "url": "https://i.ibb.co/example3.jpg"}
]
