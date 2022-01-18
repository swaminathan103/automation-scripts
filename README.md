# automation-scripts
Collection of automation scripts to enhance productivity

# List of Scripts
* [work.py](#workpy)

# work.py
Sometimes, we might need to open certain apps during work or preload specific URLs every time we log in. After we're done with work, we might need to close all those applications. This script aims to provide a simple solution by automating the entire process. Here's how you can get started.

## Getting Started 
Add the full path to the applications you want to open inside the 'appNames' array as comma-separated strings. An example for mac is shown below. 

```
appPaths = [ "/Applications/Slack.app", "/Applications/Google\ Chrome.app" ]
```

Add URLs as comma-separated strings inside the 'webURLs' array. Once you add the URLs and run the script, all the URLs will open in your default browser. An example is shown below:

```
webURLs = [ "https://www.google.com/" ]
```

After you've customized the script, run the appropriate command in the terminal to open or close your applications.

**To open the applications and URLs:**

```
python work.py -s 
```

or

```
python3 work.py -s
```

**To close the applications:**

```
python work.py -c 
```
or 

```
python3 work.py -c
```
