from ..src import file_handler, file, text_file

if __name__ == "__main__":
    # Get the content of a file from start to stop bytes (rb)
    file_content = file_handler.read_file("file_path")
    # Write the content to a file between start and stop bytes (wb)
    file_handler.write_file("file_path", file_content)

    general_file = file.File("file_path")
    general_file.read()  # Read file into internal buffer
    general_file.write()  # Write internal buffer into file
    general_file.buffer  # Acces buffer property (bytes)
    general_file.path  # Access path property

    text_file = text_file.TextFile("file_path")
    text_file.read()  # Read file into internal buffer
    text_file.write()  # Write internal buffer into file
    text_file.buffer  # Acces buffer property (str)
    text_file.path  # Access path property
    text_file.encoding  # Access encoding of buffer (str <-> bytes)
