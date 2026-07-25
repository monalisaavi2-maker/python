from fasthtml.common import *

# 1. Initialize the FastHTML application
# Rename this initialization line slightly to avoid conflict
backend_app, rt = fast_app()

def log():
    return Titled(
        "Login",
        P("Please enter your credentials to log in:"),
        Input(type="text", placeholder="Username"),
        Input(type="password", placeholder="Password"),
        Button("Login"),
        Br(),
        A("Go Back Home", href="/")
    )

def cretur():
    return Titled(
        "Create Account",
        P("Please fill in the form to create an account:"),
        Input(type="text", placeholder="Username"),
        Input(type="password", placeholder="Password"),
        Button("Create Account"),
        A("Go Back Home", href="/")
    )

def home():
    return Titled(
        "Welcome to Avilash Login Page",
        P("This is the homepage of the Avilash Login Page. You can navigate to the Create Account page or the Login page using the links below."),
        A("Go to Create Account", href="/cret", style="text-align: center;"),
        Br(),
        A("Go to Login", href="/login", style="text-align: center;")
    )

# 2. Define application routes
@rt("/")
def get_home():  
    return home()

@rt("/cret")
def get_cret():  
    return cretur()

@rt("/login")
def get_login():  
    return log()

# 3. Global Serverless Handler (NAMED "app" FOR NATIVE VERCEL RECOGNITION)
from mangum import Mangum
app = Mangum(backend_app)

# 4. Start the server ONLY when running locally
if __name__ == "__main__":
    serve()
