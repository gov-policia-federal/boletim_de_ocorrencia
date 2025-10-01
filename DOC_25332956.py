from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def capture_ip():
    # Capture user's IP address
    user_ip = request.remote_addr
    # Log the IP address (e.g., send to a logging server or save to a file)
    with open('ips.txt', 'a') as f:
        f.write(user_ip + '\n')
    return ''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
