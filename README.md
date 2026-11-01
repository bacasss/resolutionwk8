latest update:

NOTHING IS WRONGG HERES PROOF OF LIFE:
https://youtu.be/ATHPnt3kRSc

the reviewer's own confessions are there its public :(

also it may not be able to post to channels because the bot is not in them and also i was told to remove chat:write.public in the scope as it may not be allowed for the server. for testing purposes use your own dms as a test or feel free to use mine and then dm me for results im more than happy to help anything to get this approved rahh :(


<img width="1918" height="1198" alt="Screenshot 2026-06-25 051131" src="https://github.com/user-attachments/assets/6beb1b55-0c11-47b6-96a3-0ea42cb92c1c" />
<img width="1918" height="1198" alt="Screenshot 2026-06-25 051201" src="https://github.com/user-attachments/assets/2e1991c1-4898-4d2b-995a-c66772e7807b" />
<img width="1918" height="1198" alt="Screenshot 2026-06-25 051218" src="https://github.com/user-attachments/assets/b65fcba0-ed6c-4095-99e2-24e784a8c954" />
<img width="847" height="148" alt="Screenshot 2026-06-25 051234" src="https://github.com/user-attachments/assets/0003dff1-9896-4b02-a525-143bf0afd1c3" />

<img width="857" height="868" alt="image" src="https://github.com/user-attachments/assets/f6710619-8c77-4a3e-a078-2b93b17c3666" />


link: https://app.slack.com/client/E09V59WQY1E/D0BCUBGTTAR
(pls use /uselesscmd67 , its the only working command and i am a firm believer of if it aint broke dont touch it)

This is a simple anonymous confessuons bot, which runs on slack. Users can submit an anonymous confession through a slack modal, and pick where the confession will be posted, and allow everyone in that channel where its posted to anonymously indicate whether they relate or not.

To use this bot, use the unfortunately named command (story below haha): /uselesscmd67
Entering the command will open a modal, where the user can enter their anonymous confession, and pick where to post it


Running Locally:
(Prerequisites: Slack CLI installed.)
1. Clone this repository.
2. Open the project directory.
3. Install the project dependencies: pip install -r requirements.txt
4. Create and install your own copy of the Slack app using the Slack CLI: slack run

The Slack CLI will guide you through creating/installing the app in your own workspace if needed.
After installation, the bot will start and you can use the available slash commands in your workspace.

The stupidly simple fix to the bug that broke the programme:
/confess kept bringing up this error: /confess failed with the error "invalid_service"
i tried SO many things, taking SO much time, and nothing worked. i spent more time debugging this than full fletched projects with cad, code and pcbs.
this is until i made a new command, /uselesscmd67, which i linked it to the exact same thing /confess was meant to do AND IT WORKED (still had a bug but this one was much easier to fix)
as you can probably tell, i was NOT expecting this to work, and as a strong believer of if it works dont touch it, i am NOT changing that name, it is perfect as it is. if it works, it works :D.


FORGET ABOUT EVERYTH BELOW, BECAUSE IT WORKSSSSSSSSSSSS
(everything below is outdated, but i decided not to remove that because it reflects the frustration i had to go through to fix one bug that broke the entire code, and i can confirm that it does, in fact, work fully now, as intended.)
(sorry about the long readme, but below is just a rant on how much i struggled to fix my bug, its not really necassary to read it i left it there more for myself)


note: if the stars align and it somehow magically works on your end, EVERYTHING is untested, as i am unable to test them

note 2: because i made 2 bots in attempt of fixing this issue, i have completely lost track of which bot is which as they both have the same names, commands, and dont work. due to that, the submitted link may be wrong. please try both links, though neither may work.

possible link 1: https://app.slack.com/client/E09V59WQY1E/D0BCB6D088K (the one i submitted, may be wrong)

possible link 2: https://app.slack.com/client/E09V59WQY1E/D0BCM04CWBC (possibly the correct one tho i am not sure)

couldnt get it to work in socket mode, was incredibly frustrating to debug. spent over 6h trying everything i can find online of people getting similar issues but to no avail. also 0 documentation on the slack docs. some invalid_service error, i tried deleting the cache, deleting the app, reinstalling the code, redo on a fresh bot, revoking my tokens, and even resorting to ai to check my code, and the ai blamed the restrictions of the slack server and said my code was fine lol. unfortunately, without the working socket mode demo, i probably wouldnt be able to do a proper submission for this week. anyway, ill still describe what i was hoping to achieve with this.

Features:
/confess is supposed to open up a modal where the user could type an anonymous confession to be public to everyone on the server
users can have the option to also anonymously "relate" to the confession, and there is a counter to see how many people actually relates to it.
i managed to download it into the channel, and dm it but because of the error, is pretty useless lol

this was supposed to be a fun and simple project, but i have spent so much time trying to debug this error that i put more time into debugging than actually writing code and just the writing of code was my biggest Hack Club project ever, beating hardware projects with CAD, code and PCB. this obviously was extremely disappointing as the deadline is past and there is nothing i can do but accept that i have wasted time and that the past 7 weeks of work was (mostly) in vain as i REALLY wanted a raspberry pi lol. however, i learnt so much python in the process which was amnazing, so its not a complete waste haha.


the use of block kit was surprisingly easy, and i was pretty happy with what i managed to do:

<img width="1918" height="1148" alt="Screenshot 2026-06-22 115111" src="https://github.com/user-attachments/assets/e57b14ad-b01c-4f9a-917d-e5404240ca40" />

my error:

<img width="1366" height="897" alt="image" src="https://github.com/user-attachments/assets/065aa4e2-be5d-4586-8fea-93478c0414b9" />

absolutely 0 documentation:

<img width="1918" height="1198" alt="image" src="https://github.com/user-attachments/assets/c86208a3-d814-4234-8ec6-ebac8784b803" />

people with same issue with a known fix that still resulted in the same error for me:

<img width="1175" height="776" alt="image" src="https://github.com/user-attachments/assets/6999c155-6ea6-4bfd-a779-51d0416f151f" />


all in all i tried my absolute best to salvage something, but theres absolutely nothing i can do with no documentation, no time, and very limited time haha
