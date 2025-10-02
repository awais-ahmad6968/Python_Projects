import google.generativeai as genai


class gemini_model:
    __geminiApi="AIzaSyADSpASVc0gsvwfaviDwPzM7iHmlbtZikE"

    def __init__(self,model):
        self.model=genai.GenerativeModel(model)
        genai.configure(api_key =self.__geminiApi)



