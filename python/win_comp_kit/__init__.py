import pkg_resources

def where():
    return pkg_resources.resource_filename(__name__, "")

