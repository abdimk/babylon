#class that takes emoji as inpute and gives translation key as output
'''
if the user enters that emoji you can change the destnation(dest) of the Translator class as well as the sorce(src) by simply importing the class and creating an object like
import FlagTrans

'''
class FlagTrans:
    def __init__(self, user_input):
        self.user_input = user_input

    def flag_trans(self):
        afrikaans = ['🇿🇦']
        if self.user_input in afrikaans:
            user_dest = 'af'
            return user_dest
        albanian = ['🇦🇱', '🇽🇰', '🇲🇪']
        if self.user_input in albanian:
            user_dest = 'sq'
            return user_dest
        amharic = ['🇪🇷', '🇪🇹']
        if self.user_input in amharic:
            user_dest = 'am'
            return user_dest
        arabic = ['🇩🇿', '🇧🇭', '🇹🇩', '🇰🇲', '🇩🇯', '🇪🇬', '🇮🇶', '🇯🇴', '🇰🇼', '🇱🇧', '🇱🇾',
                  '🇲🇷', '🇲🇦', '🇴🇲', '🇵🇸', '🇶🇦', '🇸🇦', '🇸🇴', '🇸🇩', '🇸🇾', '🇹🇳', '🇦🇪', '🇾🇪']
        if self.user_input in arabic:
            user_dest = 'ar'
            return user_dest
        armenian = ['🇦🇲']
        if self.user_input in armenian:
            user_dest = 'hy'
            return user_dest
        azerbaijani = ['🇦🇿']
        if self.user_input in azerbaijani:
            user_dest = 'az'
            return user_dest
        bengali = ['🇧🇩']
        if self.user_input in bengali:
            user_dest = 'bn'
            return user_dest
        bosnian = ['🇧🇦']
        if self.user_input in bosnian:
            user_dest = 'bs'
            return user_dest
        bulgarian = ['🇧🇬']
        if self.user_input in bulgarian:
            user_dest = 'bg'
            return user_dest
        catalan = ['🇦🇩']
        if self.user_input in catalan:
            user_dest = 'ca'
            return user_dest
        chichewa = ['🇲🇼']
        if self.user_input in chichewa:
            user_dest = 'ny'
        chinese_simplified = ['🇨🇳', '🇹🇼']
        if self.user_input in chinese_simplified:
            user_dest = 'zh-cn'
            return user_dest
        croatian = ['🇭🇷']
        if self.user_input in croatian:
            user_dest = 'hr'
            return user_dest
        danish = ['🇧🇪', '🇩🇰', '🇳🇱']
        if self.user_input in danish:
            user_dest = 'da'
            return user_dest
        dutch = ['🇸🇷']
        if self.user_input in dutch:
            user_dest = 'nl'
            return user_dest
        english = ['🇦🇬', '🇦🇺', '🇧🇸', '🇧🇧', '🇧🇿', '🇧🇼', '🇨🇲', '🇨🇦', '🇩🇲', '🇸🇿', '🇬🇲', '🇬🇭', '🇬🇩', '🇬🇾', '🇭🇰', '🇯🇲', '🇰🇪', '🇰🇮', '🇱🇸', '🇱🇷', '🇲🇭',
                   '🇳🇦', '🇳🇷', '🇳🇬', '🇵🇼', '🇵🇬', '🇰🇳', '🇱🇨', '🇻🇨', '🇼🇸', '🇸🇨', '🇸🇱', '🇸🇧', '🇸🇸', '🇹🇿', '🇹🇴', '🇹🇹', '🇹🇻', '🇺🇬', '🇬🇧', '🇺🇸', '🇻🇺', '🇿🇲', '🇿🇼']
        if self.user_input in english:
            user_dest = 'en'
            return user_dest
        estonian = ['🇪🇪']
        if self.user_input in estonian:
            user_dest = 'et'
            return user_dest
        filipino = ['🇵🇭']
        if self.user_input in filipino:
            user_dest = 'tl'
            return user_dest
        finnish = ['🇫🇮']
        if self.user_input in finnish:
            user_dest = 'fi'
            return user_dest
        french = ['🇧🇯', '🇧🇫', '🇧🇮', '🇨🇫', '🇨🇩', '🇬🇶', '🇫🇷',
                  '🇬🇦', '🇬🇳', '🇲🇱', '🇲🇨', '🇳🇪', '🇸🇳', '🇨🇭', '🇹🇬']
        if self.user_input in french:
            user_dest = 'fr'
            return user_dest
        georgian = ['🇬🇪']
        if self.user_input in georgian:
            user_dest = 'ka'
            return user_dest
        german = ['🇦🇹', '🇩🇪', '🇱🇮']
        if self.user_input in german:
            user_dest = 'de'
            return user_dest
        greek = ['🇨🇾', '🇬🇷']
        if self.user_input in greek:
            user_dest = 'el'
            return user_dest
        haitian_creole = ['🇭🇹']
        if self.user_input in haitian_creole:
            user_dest = 'ht'
            return user_dest
        hebrew = ['🇮🇱']
        if self.user_input in hebrew:
            user_dest = 'iw'
            return user_dest
        hindi = ['🇮🇳']
        if self.user_input in hindi:
            user_dest = 'hi'
            return user_dest
        hungarian = ['🇭🇺']
        if self.user_input in hungarian:
            user_dest = 'hu'
            return user_dest
        icelandic = ['🇮🇸']
        if self.user_input in icelandic:
            user_dest = 'is'
            return user_dest
        indonesian = ['🇮🇩']
        if self.user_input in indonesian:
            user_dest = 'id'
            return user_dest
        irish = ['🇮🇪']
        if self.user_input in irish:
            user_dest = 'ga'
            return user_dest
        italian = ['🇮🇹', '🇸🇲', '🇻🇦']
        if self.user_input in italian:
            user_dest = 'it'
            return user_dest
        japanese = ['🇯🇵']
        if self.user_input in japanese:
            user_dest = 'ja'
            return user_dest
        kazakh = ['🇰🇿']
        if self.user_input in kazakh:
            user_dest = 'kk'
            return user_dest
        korean = ['🇰🇵', '🇰🇷']
        if self.user_input in korean:
            user_dest = 'ko'
            return user_dest
        kyrgyz = ['🇽🇰']
        if self.user_input in kyrgyz:
            user_dest = 'ky'
            return user_dest
        lao = ['🇱🇦']
        if self.user_input in lao:
            user_dest = 'lo'
            return user_dest
        latvian = ['🇱🇻']
        if self.user_input in latvian:
            user_dest = 'lv'
            return user_dest
        lithuanian = ['🇱🇹']
        if self.user_input in lithuanian:
            user_dest = 'lt'
            return user_dest
        luxembourgish = ['🇱🇺']
        if self.user_input in luxembourgish:
            user_dest = 'lb'
            return user_dest
        malagasy = ['🇲🇬']
        if self.user_input in malagasy:
            user_dest = 'mg'
            return user_dest
        malay = ['🇧🇳', '🇲🇾']
        if self.user_input in malay:
            user_dest = 'ms'
            return user_dest
        maltese = ['🇲🇹']
        if self.user_input in maltese:
            user_dest = 'mt'
            return user_dest
        maori = ['🇳🇿']
        if self.user_input in maori:
            user_dest = 'mi'
            return user_dest
        mongolian = ['🇲🇳']
        if self.user_input in mongolian:
            user_dest = 'mn'
            return user_dest
        nepali = ['🇳🇵']
        if self.user_input in nepali:
            user_dest = 'ne'
            return user_dest
        norwegian = ['🇳🇴']
        if self.user_input in norwegian:
            user_dest = 'no'
            return user_dest
        pashto = ['🇦🇫']
        if self.user_input in pashto:
            user_dest = 'ps'
            return user_dest
        persian = ['🇮🇷']
        if self.user_input in persian:
            user_dest = 'fa'
            return user_dest
        polish = ['🇵🇱']
        if self.user_input in polish:
            user_dest = 'pl'
            return user_dest
        portuguese = ['🇦🇴', '🇧🇷', '🇨🇻''🇬🇼', '🇲🇴', '🇲🇿', '🇵🇹', '🇸🇹']
        if self.user_input in portuguese:
            user_dest = 'pt'
            return user_dest
        romanian = ['🇲🇩', '🇷🇴']
        if self.user_input in romanian:
            user_dest = 'ro'
            return user_dest
        russian = ['🇰🇬', '🇷🇺']
        if self.user_input in russian:
            user_dest = 'ru'
            return user_dest
        serbian = ['🇷🇸']
        if self.user_input in serbian:
            user_dest = 'sr'
            return user_dest
        sinhala = ['🇱🇰']
        if self.user_input in sinhala:
            user_dest = 'si'
            return user_dest
        slovak = ['🇨🇿', '🇸🇰']
        if self.user_input in slovak:
            user_dest = 'sk'
            return user_dest
        slovenian = ['🇸🇮']
        if self.user_input in slovenian:
            user_dest = 'sl'
            return user_dest
        spanish = ['🇦🇷', '🇨🇴', '🇨🇷', '🇨🇺', '🇩🇴', '🇪🇨', '🇸🇻', '🇬🇹',
                   '🇭🇳', '🇲🇽', '🇳🇮', '🇵🇦', '🇵🇾', '🇵🇪', '🇪🇸', '🇺🇾', '🇻🇪']
        if self.user_input in spanish:
            user_dest = 'es'
            return user_dest
        swahili = ['🇷🇼']
        if self.user_input in swahili:
            user_dest = 'sw'
            return user_dest
        swedish = ['🇸🇪']
        if self.user_input in swedish:
            user_dest = 'sv'
            return user_dest
        tajik = ['🇹🇯']
        if self.user_input in tajik:
            user_dest = 'tg'
            return user_dest
        tamil = ['🇸🇬']
        if self.user_input in tamil:
            user_dest = 'ta'
            return user_dest
        thai = ['🇹🇭']
        if self.user_input in thai:
            user_dest = 'th'
            return user_dest
        ukrainian = ['🇺🇦']
        if self.user_input in ukrainian:
            user_dest = 'uk'
            return user_dest
        urdu = ['🇵🇰']
        if self.user_input in urdu:
            user_dest = 'ur'
            return user_dest
        uzbek = ['🇺🇿']
        if self.user_input in uzbek:
            user_dest = 'uz'
            return user_dest
        vietnamese = ['🇻🇳']
        if self.user_input in vietnamese:
            user_dest = 'vi'
            return user_dest
        else:
            return 'invalid destnation'
        
        
        
def return_message(input):
    p = FlagTrans(input)
    message = p.flag_trans()
    return message
