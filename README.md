# TicketsProjectFlask
This is an app about concerts. Unauthorized guests can only see the upcoming concerts. Authorized users can have the role of a simple users, hosts of events and admins. Simple user can buy tickets for concerts and see their own purchases. Hosts can create concerts events and can edit and delete thte information about their concerts. Admins can see all resources.

This is a flask app.

You can start it on port http://127.0.0.1:5000

Users can sign up through requests to http://127.0.0.1:5000/sign-up
Users can sign in through requests to http://127.0.0.1:5000/sign-in
Non registered users can see all concerts through get requests to http://127.0.0.1:5000/concerts
Hosts of concerts can add concert through post requests to http://127.0.0.1:5000/concerts
Hosts of concerts can edit the information about their own concerts through put requests to http://127.0.0.1:5000/concert/{concert_id/edit
Hosts of concerts can delete information about their own concerts through delete requests to http://127.0.0.1:5000/concert/{concert_id/delete
Simple users can purchase tickets through post requests to http://127.0.0.1:5000/purchases
Simple users can see their own purchases through get requests to http://127.0.0.1:5000/ownpurchases
Admins can see all purchases through get requests to http://127.0.0.1:5000/allpurchases


Please first install the packages in requirements.txt file.
