def shutdown(confirm):
    if confirm == "yes":
        print("Shutting down...")
    else:
        print("Shutdown cancelled")

answer = input("Do you want to shut down? ")

shutdown(answer)