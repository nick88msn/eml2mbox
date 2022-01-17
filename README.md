# Eml2mbox
A script to convert eml files from various email export systems into an mbox file to be imported inside Thunderbird Apple Mail etc.

## Need
While gmail and other major email service providers let us export directly into an mbox folder, most webmail systems exports emails into a zip folder containing a bunch of eml files.
Apple Mail, Thunderbird etc imports mailboxes rather than single email files. This email client are the best option to keep our email archive organized and searchable.
Single eml files are usually named after the original email subject. Content is usually not indexed and these files need to be opened one by one.

## Starting point (2021-05-26)
Starting from a gist found on github [Kadin - kadin2048](https://gist.github.com/kadin2048/c332a572a388acc22d56).

I'll try to test if the script works refactor it and add more features.

If you want to know more about mailboxes in Python [Official Docs](https://docs.python.org/3/library/mailbox.html#mbox)

## Current usage
The script accepts as an input either a single eml file or a directory.
It then creates a new mbox folder or append to an existing one in the output path provided by the user.
Once you get your output mbox rename it as you prefer and import inside your preferite Email Client. 

## Todos
1. Ability to provide a folder with subfolders and get multiple mbox (e.g. inbox, sent, drafts)
1. Ability to pass the output filename if provided or a default output.mbox in the script root folder if nothing is passed as second argument
1. Add performance logging
1. Add informational logging to be more user friendly
