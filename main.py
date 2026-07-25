from fasthtml.common import *

# 1. Initialize the FastHTML application
app, rt = fast_app()

def cretur():
    return Titled(
        "Create Account",
        P("Please fill in the form to create an account:"),
        Input(type="text", placeholder="Username"),
        Input(type="password", placeholder="Password"),
        Button("Create Account"),
        A("Go Back Home", href="/")
    )

# 2. Define the main homepage route
@rt("/")
def get_home():  # Changed name to get_home
    return Titled(
        "FastHTML Demo Application",
        P("Python login Application!"),
        A("Go to Create Account", href="/cret"),
        P(), # Adds a small spacing break
        A("Go to Login", href="/login")
    )

# 3. Define a second page route
@rt("/cret")
def get_cret():  # Changed name to get_cret
    return cretur()

@rt("/login")
def get_login():  # Changed name to get_login
    return Titled(
        "Login",
        P("Please enter your credentials to login:"),
        Input(type="text", placeholder="Username"),
        Input(type="password", placeholder="Password"),
        Button("Login"),
        Br(),  # Adds a small spacing break
        A("Go Back Home", href="/")
    )

# 4. Start the server ONLY when running locally
if __name__ == "__main__":
    serve()
