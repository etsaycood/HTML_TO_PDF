import os
from pypdf import PdfWriter

def merge_pdfs():
    current_dir = os.getcwd()
    # Find all PDF files
    pdf_files = [f for f in os.listdir(current_dir) if f.endswith('.pdf')]
    
    # Exclude the output file if it already exists to avoid recursive merging
    output_filename = "merged_output.pdf"
    if output_filename in pdf_files:
        pdf_files.remove(output_filename)

    if not pdf_files:
        print("No PDF files found to merge.")
        return

    # Sort files to ensure correct order
    # This simple sort works if filenames are like page_001, page_002, etc.
    pdf_files.sort()
    
    print(f"Found {len(pdf_files)} PDF files. Merging...")

    merger = PdfWriter()

    for filename in pdf_files:
        print(f"Adding {filename}...")
        try:
            merger.append(os.path.join(current_dir, filename))
        except Exception as e:
            print(f"Error adding {filename}: {e}")

    output_path = os.path.join(current_dir, output_filename)
    merger.write(output_path)
    merger.close()
    
    print(f"\nSuccessfully created: {output_filename}")

if __name__ == "__main__":
    merge_pdfs()
