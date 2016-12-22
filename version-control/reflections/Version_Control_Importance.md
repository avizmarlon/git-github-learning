#How does viewing a diff between two versions of a file help me see a bug that was introduced?

It reduces the necessary amount of time to fix a problem, allowing the programmer to compare 2 version of the code, for instance, a version that worked and a more recent version that doesn't work or that contains some bug. The programmer can then compare the two versions, see what changed and find the bug with more ease, since its very likely that the bug is in some of the lines that were modified.

===
#How could having easy access to the entire history of a file make me a more efficient programmer in the long term?

If I made a mistake I can go back to a previous working version or I can compare a working version with a non-working version and see what's differet and possibily spot the bug (easier than trying to figure out what is wrong in the non-working version without any kind of comparison).

===
#As a programmer, when would I want to have a version of my code saved?

Sometimes I might make an important change and forget to save a version with the new important change, so in this case, it would be useful for my VCS to automatically save it for me.

But saving at every edit, I think, would consume unnecessary memory. I don't know how much memory it would consume, because depending on the memory available in the machine, it might not be relevant at all. Still, saving at each edit would create a lot of points in the version history, making it difficult to find a specific point in the version history to which I might want to go back. Also saving at every edit, is a function that wouldn't allow me to elaborate the change in the version description, so I would have a huge list of versions without a description to know what was changed. I would have to open each one and find what was changed. Very unnefective and time-consuming. Not good.

I think the best option is for the programmer to manually save and to create the habit of always saving the current version when he/she judges necessary, like after an important modification in the code.

===
#Pros and cons of manually creating commits vs automatically creating commits

Manual - Pros:
- Control over version history.
- Control over message associated with commit, explaining it.
- Control over which changes to commit.

Manual - Cons:
- Risk of forgetting to commit and continue to make changes, making the changes bigger and possibly unrelated for the next commit.
- Consumes slight more time than automatic VCS.

Automatic pros and cons are opposite to the Manual pros and cons.

