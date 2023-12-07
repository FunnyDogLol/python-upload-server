# python-upload-server

Use this command to upload files to it:

Invoke-WebRequest -Uri "http://example.com:81/" -Method Post -InFile file.txt -Headers @{ 'filename' = 'filename.txt' }

curl -X POST -H "filename: filename.txt" -T /path/to/file http://example.com:81/

you need to add the filename header, as this is what the script uses to name the file it creates.
