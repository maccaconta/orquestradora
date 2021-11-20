from django.core.management.base import BaseCommand
from middle.models import CountryCode


class Command(BaseCommand):
    help = 'Valor default da configuração dos códigos para paises'

    def handle(self, **options):
        self.stdout.write('Deletando dados de códigos dos paises')
        CountryCode.objects.all().delete()

        self.stdout.write('Criando dados códigos dos paises')
        	
        CountryCode.objects.create(country_code="P0010", 
                                country_name="AFEGANISTÃO")
            
        CountryCode.objects.create(country_code="P0020", 
                                country_name="ÁFRICA DO SUL")
            
        CountryCode.objects.create(country_code="P0030", 
                                country_name="ALBÂNIA")
            
        CountryCode.objects.create(country_code="P0040", 
                                country_name="ALEMANHA")
            
        CountryCode.objects.create(country_code="P0050", 
                                country_name="ALEMANHA DEMOCRÁTICA")
            
        CountryCode.objects.create(country_code="P0060", 
                                country_name="ALEMANHA FEDERAL")
            
        CountryCode.objects.create(country_code="P0070", 
                                country_name="ALTO VOLTA")
            
        CountryCode.objects.create(country_code="P0080", 
                                country_name="ANDORRA")
            
        CountryCode.objects.create(country_code="P0100", 
                                country_name="ANGOLA")
            
        CountryCode.objects.create(country_code="P0090", 
                                country_name="ANGUILLA")
            
        CountryCode.objects.create(country_code="P0110", 
                                country_name="ANTÍGUA E BARBUDA")
            
        CountryCode.objects.create(country_code="P0120", 
                                country_name="ANTILHAS HOLANDESAS")
            
        CountryCode.objects.create(country_code="P0130", 
                                country_name="ARÁBIA SAUDITA")
            
        CountryCode.objects.create(country_code="P0140", 
                                country_name="ARGÉLIA")
            
        CountryCode.objects.create(country_code="P0150", 
                                country_name="ARGENTINA")
            
        CountryCode.objects.create(country_code="P0170", 
                                country_name="ARMÊNIA")

        CountryCode.objects.create(country_code="P0160", 
                                country_name="ARQUIPÉLAGO DE SAN ANDRES PROVIDÊNCIA E SANTA CATALINA")
            
        CountryCode.objects.create(country_code="P0180", 
                                country_name="ARUBA")
            
        CountryCode.objects.create(country_code="P0190", 
                                country_name="AUSTRÁLIA")
            
        CountryCode.objects.create(country_code="P0200", 
                                country_name="ÁUSTRIA")
            
        CountryCode.objects.create(country_code="P0210", 
                                country_name="AZERBAIDJÃO")
            
        CountryCode.objects.create(country_code="P0220", 
                                country_name="BAHAMAS")
            
        CountryCode.objects.create(country_code="P0230", 
                                country_name="BANGLADESH")
            
        CountryCode.objects.create(country_code="P0240", 
                                country_name="BARBADOS")
            
        CountryCode.objects.create(country_code="P0250", 
                                country_name="BARÉM ou BAREINE ou BAIREIN")
            
        CountryCode.objects.create(country_code="P0260", 
                                country_name="BÉLGICA")
            
        CountryCode.objects.create(country_code="P0270", 
                                country_name="BELIZE")
            
        CountryCode.objects.create(country_code="P0290", 
                                country_name="BENIN")
            
        CountryCode.objects.create(country_code="P0280", 
                                country_name="BERMUDAS")

        CountryCode.objects.create(country_code="P0300", 
                                country_name="BIELO-RÚSSIA (BELARUS)")
            
        CountryCode.objects.create(country_code="P0310", 
                                country_name="BIRMÂNIA")
            
        CountryCode.objects.create(country_code="P0320", 
                                country_name="BOLÍVIA")
            
        CountryCode.objects.create(country_code="P0330", 
                                country_name="BOSNIA-HERZEGÓVINA")

        CountryCode.objects.create(country_code="P0340", 
                                country_name="BOTSUANA (BOTSWANA)")
            
        CountryCode.objects.create(country_code="P0350", 
                                country_name="BRUNEI")
            
        CountryCode.objects.create(country_code="P0360", 
                                country_name="BULGÁRIA")
            
        CountryCode.objects.create(country_code="P0370", 
                                country_name="BURMA")
            
        CountryCode.objects.create(country_code="P0380", 
                                country_name="BURQUINA FASO ou BURKINA")
            
        CountryCode.objects.create(country_code="P0390", 
                                country_name="BURUNDI")
            
        CountryCode.objects.create(country_code="P0400", 
                                country_name="BUTAO")
            
        CountryCode.objects.create(country_code="P0410", 
                                country_name="CABO VERDE")

        CountryCode.objects.create(country_code="P0420", 
                                country_name="CAMARÕES (CAMEROUN)")
            
        CountryCode.objects.create(country_code="P0430", 
                                country_name="CAMBODJA ou CAMPUCHÉIA")
            
        CountryCode.objects.create(country_code="P0440", 
                                country_name="CANADÁ")
            
        CountryCode.objects.create(country_code="P0460", 
                                country_name="CASAQUISTÃO")
            
        CountryCode.objects.create(country_code="P0450", 
                                country_name="CATAR")
            
        CountryCode.objects.create(country_code="P0470", 
                                country_name="CAYMAN")
            
        CountryCode.objects.create(country_code="P0480", 
                                country_name="CEILÃO")
            
        CountryCode.objects.create(country_code="P0490", 
                                country_name="CEUTA E MELILLA")
            
        CountryCode.objects.create(country_code="P0500", 
                                country_name="CHADE")
            
        CountryCode.objects.create(country_code="P0510", 
                                country_name="CHILE")
            
        CountryCode.objects.create(country_code="P0520", 
                                country_name="CHINA")
            
        CountryCode.objects.create(country_code="P0530", 
                                country_name="CHINA NACIONALISTA")
            
        CountryCode.objects.create(country_code="P0540", 
                                country_name="CHIPRE")
            
        CountryCode.objects.create(country_code="P0550", 
                                country_name="CINGAPURA")
            
        CountryCode.objects.create(country_code="P0560", 
                                country_name="COLÔMBIA")
            
        CountryCode.objects.create(country_code="P0570", 
                                country_name="CONGO")
            
        CountryCode.objects.create(country_code="P0580", 
                                country_name="CORÉIA DO NORTE")
            
        CountryCode.objects.create(country_code="P0590", 
                                country_name="CORÉIA DO SUL")
            
        CountryCode.objects.create(country_code="P0600", 
                                country_name="COSTA DO MARFIM")
            
        CountryCode.objects.create(country_code="P0610", 
                                country_name="COSTA RICA")
            
        CountryCode.objects.create(country_code="P0620", 
                                country_name="CÔTE D'IVOIRE")
            
        CountryCode.objects.create(country_code="P0630", 
                                country_name="COVEITE")
            
        CountryCode.objects.create(country_code="P0640", 
                                country_name="CROÁCIA")
            
        CountryCode.objects.create(country_code="P0650", 
                                country_name="CUBA")
            
        CountryCode.objects.create(country_code="P0660", 
                                country_name="DINAMARCA")
            
        CountryCode.objects.create(country_code="P0670", 
                                country_name="DJIBUTI")
            
        CountryCode.objects.create(country_code="P0680", 
                                country_name="DOMINICA")
            
        CountryCode.objects.create(country_code="P0690", 
                                country_name="EGITO")
            
        CountryCode.objects.create(country_code="P0700", 
                                country_name="EL SALVADOR")
            
        CountryCode.objects.create(country_code="P0710", 
                                country_name="EMIRADOS ÁRABES UNIDOS")
            
        CountryCode.objects.create(country_code="P0720", 
                                country_name="EQUADOR")
            
        CountryCode.objects.create(country_code="P0730", 
                                country_name="ERITRÉIA")
            
        CountryCode.objects.create(country_code="P0740", 
                                country_name="ESCÓCIA")
            
        CountryCode.objects.create(country_code="P0750", 
                                country_name="ESLOVÊNIA")
            
        CountryCode.objects.create(country_code="P0760", 
                                country_name="ESPANHA")
            
        CountryCode.objects.create(country_code="P0770", 
                                country_name="ESTADOS UNIDOS")
            
        CountryCode.objects.create(country_code="P0780", 
                                country_name="ESTÔNIA")
            
        CountryCode.objects.create(country_code="P0790", 
                                country_name="ETIÓPIA")
            
        CountryCode.objects.create(country_code="P0800", 
                                country_name="FIJI ou FIDJI")
            
        CountryCode.objects.create(country_code="P0810", 
                                country_name="FILIPINAS")
            
        CountryCode.objects.create(country_code="P0820", 
                                country_name="FINLÂNDIA")
            
        CountryCode.objects.create(country_code="P0830", 
                                country_name="FORMOSA")
            
        CountryCode.objects.create(country_code="P0840", 
                                country_name="FRANÇA")
            
        CountryCode.objects.create(country_code="P0850", 
                                country_name="GABÃO")
            
        CountryCode.objects.create(country_code="P0860", 
                                country_name="GÂMBIA")
            
        CountryCode.objects.create(country_code="P0870", 
                                country_name="GANA")
            
        CountryCode.objects.create(country_code="P0880", 
                                country_name="GEÓRGIA")
            
        CountryCode.objects.create(country_code="P0890", 
                                country_name="GIBRALTAR")
            
        CountryCode.objects.create(country_code="P0910", 
                                country_name="GRÃ-BRETANHA")
            
        CountryCode.objects.create(country_code="P0900", 
                                country_name="GRANADA")
            
        CountryCode.objects.create(country_code="P0920", 
                                country_name="GRÉCIA")
            
        CountryCode.objects.create(country_code="P0930", 
                                country_name="GROENLÂNDIA")
            
        CountryCode.objects.create(country_code="P0940", 
                                country_name="GUADALUPE")
            
        CountryCode.objects.create(country_code="P0950", 
                                country_name="GUAM")
            
        CountryCode.objects.create(country_code="P0960", 
                                country_name="GUATEMALA")
            
        CountryCode.objects.create(country_code="P0970", 
                                country_name="GUIANA")
            
        CountryCode.objects.create(country_code="P0980", 
                                country_name="GUIANA FRANCESA")

        CountryCode.objects.create(country_code="P0990", 
                                country_name="GUINÉ")

        CountryCode.objects.create(country_code="P1010", 
                                country_name="GUINÉ EQUATORIAL")

        CountryCode.objects.create(country_code="P1000", 
                                country_name="GUINÉ-BISSAU")

            
        CountryCode.objects.create(country_code="P1020", 
                                country_name="HAITI")

            
        CountryCode.objects.create(country_code="P1030", 
                                country_name="HOLANDA")

            
        CountryCode.objects.create(country_code="P1040", 
                                country_name="HONDURAS")

            
        CountryCode.objects.create(country_code="P1050", 
                                country_name="HONG KONG")

            
        CountryCode.objects.create(country_code="P1060", 
                                country_name="HUNGRIA")

            
        CountryCode.objects.create(country_code="P1070", 
                                country_name="IÊMEM DO NORTE")

            
        CountryCode.objects.create(country_code="P1080", 
                                country_name="IÊMEM DO SUL")

            
        CountryCode.objects.create(country_code="P1090", 
                                country_name="ILHA DE MAN")

            
        CountryCode.objects.create(country_code="P1100", 
                                country_name="ILHA DE PITCAIRN")

            
        CountryCode.objects.create(country_code="P1110", 
                                country_name="ILHA JOHNSTON")

            
        CountryCode.objects.create(country_code="P1120", 
                                country_name="ILHA NORFOLK")

            
        CountryCode.objects.create(country_code="P1130", 
                                country_name="ILHA WAKE")

            
        CountryCode.objects.create(country_code="P1140", 
                                country_name="ILHAS ALAND")

            
        CountryCode.objects.create(country_code="P1150", 
                                country_name="ILHAS CAYMAN")

        CountryCode.objects.create(country_code="P1160", 
                                country_name="ILHAS COCOS (KEELING)")

            
        CountryCode.objects.create(country_code="P1170", 
                                country_name="ILHAS COMORES")

            
        CountryCode.objects.create(country_code="P1180", 
                                country_name="ILHAS COOK")

            
        CountryCode.objects.create(country_code="P1190", 
                                country_name="ILHAS DO CANAL")

            
        CountryCode.objects.create(country_code="P1200", 
                                country_name="ILHAS FAROE")

            
        CountryCode.objects.create(country_code="P1210", 
                                country_name="ILHAS GEÓRGIA e SANDWICH DO SUL")

            
        CountryCode.objects.create(country_code="P1220", 
                                country_name="ILHAS MARIANAS DO NORTE")

            
        CountryCode.objects.create(country_code="P1230", 
                                country_name="ILHAS MARSHALL")

            
        CountryCode.objects.create(country_code="P1240", 
                                country_name="ILHAS MIDWAY")

            
        CountryCode.objects.create(country_code="P1250", 
                                country_name="ILHAS VIRGENS (EUA)")

        CountryCode.objects.create(country_code="P1260", 
                                country_name="ILHAS VIRGENS (GB)")

            
        CountryCode.objects.create(country_code="P1270", 
                                country_name="ILHAS WALLIS E FUTUNA")

            
        CountryCode.objects.create(country_code="P1280", 
                                country_name="ÍNDIA")

            
        CountryCode.objects.create(country_code="P1290", 
                                country_name="INDONÉSIA")

            
        CountryCode.objects.create(country_code="P1300", 
                                country_name="INGLATERRA")

            
        CountryCode.objects.create(country_code="P1310", 
                                country_name="IRÃ ou IRAN")

            
        CountryCode.objects.create(country_code="P1320", 
                                country_name="IRAQUE")

            
        CountryCode.objects.create(country_code="P1330", 
                                country_name="IRIÃ OCIDENTAL")

            
        CountryCode.objects.create(country_code="P1350", 
                                country_name="IRLANDA (SUL)")

            
        CountryCode.objects.create(country_code="P1340", 
                                country_name="IRLANDA DO NORTE")

            
        CountryCode.objects.create(country_code="P1360", 
                                country_name="ISLÂNDIA")

            
        CountryCode.objects.create(country_code="P1370", 
                                country_name="ISRAEL")

            
        CountryCode.objects.create(country_code="P1380", 
                                country_name="ITÁLIA")

            
        CountryCode.objects.create(country_code="P1390", 
                                country_name="IUGOSLÁVIA")

            
        CountryCode.objects.create(country_code="P1400", 
                                country_name="JAMAICA")

            
        CountryCode.objects.create(country_code="P1410", 
                                country_name="JAPÃO")

            
        CountryCode.objects.create(country_code="P1420", 
                                country_name="JORDÂNIA")

            
        CountryCode.objects.create(country_code="P1430", 
                                country_name="KUAITE ou KUWEIT")

            
        CountryCode.objects.create(country_code="P1440", 
                                country_name="LAOS")

            
        CountryCode.objects.create(country_code="P1450", 
                                country_name="LESOTO")

            
        CountryCode.objects.create(country_code="P1460", 
                                country_name="LETÔNIA")

            
        CountryCode.objects.create(country_code="P1470", 
                                country_name="LÍBANO")

            
        CountryCode.objects.create(country_code="P1480", 
                                country_name="LIBÉRIA")

            
        CountryCode.objects.create(country_code="P1490", 
                                country_name="LÍBIA")

            
        CountryCode.objects.create(country_code="P1500", 
                                country_name="LIECHTENSTEIN")

            
        CountryCode.objects.create(country_code="P1510", 
                                country_name="LITUÂNIA")

            
        CountryCode.objects.create(country_code="P1520", 
                                country_name="LUXEMBURGO")

            
        CountryCode.objects.create(country_code="P1530", 
                                country_name="MACAU")

            
        CountryCode.objects.create(country_code="P1540", 
                                country_name="MACEDÔNIA")

            
        CountryCode.objects.create(country_code="P1550", 
                                country_name="MADAGASCAR")

            
        CountryCode.objects.create(country_code="P1560", 
                                country_name="MALÁSIA ou MALAÍSIA")

            
        CountryCode.objects.create(country_code="P1570", 
                                country_name="MALAVI ou MALAUI")

            
        CountryCode.objects.create(country_code="P1580", 
                                country_name="MALDIVAS")

            
        CountryCode.objects.create(country_code="P1590", 
                                country_name="MALI")

            
        CountryCode.objects.create(country_code="P1600", 
                                country_name="MALTA")

            
        CountryCode.objects.create(country_code="P1610", 
                                country_name="MALVINAS ou ILHAS FALKLAND")

            
        CountryCode.objects.create(country_code="P1620", 
                                country_name="MARROCOS")

            
        CountryCode.objects.create(country_code="P1630", 
                                country_name="MARTINICA")

            
        CountryCode.objects.create(country_code="P1640", 
                                country_name="MAURÍCIO")

            
        CountryCode.objects.create(country_code="P1650", 
                                country_name="MAURITÂNIA")

            
        CountryCode.objects.create(country_code="P1660", 
                                country_name="MAYOTTE")

            
        CountryCode.objects.create(country_code="P1670", 
                                country_name="MÉXICO")

            
        CountryCode.objects.create(country_code="P1680", 
                                country_name="MIANMÁ")

            
        CountryCode.objects.create(country_code="P1690", 
                                country_name="MICRONÉSIA")

            
        CountryCode.objects.create(country_code="P1700", 
                                country_name="MOÇAMBIQUE")

            
        CountryCode.objects.create(country_code="P1710", 
                                country_name="MOLDÁVIA (MOLDOVA)")

            
        CountryCode.objects.create(country_code="P1720", 
                                country_name="MÔNACO")

            
        CountryCode.objects.create(country_code="P1730", 
                                country_name="MONGÓLIA")

            
        CountryCode.objects.create(country_code="P1740", 
                                country_name="MONTENEGRO")

            
        CountryCode.objects.create(country_code="P1750", 
                                country_name="MONTSERRAT")

            
        CountryCode.objects.create(country_code="P1760", 
                                country_name="MYANMAR")

            
        CountryCode.objects.create(country_code="P1770", 
                                country_name="NAMÍBIA")

            
        CountryCode.objects.create(country_code="P1780", 
                                country_name="NAURU")

            
        CountryCode.objects.create(country_code="P1790", 
                                country_name="NEPAL")

            
        CountryCode.objects.create(country_code="P1800", 
                                country_name="NICARÁGUA")

            
        CountryCode.objects.create(country_code="P1810", 
                                country_name="NÍGER")

            
        CountryCode.objects.create(country_code="P1820", 
                                country_name="NIGÉRIA")

            
        CountryCode.objects.create(country_code="P1830", 
                                country_name="NIUE")

            
        CountryCode.objects.create(country_code="P1840", 
                                country_name="NORUEGA")

            
        CountryCode.objects.create(country_code="P1850", 
                                country_name="NOVA CALEDÔNIA")

            
        CountryCode.objects.create(country_code="P1860", 
                                country_name="NOVA ZELÂNDIA")

            
        CountryCode.objects.create(country_code="P1870", 
                                country_name="NUEVA ESPARTA")

            
        CountryCode.objects.create(country_code="P1880", 
                                country_name="OMÃ")

            
        CountryCode.objects.create(country_code="P1890", 
                                country_name="PAÍS DE GALES")

            
        CountryCode.objects.create(country_code="P1900", 
                                country_name="PAÍSES BAIXOS")

            
        CountryCode.objects.create(country_code="P1910", 
                                country_name="PALAU")

            
        CountryCode.objects.create(country_code="P1920", 
                                country_name="PANAMÁ")

            
        CountryCode.objects.create(country_code="P1930", 
                                country_name="PAPUA NOVA-GUINÉ")

            
        CountryCode.objects.create(country_code="P1940", 
                                country_name="PAQUISTÃO")

            
        CountryCode.objects.create(country_code="P1950", 
                                country_name="PARAGUAI")

            
        CountryCode.objects.create(country_code="P1960", 
                                country_name="PÉRSIA")

            
        CountryCode.objects.create(country_code="P1970", 
                                country_name="PERU")
            
        CountryCode.objects.create(country_code="P1980", 
                                country_name="POLINÉSIA FRANCESA")

        CountryCode.objects.create(country_code="P1990", 
                                country_name="POLÔNIA")

        CountryCode.objects.create(country_code="P2000", 
                                country_name="PORTO RICO")

        CountryCode.objects.create(country_code="P2010", 
                                country_name="PORTUGAL")

        CountryCode.objects.create(country_code="P2020", 
                                country_name="QUÊP2010NIA")

        CountryCode.objects.create(country_code="P2040", 
                                country_name="QUIRGUÍZIA ou QUIRGUIZTÃO")

        CountryCode.objects.create(country_code="P2030", 
                                country_name="QUIRIBATI")

        CountryCode.objects.create(country_code="P2050", 
                                country_name="RASD")

        CountryCode.objects.create(country_code="P2060", 
                                country_name="REINO UNIDO")

        CountryCode.objects.create(country_code="P2070", 
                                country_name="REPÚBLICA CENTROAFRICANA")

        CountryCode.objects.create(country_code="P2080", 
                                country_name="REPÚBLICA DO IÊMEN")

        CountryCode.objects.create(country_code="P2090", 
                                country_name="REPÚBLICA DOMINICANA")

        CountryCode.objects.create(country_code="P2100", 
                                country_name="REPÚBLICA ESLOVACA")

        CountryCode.objects.create(country_code="P2110", 
                                country_name="REPÚBLICA TCHECA")

        CountryCode.objects.create(country_code="P2120", 
                                country_name="REUNIÃO")

        CountryCode.objects.create(country_code="P2130", 
                                country_name="RODÉSIA")

        CountryCode.objects.create(country_code="P2140", 
                                country_name="ROMÊNIA")

        CountryCode.objects.create(country_code="P2150", 
                                country_name="RUANDA")

        CountryCode.objects.create(country_code="P2160", 
                                country_name="RÚSSIA")

        CountryCode.objects.create(country_code="P2170", 
                                country_name="SAARA OCIDENTAL")

        CountryCode.objects.create(country_code="P2180", 
                                country_name="SAINT-PIERRE E MIQUELON")

        CountryCode.objects.create(country_code="P2190", 
                                country_name="SALOMÃO")

        CountryCode.objects.create(country_code="P2210", 
                                country_name="SAMOA AMERICANA")

        CountryCode.objects.create(country_code="P2200", 
                                country_name="SAMOA OCIDENTAL")

        CountryCode.objects.create(country_code="P2220", 
                                country_name="SAN MARINO")

        CountryCode.objects.create(country_code="P2230", 
                                country_name="SANTA HELENA")

        CountryCode.objects.create(country_code="P2240", 
                                country_name="SANTA LÚCIA")

        CountryCode.objects.create(country_code="P2250", 
                                country_name="SÃO CRISTÓVÃO E NEVIS (SAINT KITTS)")

        CountryCode.objects.create(country_code="P2260", 
                                country_name="SÃO TOMÉ E PRÍNCIPE")

        CountryCode.objects.create(country_code="P2270", 
                                country_name="SÃO VICENTE E GRANADINAS")

        CountryCode.objects.create(country_code="P2280", 
                                country_name="SEICHELLES (SEYCHELLES)")

        CountryCode.objects.create(country_code="P2290", 
                                country_name="SENEGAL")

        CountryCode.objects.create(country_code="P2300", 
                                country_name="SERRA LEOA")

        CountryCode.objects.create(country_code="P2310", 
                                country_name="SÉRVIA")

        CountryCode.objects.create(country_code="P2320", 
                                country_name="SÍRIA")

        CountryCode.objects.create(country_code="P2330", 
                                country_name="SOMÁLIA")

        CountryCode.objects.create(country_code="P2340", 
                                country_name="SRI LANKA")

        CountryCode.objects.create(country_code="P2350", 
                                country_name="SUAZILÂNDIA")

        CountryCode.objects.create(country_code="P2360", 
                                country_name="SUDÃO")

        CountryCode.objects.create(country_code="P2370", 
                                country_name="SUÉCIA")

        CountryCode.objects.create(country_code="P2380", 
                                country_name="SUIÇA")

        CountryCode.objects.create(country_code="P2390", 
                                country_name="SURINAME")

        CountryCode.objects.create(country_code="P2400", 
                                country_name="SVALBARD")

        CountryCode.objects.create(country_code="P2410", 
                                country_name="TADJIQUISTÃO")

        CountryCode.objects.create(country_code="P2420", 
                                country_name="TAILÂNDIA")

        CountryCode.objects.create(country_code="P2430", 
                                country_name="TAIWAM")

        CountryCode.objects.create(country_code="P2440", 
                                country_name="TANZÂNIA")

        CountryCode.objects.create(country_code="P2450", 
                                country_name="TCHECO-ESLOVÁQUIA")

        CountryCode.objects.create(country_code="P2460", 
                                country_name="TERRAS AUSTRAIS e ANTÁRTICA")

        CountryCode.objects.create(country_code="P2470", 
                                country_name="TERRITÓRIO BRITÂNICO NA")

        CountryCode.objects.create(country_code="P2480", 
                                country_name="TERRITÓRIO BRITÂNICO NO OCEANO")

        CountryCode.objects.create(country_code="P2490", 
                                country_name="TIBETE")

        CountryCode.objects.create(country_code="P2500", 
                                country_name="TIMOR")

        CountryCode.objects.create(country_code="P2510", 
                                country_name="TOGO")

        CountryCode.objects.create(country_code="P2520", 
                                country_name="TONGA")

        CountryCode.objects.create(country_code="P2530", 
                                country_name="TOQUELAU")

        CountryCode.objects.create(country_code="P2540", 
                                country_name="TRINIDAD E TOBAGO")

        CountryCode.objects.create(country_code="P2550", 
                                country_name="TUNÍSIA")

        CountryCode.objects.create(country_code="P2560", 
                                country_name="TURCAS E CAICOS (TURKS E CAICOS)")

        CountryCode.objects.create(country_code="P2570", 
                                country_name="TURCOMENISTÃO (TURCOMÊNIA) ")

        CountryCode.objects.create(country_code="P2580", 
                                country_name="TURQUIA")

        CountryCode.objects.create(country_code="P2590", 
                                country_name="TUVALU")

        CountryCode.objects.create(country_code="P2600", 
                                country_name="UCRÂNIA")

        CountryCode.objects.create(country_code="P2610", 
                                country_name="UGANDA")

        CountryCode.objects.create(country_code="P2620", 
                                country_name="UNIÃO SOVIÉTICA")

        CountryCode.objects.create(country_code="P2630", 
                                country_name="URUGUAI")

        CountryCode.objects.create(country_code="P2640", 
                                country_name="UZBEQUISTÃO")

        CountryCode.objects.create(country_code="P2650", 
                                country_name="VANATU")

        CountryCode.objects.create(country_code="P2660", 
                                country_name="VATICANO")

        CountryCode.objects.create(country_code="P2670", 
                                country_name="VENEZUELA")

        CountryCode.objects.create(country_code="P2680", 
                                country_name="VIETNAM")

        CountryCode.objects.create(country_code="P2690", 
                                country_name="ZAIRE")

        CountryCode.objects.create(country_code="P2700", 
                                country_name="ZÂMBIA")

        CountryCode.objects.create(country_code="P2710", 
                                country_name ="ZIMBÁBUE")

        CountryCode.objects.create(country_code="PALESTINA", 
                                country_name="P2720") 	