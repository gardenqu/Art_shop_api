from src.flaskdr import create_app






app = create_app()

if __name__ == "__main__":
    app.run(host='ec2-3-228-135-242.compute-1.amazonaws.com', port=5002)
