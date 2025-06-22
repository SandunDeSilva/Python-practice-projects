import webbrowser as wb

def web_automation():
    # The '%s' is a placeholder that will be replaced by the URL when the webbrowser module runs the command.
    # For example, if the URL is 'https://www.google.com', Python will run:
    # 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe https://www.google.com'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s' # Add the path to your Chrome executable
    urls = (
        'https://www.google.com',
        'https://www.github.com',
        'https://www.stackoverflow.com'
    )
    for url in urls:
        print(f"Opening {url} in Chrome...")
        wb.get(chrome_path).open(url)


web_automation()