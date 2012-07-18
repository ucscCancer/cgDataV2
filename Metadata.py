
class Metadata():
    """This class describes the basic metadata associated with each class.  Each
    class type has its own type of metadata, but there are some elements common to
    all metadata types
    """

    def __init__(self, filename, validate=True):
        """Given the pathname of a metadata file, return the corresponding
        metadata object.  By default, run the validator method on the new
        object and return None if validation fails.
        """

    def type(self, newType=None):
        """Update the type if type is specified
        Return the metadata type. """

    def version(self, newVersion=None):
        """
        Update the version if a new version is specified
        Return the metadata version.
        """

    def shortTitle(self, newShortTitle=None):
        """
        The shortTitle is a short description of the object.
        Update the shortTitle if a new shortTitle is specified.
        Return the shortTitle if defined, or None if undefined.
        """

    def longTitle(self, newLongTitle=None):
        """
        The longTitle is a longer description of the object.
        Update the longTitle if a new longTitle is specified.
        Return the longTitle if defined, or None if undefined.
        """

    def description(self, newDescription=None):
        """
        The description is a text string detailing the object.
        Update the description if a new description is specified.
        Return the description if defined, or None if undefined.
        """

    def validate(self):
        """Validate the fields expected in all metadata objects.  Return
        True if the validation is successful, False otherwise
        """

    def write(self, filename):
        """Write the metadata object to the specified filename"""
