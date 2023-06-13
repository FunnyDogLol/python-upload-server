# python-upload-server

Use this command to upload files to it:

Invoke-WebRequest -Uri "http://example.com/" -Method Post -InFile file.txt -Headers @{ 'filename' = 'filename.txt' }

you need to add the filename header, as this is what the script uses to name the file it creates.
