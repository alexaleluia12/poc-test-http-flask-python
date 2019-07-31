import src


if __name__ == "__main__":
    instance_app = src.create_app()
    instance_app.run(debug=True, host='0.0.0.0', port=5000)
