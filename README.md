# Gmail dot trick

A minimal python script to generate email addresses using the dot trick.

## How does Gmail dot trick work?

Before I tell you how to use Gmail dot trick, it's important to know how this trick works. The loophole this trick uses is the fact that [Gmail automatically omits any dots in an email address]([https://](https://support.google.com/mail/answer/7436150)) in whatever sequence they are added. Gmail particularly does this to prevent mistyped emails from going to the wrong address. For example, an email to *gt.ri.cks@gmail.com* will always go to the original *gtricks@gmail.com* email address.

Although Gmail supports this feature, most other websites don't. Therefore, when you add a dot to your Gmail address while registering, the website thinks of it as a completely new email ID. However, Gmail will still send all the emails sent to that address to the original email address.

## Installation

Download or clone this repository and enter the main folder. Python 3 is required to
run the application.

## Usage

```
❯ python app.py gtricks@gmail.com
2022-11-20 10:04:34,802 [INFO    ] (main:48) Script starting
2022-11-20 10:04:34,803 [INFO    ] (main:58) Finished running script, stored results in result.txt

❯ head result.txt
gtricks@gmail.com
gtrick.s@gmail.com
gtric.ks@gmail.com
gtri.cks@gmail.com
gtr.icks@gmail.com
gt.ricks@gmail.com
g.tricks@gmail.com
gtric.k.s@gmail.com
gtri.ck.s@gmail.com
gtr.ick.s@gmail.com
```