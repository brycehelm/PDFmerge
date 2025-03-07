import argparse
from PyPDF2 import PdfMerger

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description='Merge multiple PDF files into one.')
    parser.add_argument('output', help='Output PDF file name')
    parser.add_argument('inputs', nargs='+', help='Input PDF files')
    args = parser.parse_args()

    # Get the list of input PDF files and the output file name from arguments
    pdf_files = args.inputs
    output_file = args.output

    # Create a PdfMerger object
    merger = PdfMerger()

    # Append each PDF file to the merger
    for pdf in pdf_files:
        try:
            merger.append(pdf)
        except FileNotFoundError:
            print(f"File not found: {pdf}")
        except Exception as e:
            print(f"Error appending {pdf}: {e}")

    # Write the merged PDF to the output file
    try:
        merger.write(output_file)
        print(f"PDFs merged successfully into {output_file}")
    except Exception as e:
        print(f"Error writing to {output_file}: {e}")
    finally:
        # Ensure the merger is closed to free resources
        merger.close()

if __name__ == '__main__':
    main()