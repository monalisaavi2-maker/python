from fasthtml.common import *

# Initialize FastHTML with Pico CSS enabled automatically
app, rt = fast_app(live=False)
passs = {"Avilash":"Avilashishero",
        "AlphaCoder47": "pass123",
        "CyberFalcon19": "cool456",
        "NovaHacker83": "user789",
        "ShadowDev52": "safe111",
        "PixelRunner36": "code222",
        "QuantumTech71": "web333",
        "ApexUser64": "open444",
        "MatrixMaker28": "make555",
        "StormKnight95": "host666",
        "VortexGhost50": "fast777"  
    }
def centered_card_layout(title_text, *components):
    return Main(
        # Standard structural layout container with a clean card styling
        Div(
            H2(title_text, style="text-align: center; margin-bottom: 1.5rem;"),
            *components,
            style="""
                max-width: 500px; 
                margin: 40px auto; 
                padding: 30px; 
                background: #ffffff;
                border-radius: 8px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            """
        ),
        style="padding: 20px;",
        data_theme="light" # Forces a clean light theme, change to "dark" if you prefer dark mode
    )
def frmd(s):
    for pwd in passs.values():
        pwd = pwd[0:len(pwd)]
        if pwd == s: 
            Script("alert('Login Successful!'); window.location.href = https://render.com;")
# --- PAGES ---

def home_view():
    return centered_card_layout(
        "Welcome to PyLogin",
        P("Welcome, please login or create an account to Render", style="text-align: center; color: #666; margin-bottom: 2rem;"),
        # Grid layout puts buttons side-by-side beautifully
        Div(
            A("Login to Account", href="/login", role="button", style="width: 100%;"),
            A("Create New Account", href="/cret", role="button", class_="secondary", style="width: 100%;"),
            style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;"
        )
    )

def login_view():
    return centered_card_layout(
        "Sign In",
        Form(
            Label("Username", Input(type="text", placeholder="Enter your username", required=True)),
            Label("Password", Input(type="password", placeholder="Enter your password", required=True,id="password")),
            Button("Login Now", type="submit", style="margin-top: 1rem;",command=frmd("password")),
            Div(
                A("← Back to Home", href="/"),
                A("Create an account", href="/cret"),
                style="display: flex; justify-content: space-between; margin-top: 1.5rem; font-size: 0.9rem;"
            )
        )
    )

def create_account_view():
    return centered_card_layout(
        "Create Account",
        Form(
            Label("Choose Username", Input(type="text", placeholder="e.g., avilash123", required=True)),
            Label("Choose Password", Input(type="password", placeholder="Minimum 8 characters", required=True,id="password")),
            Button("Register Account", type="submit", class_="secondary", style="margin-top: 1rem;"),
            Div(
                A("← Back to Home", href="/"),
                A("Already have an account?", href="/login"),
                style="""display: flex; justify-content: space-between; margin-top: 1.5rem; font-size: 0.9rem;"""
            )
        )
    )

# --- ROUTES ---

@rt("/")
def get_home():  
    return home_view()

@rt("/cret")
def get_cret():  
    return create_account_view()

@rt("/login")
def get_login():  
    return login_view()

if __name__ == "__main__":
    serve()
