import webview

html = """
<!doctype html>
<html lang="en">
	<head>
		<meta charset="utf-8">
        <title>Test app</title>
	</head>
	<body style = "background-color: transparent;">
       Test
	</body>
</html>
"""

if __name__ == '__main__':
    # Create a resizable webview window with minimum size constraints
    window = webview.create_window('Transparent window', html=html, transparent=True, frameless=True, easy_drag=True)
    window.on_top = True
    second_window = webview.create_window('FastHTML', 'http://localhost:5001/')
    webview.start()