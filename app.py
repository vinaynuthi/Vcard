import os
from flask import Flask, render_template

app = Flask(__name__)

# Configure app for Railway
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')

@app.route('/')
def index():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>VCard Management</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
            .container { max-width: 800px; margin: 0 auto; background: white; padding: 40px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
            h1 { color: #333; text-align: center; }
            .status { background: #d4edda; color: #155724; padding: 10px; border-radius: 5px; margin: 20px 0; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎉 VCard Management System</h1>
            <div class="status">
                ✅ Your Flask application is running successfully on Railway!
            </div>
            <p>This is a minimal version to verify deployment is working.</p>
            <p>Next steps: Add your full application code.</p>
        </div>
    </body>
    </html>
    """

@app.route('/test')
def test():
    return {"status": "success", "message": "App is working correctly!"}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
