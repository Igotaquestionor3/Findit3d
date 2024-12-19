import os

def make_site_blue(directory):
    """Makes all HTML files in a directory (and subdirectories) have a blue background."""

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        content = f.read()

                    # Inject CSS to set background color to blue
                    if "<head>" in content: # Check if <head> tag exists
                        head_end_index = content.find("</head>")
                        if head_end_index != -1:
                            style_tag = '<style>\nbody {\n  background-color: lightblue;\n}\n</style>\n'
                            new_content = content[:head_end_index] + style_tag + content[head_end_index:]
                            
                            with open(filepath, "w", encoding="utf-8") as f:
                                f.write(new_content)
                            print(f"Modified: {filepath}")
                        else:
                            print(f"Warning: Could not find </head> in {filepath}. Skipping.")
                    else:
                        print(f"Warning: Could not find <head> in {filepath}. Skipping.")
                except (UnicodeDecodeError, OSError) as e:
                    print(f"Error processing {filepath}: {e}")


if __name__ == "__main__":
    site_directory = "."  # Current directory. Change this if your site is in a subdirectory.
    make_site_blue(site_directory)
    print("Finished processing files.")
