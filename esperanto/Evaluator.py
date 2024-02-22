from lark import Transformer, v_args

@v_args(inline=True)
class Evaluator(Transformer):

    def start(self, expr):
        return expr

    def expr(self, operations):
        return operations

    def operations(self, op):
        return op

    def count(self, filename):
        with open(filename) as f:
            text = f.read()
        format_response = f"""The file {filename} have {len(text.split(" "))} words"""
        return format_response

    def translate(self, from_lang, to_lang, filename_from, filename_to):
        from deep_translator import GoogleTranslator
        
        with open(filename_from) as f:
            text = f.read()
            from_lang_sanityzed = from_lang.replace('"','')
            to_lang_sanityzed = to_lang.replace('"','')
            result = GoogleTranslator(source=from_lang_sanityzed, target=to_lang_sanityzed).translate(text)

        with open(filename_to, 'w') as f:
            f.write(result)
        
    def audio(self, filename_token, aud_token):
        from gtts import gTTS
        import os
        filename = filename_token.value[1:-1]
        aud = aud_token.value[1:-1]  # 
        with open(filename) as f:
            text = f.read()
            tts = gTTS(text=text, lang="es")
            tts.save(aud)

    def filename(self, fname):
        return fname