-------How to Use the Script----------

Save the Script: Copy the code above into a file, for example, merge_pdfs.py.
Prepare Your PDFs: Ensure you have your PDF files ready. They can be named anything, but you'll need to know their file names or paths. For example, let's assume they are named file1.pdf, file2.pdf, ..., file15.pdf and are in the same directory as your script.
Run the Script: Open a terminal or command prompt, navigate to the directory containing your script and PDF files, and run the script with the following command:


---------------bash-------------------

python merge_pdfs.py merged.pdf file1.pdf file2.pdf file3.pdf file4.pdf file5.pdf file6.pdf file7.pdf file8.pdf file9.pdf file10.pdf file11.pdf file12.pdf file13.pdf file14.pdf file15.pdf

merged.pdf is the name of the output file where all PDFs will be combined.
file1.pdf through file15.pdf are the input PDF files you want to merge, listed in the order you want them to appear in the final PDF.


-------------Features-----------------

Flexibility: The script accepts any number of input PDFs (not just 15), thanks to the nargs='+' parameter in argparse.
Error Handling: It handles common errors like missing files (FileNotFoundError) or issues reading PDFs, printing error messages without crashing.
Feedback: After merging, it confirms success with a message or reports any errors during the writing process.
Resource Management: The merger.close() call ensures resources are freed, even if an error occurs during writing.


----------------Notes-----------------

File Order: The PDFs are merged in the order they are listed in the command. Make sure to list them in your desired sequence.
File Paths: If your PDFs are in a different directory, provide the relative or absolute paths (e.g., pdfs/file1.pdf).
Permissions: Ensure the script has permission to read the input files and write to the output location.
PDF Properties: The script preserves the original page sizes, orientations, bookmarks, and metadata from the input PDFs.