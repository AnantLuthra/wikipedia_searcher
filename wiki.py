import wikipedia

class Wiki:
    """
    This Wiki class have functions for searching wikipedia.
    """

    @staticmethod
    def search_wiki(search:str, sentences:int=10) -> str:
        """
        This function searches wikipedia through wikipedia library
         It takes two arguments: 
        search = String data which you want to search about on wikipedia
         sentences = An Integer of how much lines you want data from wikipedia.

        return value = It returns sentences of line as a string.
        """

        try:
            return wikipedia.summary(search, sentences=sentences, features="lxml")

        except wikipedia.exceptions.PageError:
            print("Couldn't find about the given data.")
