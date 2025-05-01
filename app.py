from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="https://tinypic.host/images/2025/02/07/DeWatermark.ai_1738952933236-1.png">
    <title>SudoR2spr Repository</title>
    <link rel="icon" type="image/x-icon" href="https://tinypic.host/images/2025/02/07/DeWatermark.ai_1738952933236-1.png">
</head>

<body>
    <div class="container" style="bg-dark text-red text-center py-3 mt-5">
        <a href="https://github.com/nikhilsaini098" class="card">
            <p style="font-family: monospace; white-space: pre; font-size: 14px;">
  ____ ____     ____ _               _     _             
 / ___|  _ \\   / ___| |__   ___  ___| |__ (_)_ __   __ _ 
| |   | | | | | |   | '_ \\ / _ \\/ __| '_ \\| | '_ \\ / _` |
| |___| |_| | | |___| | | |  __/\\__ \\ | | | | | | | (_| |
 \\____|____/   \\____|_| |_|\\___||___/_| |_|_|_| |_|\\__, |
                                                  |___/  
                <br><b>v2.0.0</b>
            </p>
        </a>
    </div>
    <br><br><br>
    <footer class="bg-dark text-white text-center py-3 mt-5">
        <center>
            <img loading="lazy" class="object-none object-center" src="https://tinypic.host/images/2025/02/07/DeWatermark.ai_1738952933236-1.png" width="240" height="120">
            Powered By <b>CR CHOUDHARY</b>
            <img loading="lazy" class="object-none object-center" src="https://tinypic.host/images/2025/02/07/DeWatermark.ai_1738952933236-1.png" width="240" height="120">
            <div class="footer__copyright">
                <p class="footer__copyright-info">
                    © 2024 Video Downloader. All rights reserved.
                </p>
            </div>
        </center>
    </footer>
</body>

</html>
"""

if __name__ == "__main__":
    app.run()
