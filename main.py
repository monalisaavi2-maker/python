from fasthtml.common import *

# 1. Initialize the FastHTML application
app, rt = fast_app()
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
        A("Go to Create Account", href="/cret"),
        A("Go to Login", href="/login")
    )
# 2. Define the main homepage route
@rt("/")
def get_home():  # Changed name to get_home
    return home()

# 3. Define a second page route
@rt("/cret")
def get_cret():  # Changed name to get_cret
    return cretur()

@rt("/login")
def get_login():  # Changed name to get_login
    return log

# 4. Start the server ONLY when running locally
if __name__ == "__main__":
    serve()
