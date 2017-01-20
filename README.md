# Personal reflections about git/github

### Table of Contents

- [How does viewing a diff between two versions of a file help me see a bug that was introduced?](how-does-viewing-a-diff-between-two-versions-of-a-file-help-me-see-a-bug-that-was-introduced)
- [How could having easy access to the entire history of a file make me a more efficient programmer in the long term?](how-could-having-easy-access-to-the-entire-history-of-a-file-make-me-a-more-efficient-programmer-in-the-long-term)
- [As a programmer, when would I want to have a version of my code saved?](as-a-programmer--when-would-i-want-to-have-a-version-of-my-code-saved)
- [Pros and cons of manually creating commits vs automatically creating commits](pros-and-cons-of-manually-creating-commits-vs-automatically-creating-commits)
- [Why is it important to be able to save many files at once with one commit instead of being limited to 1 file save by commit?](why-is-it-important-to-be-able-to-save-many-files-at-once-with-one-commit-instead-of-being-limited-to-1-file-save-by-commit)
- [How can I use the commands git log and git diff to view the history of files?](how-can-i-use-the-commands-git-log-and-git-diff-to-view-the-history-of-files)
- [How might using version control make me more confident to make changes that could break something?](how-might-using-version-control-make-me-more-confident-to-make-changes-that-could-break-something)
- [What do I use Git for?](what-do-i-use-git-for)

VCS = Version Control System

## How does viewing a diff between two versions of a file help me see a bug that was introduced?

It reduces the necessary amount of time to fix a problem, allowing the programmer to compare 2 version of the code, for instance, a version that worked and a more recent version that doesn't work or that contains some bug. The programmer can then compare the two versions, see what changed and find the bug with more ease, since its very likely that the bug is in some of the lines that were modified.

===
## How could having easy access to the entire history of a file make me a more efficient programmer in the long term?

If I made a mistake I can go back to a previous working version or I can compare a working version with a non-working version and see what's differet and possibily spot the bug (easier than trying to figure out what is wrong in the non-working version without any kind of comparison).

It makes me, as a programmer, less scared to try something new, because I know that even if I mess up, I can always go back to a previous commit or just check-out the changes I made and compare using git diff to see the diferences between a working commit and a non-working commit, giving me a better perspective of the code and specially the modification in the commit so I can more easily spot the bug.

===
## As a programmer, when would I want to have a version of my code saved?

Sometimes I might make an important change and forget to save a version with the new important change, so in this case, it would be useful for my VCS to automatically save it for me.

But saving at every edit, I think, would consume unnecessary memory. I don't know how much memory it would consume, because depending on the memory available in the machine, it might not be relevant at all. Still, saving at each edit would create a lot of points in the version history, making it difficult to find a specific point in the version history to which I might want to go back. Also saving at every edit, is a function that wouldn't allow me to elaborate the change in the version description, so I would have a huge list of versions without a description to know what was changed. I would have to open each one and find what was changed. Very unnefective and time-consuming. Not good.

I think the best option is for the programmer to manually save and to create the habit of always saving the current version when he/she judges necessary, like after an important modification in the code.

===
## Pros and cons of manually creating commits vs automatically creating commits

Manual - Pros:
- Control over version history.
- Control over message associated with commit, explaining what the commit is about.
- Control over which changes to commit.

Manual - Cons:
- Risk of forgetting to commit and continue to make changes, making the changes bigger and possibly unrelated for the next commit.
- Consumes slight more time than automatic VCS.

Automatic pros and cons are opposite to the manual pros and cons.

===
## Why is it important to be able to save many files at once with one commit instead of being limited to 1 file save by commit?

Because some projects have multiple files inter-connected. This means that a modification in one of the files of such project is very likely to make necessary a change in the other files.

For ex.: If you have a variable defined in one file and used in other files and you change that variable name, you will need to make that change in all the other files.

So, tracking multiple files at once, is helpful so that you don't create conflicts frequently when changing these types of variables.

===
## How can I use the commands git log and git diff to view the history of files?

with git log I can see the history of all commits, their IDs, authors, date/time and message. Using the flag --stat will also show me the names of the files changed and how many they are and the amount of modifications (insertions and deletions) for each file.

with gif diff I can compare two commits to see how many modifications were made (insertions and deletions) and what exactly was modified (I can see the lines itself)

===
## How might using version control make me more confident to make changes that could break something?

VCS allow me to "go back in time" by giving me the option to make the repository (where the project files are) become what it was at the time of a specific commit.

So if I have 100 commits and I have a bug, I can go back to the 90th commit and the bug still exists it can mean a few things:

1. This commit introduced the bug.
2. All following commits will likely have the bug as well, unless I coincidentally changed something in the code that removed the bug.
3. The bug was introduced in an older commit.

Well, I can't assume its 1. or 2. I have to go to an older commit until I find one that doesn't have the bug so that I know exactly which commit introduced the bug.

If I keep going sequentially to an older commit, I will eventually find a commit that doesn't have the bug. When this happens, I will know that the bug is in the commit that came after the commit that doesn't have the bug.

===
## What do I use Git for?

To access, control and manipulate the versions of a project, as well as contributing and collaborating with other programmers.
