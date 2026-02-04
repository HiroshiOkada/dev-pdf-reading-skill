
import argparse
import sys
import io
import requests
from pdfminer.high_level import extract_text

def get_pdf_content(source):
    """
    Get PDF content as a file-like object (BytesIO) or file path.
    """
    if source.startswith("http://") or source.startswith("https://"):
        try:
            response = requests.get(source, stream=True)
            response.raise_for_status()
            return io.BytesIO(response.content)
        except requests.RequestException as e:
            print(f"Error fetching URL: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        return source

def main():
    parser = argparse.ArgumentParser(description="Extract text from a PDF file (local or remote).")
    parser.add_argument("source", help="Path to local PDF file or URL")
    parser.add_argument("--limit", type=int, default=None, help="Limit text extraction to the first N characters")
    
    args = parser.parse_args()

    try:
        pdf_file = get_pdf_content(args.source)
        
        # Optimization: If limit is small, we might only need the first few pages.
        # However, pdfminer extract_text maxpages is pages, not chars.
        # We'll just read everything or a conservative number of pages if we could guess.
        # But for now, we'll extract everything and slice, unless it's huge.
        # If we really wanted to be efficient we would iterate pages.
        # Let's simple slice for now as 'light' usually means 'don't use OCR'.
        
        # If limit is set and small (e.g. 1000), 5 pages is safe upper bound usually.
        maxpages = 0
        if args.limit and args.limit < 5000:
             maxpages = 5
             
        text = extract_text(pdf_file, maxpages=maxpages)
        
        if args.limit:
            print(text[:args.limit])
        else:
            print(text)
            
    except Exception as e:
        print(f"Error extracting text: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
