# ase-toy

live on https://ase-toy.herokuapp.com/

##
tech stack
```bash
Python
Flask
PostgreSQL
Bootstrap
React
```

##
running
```bash
$ git clone https://github.com/chaojiwan/ase-toy.git
```

## 
also running
```bash
$ pip install -r requirements.txt
$ npm install
$ bower install
```

##
The app has five pages like 
```bash
/index
/signup
/login
/home
/about
```

##
The app has main functions like
```bash
1. signup with form validation 
    1) email must be unique for each account and also in standard format 
    2) password must be eight characters long
2. login with credentials and also form validation
3. logged out users kept away from /home page with redirection 
    1) only logged in users can view /home page 
4. logged in users kept away from /signup and /login page with redirections
    1) only logged out users can see /signup and /login pages
```

##

