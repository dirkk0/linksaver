# linksaver
a poor man's private delicious.


Start the RESTful Flask server with ./start.sh or with 'python RESTserver.py'. This will start a minimal Flask server listening on port 5000 on locahost.

## Basic usage.
Now you can curl

    curl -H "Content-type: application/json" -X POST http://127.0.0.1:5000/messages -d '{"entry":"My important link","link":"http://github.com"}'

and it will be saved to a local sqlite database (entries,db).

## Enable Google spreadsheet support.
If you change the db_sqlite line in the RESTserver.py to db_google, you can save this to a google spreadsheet.

1. create a Google spreadsheet named 'linksaver' and create three rows named entry, link and timestamp.
![empty spreadsheet](http://content.screencast.com/users/dirkk1/folders/Jing/media/4fac8625-e254-46fb-9793-bd17521ec89d/00000040.png)
2. Create a credential.json file from the credentials_template.json with your username and password.
3. Uncomment line 8.

Then curl again and - voilá - the link is added:
![first entry, yay!](http://content.screencast.com/users/dirkk1/folders/Jing/media/2c020bd2-6be5-4352-ba09-b0ac610cbcef/00000041.png)

Of course this is more fun without curl that's why I will add a ...
## Google Chrome extension
TBD