def zip_write_str(zipf, name, content):
    zipf.writestr(name, content)
    return zipf

def zip_write(zipf, name, content):
    zipf.write(name, content)
    return zipf