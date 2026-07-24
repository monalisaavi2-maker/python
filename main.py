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
def get():
    return Titled(
        "FastHTML Demo Application",
        P("Python login Application!"),
        A("Go to Create Account", href="/cret"),
        A("Go to Login", href="/login")
    )

# 3. Define a second page route
@rt("/cret")
def get():
    return cretur()
@rt("/login")
def get():
    return Titled(
        "Login",
        P("Please enter your credentials to login:"),
        Input(type="text", placeholder="Username"),
        Input(type="password", placeholder="Password"),
        Button("Login"),
        A("Go Back Home", href="/")
    )

# 4. Start the server
serve()
