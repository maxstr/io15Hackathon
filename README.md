# io15Hackathon
Hackathon for Citrix IO15

Kevin
Makala
Max
Patrick


POST:

http://freshpicksb.appspot.com/store_user


{"user_name": "Patrick", "address_street": "412 Oregon Street", "address_street2": "Nowhere", "address_state" : "California", "user_email": "jjj@gmail.com", "address_zipcode": "90245", "user_phone": "310-683-0741", "address_city": "El Segundo"}

curl -D header.out -H "Content-Type: application/json" --data @user_create.json http://localhost:8080/store_user

TEST


GET:

http://freshpicksb.appspot.com/users
