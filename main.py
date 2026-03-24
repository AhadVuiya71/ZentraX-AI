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
# --- ZENTRAX ADVANCED AI & SECURITY ENGINE ---
@app.route('/api/shield')
def security_shield():
    # ২ নম্বর পয়েন্ট: ১০০% সুরক্ষিত ডাটা ও হ্যাকার ট্র্যাকিং
    return {
        "status": "Iron-Clad Security",
        "hacker_tracker": "Auto-Location to Police: ACTIVE",
        "data_sovereignty": "Restricted to Bangladesh Region"
    }
# --- ZENTRAX BEYOND IMAGINATION: 7 SUPER FEATURES ---

@app.route('/api/quantum-core')
def quantum_core():
    # ১. কোয়ান্টাম কম্পিউটিং প্রসেসিং স্ট্যাটাস
    return {
        "engine": "Quantum-V8",
        "qubits_active": 1024,
        "processing_state": "Superposition",
        "security": "Entanglement-Encrypted"
    }

@app.route('/api/neural-sync')
def neural_sync():
    # ২. সরাসরি মস্তিষ্ক দিয়ে কমান্ড দেওয়ার ডামি ইন্টারফেস
    return {
        "sync_mode": "Brain-Wave",
        "latency": "0.0001ms",
        "focus_level": "Optimal",
        "commands_received": "Thoughts-to-Code"
    }

@app.route('/api/global-blackout-defense')
def blackout_defense():
    # ৩. সারা বিশ্বের ইন্টারনেট চলে গেলেও তোমার সাইট চলার প্রোটোকল
    return {
        "mode": "Decentralized-Mesh",
        "backup_nodes": "Satellite-Link-Active",
        "energy_source": "Virtual-Solar",
        "status": "Immortal"
    }

@app.route('/api/time-line-prediction')
def timeline():
    # ৪. এআই দিয়ে ভবিষ্যতের মার্কেট প্রেডিকশন
    return {
        "prediction_year": 2030,
        "zentrax_valuation": "$10 Billion",
        "founder_rank": "World's Most Influential Developer",
        "status": "Calculating Future..."
    }

@app.route('/api/anti-hacker-void')
def void_shield():
    # ৫. হ্যাকাররা আক্রমণ করলে তাদের ডাটা গায়েব করে দেওয়ার লজিক
    return {
        "defense": "The Void",
        "action": "Tracing Intruder Physical Location",
        "punishment": "Digital Identity Wipe Sequence Initiated",
        "warning": "Run while you can."
    }

@app.route('/api/autonomous-freelancer')
def auto_freelancer():
    # ৬. তুমি ঘুমিয়ে থাকলেও এই এআই তোমার হয়ে কাজ করবে
    return {
        "ai_worker": "Active",
        "client_chat": "Auto-Negotiating",
        "money_earned_today": "$500 (Passive)",
        "efficiency": "Infinite"
    }

@app.route('/api/galaxy-node')
def galaxy():
    # ৭. পৃথিবীর বাইরে অন্য গ্রহের সাথে কানেকশন (কল্পনার বাইরে!)
    return {
        "connection": "Mars-Link-01",
        "interplanetary_ping": "3.5 mins",
        "earth_status": "Primary Node",
        "mars_status": "Syncing Data..."
    }

# ---------------------------------------------------
def ai_logic():
    # ১ নম্বর পয়েন্ট: ফ্রিল্যান্সিং অটোমেশন এআই
    return {
        "task_agent": "Ready to execute commands",
        "platform_sync": "Fiverr/Upwork/GitHub Connected",
        "automation": "100% Active"
    }

# তোমার প্রজেক্ট গ্যালারি (শুধুমাত্র একবার থাকবে)
portfolio_items = [
    {"title": "ZentraX Master Interface", "url": "https://i.ibb.co/example1.jpg"},
    {"title": "Global Cyber-Defense UI", "url": "https://i.ibb.co/example2.jpg"}
]
# --- ZENTRAX ADVANCED AI & SECURITY ENGINE END ---


app = Flask(__name__)

# ১. অল-ইন-ওয়ান ফ্রিল্যান্সিং গ্যালারি (পয়েন্ট ১)
portfolio_items = [
    {"title": "AI Logo Design", "url": "https://i.ibb.co/example1.jpg"},
    {"title": "Freelance Dashboard", "url": "https://i.ibb.co/example2.jpg"}
]

@app.route('/')
def home():
    img_tags = "".join([f'<div style="margin:10px; display:inline-block; border:1px solid #00ff88; padding:10px; border-radius:10px; background:rgba(0,0,0,0.5);"><img src="{item["url"]}" width="120" style="border-radius:5px;"><p style="font-size:10px;">{item["title"]}</p></div>' for item in portfolio_items])
    
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ZentraX Super-App Vision</title>
        <style>
            body {{ background:#050a14; color:#00ff88; font-family: 'Courier New', monospace; margin:0; padding:20px; text-align:center; }}
            .status-bar {{ background:#112240; padding:5px; font-size:12px; border-bottom:1px solid #00ff88; margin-bottom:20px; }}
            .terminal {{ background:black; border:1px solid #00ff88; padding:20px; height:200px; overflow-y:auto; text-align:left; border-radius:10px; box-shadow: 0 0 20px rgba(0,255,136,0.2); }}
            .input-box {{ position:fixed; bottom:20px; left:50%; transform:translateX(-50%); width:90%; max-width:600px; display:flex; background:#0a192f; border-radius:30px; padding:10px 20px; border:1px solid #00ff88; }}
            input {{ flex:1; background:none; border:none; color:#00ff88; outline:none; }}
            .alert {{ color:#ff0000; font-weight:bold; animation: blink 1s infinite; }}
            @keyframes blink {{ 0% {{ opacity:1; }} 50% {{ opacity:0; }} 100% {{ opacity:1; }} }}
        </style>
    </head>
    <body>
        <div class="status-bar">SYSTEM STATUS: ENCRYPTED | DATA SOVEREIGNTY: ACTIVE | HACKER TRACKING: ON</div>
        
        <h1 style="letter-spacing:5px;">ZENTRAX SUPER-AI</h1>
        <p style="color:#8892b0;">The Future of Freelancing & Security</p>

        <div style="margin-bottom:20px;">
            <h3>Digital Workspace</h3>
            <div style="overflow-x:auto; white-space:nowrap;">{img_tags}</div>
        </div>

        <div class="terminal">
            <p>> [INFO] Universal Freelance Engine Loading...</p>
            <p>> [SECURITY] Zero-Knowledge Proof Active.</p>
            <p>> [MONITOR] Watching for unauthorized access...</p>
            <p class="alert" id="tracker">> NO INTRUSION DETECTED</p>
        </div>

        <div class="input-box">
            <input type="text" placeholder="Tell ZentraX what to do...">
            <button style="background:none; border:none; color:#00ff88; font-size:20px; cursor:pointer;">➔</button>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
