import time

class txtTime:
    __localTime = None
    __ascTime = None
    __timeOfDay = None
    __h,__m,__s = None,None,None
    __conversions = None
    

    def __init__(self,localTime):
        self.__localTime = localTime
        self.__ascTime = time.asctime(self.__localTime)
        self.__timeOfDay = self.__ascTime.split(' ')[3]
        self.__h,self.__m,self.__s = self.__timeOfDay.split(':')
        self.__conversions = [
            ("00","zero zero"),
            ("01","o'one"),
            ("02","o'two"),
            ("03","o'three"),
            ("04","o'four"),
            ("05","o'five"),
            ("06","o'six"),
            ("07","o'seven"),
            ("08","o'eight"),
            ("09","o'nine"),
            ("10","ten"),
            ("11","eleven"),
            ("12","twelve"),
            ("13","thirteen"),
            ("14","fourteen"),
            ("15","fifteen"),
            ("16","sixteen"),
            ("17","seventeen"),
            ("18","eighteen"),
            ("19","nineteen"),
            ("20","twenty"),
            ("21","twenty-one"),
            ("22","twenty-two"),
            ("23","twenty-three"),
            ("24","twenty-four"),
            ("25","twenty-five"),
            ("26","twenty-six"),
            ("27","twenty-seven"),
            ("28","twenty-eight"),
            ("29","twenty-nine"),
            ("30","thirty"),
            ("31","thirty-one"),
            ("32","thirty-two"),
            ("33","thirty-three"),
            ("34","thirty-four"),
            ("35","thirty-five"),
            ("36","thirty-six"),
            ("37","thirty-seven"),
            ("38","thirty-eight"),
            ("39","thirty-nine"),
            ("40","forty"),
            ("41","forty-one"),
            ("42","forty-two"),
            ("43","forty-three"),
            ("44","forty-four"),
            ("45","forty-five"),
            ("46","forty-six"),
            ("47","forty-seven"),
            ("48","forty-eight"),
            ("49","forty-nine"),
            ("50","fifty"),
            ("51","fifty-one"),
            ("52","fifty-two"),
            ("53","fifty-three"),
            ("54","fifty-four"),
            ("55","fifty-five"),
            ("56","fifty-six"),
            ("57","fifty-seven"),
            ("58","fifty-eight"),
            ("59","fifty-nine"),
        ]

    def __convert(self,number):
        timeStr = ''
        for pair in self.__conversions:
            if(pair[0] == number):
                timeStr = pair[1]
        return timeStr

    def printTime(self):
        hour = self.__convert(self.__h)
        minute = self.__convert(self.__m)
        second = self.__convert(self.__s)
        print(hour + ' ' + minute + ' ' + second)


#--------- How to use -------------------------------------------#
localTime = time.localtime(time.time())
classObject = txtTime(localTime)
txtTime.printTime(classObject)
#--------- How to use -------------------------------------------#