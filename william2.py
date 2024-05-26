from IPython.display import HTML, display

def generate_bank_website():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Bank Website</title>
    </head>
    <body>
        <img src="https://mh-1-stockagency.panthermedia.net/media/media_detail/0009000000/09581000/~bank-building_09581808_detail.jpg">
        <h1>Welcome to Our Bank</h1>
        <h3>How can I assist you today?</h3>
        <form action="/main" method="post">
            <p>How are you doing?</p>
            <p><input type="text" name="feeling" placeholder="Enter how you are feeling"></p>
            <p>What service do you need?</p>
            <select name="service">
                <option value="Deposit">Deposit</option>
                <option value="Withdraw">Withdraw</option>
                <option value="Transfer">Transfer</option>
                <option value="Other">Other</option>
            </select>
            <p>How can I help you?</p>
            <textarea name="help" rows="4" cols="50" placeholder="Enter your request"></textarea>
            <p><input type="submit" value="Submit"></p>
        </form>
        <p><a href="/main">Back to Main Page</a></p>
    </body>
    </html>
    """
    return html_content

# Display the generated HTML content
display(HTML(generate_bank_website()))