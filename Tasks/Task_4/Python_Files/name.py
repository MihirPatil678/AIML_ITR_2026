# Define Function
def greet():
    print("Hello, Welcome To Python!")

# This Condition Checks Whether The Script Runs Directly
# If True, The Code Inside This Block Will Execute
# If The File Is Imported Into Another File, This Block Will Not Run
if __name__ == "__main__":
    print("This File Is Being Run Directly.")
    
    # Call The Greet Function
    greet()