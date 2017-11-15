# SendCloud API Integration Example

There are various ways to integrate the SendCloud shipping solution with your own platform.  
The [API documentation][sc_api_docs] gives a complete overview of the possibilities.  
This repository should provide you clear and understandable examples on how you can integrate SendCloud.

## Setting up the API credentials

Before you can interact with the API it is essential that you setup API credentials.  
Make sure that you are signed up by creating an account:  
https://panel.sendcloud.sc/accounts/signup/

Once you have set up an account we advice you to setup your payment contract:  
https://panel.sendcloud.sc/#/settings/financial/payments/direct-debit  
Registering your payment credentials is necessary to ensure you can make use of the full capabilities of the API.

Once done you can create API keys:  
https://panel.sendcloud.sc/#/settings/integrations/api/add  
Make sure that you give it a recognizable name. Ensure that you press the save button.

Once saved you should see the Public key and Secret key. Make sure you save them somewhere safely.
You are going to need those credentials to authenticate with the API. 

## Examples
Below you can find the links to Python files which show how to use the API. 
The scripts are written in Python 3 and require [Requests][requests_docs] to be installed.  
You can easily inspect and learn more about the code. 

Running the scripts to interact with the API simple. Take the following create parcel example:

```
python3 examples/basic_integration_example.py --action create --public XXXXX --secret XXXXX --partner_id YYYYY
```

You can change _action_ from create to one of the options which you can find in the section below.  
Make sure you replace _XXXXX_ by your public and secret key.  
You can replace _YYYYY_ by the partner id.  
Also can drop the partner_id if you don't have one as it is optional.  
At last it is recommended to inspect the code before running it. 

### Actions

+ [basic_integration_example.py](examples/basic_integration_example.py)
	+ __create:__ Create a shipment in SendCloud to be processed.
	+ __cancel__ Cancel a shipment in SendCloud before or after processing.
		+ _NOTE:_ This action asks for input while executing!

### Final note about testing

SendCloud offers no sandbox. If you are testing please notice that there are free and paid shipping options in your account.
There is a unstamped label option in the platform which is free and which is recommended for testing. 

Once your integration is working you can check with paid shipping methods, but make sure that you cancel them before the cancellation 
deadline otherwise you have to pay for this label on the next invoice.
[More info about cancelling a shipment.][cancel_shipment]


[sc_api_docs]: https://docs.sendcloud.sc/api/v2/index.html
[requests_docs]: http://docs.python-requests.org/en/master/
[cancel_shipment]: https://support.sendcloud.com/english/settings/how-do-i-cancel-my-shipment
