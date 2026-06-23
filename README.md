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
