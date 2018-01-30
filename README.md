# Whatsapp Web-Driving

Whatsapp driving for message automation using **python 3.6**.
For **linux** and **mac os**.

## Requirements

* Python 3 or greater.
* Virtualenv.
* Google Chrome.

## Usage

This repo provides a python app to automate message sending for whatsapp using python-selenium.

The main idea is to create a `messages.json` file containing **key:value** 
data where the **key** is the name of the contact (as in the app) 
and the **value** is a list of messages. 
Each message is a json structure as well. Example:
```json
{
  "Contact Name": [
    {
      "type": "text",
      "content": "This is a  sample text-message."
    }
  ]
}
```

Example message file: `cat resources/user-messages/messages.json.example`

Feel free to change the *send_message* function at *util.messages* according to your use-case.

### First usage

Follow these instructions for first-use:

1. Download this repo.
1. Create a virtual-environment and install requirements.
    * `virtualenv --python=python3 venv`
    * `source venv/bin/activate`
    * `pip install -r requirements.txt`
1. Create the .env file: `cp setting/.env.example setting/.env`
1. Run the setup script: `python setup.py`
1. Add executable permissions to the web-driver e.g. `chmod u+rx resources/drivers/linux/chromedriver`
1. Create your messages file. See example: `resources/user-messages/messages.json.example`


### After setup

1. Modify the message file and the *send_message* function according to your use-case.
1. Run the app: `python main.py`

**Note** when running the app, Selenium will open a Chrome-browser with the Whatsapp-web page. Scan the QR to initialize your session.


## Contributions and authors

Contact the main developer for contributions. 

* **Main developer**: Rodrigo Hernandez Mota (rohdzmota@gmail.com)

## License

See the **LICENSE.md** file for more information.