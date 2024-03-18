xpath_1 = "//span[contains(text(),'Версия iOS') or contains(text(),'Версия Android')]/../following-sibling::*" 

xpath_2 = "//span[contains(translate(text(), 'ОПЕРАЦИОННАЯСИСТЕМА', 'операционнаясистема'),'операционная система -') or contains(text(), 'ОС')]"

xpath_3 = "//span[contains(text(), '> OS -')]"


filters = [xpath_1, xpath_2, xpath_3]  