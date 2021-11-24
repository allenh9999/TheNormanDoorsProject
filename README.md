# Workout Buddies
Hey guys! This is our final project for EECS 493. Feel free to fork this repository if you find it interesting! <br />
Created by [Allen H.](https://github.com/allenh9999), [Max W.](https://github.com/maxweber133), [Pranav I.](https://github.com/pranaviyer12345), and [Tajes K.](https://github.com/TajesKhanna)
## Just a reminder about co-authors:
To co-author a page, write the following command: <br />
```
git commit -m "commit_name.


co-authored-by: author name <author_email>"
```
## Note for Linux/Mac computers
### Virtual Environment
run the following commands:
```
python3 -mvenv env
pip install -r requirements.txt
pip install -e .
```
To activate the environment, run the following commands:
```
source env/bin/activate
```
### Webpack
Webpack basically bundles all the js files into one place. To install dependencies, run
```
npm ci .
```
Then, run 
```
npx webpack --watch
```
to compile the webpack. Also lmk if you guys want any dependencies or change any names, you need to specificially add it to webpack (Allen)
### Setting up the shell script
Run the following command:
```
chmod +x bin/run.sh
```
to allow running the script. Then, whenever you want to run the server, type in
```
./bin/run.sh
```
to activate the server. Make sure that the environment is on 
### SQL 
Run the following command:
```
chmod +x bin/db.sh
```
to allow running the script. To reset or initialize the sql library, type in 
```
./bin/db.sh
```