from django.core.management.base import BaseCommand
from middle.models import CityCode


class Command(BaseCommand):
    help = 'Valor default da configuração dos códigos para cidades'

    def handle(self, **options):
        self.stdout.write('Deletando dados de códigos das cidades')
        CityCode.objects.all().delete()

        self.stdout.write('Criando dados códigos das cidades')
    	
        CityCode.objects.create(city_code ="1100015", 
                                city_name ="Alta Floresta D'Oeste")

        CityCode.objects.create(city_code ="1100379", 
                                city_name ="Alto Alegre dos Parecis")

        CityCode.objects.create(city_code ="1100403", 
                                city_name ="Alto Paraíso")

        CityCode.objects.create(city_code ="1100346", 
                                city_name ="Alvorada D'Oeste")

        CityCode.objects.create(city_code ="1100023", 
                                city_name ="Ariquemes")

        CityCode.objects.create(city_code ="1100452", 
                                city_name ="Buritis")

        CityCode.objects.create(city_code ="1100031", 
                                city_name ="Cabixi")

        CityCode.objects.create(city_code ="1100601", 
                                city_name ="Cacaulândia")

        CityCode.objects.create(city_code ="1100049", 
                                city_name ="Cacoal")

        CityCode.objects.create(city_code ="1100700", 
                                city_name ="Campo Novo de Rondônia")

        CityCode.objects.create(city_code ="1100809", 
                                city_name ="Candeias do Jamari")

        CityCode.objects.create(city_code ="1100908", 
                                city_name ="Castanheiras")

        CityCode.objects.create(city_code ="1100056", 
                                city_name ="Cerejeiras")

        CityCode.objects.create(city_code ="1100924", 
                                city_name ="Chupinguaia")

        CityCode.objects.create(city_code ="1100064", 
                                city_name ="Colorado do Oeste")

        CityCode.objects.create(city_code ="1100072", 
                                city_name ="Corumbiara")

        CityCode.objects.create(city_code ="1100080", 
                                city_name ="Costa Marques")

        CityCode.objects.create(city_code ="1100940", 
                                city_name ="Cujubim")

        CityCode.objects.create(city_code ="1100098", 
                                city_name ="Espigão D'Oeste")

        CityCode.objects.create(city_code ="1101005", 
                                city_name ="Governador Jorge Teixeira")

        CityCode.objects.create(city_code ="1100106", 
                                city_name ="Guajará-Mirim")

        CityCode.objects.create(city_code ="1101104", 
                                city_name ="Itapuã do Oeste")

        CityCode.objects.create(city_code ="110011", 
                                city_name="Jaru")

        CityCode.objects.create(city_code ="1100122", 
                                city_name ="Ji-Paraná")

        CityCode.objects.create(city_code ="1100130", 
                                city_name ="Machadinho D'Oeste")

        CityCode.objects.create(city_code ="1101203", 
                                city_name ="Ministro Andreazza")

        CityCode.objects.create(city_code ="1101302", 
                                city_name ="Mirante da Serra")

        CityCode.objects.create(city_code ="1101401", 
                                city_name ="Monte Negro")

        CityCode.objects.create(city_code ="1100148", 
                                city_name ="Nova Brasilândia D'Oeste")

        CityCode.objects.create(city_code ="1100338", 
                                city_name ="Nova Mamoré")

        CityCode.objects.create(city_code ="1101435", 
                                city_name ="Nova União")

        CityCode.objects.create(city_code ="1100502", 
                                city_name ="Novo Horizonte do Oeste")

        CityCode.objects.create(city_code ="1100155", 
                                city_name ="Ouro Preto do Oeste")

        CityCode.objects.create(city_code ="1101450", 
                                city_name ="Parecis")

        CityCode.objects.create(city_code ="1100189", 
                                city_name ="Pimenta Bueno")

        CityCode.objects.create(city_code ="1101468", 
                                city_name ="Pimenteiras do Oeste")

        CityCode.objects.create(city_code ="1100205", 
                                city_name ="Porto Velho")

        CityCode.objects.create(city_code ="1100254", 
                                city_name ="Presidente Médici")

        CityCode.objects.create(city_code ="1101476", 
                                city_name ="Primavera de Rondônia")

        CityCode.objects.create(city_code ="1100262", 
                                city_name ="Rio Crespo")

        CityCode.objects.create(city_code ="1100288", 
                                city_name ="Rolim de Moura")

        CityCode.objects.create(city_code ="1100296", 
                                city_name ="Santa Luzia D'Oeste")

        CityCode.objects.create(city_code ="1101484", 
                                city_name ="São Felipe D'Oeste")

        CityCode.objects.create(city_code ="1101492", 
                                city_name ="São Francisco do Guaporé")

        CityCode.objects.create(city_code ="1100320", 
                                city_name ="São Miguel do Guaporé")

        CityCode.objects.create(city_code ="1101500", 
                                city_name ="Seringueiras")

        CityCode.objects.create(city_code ="1101559", 
                                city_name ="Teixeirópolis")

        CityCode.objects.create(city_code ="1101609", 
                                city_name ="Theobroma")

        CityCode.objects.create(city_code ="1101708", 
                                city_name = "Urupá")

        CityCode.objects.create(city_code ="1101757", 
                                city_name ="Vale do Anari")

        CityCode.objects.create(city_code ="1101807", 
                                city_name ="Vale do Paraíso")

        CityCode.objects.create(city_code ="1100304", 
                                city_name ="Vilhena")

        CityCode.objects.create(city_code ="1200013", 
                                city_name ="Acrelândia")

        CityCode.objects.create(city_code ="1200054", 
                                city_name ="Assis Brasil")

        CityCode.objects.create(city_code ="1200104", 
                                city_name ="Brasiléia")

        CityCode.objects.create(city_code ="1200138", 
                                city_name ="Bujari")

        CityCode.objects.create(city_code ="1200179", 
                                city_name ="Capixaba")

        CityCode.objects.create(city_code ="1200203", 
                                city_name ="Cruzeiro do Sul")

        CityCode.objects.create(city_code ="1200252", 
                                city_name ="Epitaciolândia")

        CityCode.objects.create(city_code ="1200302", 
                                city_name= "Feijó")

        CityCode.objects.create(city_code ="1200328", 
                                city_name ="Jordão")

        CityCode.objects.create(city_code ="1200336", 
                                city_name ="Mâncio Lima")

        CityCode.objects.create(city_code ="1200344", 
                                city_name ="Manoel Urbano")

        CityCode.objects.create(city_code ="1200351", 
                                city_name ="Marechal Thaumaturgo")

        CityCode.objects.create(city_code ="1200385", 
                                city_name ="Plácido de Castro")

        CityCode.objects.create(city_code ="1200807", 
                                city_name ="Porto Acre")

        CityCode.objects.create(city_code ="1200393", 
                                city_name ="Porto Walter")

        CityCode.objects.create(city_code ="1200401", 
                                city_name ="Rio Branco")

        CityCode.objects.create(city_code ="1200427", 
                                city_name ="Rodrigues Alves")

        CityCode.objects.create(city_code ="1200435", 
                                city_name ="Santa Rosa do Purus")

        CityCode.objects.create(city_code ="1200500", 
                                city_name ="Sena Madureira")

        CityCode.objects.create(city_code ="1200450", 
                                city_name ="Senador Guiomard")

        CityCode.objects.create(city_code ="1200609", 
                                city_name ="Tarauacá")

        CityCode.objects.create(city_code ="1200708", 
                                city_name ="Xapuri")

        CityCode.objects.create(city_code ="1300029", 
                                city_name ="Alvarães")

        CityCode.objects.create(city_code ="1300060", 
                                city_name ="Amaturá")

        CityCode.objects.create(city_code ="1300086", 
                                city_name="Anamã")

        CityCode.objects.create(city_code ="1300102", 
                                city_name="Anori")

        CityCode.objects.create(city_code ="130014",
                                city_name="Apuí")

        CityCode.objects.create(city_code ="1300201", 
                                city_name ="Atalaia do Norte")

        CityCode.objects.create(city_code ="1300300", 
                                city_name ="Autazes")

        CityCode.objects.create(city_code ="1300409", 
                                city_name ="Barcelos")

        CityCode.objects.create(city_code ="1300508", 
                                city_name ="Barreirinha")

        CityCode.objects.create(city_code ="1300607", 
                                city_name ="Benjamin Constant")

        CityCode.objects.create(city_code ="1300631", 
                                city_name ="Beruri")

        CityCode.objects.create(city_code ="1300680", 
                                city_name ="Boa Vista do Ramos")

        CityCode.objects.create(city_code ="1300706", 
                                city_name ="Boca do Acre")

        CityCode.objects.create(city_code ="1300805", 
                                city_name="Borba")

        CityCode.objects.create(city_code ="1300839", 
                                city_name ="Caapiranga")

        CityCode.objects.create(city_code ="1300904", 
                                city_name ="Canutama")

        CityCode.objects.create(city_code ="1301001", 
                                city_name ="Carauari")

        CityCode.objects.create(city_code ="1301100", 
                                city_name ="Careiro")

        CityCode.objects.create(city_code ="1301159", 
                                city_name ="Careiro da Várzea")

        CityCode.objects.create(city_code ="1301209", 
                                city_name="Coari")

        CityCode.objects.create(city_code ="1301308", 
                                city_name ="Codajás")

        CityCode.objects.create(city_code ="1301407", 
                                city_name ="Eirunepé")

        CityCode.objects.create(city_code ="1301506", 
                                city_name ="Envira")

        CityCode.objects.create(city_code ="1301605", 
                                city_name ="Fonte Boa")

        CityCode.objects.create(city_code ="1301654", 
                                city_name ="Guajará")

        CityCode.objects.create(city_code ="1301704", 
                                city_name ="Humaitá")

        CityCode.objects.create(city_code ="1301803", 
                                city_name ="Ipixuna")

        CityCode.objects.create(city_code ="1301852", 
                                city_name ="Iranduba")

        CityCode.objects.create(city_code ="1301902", 
                                city_name ="Itacoatiara")

        CityCode.objects.create(city_code ="1301951", 
                                city_name ="Itamarati")

        CityCode.objects.create(city_code ="1302009", 
                                city_name ="Itapiranga")

        CityCode.objects.create(city_code ="1302108", 
                                city_name ="Japurá")

        CityCode.objects.create(city_code ="1302207", 
                                city_name="Juruá")

        CityCode.objects.create(city_code ="1302306", 
                                city_name="Jutaí")

        CityCode.objects.create(city_code ="1302405", 
                                city_name ="Lábrea")

        CityCode.objects.create(city_code ="1302504", 
                                city_name ="Manacapuru")

        CityCode.objects.create(city_code ="1302553", 
                                city_name ="Manaquiri")

        CityCode.objects.create(city_code ="1302603", 
                                city_name ="Manaus")

        CityCode.objects.create(city_code ="1302702", 
                                city_name ="Manicoré")

        CityCode.objects.create(city_code ="1302801", 
                                city_name="Maraã")

        CityCode.objects.create(city_code ="1302900", 
                                city_name="Maués")

        CityCode.objects.create(city_code ="1303007", 
                                city_name ="Nhamundá")

        CityCode.objects.create(city_code ="1303106", 
                                city_name ="Nova Olinda do Norte")

        CityCode.objects.create(city_code ="1303205", 
                                city_name ="Novo Airão")

        CityCode.objects.create(city_code ="1303304", 
                                city_name ="Novo Aripuanã")

        CityCode.objects.create(city_code ="1303403", 
                                city_name ="Parintins")

        CityCode.objects.create(city_code ="1303502", 
                                city_name ="Pauini")

        CityCode.objects.create(city_code ="1303536", 
                                city_name ="Presidente Figueiredo")

        CityCode.objects.create(city_code ="1303569", 
                                city_name ="Rio Preto da Eva")

        CityCode.objects.create(city_code ="1303601", 
                                city_name ="Santa Isabel do Rio Negro")

        CityCode.objects.create(city_code ="1303700", 
                                city_name ="Santo Antônio do Içá")

        CityCode.objects.create(city_code ="1303809", 
                                city_name ="São Gabriel da Cachoeira")

        CityCode.objects.create(city_code ="1303908", 
                                city_name ="São Paulo de Olivença")

        CityCode.objects.create(city_code ="1303957", 
                                city_name ="São Sebastião do Uatumã")

        CityCode.objects.create(city_code ="1304005", 
                                city_name ="Silves")

        CityCode.objects.create(city_code ="1304062", 
                                city_name ="Tabatinga")

        CityCode.objects.create(city_code ="1304104", 
                                city_name ="Tapauá")

        CityCode.objects.create(city_code ="130420", 
                                city_name="Tefé")

        CityCode.objects.create(city_code ="1304237", 
                                city_name ="Tonantins")

        CityCode.objects.create(city_code ="1304260", 
                                city_name ="Uarini")

        CityCode.objects.create(city_code ="1304302", 
                                city_name ="Urucará")

        CityCode.objects.create(city_code ="1304401", 
                                city_name ="Urucurituba")

        CityCode.objects.create(city_code ="1400050", 
                                city_name ="Alto Alegre")

        CityCode.objects.create(city_code ="1400027", 
                                city_name ="Amajari")

        CityCode.objects.create(city_code ="1400100", 
                                city_name ="Boa Vista")

        CityCode.objects.create(city_code ="1400159", 
                                city_name ="Bonfim")

        CityCode.objects.create(city_code ="1400175", 
                                city_name="Cantá")

        CityCode.objects.create(city_code ="1400209", 
                                city_name ="Caracaraí")

        CityCode.objects.create(city_code ="1400233", 
                                city_name ="Caroebe")

        CityCode.objects.create(city_code ="1400282", 
                                city_name ="Iracema")

        CityCode.objects.create(city_code ="1400308", 
                                city_name ="Mucajaí")

        CityCode.objects.create(city_code ="1400407", 
                                city_name ="Normandia")

        CityCode.objects.create(city_code ="1400456", 
                                city_name ="Pacaraima")

        CityCode.objects.create(city_code ="1400472", 
                                city_name ="Rorainópolis")

        CityCode.objects.create(city_code ="1400506", 
                                city_name ="São João da Baliza")

        CityCode.objects.create(city_code ="1400605", 
                                city_name ="São Luiz")

        CityCode.objects.create(city_code ="1400704", 
                                city_name ="Uiramutã")

        CityCode.objects.create(city_code ="1500107", 
                                city_name ="Abaetetuba")

        CityCode.objects.create(city_code ="1500131", 
                                city_name ="Abel Figueiredo")

        CityCode.objects.create(city_code ="1500206", 
                                city_name="Acará")

        CityCode.objects.create(city_code ="150030", 
                                city_name="Afuá")

        CityCode.objects.create(city_code ="1500347", 
                                city_name ="Água Azul do Norte")

        CityCode.objects.create(city_code ="1500404", 
                                city_name ="Alenquer")

        CityCode.objects.create(city_code ="1500503", 
                                city_name ="Almeirim")

        CityCode.objects.create(city_code ="1500602", 
                                city_name ="Altamira")

        CityCode.objects.create(city_code ="1500701", 
                                city_name ="Anajás")

        CityCode.objects.create(city_code ="1500800", 
                                city_name ="Ananindeua")

        CityCode.objects.create(city_code ="1500859", 
                                city_name="Anapu")

        CityCode.objects.create(city_code ="1500909", 
                                city_name ="Augusto Corrêa")

        CityCode.objects.create(city_code ="1500958", 
                                city_name ="Aurora do Pará")

        CityCode.objects.create(city_code ="1501006", 
                                city_name ="Aveiro")

        CityCode.objects.create(city_code ="1501105", 
                                city_name="Bagre")

        CityCode.objects.create(city_code ="1501204", 
                                city_name="Baião")

        CityCode.objects.create(city_code ="1501253", 
                                city_name ="Bannach")

        CityCode.objects.create(city_code ="1501303", 
                                city_name ="Barcarena")

        CityCode.objects.create(city_code ="1501402", 
                                city_name="Belém")

        CityCode.objects.create(city_code ="1501451", 
                                city_name ="Belterra")

        CityCode.objects.create(city_code ="1501501", 
                                city_name ="Benevides")

        CityCode.objects.create(city_code ="1501576", 
                                city_name ="Bom Jesus do Tocantins")

        CityCode.objects.create(city_code ="1501600", 
                                city_name ="Bonito")

        CityCode.objects.create(city_code ="1501709", 
                                city_name ="Bragança")

        CityCode.objects.create(city_code ="1501725", 
                                city_name ="Brasil Novo")

        CityCode.objects.create(city_code ="1501758", 
                                city_name ="Brejo Grande do Araguaia")

        CityCode.objects.create(city_code ="1501782", 
                                city_name ="Breu Branco")

        CityCode.objects.create(city_code ="1501808", 
                                city_name ="Breves")

        CityCode.objects.create(city_code ="1501907", 
                                city_name ="Bujaru")

        CityCode.objects.create(city_code ="1502004", 
                                city_name ="Cachoeira do Arari")

        CityCode.objects.create(city_code ="1501956", 
                                city_name ="Cachoeira do Piriá")

        CityCode.objects.create(city_code ="1502103", 
                                city_name ="Cametá")

        CityCode.objects.create(city_code ="1502152", 
                                city_name ="Canaã dos Carajás")

        CityCode.objects.create(city_code ="1502202", 
                                city_name ="Capanema")

        CityCode.objects.create(city_code ="1502301", 
                                city_name ="Capitão Poço")

        CityCode.objects.create(city_code ="1502400", 
                                city_name ="Castanhal")

        CityCode.objects.create(city_code ="1502509", 
                                city_name ="Chaves")

        CityCode.objects.create(city_code ="1502608", 
                                city_name ="Colares")

        CityCode.objects.create(city_code ="1502707", 
                                city_name ="Conceição do Araguaia")

        CityCode.objects.create(city_code ="1502756", 
                                city_name ="Concórdia do Pará")

        CityCode.objects.create(city_code ="1502764", 
                                city_name ="Cumaru do Norte")

        CityCode.objects.create(city_code ="1502772", 
                                city_name ="Curionópolis")

        CityCode.objects.create(city_code ="1502806", 
                                city_name ="Curralinho")

        CityCode.objects.create(city_code ="1502855", 
                                city_name="Curuá")

        CityCode.objects.create(city_code ="1502905", 
                                city_name ="Curuçá")

        CityCode.objects.create(city_code ="1502939", 
                                city_name ="Dom Eliseu")

        CityCode.objects.create(city_code ="1502954", 
                                city_name ="Eldorado do Carajás")

        CityCode.objects.create(city_code ="150300", 
                                city_name="Faro")

        CityCode.objects.create(city_code ="1503044", 
                                city_name ="Floresta do Araguaia")

        CityCode.objects.create(city_code ="1503077", 
                                city_name ="Garrafão do Norte")

        CityCode.objects.create(city_code ="1503093", 
                                city_name ="Goianésia do Pará")

        CityCode.objects.create(city_code ="1503101", 
                                city_name ="Gurupá")

        CityCode.objects.create(city_code ="1503200", 
                                city_name ="Igarapé-Açu")

        CityCode.objects.create(city_code ="1503309", 
                                city_name ="Igarapé-Miri")

        CityCode.objects.create(city_code ="1503408", 
                                city_name ="Inhangapi")

        CityCode.objects.create(city_code ="1503457", 
                                city_name ="Ipixuna do Pará")

        CityCode.objects.create(city_code ="1503507", 
                                city_name ="Irituia")

        CityCode.objects.create(city_code ="1503606", 
                                city_name ="Itaituba")

        CityCode.objects.create(city_code ="1503705", 
                                city_name ="Itupiranga")

        CityCode.objects.create(city_code ="1503754", 
                                city_name ="Jacareacanga")

        CityCode.objects.create(city_code ="1503804", 
                                city_name ="Jacundá")

        CityCode.objects.create(city_code ="1503903", 
                                city_name ="Juruti")

        CityCode.objects.create(city_code ="1504000", 
                                city_name ="Limoeiro do Ajuru")

        CityCode.objects.create(city_code ="1504059", 
                                city_name ="Mãe do Rio")

        CityCode.objects.create(city_code ="1504109", 
                                city_name ="Magalhães Barata")

        CityCode.objects.create(city_code ="1504208", 
                                city_name ="Marabá")

        CityCode.objects.create(city_code ="1504307", 
                                city_name ="Maracanã")

        CityCode.objects.create(city_code ="1504406", 
                                city_name ="Marapanim")

        CityCode.objects.create(city_code ="1504422", 
                                city_name ="Marituba")

        CityCode.objects.create(city_code ="1504455", 
                                city_name ="Medicilândia")

        CityCode.objects.create(city_code ="1504505", 
                                city_name ="Melgaço")

        CityCode.objects.create(city_code ="1504604", 
                                city_name ="Mocajuba")

        CityCode.objects.create(city_code ="150470", 
                                city_name="Moju")

        CityCode.objects.create(city_code ="1504752", 
                                city_name ="Mojuí dos Campos")

        CityCode.objects.create(city_code ="1504802", 
                                city_name ="Monte Alegre")

        CityCode.objects.create(city_code ="1504901", 
                                city_name="Muaná")

        CityCode.objects.create(city_code ="1504950", 
                                city_name ="Nova Esperança do Piriá")

        CityCode.objects.create(city_code ="1504976", 
                                city_name ="Nova Ipixuna")

        CityCode.objects.create(city_code ="1505007", 
                                city_name ="Nova Timboteua")

        CityCode.objects.create(city_code ="1505031", 
                                city_name ="Novo Progresso")

        CityCode.objects.create(city_code ="1505064", 
                                city_name ="Novo Repartimento")

        CityCode.objects.create(city_code ="1505106", 
                                city_name ="Óbidos")

        CityCode.objects.create(city_code ="1505205", 
                                city_name ="Oeiras do Pará")

        CityCode.objects.create(city_code ="1505304", 
                                city_name ="Oriximiná")

        CityCode.objects.create(city_code ="1505403", 
                                city_name="Ourém")

        CityCode.objects.create(city_code ="1505437", 
                                city_name ="Ourilândia do Norte")

        CityCode.objects.create(city_code ="1505486", 
                                city_name ="Pacajá")

        CityCode.objects.create(city_code ="1505494", 
                                city_name ="Palestina do Pará")

        CityCode.objects.create(city_code ="1505502", 
                                city_name ="Paragominas")

        CityCode.objects.create(city_code ="1505536", 
                                city_name ="Parauapebas")

        CityCode.objects.create(city_code ="1505551", 
                                city_name ="Pau D'Arco")

        CityCode.objects.create(city_code ="1505601", 
                                city_name ="Peixe-Boi")

        CityCode.objects.create(city_code ="1505635", 
                                city_name ="Piçarra")

        CityCode.objects.create(city_code ="1505650", 
                                city_name ="Placas")

        CityCode.objects.create(city_code ="1505700", 
                                city_name ="Ponta de Pedras")

        CityCode.objects.create(city_code ="1505809", 
                                city_name ="Portel")

        CityCode.objects.create(city_code ="1505908", 
                                city_name ="Porto de Moz")

        CityCode.objects.create(city_code ="1506005", 
                                city_name ="Prainha")

        CityCode.objects.create(city_code ="1506104", 
                                city_name ="Primavera")

        CityCode.objects.create(city_code ="1506112", 
                                city_name ="Quatipuru")

        CityCode.objects.create(city_code ="1506138", 
                                city_name ="Redenção")

        CityCode.objects.create(city_code ="1506161", 
                                city_name ="Rio Maria")

        CityCode.objects.create(city_code ="1506187", 
                                city_name ="Rondon do Pará")

        CityCode.objects.create(city_code ="1506195", 
                                city_name ="Rurópolis")

        CityCode.objects.create(city_code ="1506203", 
                                city_name ="Salinópolis")

        CityCode.objects.create(city_code ="1506302", 
                                city_name ="Salvaterra")

        CityCode.objects.create(city_code ="1506351", 
                                city_name ="Santa Bárbara do Pará")

        CityCode.objects.create(city_code ="1506401", 
                                city_name ="Santa Cruz do Arari")

        CityCode.objects.create(city_code ="1506500", 
                                city_name ="Santa Izabel do Pará")

        CityCode.objects.create(city_code ="1506559", 
                                city_name ="Santa Luzia do Pará")

        CityCode.objects.create(city_code ="1506583", 
                                city_name ="Santa Maria das Barreiras")

        CityCode.objects.create(city_code ="1506609", 
                                city_name ="Santa Maria do Pará")

        CityCode.objects.create(city_code ="1506708", 
                                city_name ="Santana do Araguaia")

        CityCode.objects.create(city_code ="1506807", 
                                city_name ="Santarém")

        CityCode.objects.create(city_code ="1506906", 
                                city_name ="Santarém Novo")

        CityCode.objects.create(city_code ="1507003", 
                                city_name ="Santo Antônio do Tauá")

        CityCode.objects.create(city_code ="1507102", 
                                city_name ="São Caetano de Odivelas")

        CityCode.objects.create(city_code ="1507151", 
                                city_name ="São Domingos do Araguaia")

        CityCode.objects.create(city_code ="1507201", 
                                city_name ="São Domingos do Capim")

        CityCode.objects.create(city_code ="1507300", 
                                city_name ="São Félix do Xingu")

        CityCode.objects.create(city_code ="1507409", 
                                city_name ="São Francisco do Pará")

        CityCode.objects.create(city_code ="1507458", 
                                city_name ="São Geraldo do Araguaia")

        CityCode.objects.create(city_code ="1507466", 
                                city_name ="São João da Ponta")

        CityCode.objects.create(city_code ="1507474", 
                                city_name ="São João de Pirabas")

        CityCode.objects.create(city_code ="1507508", 
                                city_name ="São João do Araguaia")

        CityCode.objects.create(city_code ="1507607", 
                                city_name ="São Miguel do Guamá")

        CityCode.objects.create(city_code ="1507706", 
                                city_name ="São Sebastião da Boa Vista")

        CityCode.objects.create(city_code ="1507755", 
                                city_name ="Sapucaia")

        CityCode.objects.create(city_code ="1507805", 
                                city_name ="Senador José Porfírio")

        CityCode.objects.create(city_code ="1507904", 
                                city_name="Soure")

        CityCode.objects.create(city_code ="1507953", 
                                city_name ="Tailândia")

        CityCode.objects.create(city_code ="1507961", 
                                city_name ="Terra Alta")

        CityCode.objects.create(city_code ="1507979", 
                                city_name ="Terra Santa")

        CityCode.objects.create(city_code ="1508001", 
                                city_name ="Tomé-Açu")

        CityCode.objects.create(city_code ="1508035", 
                                city_name ="Tracuateua")

        CityCode.objects.create(city_code ="1508050", 
                                city_name ="Trairão")

        CityCode.objects.create(city_code ="1508084", 
                                city_name ="Tucumã")

        CityCode.objects.create(city_code ="1508100", 
                                city_name ="Tucuruí")

        CityCode.objects.create(city_code ="1508126", 
                                city_name ="Ulianópolis")

        CityCode.objects.create(city_code ="1508159", 
                                city_name ="Uruará")

        CityCode.objects.create(city_code ="1508209", 
                                city_name="Vigia")

        CityCode.objects.create(city_code ="1508308", 
                                city_name="Viseu")

        CityCode.objects.create(city_code ="1508357", 
                                city_name ="Vitória do Xingu")

        CityCode.objects.create(city_code ="1508407", 
                                city_name ="Xinguara")

        CityCode.objects.create(city_code ="1600105", 
                                city_name="Amapá")

        CityCode.objects.create(city_code ="1600204", 
                                city_name ="Calçoene")

        CityCode.objects.create(city_code ="1600212", 
                                city_name ="Cutias")

        CityCode.objects.create(city_code ="1600238", 
                                city_name ="Ferreira Gomes")

        CityCode.objects.create(city_code ="1600253", 
                                city_name ="Itaubal")

        CityCode.objects.create(city_code ="1600279", 
                                city_name ="Laranjal do Jari")

        CityCode.objects.create(city_code ="1600303", 
                                city_name ="Macapá")

        CityCode.objects.create(city_code ="1600402", 
                                city_name ="Mazagão")

        CityCode.objects.create(city_code ="1600501", 
                                city_name ="Oiapoque")

        CityCode.objects.create(city_code ="1600154", 
                                city_name ="Pedra Branca do Amapari")

        CityCode.objects.create(city_code ="1600535", 
                                city_name ="Porto Grande")

        CityCode.objects.create(city_code ="1600550", 
                                city_name ="Pracuúba")

        CityCode.objects.create(city_code ="1600600", 
                                city_name ="Santana")

        CityCode.objects.create(city_code ="1600055", 
                                city_name ="Serra do Navio")

        CityCode.objects.create(city_code ="1600709", 
                                city_name ="Tartarugalzinho")

        CityCode.objects.create(city_code ="1600808", 
                                city_name ="Vitória do Jari")

        CityCode.objects.create(city_code ="1700251", 
                                city_name ="Abreulândia")

        CityCode.objects.create(city_code ="1700301", 
                                city_name ="Aguiarnópolis")

        CityCode.objects.create(city_code ="1700350", 
                                city_name ="Aliança do Tocantins")

        CityCode.objects.create(city_code ="1700400", 
                                city_name="Almas")

        CityCode.objects.create(city_code ="1700707", 
                                city_name ="Alvorada")

        CityCode.objects.create(city_code ="1701002", 
                                city_name ="Ananás")

        CityCode.objects.create(city_code ="1701051", 
                                city_name ="Angico")

        CityCode.objects.create(city_code ="1701101", 
                                city_name ="Aparecida do Rio Negro")

        CityCode.objects.create(city_code ="1701309", 
                                city_name ="Aragominas")

        CityCode.objects.create(city_code ="1701903", 
                                city_name ="Araguacema")

        CityCode.objects.create(city_code ="1702000", 
                                city_name ="Araguaçu")

        CityCode.objects.create(city_code ="1702109", 
                                city_name ="Araguaína")

        CityCode.objects.create(city_code ="1702158", 
                                city_name ="Araguanã")

        CityCode.objects.create(city_code ="1702208", 
                                city_name ="Araguatins")

        CityCode.objects.create(city_code ="1702307", 
                                city_name ="Arapoema")

        CityCode.objects.create(city_code ="1702406", 
                                city_name ="Arraias")

        CityCode.objects.create(city_code ="1702554", 
                                city_name ="Augustinópolis")

        CityCode.objects.create(city_code ="1702703", 
                                city_name ="Aurora do Tocantins")

        CityCode.objects.create(city_code ="1702901", 
                                city_name ="Axixá do Tocantins")

        CityCode.objects.create(city_code ="1703008", 
                                city_name ="Babaçulândia")

        CityCode.objects.create(city_code ="1703057", 
                                city_name ="Bandeirantes do Tocantins")

        CityCode.objects.create(city_code ="1703073", 
                                city_name ="Barra do Ouro")

        CityCode.objects.create(city_code ="1703107", 
                                city_name ="Barrolândia")

        CityCode.objects.create(city_code ="1703206", 
                                city_name ="Bernardo Sayão")

        CityCode.objects.create(city_code ="1703305", 
                                city_name ="Bom Jesus do Tocantins")

        CityCode.objects.create(city_code ="1703602", 
                                city_name ="Brasilândia do Tocantins")

        CityCode.objects.create(city_code ="1703701", 
                                city_name ="Brejinho de Nazaré")

        CityCode.objects.create(city_code ="1703800", 
                                city_name ="Buriti do Tocantins")

        CityCode.objects.create(city_code ="1703826", 
                                city_name ="Cachoeirinha")

        CityCode.objects.create(city_code ="1703842", 
                                city_name ="Campos Lindos")

        CityCode.objects.create(city_code ="1703867", 
                                city_name ="Cariri do Tocantins")

        CityCode.objects.create(city_code ="1703883", 
                                city_name ="Carmolândia")

        CityCode.objects.create(city_code ="1703891", 
                                city_name ="Carrasco Bonito")

        CityCode.objects.create(city_code ="1703909", 
                                city_name ="Caseara")

        CityCode.objects.create(city_code ="1704105", 
                                city_name ="Centenário")

        CityCode.objects.create(city_code ="1705102", 
                                city_name ="Chapada da Natividade")

        CityCode.objects.create(city_code ="1704600", 
                                city_name ="Chapada de Areia")

        CityCode.objects.create(city_code ="1705508", 
                                city_name ="Colinas do Tocantins")

        CityCode.objects.create(city_code ="1716703", 
                                city_name ="Colméia")

        CityCode.objects.create(city_code ="1705557", 
                                city_name ="Combinado")

        CityCode.objects.create(city_code ="1705607", 
                                city_name ="Conceição do Tocantins")

        CityCode.objects.create(city_code ="1706001", 
                                city_name ="Couto Magalhães")

        CityCode.objects.create(city_code ="1706100", 
                                city_name ="Cristalândia")

        CityCode.objects.create(city_code ="1706258", 
                                city_name ="Crixás do Tocantins")

        CityCode.objects.create(city_code ="1706506", 
                                city_name ="Darcinópolis")

        CityCode.objects.create(city_code ="1707009", 
                                city_name ="Dianópolis")

        CityCode.objects.create(city_code ="1707108", 
                                city_name ="Divinópolis do Tocantins")

        CityCode.objects.create(city_code ="1707207", 
                                city_name ="Dois Irmãos do Tocantins")

        CityCode.objects.create(city_code ="1707306", 
                                city_name="Dueré")

        CityCode.objects.create(city_code ="1707405", 
                                city_name ="Esperantina")

        CityCode.objects.create(city_code ="1707553", 
                                city_name ="Fátima")

        CityCode.objects.create(city_code ="1707652", 
                                city_name ="Figueirópolis")

        CityCode.objects.create(city_code ="1707702", 
                                city_name ="Filadélfia")

        CityCode.objects.create(city_code ="1708205", 
                                city_name ="Formoso do Araguaia")

        CityCode.objects.create(city_code ="1708304", 
                                city_name ="Goianorte")

        CityCode.objects.create(city_code ="1709005", 
                                city_name ="Goiatins")

        CityCode.objects.create(city_code ="1709302", 
                                city_name ="Guaraí")

        CityCode.objects.create(city_code ="1709500", 
                                city_name ="Gurupi")

        CityCode.objects.create(city_code ="1709807", 
                                city_name ="Ipueiras")

        CityCode.objects.create(city_code ="1710508", 
                                city_name ="Itacajá")

        CityCode.objects.create(city_code ="1710706", 
                                city_name ="Itaguatins")

        CityCode.objects.create(city_code ="1710904", 
                                city_name ="Itapiratins")

        CityCode.objects.create(city_code ="1711100", 
                                city_name ="Itaporã do Tocantins")

        CityCode.objects.create(city_code ="1711506", 
                                city_name ="Jaú do Tocantins")

        CityCode.objects.create(city_code ="1711803", 
                                city_name ="Juarina")

        CityCode.objects.create(city_code ="1711902", 
                                city_name ="Lagoa da Confusão")

        CityCode.objects.create(city_code ="1711951", 
                                city_name ="Lagoa do Tocantins")

        CityCode.objects.create(city_code ="1712009", 
                                city_name ="Lajeado")

        CityCode.objects.create(city_code ="1712157", 
                                city_name ="Lavandeira")

        CityCode.objects.create(city_code ="1712405", 
                                city_name ="Lizarda")

        CityCode.objects.create(city_code ="1712454", 
                                city_name ="Luzinópolis")

        CityCode.objects.create(city_code ="1712504", 
                                city_name ="Marianópolis do Tocantins")

        CityCode.objects.create(city_code ="1712702", 
                                city_name ="Mateiros")

        CityCode.objects.create(city_code ="1712801", 
                                city_name ="Maurilândia do Tocantins")

        CityCode.objects.create(city_code ="1713205", 
                                city_name ="Miracema do Tocantins")

        CityCode.objects.create(city_code ="1713304", 
                                city_name ="Miranorte")

        CityCode.objects.create(city_code ="1713601", 
                                city_name ="Monte do Carmo")

        CityCode.objects.create(city_code ="1713700", 
                                city_name ="Monte Santo do Tocantins")

        CityCode.objects.create(city_code ="1713957", 
                                city_name ="Muricilândia")

        CityCode.objects.create(city_code ="1714203", 
                                city_name ="Natividade")

        CityCode.objects.create(city_code ="1714302", 
                                city_name ="Nazaré")

        CityCode.objects.create(city_code ="1714880", 
                                city_name ="Nova Olinda")

        CityCode.objects.create(city_code ="1715002", 
                                city_name ="Nova Rosalândia")

        CityCode.objects.create(city_code ="1715101", 
                                city_name ="Novo Acordo")

        CityCode.objects.create(city_code ="1715150", 
                                city_name ="Novo Alegre")

        CityCode.objects.create(city_code ="1715259", 
                                city_name ="Novo Jardim")

        CityCode.objects.create(city_code ="1715507", 
                                city_name ="Oliveira de Fátima")

        CityCode.objects.create(city_code ="1721000", 
                                city_name ="Palmas")

        CityCode.objects.create(city_code ="1715705", 
                                city_name ="Palmeirante")

        CityCode.objects.create(city_code ="1713809", 
                                city_name ="Palmeiras do Tocantins")

        CityCode.objects.create(city_code ="1715754", 
                                city_name ="Palmeirópolis")

        CityCode.objects.create(city_code ="1716109", 
                                city_name ="Paraíso do Tocantins")

        CityCode.objects.create(city_code ="1716208", 
                                city_name ="Paranã")

        CityCode.objects.create(city_code ="1716307", 
                                city_name ="Pau D'Arco")

        CityCode.objects.create(city_code ="1716505", 
                                city_name ="Pedro Afonso")

        CityCode.objects.create(city_code ="1716604", 
                                city_name="Peixe")

        CityCode.objects.create(city_code ="1716653", 
                                city_name ="Pequizeiro")

        CityCode.objects.create(city_code ="1717008", 
                                city_name ="Pindorama do Tocantins")

        CityCode.objects.create(city_code ="1717206", 
                                city_name ="Piraquê")

        CityCode.objects.create(city_code ="171750", 
                                city_name="Pium")

        CityCode.objects.create(city_code ="1717800", 
                                city_name ="Ponte Alta do Bom Jesus")

        CityCode.objects.create(city_code ="1717909", 
                                city_name ="Ponte Alta do Tocantins")

        CityCode.objects.create(city_code ="1718006", 
                                city_name ="Porto Alegre do Tocantins")

        CityCode.objects.create(city_code ="1718204", 
                                city_name ="Porto Nacional")

        CityCode.objects.create(city_code ="1718303", 
                                city_name ="Praia Norte")

        CityCode.objects.create(city_code ="1718402", 
                                city_name ="Presidente Kennedy")

        CityCode.objects.create(city_code ="1718451", 
                                city_name ="Pugmil")

        CityCode.objects.create(city_code ="1718501", 
                                city_name ="Recursolândia")

        CityCode.objects.create(city_code ="1718550", 
                                city_name ="Riachinho")

        CityCode.objects.create(city_code ="1718659", 
                                city_name ="Rio da Conceição")

        CityCode.objects.create(city_code ="1718709", 
                                city_name ="Rio dos Bois")

        CityCode.objects.create(city_code ="1718758", 
                                city_name ="Rio Sono")

        CityCode.objects.create(city_code ="1718808", 
                                city_name ="Sampaio")

        CityCode.objects.create(city_code ="1718840", 
                                city_name ="Sandolândia")
    	
        CityCode.objects.create(city_code ="1718865", 
                                city_name ="Santa Fé do Araguaia")
            
        CityCode.objects.create(city_code ="1718881", 
                                city_name ="Santa Maria do Tocantins")
            
        CityCode.objects.create(city_code ="1718899", 
                                city_name ="Santa Rita do Tocantins")
            
        CityCode.objects.create(city_code ="1718907", 
                                city_name ="Santa Rosa do Tocantins")
            
        CityCode.objects.create(city_code ="1719004", 
                                city_name ="Santa Tereza do Tocantins")
            
        CityCode.objects.create(city_code ="1720002", 
                                city_name ="Santa Terezinha do Tocantins")
            
        CityCode.objects.create(city_code ="1720101", 
                                city_name ="São Bento do Tocantins")
            
        CityCode.objects.create(city_code ="1720150", 
                                city_name ="São Félix do Tocantins")
            
        CityCode.objects.create(city_code ="1720200", 
                                city_name ="São Miguel do Tocantins")
            
        CityCode.objects.create(city_code ="1720259", 
                                city_name ="São Salvador do Tocantins")
            
        CityCode.objects.create(city_code ="1720309", 
                                city_name ="São Sebastião do Tocantins")
            
        CityCode.objects.create(city_code ="1720499", 
                                city_name ="São Valério")
            
        CityCode.objects.create(city_code ="1720655", 
                                city_name ="Silvanópolis")
            
        CityCode.objects.create(city_code ="1720804", 
                                city_name ="Sítio Novo do Tocantins")
            
        CityCode.objects.create(city_code ="1720853", 
                                city_name ="Sucupira")
            
        CityCode.objects.create(city_code ="1708254", 
                                city_name ="Tabocão")
            
        CityCode.objects.create(city_code ="1720903", 
                                city_name ="Taguatinga")
            
        CityCode.objects.create(city_code ="1720937", 
                                city_name ="Taipas do Tocantins")
            
        CityCode.objects.create(city_code ="1720978", 
                                city_name ="Talismã")
            
        CityCode.objects.create(city_code ="1721109", 
                                city_name ="Tocantínia")
            
        CityCode.objects.create(city_code ="1721208", 
                                city_name ="Tocantinópolis")
            
        CityCode.objects.create(city_code ="1721257", 
                                city_name ="Tupirama")
            
        CityCode.objects.create(city_code ="1721307", 
                                city_name ="Tupiratins")
            
        CityCode.objects.create(city_code ="1722081", 
                                city_name ="Wanderlândia")

        CityCode.objects.create(city_code ="1722107", 
                                city_name ="Xambioá")

        CityCode.objects.create(city_code ="2100055",
                                city_name ="Açailândia")
            
        CityCode.objects.create(city_code ="2100105",
                                city_name ="Afonso Cunha")
            
        CityCode.objects.create(city_code ="2100154",
                                city_name ="Água Doce do Maranhão")
            
        CityCode.objects.create(city_code ="2100204",
                                city_name ="Alcântara")
            
        CityCode.objects.create(city_code ="2100303",
                                city_name ="Aldeias Altas")
            
        CityCode.objects.create(city_code ="2100402",
                                city_name ="Altamira do Maranhão")
            
        CityCode.objects.create(city_code ="2100436",
                                city_name ="Alto Alegre do Maranhão")
            
        CityCode.objects.create(city_code ="2100477",
                                city_name ="Alto Alegre do Pindaré")
            
        CityCode.objects.create(city_code ="2100501",
                                city_name ="Alto Parnaíba")
            
        CityCode.objects.create(city_code ="2100550",
                                city_name ="Amapá do Maranhão")
            
        CityCode.objects.create(city_code ="2100600",
                                city_name ="Amarante do Maranhão")
            
        CityCode.objects.create(city_code ="2100709",
                                city_name ="Anajatuba")
            
        CityCode.objects.create(city_code ="2100808",
                                city_name ="Anapurus")
            
        CityCode.objects.create(city_code ="2100832",
                                city_name ="Apicum-Açu")
            
        CityCode.objects.create(city_code ="2100873",
                                city_name ="Araguanã")
            
        CityCode.objects.create(city_code ="2100907",
                                city_name ="Araioses")
            
        CityCode.objects.create(city_code ="2100956",
                                city_name ="Arame")
            
        CityCode.objects.create(city_code ="2101004",
                                city_name ="Arari")
            
        CityCode.objects.create(city_code ="2101103",
                                city_name ="Axixá")
            
        CityCode.objects.create(city_code ="2101202",
                                city_name ="Bacabal")
            
        CityCode.objects.create(city_code ="2101251",
                                city_name ="Bacabeira")
            
        CityCode.objects.create(city_code ="2101301",
                                city_name ="Bacuri")
            
        CityCode.objects.create(city_code ="2101350",
                                city_name ="Bacurituba")
            
        CityCode.objects.create(city_code ="2101400",
                                city_name ="Balsas")
            
        CityCode.objects.create(city_code ="2101509",
                                city_name ="Barão de Grajaú")
            
        CityCode.objects.create(city_code ="2101608",
                                city_name ="Barra do Corda")
            
        CityCode.objects.create(city_code ="2101707",
                                city_name ="Barreirinhas")
            
        CityCode.objects.create(city_code ="2101772",
                                city_name ="Bela Vista do Maranhão")
            
        CityCode.objects.create(city_code ="2101731",
                                city_name ="Belágua")
            
        CityCode.objects.create(city_code ="2101806",
                                city_name ="Benedito Leite")
            
        CityCode.objects.create(city_code ="2101905",
                                city_name ="Bequimão")
            
        CityCode.objects.create(city_code ="2101939",
                                city_name ="Bernardo do Mearim")
            
        CityCode.objects.create(city_code ="2101970",
                                city_name ="Boa Vista do Gurupi")
            
        CityCode.objects.create(city_code ="2102002",
                                city_name ="Bom Jardim")
            
        CityCode.objects.create(city_code ="2102036",
                                city_name ="Bom Jesus das Selvas")
            
        CityCode.objects.create(city_code ="2102077",
                                city_name ="Bom Lugar")
            
        CityCode.objects.create(city_code ="2102101",
                                city_name ="Brejo")
            
        CityCode.objects.create(city_code ="2102150",
                                city_name ="Brejo de Areia")
            
        CityCode.objects.create(city_code ="2102200",
                                city_name ="Buriti")
            
        CityCode.objects.create(city_code ="2102309",
                                city_name ="Buriti Bravo")
            
        CityCode.objects.create(city_code ="2102325",
                                city_name ="Buriticupu")
            
        CityCode.objects.create(city_code ="2102358",
                                city_name ="Buritirana")
            
        CityCode.objects.create(city_code ="2102374",
                                city_name ="Cachoeira Grande")
            
        CityCode.objects.create(city_code ="2102408",
                                city_name ="Cajapió")
            
        CityCode.objects.create(city_code ="2102507",
                                city_name ="Cajari")
            
        CityCode.objects.create(city_code ="2102556",
                                city_name ="Campestre do Maranhão")
            
        CityCode.objects.create(city_code ="2102606",
                                city_name ="Cândido Mendes")
            
        CityCode.objects.create(city_code ="2102705",
                                city_name ="Cantanhede")
            
        CityCode.objects.create(city_code ="2102754",
                                city_name ="Capinzal do Norte")
            
        CityCode.objects.create(city_code ="2102804",
                                city_name ="Carolina")
            
        CityCode.objects.create(city_code ="2102903",
                                city_name ="Carutapera")
            
        CityCode.objects.create(city_code ="2103000",
                                city_name ="Caxias")
            
        CityCode.objects.create(city_code ="2103109",
                                city_name ="Cedral")
            
        CityCode.objects.create(city_code ="2103125",
                                city_name ="Central do Maranhão")
            
        CityCode.objects.create(city_code ="2103158",
                                city_name ="Centro do Guilherme")
            
        CityCode.objects.create(city_code ="2103174",
                                city_name ="Centro Novo do Maranhão")
            
        CityCode.objects.create(city_code ="2103208",
                                city_name ="Chapadinha")
            
        CityCode.objects.create(city_code ="2103257",
                                city_name ="Cidelândia")
            
        CityCode.objects.create(city_code ="2103307",
                                city_name ="Codó")
            
        CityCode.objects.create(city_code ="2103406",
                                city_name ="Coelho Neto")
            
        CityCode.objects.create(city_code ="2103505",
                                city_name ="Colinas")
            
        CityCode.objects.create(city_code ="2103554",
                                city_name ="Conceição do Lago-Açu")
            
        CityCode.objects.create(city_code ="2103604",
                                city_name ="Coroatá")
            
        CityCode.objects.create(city_code ="2103703",
                                city_name ="Cururupu")
            
        CityCode.objects.create(city_code ="2103752",
                                city_name ="Davinópolis")
            
        CityCode.objects.create(city_code ="2103802",
                                city_name ="Dom Pedro")
            
        CityCode.objects.create(city_code ="2103901",
                                city_name ="Duque Bacelar")
            
        CityCode.objects.create(city_code ="2104008",
                                city_name ="Esperantinópolis")
            
        CityCode.objects.create(city_code ="2104057",
                                city_name ="Estreito")
            
        CityCode.objects.create(city_code ="2104073",
                                city_name ="Feira Nova do Maranhão")
            
        CityCode.objects.create(city_code ="2104081",
                                city_name ="Fernando Falcão")
            
        CityCode.objects.create(city_code ="2104099",
                                city_name ="Formosa da Serra Negra")
            
        CityCode.objects.create(city_code ="2104107",
                                city_name ="Fortaleza dos Nogueiras")
            
        CityCode.objects.create(city_code ="2104206",
                                city_name ="Fortuna")
            
        CityCode.objects.create(city_code ="2104305",
                                city_name ="Godofredo Viana")
            
        CityCode.objects.create(city_code ="2104404",
                                city_name ="Gonçalves Dias")
            
        CityCode.objects.create(city_code ="2104503",
                                city_name ="Governador Archer")
            
        CityCode.objects.create(city_code ="2104552",
                                city_name ="Governador Edison Lobão")
            
        CityCode.objects.create(city_code ="2104602",
                                city_name ="Governador Eugênio Barros")
            
        CityCode.objects.create(city_code ="2104628",
                                city_name ="Governador Luiz Rocha")
            
        CityCode.objects.create(city_code ="2104651",
                                city_name ="Governador Newton Bello")
            
        CityCode.objects.create(city_code ="2104677",
                                city_name ="Governador Nunes Freire")
            
        CityCode.objects.create(city_code ="2104701",
                                city_name ="Graça Aranha")
            
        CityCode.objects.create(city_code ="2104800",
                                city_name ="Grajaú")
            
        CityCode.objects.create(city_code ="2104909",
                                city_name ="Guimarães")
            
        CityCode.objects.create(city_code ="2105005",
                                city_name ="Humberto de Campos")
            
        CityCode.objects.create(city_code ="2105104",
                                city_name ="Icatu")
            
        CityCode.objects.create(city_code ="2105153",
                                city_name ="Igarapé do Meio")
            
        CityCode.objects.create(city_code ="2105203",
                                city_name ="Igarapé Grande")
            
        CityCode.objects.create(city_code ="2105302",
                                city_name ="Imperatriz")
            
        CityCode.objects.create(city_code ="2105351",
                                city_name ="Itaipava do Grajaú")
            
        CityCode.objects.create(city_code ="2105401",
                                city_name ="Itapecuru Mirim")
            
        CityCode.objects.create(city_code ="2105427",
                                city_name ="Itinga do Maranhão")
            
        CityCode.objects.create(city_code ="2105450",
                                city_name ="Jatobá")
            
        CityCode.objects.create(city_code ="2105476",
                                city_name ="Jenipapo dos Vieiras")
            
        CityCode.objects.create(city_code ="2105500",
                                city_name ="João Lisboa")
            
        CityCode.objects.create(city_code ="2105609",
                                city_name ="Joselândia")
            
        CityCode.objects.create(city_code ="2105658",
                                city_name ="Junco do Maranhão")
            
        CityCode.objects.create(city_code ="2105708",
                                city_name ="Lago da Pedra")
            
        CityCode.objects.create(city_code ="2105807",
                                city_name ="Lago do Junco")
            
        CityCode.objects.create(city_code ="2105948",
                                city_name ="Lago dos Rodrigues")
            
        CityCode.objects.create(city_code ="2105906",
                                city_name ="Lago Verde")
            
        CityCode.objects.create(city_code ="2105922",
                                city_name ="Lagoa do Mato")
            
        CityCode.objects.create(city_code ="2105963",
                                city_name ="Lagoa Grande do Maranhão")
            
        CityCode.objects.create(city_code ="2105989",
                                city_name ="Lajeado Novo")
            
        CityCode.objects.create(city_code ="2106003",
                                city_name ="Lima Campos")
            
        CityCode.objects.create(city_code ="2106102",
                                city_name ="Loreto")
            
        CityCode.objects.create(city_code ="2106201",
                                city_name ="Luís Domingues")
            
        CityCode.objects.create(city_code ="2106300",
                                city_name ="Magalhães de Almeida")
            
        CityCode.objects.create(city_code ="2106326",
                                city_name ="Maracaçumé")
            
        CityCode.objects.create(city_code ="2106359",
                                city_name ="Marajá do Sena")
            
        CityCode.objects.create(city_code ="2106375",
                                city_name ="Maranhãozinho")
            
        CityCode.objects.create(city_code ="2106409",
                                city_name ="Mata Roma")
            
        CityCode.objects.create(city_code ="2106508",
                                city_name ="Matinha")
            
        CityCode.objects.create(city_code ="2106607",
                                city_name ="Matões")
            
        CityCode.objects.create(city_code ="2106631",
                                city_name ="Matões do Norte")
            
        CityCode.objects.create(city_code ="2106672",
                                city_name ="Milagres do Maranhão")
            
        CityCode.objects.create(city_code ="2106706",
                                city_name ="Mirador")
            
        CityCode.objects.create(city_code ="2106755",
                                city_name ="Miranda do Norte")
            
        CityCode.objects.create(city_code ="2106805",
                                city_name ="Mirinzal")
            
        CityCode.objects.create(city_code ="2106904",
                                city_name ="Monção")
            
        CityCode.objects.create(city_code ="2107001",
                                city_name ="Montes Altos")
            
        CityCode.objects.create(city_code ="2107100",
                                city_name ="Morros")
            
        CityCode.objects.create(city_code ="2107209",
                                city_name ="Nina Rodrigues")
            
        CityCode.objects.create(city_code ="2107258",
                                city_name ="Nova Colinas")
            
        CityCode.objects.create(city_code ="2107308",
                                city_name ="Nova Iorque")
            
        CityCode.objects.create(city_code ="2107357",
                                city_name ="Nova Olinda do Maranhão")
            
        CityCode.objects.create(city_code ="2107407",
                                city_name ="Olho d'Água das Cunhãs")
            
        CityCode.objects.create(city_code ="2107456",
                                city_name ="Olinda Nova do Maranhão")
            
        CityCode.objects.create(city_code ="2107506",
                                city_name ="Paço do Lumiar")
            
        CityCode.objects.create(city_code ="2107605",
                                city_name ="Palmeirândia")
            
        CityCode.objects.create(city_code ="2107704",
                                city_name ="Paraibano")
            
        CityCode.objects.create(city_code ="2107803",
                                city_name ="Parnarama")
            
        CityCode.objects.create(city_code ="2107902",
                                city_name ="Passagem Franca")
            
        CityCode.objects.create(city_code ="2108009",
                                city_name ="Pastos Bons")
            
        CityCode.objects.create(city_code ="2108058",
                                city_name ="Paulino Neves")
            
        CityCode.objects.create(city_code ="2108108",
                                city_name ="Paulo Ramos")
            
        CityCode.objects.create(city_code ="2108207",
                                city_name ="Pedreiras")
            
        CityCode.objects.create(city_code ="2108256",
                                city_name ="Pedro do Rosário")
            
        CityCode.objects.create(city_code ="2108306",
                                city_name ="Penalva")
            
        CityCode.objects.create(city_code ="2108405",
                                city_name ="Peri Mirim")
            
        CityCode.objects.create(city_code ="2108454",
                                city_name ="Peritoró")
            
        CityCode.objects.create(city_code ="2108504",
                                city_name ="Pindaré-Mirim")
            
        CityCode.objects.create(city_code ="2108603",
                                city_name ="Pinheiro")
            
        CityCode.objects.create(city_code ="2108702",
                                city_name ="Pio XII")
            
        CityCode.objects.create(city_code ="2108801",
                                city_name ="Pirapemas")
            
        CityCode.objects.create(city_code ="2108900",
                                city_name ="Poção de Pedras")
            
        CityCode.objects.create(city_code ="2109007",
                                city_name ="Porto Franco")
            
        CityCode.objects.create(city_code ="2109056",
                                city_name ="Porto Rico do Maranhão")
            
        CityCode.objects.create(city_code ="2109106",
                                city_name ="Presidente Dutra")
            
        CityCode.objects.create(city_code ="2109205",
                                city_name ="Presidente Juscelino")
            
        CityCode.objects.create(city_code ="2109239",
                                city_name ="Presidente Médici")
            
        CityCode.objects.create(city_code ="2109270",
                                city_name ="Presidente Sarney")
            
        CityCode.objects.create(city_code ="2109304",
                                city_name ="Presidente Vargas")
            
        CityCode.objects.create(city_code ="2109403",
                                city_name ="Primeira Cruz")
            
        CityCode.objects.create(city_code ="2109452",
                                city_name ="Raposa")
            
        CityCode.objects.create(city_code ="2109502",
                                city_name ="Riachão")
            
        CityCode.objects.create(city_code ="2109551",
                                city_name ="Ribamar Fiquene")
            
        CityCode.objects.create(city_code ="2109601",
                                city_name ="Rosário")
            
        CityCode.objects.create(city_code ="2109700",
                                city_name ="Sambaíba")
            
        CityCode.objects.create(city_code ="2109759",
                                city_name ="Santa Filomena do Maranhão")
            
        CityCode.objects.create(city_code ="2109809",
                                city_name ="Santa Helena")
            
        CityCode.objects.create(city_code ="2109908",
                                city_name ="Santa Inês")
            
        CityCode.objects.create(city_code ="2110005",
                                city_name ="Santa Luzia")
            
        CityCode.objects.create(city_code ="2110039",
                                city_name ="Santa Luzia do Paruá")
            
        CityCode.objects.create(city_code ="2110104",
                                city_name ="Santa Quitéria do Maranhão")
            
        CityCode.objects.create(city_code ="2110203",
                                city_name ="Santa Rita")
            
        CityCode.objects.create(city_code ="2110237",
                                city_name ="Santana do Maranhão")
            
        CityCode.objects.create(city_code ="2110278",
                                city_name ="Santo Amaro do Maranhão")
            
        CityCode.objects.create(city_code ="2110302",
                                city_name ="Santo Antônio dos Lopes")
            
        CityCode.objects.create(city_code ="2110401",
                                city_name ="São Benedito do Rio Preto")
            
        CityCode.objects.create(city_code ="2110500",
                                city_name ="São Bento")
            
        CityCode.objects.create(city_code ="2110609",
                                city_name ="São Bernardo")
            
        CityCode.objects.create(city_code ="2110658",
                                city_name ="São Domingos do Azeitão")
            
        CityCode.objects.create(city_code ="2110708",
                                city_name ="São Domingos do Maranhão")
            
        CityCode.objects.create(city_code ="2110807",
                                city_name ="São Félix de Balsas")
            
        CityCode.objects.create(city_code ="2110856",
                                city_name ="São Francisco do Brejão")
            
        CityCode.objects.create(city_code ="2110906",
                                city_name ="São Francisco do Maranhão")
            
        CityCode.objects.create(city_code ="2111003",
                                city_name ="São João Batista")
            
        CityCode.objects.create(city_code ="2111029",
                                city_name ="São João do Carú")
            
        CityCode.objects.create(city_code ="2111052",
                                city_name ="São João do Paraíso")
            
        CityCode.objects.create(city_code ="2111078",
                                city_name ="São João do Soter")
            
        CityCode.objects.create(city_code ="2111102",
                                city_name ="São João dos Patos")
            
        CityCode.objects.create(city_code ="2111201",
                                city_name ="São José de Ribamar")
            
        CityCode.objects.create(city_code ="2111250",
                                city_name ="São José dos Basílios")
            
        CityCode.objects.create(city_code ="2111300",
                                city_name ="São Luís")
            
        CityCode.objects.create(city_code ="2111409",
                                city_name ="São Luís Gonzaga do Maranhão")
            
        CityCode.objects.create(city_code ="2111508",
                                city_name ="São Mateus do Maranhão")
            
        CityCode.objects.create(city_code ="2111532",
                                city_name ="São Pedro da Água Branca")
            
        CityCode.objects.create(city_code ="2111573",
                                city_name ="São Pedro dos Crentes")
            
        CityCode.objects.create(city_code ="2111607",
                                city_name ="São Raimundo das Mangabeiras")
            
        CityCode.objects.create(city_code ="2111631",
                                city_name ="São Raimundo do Doca Bezerra")
            
        CityCode.objects.create(city_code ="2111672",
                                city_name ="São Roberto")
            
        CityCode.objects.create(city_code ="2111706",
                                city_name ="São Vicente Ferrer")
            
        CityCode.objects.create(city_code ="2111722",
                                city_name ="Satubinha")
            
        CityCode.objects.create(city_code ="2111748",
                                city_name ="Senador Alexandre Costa")
            
        CityCode.objects.create(city_code ="2111763",
                                city_name ="Senador La Rocque")
            
        CityCode.objects.create(city_code ="2111789",
                                city_name ="Serrano do Maranhão")
            
        CityCode.objects.create(city_code ="2111805",
                                city_name ="Sítio Novo")
            
        CityCode.objects.create(city_code ="2111904",
                                city_name ="Sucupira do Norte")
            
        CityCode.objects.create(city_code ="2111953",
                                city_name ="Sucupira do Riachão")
            
        CityCode.objects.create(city_code ="2112001",
                                city_name ="Tasso Fragoso")
            
        CityCode.objects.create(city_code ="2112100",
                                city_name ="Timbiras")
            
        CityCode.objects.create(city_code ="2112209",
                                city_name ="Timon")
            
        CityCode.objects.create(city_code ="2112233",
                                city_name ="Trizidela do Vale")
            
        CityCode.objects.create(city_code ="2112274",
                                city_name ="Tufilândia")
            
        CityCode.objects.create(city_code ="2112308",
                                city_name ="Tuntum")
            
        CityCode.objects.create(city_code ="2112407",
                                city_name ="Turiaçu")
            
        CityCode.objects.create(city_code ="2112456",
                                city_name ="Turilândia")
            
        CityCode.objects.create(city_code ="2112506",
                                city_name ="Tutóia")
            
        CityCode.objects.create(city_code ="2112605",
                                city_name ="Urbano Santos")
            
        CityCode.objects.create(city_code ="2112704",
                                city_name ="Vargem Grande")
            
        CityCode.objects.create(city_code ="2112803",
                                city_name ="Viana")
            
        CityCode.objects.create(city_code ="2112852",
                                city_name ="Vila Nova dos Martírios")
            
        CityCode.objects.create(city_code ="2112902",
                                city_name ="Vitória do Mearim")
            
        CityCode.objects.create(city_code ="2113009",
                                city_name ="Vitorino Freire")
            
        CityCode.objects.create(city_code ="2114007",
                                city_name ="Zé Doca")
            
        CityCode.objects.create(city_code ="2200053",
                                city_name ="Acauã")
            
        CityCode.objects.create(city_code ="2200103",
                                city_name ="Agricolândia")
            
        CityCode.objects.create(city_code ="2200202",
                                city_name ="Água Branca")
            
        CityCode.objects.create(city_code ="2200251",
                                city_name ="Alagoinha do Piauí")
            
        CityCode.objects.create(city_code ="2200277",
                                city_name ="Alegrete do Piauí")
            
        CityCode.objects.create(city_code ="2200301",
                                city_name ="Alto Longá")
            
        CityCode.objects.create(city_code ="2200400",
                                city_name ="Altos")
            
        CityCode.objects.create(city_code ="2200459",
                                city_name ="Alvorada do Gurguéia")
            
        CityCode.objects.create(city_code ="2200509",
                                city_name ="Amarante")
            
        CityCode.objects.create(city_code ="2200608",
                                city_name ="Angical do Piauí")
            
        CityCode.objects.create(city_code ="2200707",
                                city_name ="Anísio de Abreu")
            
        CityCode.objects.create(city_code ="2200806",
                                city_name ="Antônio Almeida")
            
        CityCode.objects.create(city_code ="2200905",
                                city_name ="Aroazes")
            
        CityCode.objects.create(city_code ="2200954",
                                city_name ="Aroeiras do Itaim")
            
        CityCode.objects.create(city_code ="2201002",
                                city_name ="Arraial")
            
        CityCode.objects.create(city_code ="2201051",
                                city_name ="Assunção do Piauí")
            
        CityCode.objects.create(city_code ="2201101",
                                city_name ="Avelino Lopes")
            
        CityCode.objects.create(city_code ="2201150",
                                city_name ="Baixa Grande do Ribeiro")
            
        CityCode.objects.create(city_code ="2201176",
                                city_name ="Barra D'Alcântara")
            
        CityCode.objects.create(city_code ="2201200",
                                city_name ="Barras")
            
        CityCode.objects.create(city_code ="2201309",
                                city_name ="Barreiras do Piauí")
            
        CityCode.objects.create(city_code ="2201408",
                                city_name ="Barro Duro")
            
        CityCode.objects.create(city_code ="2201507",
                                city_name ="Batalha")
            
        CityCode.objects.create(city_code ="2201556",
                                city_name ="Bela Vista do Piauí")
            
        CityCode.objects.create(city_code ="2201572",
                                city_name ="Belém do Piauí")
            
        CityCode.objects.create(city_code ="2201606",
                                city_name ="Beneditinos")
            
        CityCode.objects.create(city_code ="2201705",
                                city_name ="Bertolínia")
            
        CityCode.objects.create(city_code ="2201739",
                                city_name ="Betânia do Piauí")
            
        CityCode.objects.create(city_code ="2201770",
                                city_name ="Boa Hora")
            
        CityCode.objects.create(city_code ="2201804",
                                city_name ="Bocaina")
            
        CityCode.objects.create(city_code ="2201903",
                                city_name ="Bom Jesus")
            
        CityCode.objects.create(city_code ="2201919",
                                city_name ="Bom Princípio do Piauí")
            
        CityCode.objects.create(city_code ="2201929",
                                city_name ="Bonfim do Piauí")
            
        CityCode.objects.create(city_code ="2201945",
                                city_name ="Boqueirão do Piauí")
            
        CityCode.objects.create(city_code ="2201960",
                                city_name ="Brasileira")
            
        CityCode.objects.create(city_code ="2201988",
                                city_name ="Brejo do Piauí")
            
        CityCode.objects.create(city_code ="2202000",
                                city_name ="Buriti dos Lopes")
            
        CityCode.objects.create(city_code ="2202026",
                                city_name ="Buriti dos Montes")
            
        CityCode.objects.create(city_code ="2202059",
                                city_name ="Cabeceiras do Piauí")
            
        CityCode.objects.create(city_code ="2202075",
                                city_name ="Cajazeiras do Piauí")
            
        CityCode.objects.create(city_code ="2202083",
                                city_name ="Cajueiro da Praia")
            
        CityCode.objects.create(city_code ="2202091",
                                city_name ="Caldeirão Grande do Piauí")
            
        CityCode.objects.create(city_code ="2202109",
                                city_name ="Campinas do Piauí")
            
        CityCode.objects.create(city_code ="2202117",
                                city_name ="Campo Alegre do Fidalgo")
            
        CityCode.objects.create(city_code ="2202133",
                                city_name ="Campo Grande do Piauí")
            
        CityCode.objects.create(city_code ="2202174",
                                city_name ="Campo Largo do Piauí")
            
        CityCode.objects.create(city_code ="2202208",
                                city_name ="Campo Maior")
            
        CityCode.objects.create(city_code ="2202251",
                                city_name ="Canavieira")
            
        CityCode.objects.create(city_code ="2202307",
                                city_name ="Canto do Buriti")
            
        CityCode.objects.create(city_code ="2202406",
                                city_name ="Capitão de Campos")
            
        CityCode.objects.create(city_code ="2202455",
                                city_name ="Capitão Gervásio Oliveira")
            
        CityCode.objects.create(city_code ="2202505",
                                city_name ="Caracol")
            
        CityCode.objects.create(city_code ="2202539",
                                city_name ="Caraúbas do Piauí")
            
        CityCode.objects.create(city_code ="2202554",
                                city_name ="Caridade do Piauí")
            
        CityCode.objects.create(city_code ="2202604",
                                city_name ="Castelo do Piauí")
            
        CityCode.objects.create(city_code ="2202653",
                                city_name ="Caxingó")
            
        CityCode.objects.create(city_code ="2202703",
                                city_name ="Cocal")
            
        CityCode.objects.create(city_code ="2202711",
                                city_name ="Cocal de Telha")
            
        CityCode.objects.create(city_code ="2202729",
                                city_name ="Cocal dos Alves")
            
        CityCode.objects.create(city_code ="2202737",
                                city_name ="Coivaras")
            
        CityCode.objects.create(city_code ="2202752",
                                city_name ="Colônia do Gurguéia")
            
        CityCode.objects.create(city_code ="2202778",
                                city_name ="Colônia do Piauí")
            
        CityCode.objects.create(city_code ="2202802",
                                city_name ="Conceição do Canindé")
            
        CityCode.objects.create(city_code ="2202851",
                                city_name ="Coronel José Dias")
            
        CityCode.objects.create(city_code ="2202901",
                                city_name ="Corrente")
            
        CityCode.objects.create(city_code ="2203008",
                                city_name ="Cristalândia do Piauí")
            
        CityCode.objects.create(city_code ="2203107",
                                city_name ="Cristino Castro")
            
        CityCode.objects.create(city_code ="2203206",
                                city_name ="Curimatá")
            
        CityCode.objects.create(city_code ="2203230",
                                city_name ="Currais")
            
        CityCode.objects.create(city_code ="2203271",
                                city_name ="Curral Novo do Piauí")
            
        CityCode.objects.create(city_code ="2203255",
                                city_name ="Curralinhos")
            
        CityCode.objects.create(city_code ="2203305",
                                city_name ="Demerval Lobão")
            
        CityCode.objects.create(city_code ="2203354",
                                city_name ="Dirceu Arcoverde")
            
        CityCode.objects.create(city_code ="2203404",
                                city_name ="Dom Expedito Lopes")
            
        CityCode.objects.create(city_code ="2203453",
                                city_name ="Dom Inocêncio")
            
        CityCode.objects.create(city_code ="2203420",
                                city_name ="Domingos Mourão")
            
        CityCode.objects.create(city_code ="2203503",
                                city_name ="Elesbão Veloso")
            
        CityCode.objects.create(city_code ="2203602",
                                city_name ="Eliseu Martins")
            
        CityCode.objects.create(city_code ="2203701",
                                city_name ="Esperantina")
            
        CityCode.objects.create(city_code ="2203750",
                                city_name ="Fartura do Piauí")
            
        CityCode.objects.create(city_code ="2203800",
                                city_name ="Flores do Piauí")
            
        CityCode.objects.create(city_code ="2203859",
                                city_name ="Floresta do Piauí")
            
        CityCode.objects.create(city_code ="2203909",
                                city_name ="Floriano")
            
        CityCode.objects.create(city_code ="2204006",
                                city_name ="Francinópolis")
            
        CityCode.objects.create(city_code ="2204105",
                                city_name ="Francisco Ayres")
            
        CityCode.objects.create(city_code ="2204154",
                                city_name ="Francisco Macedo")
            
        CityCode.objects.create(city_code ="2204204",
                                city_name ="Francisco Santos")
            
        CityCode.objects.create(city_code ="2204303",
                                city_name ="Fronteiras")
            
        CityCode.objects.create(city_code ="2204352",
                                city_name ="Geminiano")
            
        CityCode.objects.create(city_code ="2204402",
                                city_name ="Gilbués")
            
        CityCode.objects.create(city_code ="2204501",
                                city_name ="Guadalupe")
            
        CityCode.objects.create(city_code ="2204550",
                                city_name ="Guaribas")
            
        CityCode.objects.create(city_code ="2204600",
                                city_name ="Hugo Napoleão")
            
        CityCode.objects.create(city_code ="2204659",
                                city_name ="Ilha Grande")
            
        CityCode.objects.create(city_code ="2204709",
                                city_name ="Inhuma")
            
        CityCode.objects.create(city_code ="2204808",
                                city_name ="Ipiranga do Piauí")
            
        CityCode.objects.create(city_code ="2204907",
                                city_name ="Isaías Coelho")
            
        CityCode.objects.create(city_code ="2205003",
                                city_name ="Itainópolis")
            
        CityCode.objects.create(city_code ="2205102",
                                city_name ="Itaueira")
            
        CityCode.objects.create(city_code ="2205151",
                                city_name ="Jacobina do Piauí")
            
        CityCode.objects.create(city_code ="2205201",
                                city_name ="Jaicós")
            
        CityCode.objects.create(city_code ="2205250",
                                city_name ="Jardim do Mulato")
            
        CityCode.objects.create(city_code ="2205276",
                                city_name ="Jatobá do Piauí")
            
        CityCode.objects.create(city_code ="2205300",
                                city_name ="Jerumenha")
            
        CityCode.objects.create(city_code ="2205359",
                                city_name ="João Costa")
            
        CityCode.objects.create(city_code ="2205409",
                                city_name ="Joaquim Pires")
            
        CityCode.objects.create(city_code ="2205458",
                                city_name ="Joca Marques")
            
        CityCode.objects.create(city_code ="2205508",
                                city_name ="José de Freitas")
            
        CityCode.objects.create(city_code ="2205516",
                                city_name ="Juazeiro do Piauí")
            
        CityCode.objects.create(city_code ="2205524",
                                city_name ="Júlio Borges")
            
        CityCode.objects.create(city_code ="2205532",
                                city_name ="Jurema")
            
        CityCode.objects.create(city_code ="2205557",
                                city_name ="Lagoa Alegre")
            
        CityCode.objects.create(city_code ="2205573",
                                city_name ="Lagoa de São Francisco")
            
        CityCode.objects.create(city_code ="2205565",
                                city_name ="Lagoa do Barro do Piauí")
            
        CityCode.objects.create(city_code ="2205581",
                                city_name ="Lagoa do Piauí")
            
        CityCode.objects.create(city_code ="2205599",
                                city_name ="Lagoa do Sítio")
            
        CityCode.objects.create(city_code ="2205540",
                                city_name ="Lagoinha do Piauí")
            
        CityCode.objects.create(city_code ="2205607",
                                city_name ="Landri Sales")
            
        CityCode.objects.create(city_code ="2205706",
                                city_name ="Luís Correia")
            
        CityCode.objects.create(city_code ="2205805",
                                city_name ="Luzilândia")
            
        CityCode.objects.create(city_code ="2205854",
                                city_name ="Madeiro")
            
        CityCode.objects.create(city_code ="2205904",
                                city_name ="Manoel Emídio")
            
        CityCode.objects.create(city_code ="2205953",
                                city_name ="Marcolândia")
            
        CityCode.objects.create(city_code ="2206001",
                                city_name ="Marcos Parente")
            
        CityCode.objects.create(city_code ="2206050",
                                city_name ="Massapê do Piauí")
            
        CityCode.objects.create(city_code ="2206100",
                                city_name ="Matias Olímpio")
            
        CityCode.objects.create(city_code ="2206209",
                                city_name ="Miguel Alves")
            
        CityCode.objects.create(city_code ="2206308",
                                city_name ="Miguel Leão")
            
        CityCode.objects.create(city_code ="2206357",
                                city_name ="Milton Brandão")
            
        CityCode.objects.create(city_code ="2206407",
                                city_name ="Monsenhor Gil")
            
        CityCode.objects.create(city_code ="2206506",
                                city_name ="Monsenhor Hipólito")
            
        CityCode.objects.create(city_code ="2206605",
                                city_name ="Monte Alegre do Piauí")
            
        CityCode.objects.create(city_code ="2206654",
                                city_name ="Morro Cabeça no Tempo")
            
        CityCode.objects.create(city_code ="2206670",
                                city_name ="Morro do Chapéu do Piauí")
            
        CityCode.objects.create(city_code ="2206696",
                                city_name ="Murici dos Portelas")
            
        CityCode.objects.create(city_code ="2206704",
                                city_name ="Nazaré do Piauí")
            
        CityCode.objects.create(city_code ="2206720",
                                city_name ="Nazária")
            
        CityCode.objects.create(city_code ="2206753",
                                city_name ="Nossa Senhora de Nazaré")
            
        CityCode.objects.create(city_code ="2206803",
                                city_name ="Nossa Senhora dos Remédios")
            
        CityCode.objects.create(city_code ="2207959",
                                city_name ="Nova Santa Rita")
            
        CityCode.objects.create(city_code ="2206902",
                                city_name ="Novo Oriente do Piauí")
            
        CityCode.objects.create(city_code ="2206951",
                                city_name ="Novo Santo Antônio")
            
        CityCode.objects.create(city_code ="2207009",
                                city_name ="Oeiras")
            
        CityCode.objects.create(city_code ="2207108",
                                city_name ="Olho D'Água do Piauí")
            
        CityCode.objects.create(city_code ="2207207",
                                city_name ="Padre Marcos")
            
        CityCode.objects.create(city_code ="2207306",
                                city_name ="Paes Landim")
            
        CityCode.objects.create(city_code ="2207355",
                                city_name ="Pajeú do Piauí")
            
        CityCode.objects.create(city_code ="2207405",
                                city_name ="Palmeira do Piauí")
            
        CityCode.objects.create(city_code ="2207504",
                                city_name ="Palmeirais")
            
        CityCode.objects.create(city_code ="2207553",
                                city_name ="Paquetá")
            
        CityCode.objects.create(city_code ="2207603",
                                city_name ="Parnaguá")
            
        CityCode.objects.create(city_code ="2207702",
                                city_name ="Parnaíba")
            
        CityCode.objects.create(city_code ="2207751",
                                city_name ="Passagem Franca do Piauí")
            
        CityCode.objects.create(city_code ="2207777",
                                city_name ="Patos do Piauí")
            
        CityCode.objects.create(city_code ="2207793",
                                city_name ="Pau D'Arco do Piauí")
            
        CityCode.objects.create(city_code ="2207801",
                                city_name ="Paulistana")
            
        CityCode.objects.create(city_code ="2207850",
                                city_name ="Pavussu")
            
        CityCode.objects.create(city_code ="2207900",
                                city_name ="Pedro II")
            
        CityCode.objects.create(city_code ="2207934",
                                city_name ="Pedro Laurentino")
            
        CityCode.objects.create(city_code ="2208007",
                                city_name ="Picos")
            
        CityCode.objects.create(city_code ="2208106",
                                city_name ="Pimenteiras")
            
        CityCode.objects.create(city_code ="2208205",
                                city_name ="Pio IX")
            
        CityCode.objects.create(city_code ="2208304",
                                city_name ="Piracuruca")
            
        CityCode.objects.create(city_code ="2208403",
                                city_name ="Piripiri")
            
        CityCode.objects.create(city_code ="2208502",
                                city_name ="Porto")
            
        CityCode.objects.create(city_code ="2208551",
                                city_name ="Porto Alegre do Piauí")
            
        CityCode.objects.create(city_code ="2208601",
                                city_name ="Prata do Piauí")
            
        CityCode.objects.create(city_code ="2208650",
                                city_name ="Queimada Nova")
            
        CityCode.objects.create(city_code ="2208700",
                                city_name ="Redenção do Gurguéia")
            
        CityCode.objects.create(city_code ="2208809",
                                city_name ="Regeneração")
            
        CityCode.objects.create(city_code ="2208858",
                                city_name ="Riacho Frio")
            
        CityCode.objects.create(city_code ="2208874",
                                city_name ="Ribeira do Piauí")
            
        CityCode.objects.create(city_code ="2208908",
                                city_name ="Ribeiro Gonçalves")
            
        CityCode.objects.create(city_code ="2209005",
                                city_name ="Rio Grande do Piauí")
            
        CityCode.objects.create(city_code ="2209104",
                                city_name ="Santa Cruz do Piauí")
            
        CityCode.objects.create(city_code ="2209153",
                                city_name ="Santa Cruz dos Milagres")
            
        CityCode.objects.create(city_code ="2209203",
                                city_name ="Santa Filomena")
            
        CityCode.objects.create(city_code ="2209302",
                                city_name ="Santa Luz")
            
        CityCode.objects.create(city_code ="2209377",
                                city_name ="Santa Rosa do Piauí")
            
        CityCode.objects.create(city_code ="2209351",
                                city_name ="Santana do Piauí")
            
        CityCode.objects.create(city_code ="2209401",
                                city_name ="Santo Antônio de Lisboa")
            
        CityCode.objects.create(city_code ="2209450",
                                city_name ="Santo Antônio dos Milagres")
            
        CityCode.objects.create(city_code ="2209500",
                                city_name ="Santo Inácio do Piauí")
            
        CityCode.objects.create(city_code ="2209559",
                                city_name ="São Braz do Piauí")
            
        CityCode.objects.create(city_code ="2209609",
                                city_name ="São Félix do Piauí")
            
        CityCode.objects.create(city_code ="2209658",
                                city_name ="São Francisco de Assis do Piauí")
            
        CityCode.objects.create(city_code ="2209708",
                                city_name ="São Francisco do Piauí")
            
        CityCode.objects.create(city_code ="2209757",
                                city_name ="São Gonçalo do Gurguéia")
            
        CityCode.objects.create(city_code ="2209807",
                                city_name ="São Gonçalo do Piauí")
            
        CityCode.objects.create(city_code ="2209856",
                                city_name ="São João da Canabrava")
            
        CityCode.objects.create(city_code ="2209872",
                                city_name ="São João da Fronteira")
            
        CityCode.objects.create(city_code ="2209906",
                                city_name ="São João da Serra")
            
        CityCode.objects.create(city_code ="2209955",
                                city_name ="São João da Varjota")
            
        CityCode.objects.create(city_code ="2209971",
                                city_name ="São João do Arraial")
            
        CityCode.objects.create(city_code ="2210003",
                                city_name ="São João do Piauí")
            
        CityCode.objects.create(city_code ="2210052",
                                city_name ="São José do Divino")
            
        CityCode.objects.create(city_code ="2210102",
                                city_name ="São José do Peixe")
            
        CityCode.objects.create(city_code ="2210201",
                                city_name ="São José do Piauí")
            
        CityCode.objects.create(city_code ="2210300",
                                city_name ="São Julião")
            
        CityCode.objects.create(city_code ="2210359",
                                city_name ="São Lourenço do Piauí")
            
        CityCode.objects.create(city_code ="2210375",
                                city_name ="São Luis do Piauí")
            
        CityCode.objects.create(city_code ="2210383",
                                city_name ="São Miguel da Baixa Grande")
            
        CityCode.objects.create(city_code ="2210391",
                                city_name ="São Miguel do Fidalgo")
            
        CityCode.objects.create(city_code ="2210409",
                                city_name ="São Miguel do Tapuio")
            
        CityCode.objects.create(city_code ="2210508",
                                city_name ="São Pedro do Piauí")
            
        CityCode.objects.create(city_code ="2210607",
                                city_name ="São Raimundo Nonato")
            
        CityCode.objects.create(city_code ="2210623",
                                city_name ="Sebastião Barros")
            
        CityCode.objects.create(city_code ="2210631",
                                city_name ="Sebastião Leal")
            
        CityCode.objects.create(city_code ="2210656",
                                city_name ="Sigefredo Pacheco")
            
        CityCode.objects.create(city_code ="2210706",
                                city_name ="Simões")
            
        CityCode.objects.create(city_code ="2210805",
                                city_name ="Simplício Mendes")
            
        CityCode.objects.create(city_code ="2210904",
                                city_name ="Socorro do Piauí")
            
        CityCode.objects.create(city_code ="2210938",
                                city_name ="Sussuapara")
            
        CityCode.objects.create(city_code ="2210953",
                                city_name ="Tamboril do Piauí")
            
        CityCode.objects.create(city_code ="2210979",
                                city_name ="Tanque do Piauí")
            
        CityCode.objects.create(city_code ="2211001",
                                city_name ="Teresina")
            
        CityCode.objects.create(city_code ="2211100",
                                city_name ="União")
            
        CityCode.objects.create(city_code ="2211209",
                                city_name ="Uruçuí")
            
        CityCode.objects.create(city_code ="2211308",
                                city_name ="Valença do Piauí")
            
        CityCode.objects.create(city_code ="2211357",
                                city_name ="Várzea Branca")
            
        CityCode.objects.create(city_code ="2211407",
                                city_name ="Várzea Grande")
            
        CityCode.objects.create(city_code ="2211506",
                                city_name ="Vera Mendes")
            
        CityCode.objects.create(city_code ="2211605",
                                city_name ="Vila Nova do Piauí")
            
        CityCode.objects.create(city_code ="2211704",
                                city_name ="Wall Ferraz")
            
        CityCode.objects.create(city_code ="2300101",
                                city_name ="Abaiara")
            
        CityCode.objects.create(city_code ="2300150",
                                city_name ="Acarape")
            
        CityCode.objects.create(city_code ="2300200",
                                city_name ="Acaraú")
            
        CityCode.objects.create(city_code ="2300309",
                                city_name ="Acopiara")
            
        CityCode.objects.create(city_code ="2300408",
                                city_name ="Aiuaba")
            
        CityCode.objects.create(city_code ="2300507",
                                city_name ="Alcântaras")
            
        CityCode.objects.create(city_code ="2300606",
                                city_name ="Altaneira")
            
        CityCode.objects.create(city_code ="2300705",
                                city_name ="Alto Santo")
            
        CityCode.objects.create(city_code ="2300754",
                                city_name ="Amontada")
            
        CityCode.objects.create(city_code ="2300804",
                                city_name ="Antonina do Norte")
            
        CityCode.objects.create(city_code ="2300903",
                                city_name ="Apuiarés")
            
        CityCode.objects.create(city_code ="2301000",
                                city_name ="Aquiraz")
            
        CityCode.objects.create(city_code ="2301109",
                                city_name ="Aracati")
            
        CityCode.objects.create(city_code ="2301208",
                                city_name ="Aracoiaba")
            
        CityCode.objects.create(city_code ="2301257",
                                city_name ="Ararendá")
            
        CityCode.objects.create(city_code ="2301307",
                                city_name ="Araripe")
            
        CityCode.objects.create(city_code ="2301406",
                                city_name ="Aratuba")
            
        CityCode.objects.create(city_code ="2301505",
                                city_name ="Arneiroz")
            
        CityCode.objects.create(city_code ="2301604",
                                city_name ="Assaré")
            
        CityCode.objects.create(city_code ="2301703",
                                city_name ="Aurora")
            
        CityCode.objects.create(city_code ="2301802",
                                city_name ="Baixio")
            
        CityCode.objects.create(city_code ="2301851",
                                city_name ="Banabuiú")
            
        CityCode.objects.create(city_code ="2301901",
                                city_name ="Barbalha")
            
        CityCode.objects.create(city_code ="2301950",
                                city_name ="Barreira")
            
        CityCode.objects.create(city_code ="2302008",
                                city_name ="Barro")
            
        CityCode.objects.create(city_code ="2302057",
                                city_name ="Barroquinha")
            
        CityCode.objects.create(city_code ="2302107",
                                city_name ="Baturité")
            
        CityCode.objects.create(city_code ="2302206",
                                city_name ="Beberibe")
            
        CityCode.objects.create(city_code ="2302305",
                                city_name ="Bela Cruz")
            
        CityCode.objects.create(city_code ="2302404",
                                city_name ="Boa Viagem")
            
        CityCode.objects.create(city_code ="2302503",
                                city_name ="Brejo Santo")
            
        CityCode.objects.create(city_code ="2302602",
                                city_name ="Camocim")
            
        CityCode.objects.create(city_code ="2302701",
                                city_name ="Campos Sales")
            
        CityCode.objects.create(city_code ="2302800",
                                city_name ="Canindé")
            
        CityCode.objects.create(city_code ="2302909",
                                city_name ="Capistrano")
            
        CityCode.objects.create(city_code ="2303006",
                                city_name ="Caridade")
            
        CityCode.objects.create(city_code ="2303105",
                                city_name ="Cariré")
            
        CityCode.objects.create(city_code ="2303204",
                                city_name ="Caririaçu")
            
        CityCode.objects.create(city_code ="2303303",
                                city_name ="Cariús")
            
        CityCode.objects.create(city_code ="2303402",
                                city_name ="Carnaubal")
            
        CityCode.objects.create(city_code ="2303501",
                                city_name ="Cascavel")
            
        CityCode.objects.create(city_code ="2303600",
                                city_name ="Catarina")
            
        CityCode.objects.create(city_code ="2303659",
                                city_name ="Catunda")
            
        CityCode.objects.create(city_code ="2303709",
                                city_name ="Caucaia")
            
        CityCode.objects.create(city_code ="2303808",
                                city_name ="Cedro")
            
        CityCode.objects.create(city_code ="2303907",
                                city_name ="Chaval")
            
        CityCode.objects.create(city_code ="2303931",
                                city_name ="Choró")
            
        CityCode.objects.create(city_code ="2303956",
                                city_name ="Chorozinho")
            
        CityCode.objects.create(city_code ="2304004",
                                city_name ="Coreaú")
            
        CityCode.objects.create(city_code ="2304103",
                                city_name ="Crateús")
            
        CityCode.objects.create(city_code ="2304202",
                                city_name ="Crato")
            
        CityCode.objects.create(city_code ="2304236",
                                city_name ="Croatá")
            
        CityCode.objects.create(city_code ="2304251",
                                city_name ="Cruz")
            
        CityCode.objects.create(city_code ="2304269",
                                city_name ="Deputado Irapuan Pinheiro")
            
        CityCode.objects.create(city_code ="2304277",
                                city_name ="Ereré")
            
        CityCode.objects.create(city_code ="2304285",
                                city_name ="Eusébio")
            
        CityCode.objects.create(city_code ="2304301",
                                city_name ="Farias Brito")
            
        CityCode.objects.create(city_code ="2304350",
                                city_name ="Forquilha")
            
        CityCode.objects.create(city_code ="2304400",
                                city_name ="Fortaleza")
            
        CityCode.objects.create(city_code ="2304459",
                                city_name ="Fortim")
            
        CityCode.objects.create(city_code ="2304509",
                                city_name ="Frecheirinha")
            
        CityCode.objects.create(city_code ="2304608",
                                city_name ="General Sampaio")
            
        CityCode.objects.create(city_code ="2304657",
                                city_name ="Graça")
            
        CityCode.objects.create(city_code ="2304707",
                                city_name ="Granja")
            
        CityCode.objects.create(city_code ="2304806",
                                city_name ="Granjeiro")
            
        CityCode.objects.create(city_code ="2304905",
                                city_name ="Groaíras")
            
        CityCode.objects.create(city_code ="2304954",
                                city_name ="Guaiúba")
            
        CityCode.objects.create(city_code ="2305001",
                                city_name ="Guaraciaba do Norte")
            
        CityCode.objects.create(city_code ="2305100",
                                city_name ="Guaramiranga")
            
        CityCode.objects.create(city_code ="2305209",
                                city_name ="Hidrolândia")
            
        CityCode.objects.create(city_code ="2305233",
                                city_name ="Horizonte")
            
        CityCode.objects.create(city_code ="2305266",
                                city_name ="Ibaretama")
            
        CityCode.objects.create(city_code ="2305308",
                                city_name ="Ibiapina")
            
        CityCode.objects.create(city_code ="2305332",
                                city_name ="Ibicuitinga")
            
        CityCode.objects.create(city_code ="2305357",
                                city_name ="Icapuí")
            
        CityCode.objects.create(city_code ="2305407",
                                city_name ="Icó")
            
        CityCode.objects.create(city_code ="2305506",
                                city_name ="Iguatu")
            
        CityCode.objects.create(city_code ="2305605",
                                city_name ="Independência")
            
        CityCode.objects.create(city_code ="2305654",
                                city_name ="Ipaporanga")
            
        CityCode.objects.create(city_code ="2305704",
                                city_name ="Ipaumirim")
            
        CityCode.objects.create(city_code ="2305803",
                                city_name ="Ipu")
            
        CityCode.objects.create(city_code ="2305902",
                                city_name ="Ipueiras")
            
        CityCode.objects.create(city_code ="2306009",
                                city_name ="Iracema")
            
        CityCode.objects.create(city_code ="2306108",
                                city_name ="Irauçuba")
            
        CityCode.objects.create(city_code ="2306207",
                                city_name ="Itaiçaba")
            
        CityCode.objects.create(city_code ="2306256",
                                city_name ="Itaitinga")
            
        CityCode.objects.create(city_code ="2306306",
                                city_name ="Itapajé")
            
        CityCode.objects.create(city_code ="2306405",
                                city_name ="Itapipoca")
            
        CityCode.objects.create(city_code ="2306504",
                                city_name ="Itapiúna")
            
        CityCode.objects.create(city_code ="2306553",
                                city_name ="Itarema")
            
        CityCode.objects.create(city_code ="2306603",
                                city_name ="Itatira")
            
        CityCode.objects.create(city_code ="2306702",
                                city_name ="Jaguaretama")
            
        CityCode.objects.create(city_code ="2306801",
                                city_name ="Jaguaribara")
            
        CityCode.objects.create(city_code ="2306900",
                                city_name ="Jaguaribe")
            
        CityCode.objects.create(city_code ="2307007",
                                city_name ="Jaguaruana")
            
        CityCode.objects.create(city_code ="2307106",
                                city_name ="Jardim")
            
        CityCode.objects.create(city_code ="2307205",
                                city_name ="Jati")
            
        CityCode.objects.create(city_code ="2307254",
                                city_name ="Jijoca de Jericoacoara")
            
        CityCode.objects.create(city_code ="2307304",
                                city_name ="Juazeiro do Norte")
            
        CityCode.objects.create(city_code ="2307403",
                                city_name ="Jucás")
            
        CityCode.objects.create(city_code ="2307502",
                                city_name ="Lavras da Mangabeira")
            
        CityCode.objects.create(city_code ="2307601",
                                city_name ="Limoeiro do Norte")
            
        CityCode.objects.create(city_code ="2307635",
                                city_name ="Madalena")
            
        CityCode.objects.create(city_code ="2307650",
                                city_name ="Maracanaú")
            
        CityCode.objects.create(city_code ="2307700",
                                city_name ="Maranguape")
            
        CityCode.objects.create(city_code ="2307809",
                                city_name ="Marco")
            
        CityCode.objects.create(city_code ="2307908",
                                city_name ="Martinópole")
            
        CityCode.objects.create(city_code ="2308005",
                                city_name ="Massapê")
            
        CityCode.objects.create(city_code ="2308104",
                                city_name ="Mauriti")
            
        CityCode.objects.create(city_code ="2308203",
                                city_name ="Meruoca")
            
        CityCode.objects.create(city_code ="2308302",
                                city_name ="Milagres")
            
        CityCode.objects.create(city_code ="2308351",
                                city_name ="Milhã")
            
        CityCode.objects.create(city_code ="2308377",
                                city_name ="Miraíma")
            
        CityCode.objects.create(city_code ="2308401",
                                city_name ="Missão Velha")
            
        CityCode.objects.create(city_code ="2308500",
                                city_name ="Mombaça")
            
        CityCode.objects.create(city_code ="2308609",
                                city_name ="Monsenhor Tabosa")
            
        CityCode.objects.create(city_code ="2308708",
                                city_name ="Morada Nova")
            
        CityCode.objects.create(city_code ="2308807",
                                city_name ="Moraújo")
            
        CityCode.objects.create(city_code ="2308906",
                                city_name ="Morrinhos")
            
        CityCode.objects.create(city_code ="2309003",
                                city_name ="Mucambo")
            
        CityCode.objects.create(city_code ="2309102",
                                city_name ="Mulungu")
            
        CityCode.objects.create(city_code ="2309201",
                                city_name ="Nova Olinda")
            
        CityCode.objects.create(city_code ="2309300",
                                city_name ="Nova Russas")
            
        CityCode.objects.create(city_code ="2309409",
                                city_name ="Novo Oriente")
            
        CityCode.objects.create(city_code ="2309458",
                                city_name ="Ocara")
            
        CityCode.objects.create(city_code ="2309508",
                                city_name ="Orós")
            
        CityCode.objects.create(city_code ="2309607",
                                city_name ="Pacajus")
            
        CityCode.objects.create(city_code ="2309706",
                                city_name ="Pacatuba")
            
        CityCode.objects.create(city_code ="2309805",
                                city_name ="Pacoti")
            
        CityCode.objects.create(city_code ="2309904",
                                city_name ="Pacujá")
            
        CityCode.objects.create(city_code ="2310001",
                                city_name ="Palhano")
            
        CityCode.objects.create(city_code ="2310100",
                                city_name ="Palmácia")
            
        CityCode.objects.create(city_code ="2310209",
                                city_name ="Paracuru")
            
        CityCode.objects.create(city_code ="2310258",
                                city_name ="Paraipaba")
            
        CityCode.objects.create(city_code ="2310308",
                                city_name ="Parambu")
            
        CityCode.objects.create(city_code ="2310407",
                                city_name ="Paramoti")
            
        CityCode.objects.create(city_code ="2310506",
                                city_name ="Pedra Branca")
            
        CityCode.objects.create(city_code ="2310605",
                                city_name ="Penaforte")
            
        CityCode.objects.create(city_code ="2310704",
                                city_name ="Pentecoste")
            
        CityCode.objects.create(city_code ="2310803",
                                city_name ="Pereiro")
            
        CityCode.objects.create(city_code ="2310852",
                                city_name ="Pindoretama")
            
        CityCode.objects.create(city_code ="2310902",
                                city_name ="Piquet Carneiro")
            
        CityCode.objects.create(city_code ="2310951",
                                city_name ="Pires Ferreira")
            
        CityCode.objects.create(city_code ="2311009",
                                city_name ="Poranga")
            
        CityCode.objects.create(city_code ="2311108",
                                city_name ="Porteiras")
            
        CityCode.objects.create(city_code ="2311207",
                                city_name ="Potengi")
            
        CityCode.objects.create(city_code ="2311231",
                                city_name ="Potiretama")
            
        CityCode.objects.create(city_code ="2311264",
                                city_name ="Quiterianópolis")
            
        CityCode.objects.create(city_code ="2311306",
                                city_name ="Quixadá")
            
        CityCode.objects.create(city_code ="2311355",
                                city_name ="Quixelô")
            
        CityCode.objects.create(city_code ="2311405",
                                city_name ="Quixeramobim")
            
        CityCode.objects.create(city_code ="2311504",
                                city_name ="Quixeré")
            
        CityCode.objects.create(city_code ="2311603",
                                city_name ="Redenção")
            
        CityCode.objects.create(city_code ="2311702",
                                city_name ="Reriutaba")
            
        CityCode.objects.create(city_code ="2311801",
                                city_name ="Russas")
            
        CityCode.objects.create(city_code ="2311900",
                                city_name ="Saboeiro")
            
        CityCode.objects.create(city_code ="2311959",
                                city_name ="Salitre")
            
        CityCode.objects.create(city_code ="2312205",
                                city_name ="Santa Quitéria")
            
        CityCode.objects.create(city_code ="2312007",
                                city_name ="Santana do Acaraú")
            
        CityCode.objects.create(city_code ="2312106",
                                city_name ="Santana do Cariri")
            
        CityCode.objects.create(city_code ="2312304",
                                city_name ="São Benedito")
            
        CityCode.objects.create(city_code ="2312403",
                                city_name ="São Gonçalo do Amarante")
            
        CityCode.objects.create(city_code ="2312502",
                                city_name ="São João do Jaguaribe")
            
        CityCode.objects.create(city_code ="2312601",
                                city_name ="São Luís do Curu")
            
        CityCode.objects.create(city_code ="2312700",
                                city_name ="Senador Pompeu")
            
        CityCode.objects.create(city_code ="2312809",
                                city_name ="Senador Sá")
            
        CityCode.objects.create(city_code ="2312908",
                                city_name ="Sobral")
            
        CityCode.objects.create(city_code ="2313005",
                                city_name ="Solonópole")
            
        CityCode.objects.create(city_code ="2313104",
                                city_name ="Tabuleiro do Norte")
            
        CityCode.objects.create(city_code ="2313203",
                                city_name ="Tamboril")
            
        CityCode.objects.create(city_code ="2313252",
                                city_name ="Tarrafas")
            
        CityCode.objects.create(city_code ="2313302",
                                city_name ="Tauá")
            
        CityCode.objects.create(city_code ="2313351",
                                city_name ="Tejuçuoca")
            
        CityCode.objects.create(city_code ="2313401",
                                city_name ="Tianguá")
            
        CityCode.objects.create(city_code ="2313500",
                                city_name ="Trairi")
            
        CityCode.objects.create(city_code ="2313559",
                                city_name ="Tururu")
            
        CityCode.objects.create(city_code ="2313609",
                                city_name ="Ubajara")
            
        CityCode.objects.create(city_code ="2313708",
                                city_name ="Umari")
            
        CityCode.objects.create(city_code ="2313757",
                                city_name ="Umirim")
            
        CityCode.objects.create(city_code ="2313807",
                                city_name ="Uruburetama")
            
        CityCode.objects.create(city_code ="2313906",
                                city_name ="Uruoca")
            
        CityCode.objects.create(city_code ="2313955",
                                city_name ="Varjota")
            
        CityCode.objects.create(city_code ="2314003",
                                city_name ="Várzea Alegre")
            
        CityCode.objects.create(city_code ="2314102",
                                city_name ="Viçosa do Ceará")
            
        CityCode.objects.create(city_code ="2400109",
                                city_name ="Acari")
            
        CityCode.objects.create(city_code ="2400208",
                                city_name ="Açu")
            
        CityCode.objects.create(city_code ="2400307",
                                city_name ="Afonso Bezerra")
            
        CityCode.objects.create(city_code ="2400406",
                                city_name ="Água Nova")
            
        CityCode.objects.create(city_code ="2400505",
                                city_name ="Alexandria")
            
        CityCode.objects.create(city_code ="2400604",
                                city_name ="Almino Afonso")
            
        CityCode.objects.create(city_code ="2400703",
                                city_name ="Alto do Rodrigues")
            
        CityCode.objects.create(city_code ="2400802",
                                city_name ="Angicos")
            
        CityCode.objects.create(city_code ="2400901",
                                city_name ="Antônio Martins")
            
        CityCode.objects.create(city_code ="2401008",
                                city_name ="Apodi")
            
        CityCode.objects.create(city_code ="2401107",
                                city_name ="Areia Branca")
            
        CityCode.objects.create(city_code ="2401206",
                                city_name ="Arês")
            
        CityCode.objects.create(city_code ="2401404",
                                city_name ="Baía Formosa")
            
        CityCode.objects.create(city_code ="2401453",
                                city_name ="Baraúna")
            
        CityCode.objects.create(city_code ="2401503",
                                city_name ="Barcelona")
            
        CityCode.objects.create(city_code ="2401602",
                                city_name ="Bento Fernandes")
            
        CityCode.objects.create(city_code ="2401651",
                                city_name ="Bodó")
            
        CityCode.objects.create(city_code ="2401701",
                                city_name ="Bom Jesus")
            
        CityCode.objects.create(city_code ="2401800",
                                city_name ="Brejinho")
            
        CityCode.objects.create(city_code ="2401859",
                                city_name ="Caiçara do Norte")
            
        CityCode.objects.create(city_code ="2401909",
                                city_name ="Caiçara do Rio do Vento")
            
        CityCode.objects.create(city_code ="2402006",
                                city_name ="Caicó")
            
        CityCode.objects.create(city_code ="2401305",
                                city_name ="Campo Grande")
            
        CityCode.objects.create(city_code ="2402105",
                                city_name ="Campo Redondo")
            
        CityCode.objects.create(city_code ="2402204",
                                city_name ="Canguaretama")
            
        CityCode.objects.create(city_code ="2402303",
                                city_name ="Caraúbas")
            
        CityCode.objects.create(city_code ="2402402",
                                city_name ="Carnaúba dos Dantas")
            
        CityCode.objects.create(city_code ="2402501",
                                city_name ="Carnaubais")
            
        CityCode.objects.create(city_code ="2402600",
                                city_name ="Ceará-Mirim")
            
        CityCode.objects.create(city_code ="2402709",
                                city_name ="Cerro Corá")
            
        CityCode.objects.create(city_code ="2402808",
                                city_name ="Coronel Ezequiel")
            
        CityCode.objects.create(city_code ="2402907",
                                city_name ="Coronel João Pessoa")
            
        CityCode.objects.create(city_code ="2403004",
                                city_name ="Cruzeta")
            
        CityCode.objects.create(city_code ="2403103",
                                city_name ="Currais Novos")
            
        CityCode.objects.create(city_code ="2403202",
                                city_name ="Doutor Severiano")
            
        CityCode.objects.create(city_code ="2403301",
                                city_name ="Encanto")
            
        CityCode.objects.create(city_code ="2403400",
                                city_name ="Equador")
            
        CityCode.objects.create(city_code ="2403509",
                                city_name ="Espírito Santo")
            
        CityCode.objects.create(city_code ="2403608",
                                city_name ="Extremoz")
            
        CityCode.objects.create(city_code ="2403707",
                                city_name ="Felipe Guerra")
            
        CityCode.objects.create(city_code ="2403756",
                                city_name ="Fernando Pedroza")
            
        CityCode.objects.create(city_code ="2403806",
                                city_name ="Florânia")
            
        CityCode.objects.create(city_code ="2403905",
                                city_name ="Francisco Dantas")
            
        CityCode.objects.create(city_code ="2404002",
                                city_name ="Frutuoso Gomes")
            
        CityCode.objects.create(city_code ="2404101",
                                city_name ="Galinhos")
            
        CityCode.objects.create(city_code ="2404200",
                                city_name ="Goianinha")
            
        CityCode.objects.create(city_code ="2404309",
                                city_name ="Governador Dix-Sept Rosado")
            
        CityCode.objects.create(city_code ="2404408",
                                city_name ="Grossos")
            
        CityCode.objects.create(city_code ="2404507",
                                city_name ="Guamaré")
            
        CityCode.objects.create(city_code ="2404606",
                                city_name ="Ielmo Marinho")
            
        CityCode.objects.create(city_code ="2404705",
                                city_name ="Ipanguaçu")
            
        CityCode.objects.create(city_code ="2404804",
                                city_name ="Ipueira")
            
        CityCode.objects.create(city_code ="2404853",
                                city_name ="Itajá")
            
        CityCode.objects.create(city_code ="2404903",
                                city_name ="Itaú")
            
        CityCode.objects.create(city_code ="2405009",
                                city_name ="Jaçanã")
            
        CityCode.objects.create(city_code ="2405108",
                                city_name ="Jandaíra")
            
        CityCode.objects.create(city_code ="2405207",
                                city_name ="Janduís")
            
        CityCode.objects.create(city_code ="2405306",
                                city_name ="Januário Cicco")
            
        CityCode.objects.create(city_code ="2405405",
                                city_name ="Japi")
            
        CityCode.objects.create(city_code ="2405504",
                                city_name ="Jardim de Angicos")
            
        CityCode.objects.create(city_code ="2405603",
                                city_name ="Jardim de Piranhas")
            
        CityCode.objects.create(city_code ="2405702",
                                city_name ="Jardim do Seridó")
            
        CityCode.objects.create(city_code ="2405801",
                                city_name ="João Câmara")
            
        CityCode.objects.create(city_code ="2405900",
                                city_name ="João Dias")
            
        CityCode.objects.create(city_code ="2406007",
                                city_name ="José da Penha")
            
        CityCode.objects.create(city_code ="2406106",
                                city_name ="Jucurutu")
            
        CityCode.objects.create(city_code ="2406155",
                                city_name ="Jundiá")
            
        CityCode.objects.create(city_code ="2406205",
                                city_name ="Lagoa d'Anta")
            
        CityCode.objects.create(city_code ="2406304",
                                city_name ="Lagoa de Pedras")
            
        CityCode.objects.create(city_code ="2406403",
                                city_name ="Lagoa de Velhos")
            
        CityCode.objects.create(city_code ="2406502",
                                city_name ="Lagoa Nova")
            
        CityCode.objects.create(city_code ="2406601",
                                city_name ="Lagoa Salgada")
            
        CityCode.objects.create(city_code ="2406700",
                                city_name ="Lajes")
            
        CityCode.objects.create(city_code ="2406809",
                                city_name ="Lajes Pintadas")
            
        CityCode.objects.create(city_code ="2406908",
                                city_name ="Lucrécia")
            
        CityCode.objects.create(city_code ="2407005",
                                city_name ="Luís Gomes")
            
        CityCode.objects.create(city_code ="2407104",
                                city_name ="Macaíba")
            
        CityCode.objects.create(city_code ="2407203",
                                city_name ="Macau")
            
        CityCode.objects.create(city_code ="2407252",
                                city_name ="Major Sales")
            
        CityCode.objects.create(city_code ="2407302",
                                city_name ="Marcelino Vieira")
            
        CityCode.objects.create(city_code ="2407401",
                                city_name ="Martins")
            
        CityCode.objects.create(city_code ="2407500",
                                city_name ="Maxaranguape")
            
        CityCode.objects.create(city_code ="2407609",
                                city_name ="Messias Targino")
            
        CityCode.objects.create(city_code ="2407708",
                                city_name ="Montanhas")
            
        CityCode.objects.create(city_code ="2407807",
                                city_name ="Monte Alegre")
            
        CityCode.objects.create(city_code ="2407906",
                                city_name ="Monte das Gameleiras")
            
        CityCode.objects.create(city_code ="2408003",
                                city_name ="Mossoró")
            
        CityCode.objects.create(city_code ="2408102",
                                city_name ="Natal")
            
        CityCode.objects.create(city_code ="2408201",
                                city_name ="Nísia Floresta")
            
        CityCode.objects.create(city_code ="2408300",
                                city_name ="Nova Cruz")
            
        CityCode.objects.create(city_code ="2408409",
                                city_name ="Olho d'Água do Borges")
            
        CityCode.objects.create(city_code ="2408508",
                                city_name ="Ouro Branco")
            
        CityCode.objects.create(city_code ="2408607",
                                city_name ="Paraná")
            
        CityCode.objects.create(city_code ="2408706",
                                city_name ="Paraú")
            
        CityCode.objects.create(city_code ="2408805",
                                city_name ="Parazinho")
            
        CityCode.objects.create(city_code ="2408904",
                                city_name ="Parelhas")
            
        CityCode.objects.create(city_code ="2403251",
                                city_name ="Parnamirim")
            
        CityCode.objects.create(city_code ="2409100",
                                city_name ="Passa e Fica")
            
        CityCode.objects.create(city_code ="2409209",
                                city_name ="Passagem")
            
        CityCode.objects.create(city_code ="2409308",
                                city_name ="Patu")
            
        CityCode.objects.create(city_code ="2409407",
                                city_name ="Pau dos Ferros")
            
        CityCode.objects.create(city_code ="2409506",
                                city_name ="Pedra Grande")
            
        CityCode.objects.create(city_code ="2409605",
                                city_name ="Pedra Preta")
            
        CityCode.objects.create(city_code ="2409704",
                                city_name ="Pedro Avelino")
            
        CityCode.objects.create(city_code ="2409803",
                                city_name ="Pedro Velho")
            
        CityCode.objects.create(city_code ="2409902",
                                city_name ="Pendências")
            
        CityCode.objects.create(city_code ="2410009",
                                city_name ="Pilões")
            
        CityCode.objects.create(city_code ="2410108",
                                city_name ="Poço Branco")
            
        CityCode.objects.create(city_code ="2410207",
                                city_name ="Portalegre")
            
        CityCode.objects.create(city_code ="2410256",
                                city_name ="Porto do Mangue")
            
        CityCode.objects.create(city_code ="2410405",
                                city_name ="Pureza")
            
        CityCode.objects.create(city_code ="2410504",
                                city_name ="Rafael Fernandes")
            
        CityCode.objects.create(city_code ="2410603",
                                city_name ="Rafael Godeiro")
            
        CityCode.objects.create(city_code ="2410702",
                                city_name ="Riacho da Cruz")
            
        CityCode.objects.create(city_code ="2410801",
                                city_name ="Riacho de Santana")
            
        CityCode.objects.create(city_code ="2410900",
                                city_name ="Riachuelo")
            
        CityCode.objects.create(city_code ="2408953",
                                city_name ="Rio do Fogo")
            
        CityCode.objects.create(city_code ="2411007",
                                city_name ="Rodolfo Fernandes")
            
        CityCode.objects.create(city_code ="2411106",
                                city_name ="Ruy Barbosa")
            
        CityCode.objects.create(city_code ="2411205",
                                city_name ="Santa Cruz")
            
        CityCode.objects.create(city_code ="2409332",
                                city_name ="Santa Maria")
            
        CityCode.objects.create(city_code ="2411403",
                                city_name ="Santana do Matos")
            
        CityCode.objects.create(city_code ="2411429",
                                city_name ="Santana do Seridó")
            
        CityCode.objects.create(city_code ="2411502",
                                city_name ="Santo Antônio")
            
        CityCode.objects.create(city_code ="2411601",
                                city_name ="São Bento do Norte")
            
        CityCode.objects.create(city_code ="2411700",
                                city_name ="São Bento do Trairí")
            
        CityCode.objects.create(city_code ="2411809",
                                city_name ="São Fernando")
            
        CityCode.objects.create(city_code ="2411908",
                                city_name ="São Francisco do Oeste")
            
        CityCode.objects.create(city_code ="2412005",
                                city_name ="São Gonçalo do Amarante")
            
        CityCode.objects.create(city_code ="2412104",
                                city_name ="São João do Sabugi")
            
        CityCode.objects.create(city_code ="2412203",
                                city_name ="São José de Mipibu")
            
        CityCode.objects.create(city_code ="2412302",
                                city_name ="São José do Campestre")
            
        CityCode.objects.create(city_code ="2412401",
                                city_name ="São José do Seridó")
            
        CityCode.objects.create(city_code ="2412500",
                                city_name ="São Miguel")
            
        CityCode.objects.create(city_code ="2412559",
                                city_name ="São Miguel do Gostoso")
            
        CityCode.objects.create(city_code ="2412609",
                                city_name ="São Paulo do Potengi")
            
        CityCode.objects.create(city_code ="2412708",
                                city_name ="São Pedro")
            
        CityCode.objects.create(city_code ="2412807",
                                city_name ="São Rafael")
            
        CityCode.objects.create(city_code ="2412906",
                                city_name ="São Tomé")
            
        CityCode.objects.create(city_code ="2413003",
                                city_name ="São Vicente")
            
        CityCode.objects.create(city_code ="2413102",
                                city_name ="Senador Elói de Souza")
            
        CityCode.objects.create(city_code ="2413201",
                                city_name ="Senador Georgino Avelino")
            
        CityCode.objects.create(city_code ="2410306",
                                city_name ="Serra Caiada")
            
        CityCode.objects.create(city_code ="2413300",
                                city_name ="Serra de São Bento")
            
        CityCode.objects.create(city_code ="2413359",
                                city_name ="Serra do Mel")
            
        CityCode.objects.create(city_code ="2413409",
                                city_name ="Serra Negra do Norte")
            
        CityCode.objects.create(city_code ="2413508",
                                city_name ="Serrinha")
            
        CityCode.objects.create(city_code ="2413557",
                                city_name ="Serrinha dos Pintos")
            
        CityCode.objects.create(city_code ="2413607",
                                city_name ="Severiano Melo")
            
        CityCode.objects.create(city_code ="2413706",
                                city_name ="Sítio Novo")
            
        CityCode.objects.create(city_code ="2413805",
                                city_name ="Taboleiro Grande")
            
        CityCode.objects.create(city_code ="2413904",
                                city_name ="Taipu")
            
        CityCode.objects.create(city_code ="2414001",
                                city_name ="Tangará")
            
        CityCode.objects.create(city_code ="2414100",
                                city_name ="Tenente Ananias")
            
        CityCode.objects.create(city_code ="2414159",
                                city_name ="Tenente Laurentino Cruz")
            
        CityCode.objects.create(city_code ="2411056",
                                city_name ="Tibau")
            
        CityCode.objects.create(city_code ="2414209",
                                city_name ="Tibau do Sul")
            
        CityCode.objects.create(city_code ="2414308",
                                city_name ="Timbaúba dos Batistas")
            
        CityCode.objects.create(city_code ="2414407",
                                city_name ="Touros")
            
        CityCode.objects.create(city_code ="2414456",
                                city_name ="Triunfo Potiguar")
            
        CityCode.objects.create(city_code ="2414506",
                                city_name ="Umarizal")
            
        CityCode.objects.create(city_code ="2414605",
                                city_name ="Upanema")
            
        CityCode.objects.create(city_code ="2414704",
                                city_name ="Várzea")
            
        CityCode.objects.create(city_code ="2414753",
                                city_name ="Venha-Ver")
            
        CityCode.objects.create(city_code ="2414803",
                                city_name ="Vera Cruz")
            
        CityCode.objects.create(city_code ="2414902",
                                city_name ="Viçosa")
            
        CityCode.objects.create(city_code ="2415008",
                                city_name ="Vila Flor")
            
        CityCode.objects.create(city_code ="2500106",
                                city_name ="Água Branca")
            
        CityCode.objects.create(city_code ="2500205",
                                city_name ="Aguiar")
            
        CityCode.objects.create(city_code ="2500304",
                                city_name ="Alagoa Grande")
            
        CityCode.objects.create(city_code ="2500403",
                                city_name ="Alagoa Nova")
            
        CityCode.objects.create(city_code ="2500502",
                                city_name ="Alagoinha")
            
        CityCode.objects.create(city_code ="2500536",
                                city_name ="Alcantil")
            
        CityCode.objects.create(city_code ="2500577",
                                city_name ="Algodão de Jandaíra")
            
        CityCode.objects.create(city_code ="2500601",
                                city_name ="Alhandra")
            
        CityCode.objects.create(city_code ="2500734",
                                city_name ="Amparo")
            
        CityCode.objects.create(city_code ="2500775",
                                city_name ="Aparecida")
            
        CityCode.objects.create(city_code ="2500809",
                                city_name ="Araçagi")
            
        CityCode.objects.create(city_code ="2500908",
                                city_name ="Arara")
            
        CityCode.objects.create(city_code ="2501005",
                                city_name ="Araruna")
            
        CityCode.objects.create(city_code ="2501104",
                                city_name ="Areia")
            
        CityCode.objects.create(city_code ="2501153",
                                city_name ="Areia de Baraúnas")
            
        CityCode.objects.create(city_code ="2501203",
                                city_name ="Areial")
            
        CityCode.objects.create(city_code ="2501302",
                                city_name ="Aroeiras")
            
        CityCode.objects.create(city_code ="2501351",
                                city_name ="Assunção")
            
        CityCode.objects.create(city_code ="2501401",
                                city_name ="Baía da Traição")
            
        CityCode.objects.create(city_code ="2501500",
                                city_name ="Bananeiras")
            
        CityCode.objects.create(city_code ="2501534",
                                city_name ="Baraúna")
            
        CityCode.objects.create(city_code ="2501609",
                                city_name ="Barra de Santa Rosa")
            
        CityCode.objects.create(city_code ="2501575",
                                city_name ="Barra de Santana")
            
        CityCode.objects.create(city_code ="2501708",
                                city_name ="Barra de São Miguel")
            
        CityCode.objects.create(city_code ="2501807",
                                city_name ="Bayeux")
            
        CityCode.objects.create(city_code ="2501906",
                                city_name ="Belém")
            
        CityCode.objects.create(city_code ="2502003",
                                city_name ="Belém do Brejo do Cruz")
            
        CityCode.objects.create(city_code ="2502052",
                                city_name ="Bernardino Batista")
            
        CityCode.objects.create(city_code ="2502102",
                                city_name ="Boa Ventura")
            
        CityCode.objects.create(city_code ="2502151",
                                city_name ="Boa Vista")
            
        CityCode.objects.create(city_code ="2502201",
                                city_name ="Bom Jesus")
            
        CityCode.objects.create(city_code ="2502300",
                                city_name ="Bom Sucesso")
            
        CityCode.objects.create(city_code ="2502409",
                                city_name ="Bonito de Santa Fé")
            
        CityCode.objects.create(city_code ="2502508",
                                city_name ="Boqueirão")
            
        CityCode.objects.create(city_code ="2502706",
                                city_name ="Borborema")
            
        CityCode.objects.create(city_code ="2502805",
                                city_name ="Brejo do Cruz")
            
        CityCode.objects.create(city_code ="2502904",
                                city_name ="Brejo dos Santos")
            
        CityCode.objects.create(city_code ="2503001",
                                city_name ="Caaporã")
            
        CityCode.objects.create(city_code ="2503100",
                                city_name ="Cabaceiras")
            
        CityCode.objects.create(city_code ="2503209",
                                city_name ="Cabedelo")
            
        CityCode.objects.create(city_code ="2503308",
                                city_name ="Cachoeira dos Índios")
            
        CityCode.objects.create(city_code ="2503407",
                                city_name ="Cacimba de Areia")
            
        CityCode.objects.create(city_code ="2503506",
                                city_name ="Cacimba de Dentro")
            
        CityCode.objects.create(city_code ="2503555",
                                city_name ="Cacimbas")
            
        CityCode.objects.create(city_code ="2503605",
                                city_name ="Caiçara")
            
        CityCode.objects.create(city_code ="2503704",
                                city_name ="Cajazeiras")
            
        CityCode.objects.create(city_code ="2503753",
                                city_name ="Cajazeirinhas")
            
        CityCode.objects.create(city_code ="2503803",
                                city_name ="Caldas Brandão")
            
        CityCode.objects.create(city_code ="2503902",
                                city_name ="Camalaú")
            
        CityCode.objects.create(city_code ="2504009",
                                city_name ="Campina Grande")
            
        CityCode.objects.create(city_code ="2504033",
                                city_name ="Capim")
            
        CityCode.objects.create(city_code ="2504074",
                                city_name ="Caraúbas")
            
        CityCode.objects.create(city_code ="2504108",
                                city_name ="Carrapateira")
            
        CityCode.objects.create(city_code ="2504157",
                                city_name ="Casserengue")
            
        CityCode.objects.create(city_code ="2504207",
                                city_name ="Catingueira")
            
        CityCode.objects.create(city_code ="2504306",
                                city_name ="Catolé do Rocha")
            
        CityCode.objects.create(city_code ="2504355",
                                city_name ="Caturité")
            
        CityCode.objects.create(city_code ="2504405",
                                city_name ="Conceição")
            
        CityCode.objects.create(city_code ="2504504",
                                city_name ="Condado")
            
        CityCode.objects.create(city_code ="2504603",
                                city_name ="Conde")
            
        CityCode.objects.create(city_code ="2504702",
                                city_name ="Congo")
            
        CityCode.objects.create(city_code ="2504801",
                                city_name ="Coremas")
            
        CityCode.objects.create(city_code ="2504850",
                                city_name ="Coxixola")
            
        CityCode.objects.create(city_code ="2504900",
                                city_name ="Cruz do Espírito Santo")
            
        CityCode.objects.create(city_code ="2505006",
                                city_name ="Cubati")
            
        CityCode.objects.create(city_code ="2505105",
                                city_name ="Cuité")
            
        CityCode.objects.create(city_code ="2505238",
                                city_name ="Cuité de Mamanguape")
            
        CityCode.objects.create(city_code ="2505204",
                                city_name ="Cuitegi")
            
        CityCode.objects.create(city_code ="2505279",
                                city_name ="Curral de Cima")
            
        CityCode.objects.create(city_code ="2505303",
                                city_name ="Curral Velho")
            
        CityCode.objects.create(city_code ="2505352",
                                city_name ="Damião")
            
        CityCode.objects.create(city_code ="2505402",
                                city_name ="Desterro")
            
        CityCode.objects.create(city_code ="2505600",
                                city_name ="Diamante")
            
        CityCode.objects.create(city_code ="2505709",
                                city_name ="Dona Inês")
            
        CityCode.objects.create(city_code ="2505808",
                                city_name ="Duas Estradas")
            
        CityCode.objects.create(city_code ="2505907",
                                city_name ="Emas")
            
        CityCode.objects.create(city_code ="2506004",
                                city_name ="Esperança")
            
        CityCode.objects.create(city_code ="2506103",
                                city_name ="Fagundes")
            
        CityCode.objects.create(city_code ="2506202",
                                city_name ="Frei Martinho")
            
        CityCode.objects.create(city_code ="2506251",
                                city_name ="Gado Bravo")
            
        CityCode.objects.create(city_code ="2506301",
                                city_name ="Guarabira")
            
        CityCode.objects.create(city_code ="2506400",
                                city_name ="Gurinhém")
            
        CityCode.objects.create(city_code ="2506509",
                                city_name ="Gurjão")
            
        CityCode.objects.create(city_code ="2506608",
                                city_name ="Ibiara")
            
        CityCode.objects.create(city_code ="2502607",
                                city_name ="Igaracy")
            
        CityCode.objects.create(city_code ="2506707",
                                city_name ="Imaculada")
            
        CityCode.objects.create(city_code ="2506806",
                                city_name ="Ingá")
            
        CityCode.objects.create(city_code ="2506905",
                                city_name ="Itabaiana")
            
        CityCode.objects.create(city_code ="2507002",
                                city_name ="Itaporanga")
            
        CityCode.objects.create(city_code ="2507101",
                                city_name ="Itapororoca")
            
        CityCode.objects.create(city_code ="2507200",
                                city_name ="Itatuba")
            
        CityCode.objects.create(city_code ="2507309",
                                city_name ="Jacaraú")
            
        CityCode.objects.create(city_code ="2507408",
                                city_name ="Jericó")
            
        CityCode.objects.create(city_code ="2507507",
                                city_name ="João Pessoa")
            
        CityCode.objects.create(city_code ="2513653",
                                city_name ="Joca Claudino")
            
        CityCode.objects.create(city_code ="2507606",
                                city_name ="Juarez Távora")
            
        CityCode.objects.create(city_code ="2507705",
                                city_name ="Juazeirinho")
            
        CityCode.objects.create(city_code ="2507804",
                                city_name ="Junco do Seridó")
            
        CityCode.objects.create(city_code ="2507903",
                                city_name ="Juripiranga")
            
        CityCode.objects.create(city_code ="2508000",
                                city_name ="Juru")
            
        CityCode.objects.create(city_code ="2508109",
                                city_name ="Lagoa")
            
        CityCode.objects.create(city_code ="2508208",
                                city_name ="Lagoa de Dentro")
            
        CityCode.objects.create(city_code ="2508307",
                                city_name ="Lagoa Seca")
            
        CityCode.objects.create(city_code ="2508406",
                                city_name ="Lastro")
            
        CityCode.objects.create(city_code ="2508505",
                                city_name ="Livramento")
            
        CityCode.objects.create(city_code ="2508554",
                                city_name ="Logradouro")
            
        CityCode.objects.create(city_code ="2508604",
                                city_name ="Lucena")
            
        CityCode.objects.create(city_code ="2508703",
                                city_name ="Mãe d'Água")
            
        CityCode.objects.create(city_code ="2508802",
                                city_name ="Malta")
            
        CityCode.objects.create(city_code ="2508901",
                                city_name ="Mamanguape")
            
        CityCode.objects.create(city_code ="2509008",
                                city_name ="Manaíra")
            
        CityCode.objects.create(city_code ="2509057",
                                city_name ="Marcação")
            
        CityCode.objects.create(city_code ="2509107",
                                city_name ="Mari")
            
        CityCode.objects.create(city_code ="2509156",
                                city_name ="Marizópolis")
            
        CityCode.objects.create(city_code ="2509206",
                                city_name ="Massaranduba")
            
        CityCode.objects.create(city_code ="2509305",
                                city_name ="Mataraca")
            
        CityCode.objects.create(city_code ="2509339",
                                city_name ="Matinhas")
            
        CityCode.objects.create(city_code ="2509370",
                                city_name ="Mato Grosso")
            
        CityCode.objects.create(city_code ="2509396",
                                city_name ="Maturéia")
            
        CityCode.objects.create(city_code ="2509404",
                                city_name ="Mogeiro")
            
        CityCode.objects.create(city_code ="2509503",
                                city_name ="Montadas")
            
        CityCode.objects.create(city_code ="2509602",
                                city_name ="Monte Horebe")
            
        CityCode.objects.create(city_code ="2509701",
                                city_name ="Monteiro")
            
        CityCode.objects.create(city_code ="2509800",
                                city_name ="Mulungu")
            
        CityCode.objects.create(city_code ="2509909",
                                city_name ="Natuba")
            
        CityCode.objects.create(city_code ="2510006",
                                city_name ="Nazarezinho")
            
        CityCode.objects.create(city_code ="2510105",
                                city_name ="Nova Floresta")
            
        CityCode.objects.create(city_code ="2510204",
                                city_name ="Nova Olinda")
            
        CityCode.objects.create(city_code ="2510303",
                                city_name ="Nova Palmeira")
            
        CityCode.objects.create(city_code ="2510402",
                                city_name ="Olho d'Água")
            
        CityCode.objects.create(city_code ="2510501",
                                city_name ="Olivedos")
            
        CityCode.objects.create(city_code ="2510600",
                                city_name ="Ouro Velho")
            
        CityCode.objects.create(city_code ="2510659",
                                city_name ="Parari")
            
        CityCode.objects.create(city_code ="2510709",
                                city_name ="Passagem")
            
        CityCode.objects.create(city_code ="2510808",
                                city_name ="Patos")
            
        CityCode.objects.create(city_code ="2510907",
                                city_name ="Paulista")
            
        CityCode.objects.create(city_code ="2511004",
                                city_name ="Pedra Branca")
            
        CityCode.objects.create(city_code ="2511103",
                                city_name ="Pedra Lavrada")
            
        CityCode.objects.create(city_code ="2511202",
                                city_name ="Pedras de Fogo")
            
        CityCode.objects.create(city_code ="2512721",
                                city_name ="Pedro Régis")
            
        CityCode.objects.create(city_code ="2511301",
                                city_name ="Piancó")
            
        CityCode.objects.create(city_code ="2511400",
                                city_name ="Picuí")
            
        CityCode.objects.create(city_code ="2511509",
                                city_name ="Pilar")
            
        CityCode.objects.create(city_code ="2511608",
                                city_name ="Pilões")
            
        CityCode.objects.create(city_code ="2511707",
                                city_name ="Pilõezinhos")
            
        CityCode.objects.create(city_code ="2511806",
                                city_name ="Pirpirituba")
            
        CityCode.objects.create(city_code ="2511905",
                                city_name ="Pitimbu")
            
        CityCode.objects.create(city_code ="2512002",
                                city_name ="Pocinhos")
            
        CityCode.objects.create(city_code ="2512036",
                                city_name ="Poço Dantas")
            
        CityCode.objects.create(city_code ="2512077",
                                city_name ="Poço de José de Moura")
            
        CityCode.objects.create(city_code ="2512101",
                                city_name ="Pombal")
            
        CityCode.objects.create(city_code ="2512200",
                                city_name ="Prata")
            
        CityCode.objects.create(city_code ="2512309",
                                city_name ="Princesa Isabel")
            
        CityCode.objects.create(city_code ="2512408",
                                city_name ="Puxinanã")
            
        CityCode.objects.create(city_code ="2512507",
                                city_name ="Queimadas")
            
        CityCode.objects.create(city_code ="2512606",
                                city_name ="Quixaba")
            
        CityCode.objects.create(city_code ="2512705",
                                city_name ="Remígio")
            
        CityCode.objects.create(city_code ="2512747",
                                city_name ="Riachão")
            
        CityCode.objects.create(city_code ="2512754",
                                city_name ="Riachão do Bacamarte")
            
        CityCode.objects.create(city_code ="2512762",
                                city_name ="Riachão do Poço")
            
        CityCode.objects.create(city_code ="2512788",
                                city_name ="Riacho de Santo Antônio")
            
        CityCode.objects.create(city_code ="2512804",
                                city_name ="Riacho dos Cavalos")
            
        CityCode.objects.create(city_code ="2512903",
                                city_name ="Rio Tinto")
            
        CityCode.objects.create(city_code ="2513000",
                                city_name ="Salgadinho")
            
        CityCode.objects.create(city_code ="2513109",
                                city_name ="Salgado de São Félix")
            
        CityCode.objects.create(city_code ="2513158",
                                city_name ="Santa Cecília")
            
        CityCode.objects.create(city_code ="2513208",
                                city_name ="Santa Cruz")
            
        CityCode.objects.create(city_code ="2513307",
                                city_name ="Santa Helena")
            
        CityCode.objects.create(city_code ="2513356",
                                city_name ="Santa Inês")
            
        CityCode.objects.create(city_code ="2513406",
                                city_name ="Santa Luzia")
            
        CityCode.objects.create(city_code ="2513703",
                                city_name ="Santa Rita")
            
        CityCode.objects.create(city_code ="2513802",
                                city_name ="Santa Teresinha")
            
        CityCode.objects.create(city_code ="2513505",
                                city_name ="Santana de Mangueira")
            
        CityCode.objects.create(city_code ="2513604",
                                city_name ="Santana dos Garrotes")
            
        CityCode.objects.create(city_code ="2513851",
                                city_name ="Santo André")
            
        CityCode.objects.create(city_code ="2513927",
                                city_name ="São Bentinho")
            
        CityCode.objects.create(city_code ="2513901",
                                city_name ="São Bento")
            
        CityCode.objects.create(city_code ="2513968",
                                city_name ="São Domingos")
            
        CityCode.objects.create(city_code ="2513943",
                                city_name ="São Domingos do Cariri")
            
        CityCode.objects.create(city_code ="2513984",
                                city_name ="São Francisco")
            
        CityCode.objects.create(city_code ="2514008",
                                city_name ="São João do Cariri")
            
        CityCode.objects.create(city_code ="2500700",
                                city_name ="São João do Rio do Peixe")
            
        CityCode.objects.create(city_code ="2514107",
                                city_name ="São João do Tigre")
            
        CityCode.objects.create(city_code ="2514206",
                                city_name ="São José da Lagoa Tapada")
            
        CityCode.objects.create(city_code ="2514305",
                                city_name ="São José de Caiana")
            
        CityCode.objects.create(city_code ="2514404",
                                city_name ="São José de Espinharas")
            
        CityCode.objects.create(city_code ="2514503",
                                city_name ="São José de Piranhas")
            
        CityCode.objects.create(city_code ="2514552",
                                city_name ="São José de Princesa")
            
        CityCode.objects.create(city_code ="2514602",
                                city_name ="São José do Bonfim")
            
        CityCode.objects.create(city_code ="2514651",
                                city_name ="São José do Brejo do Cruz")
            
        CityCode.objects.create(city_code ="2514701",
                                city_name ="São José do Sabugi")
            
        CityCode.objects.create(city_code ="2514800",
                                city_name ="São José dos Cordeiros")
            
        CityCode.objects.create(city_code ="2514453",
                                city_name ="São José dos Ramos")
            
        CityCode.objects.create(city_code ="2514909",
                                city_name ="São Mamede")
            
        CityCode.objects.create(city_code ="2515005",
                                city_name ="São Miguel de Taipu")
            
        CityCode.objects.create(city_code ="2515104",
                                city_name ="São Sebastião de Lagoa de Roça")
            
        CityCode.objects.create(city_code ="2515203",
                                city_name ="São Sebastião do Umbuzeiro")
            
        CityCode.objects.create(city_code ="2515401",
                                city_name ="São Vicente do Seridó")
            
        CityCode.objects.create(city_code ="2515302",
                                city_name ="Sapé")
            
        CityCode.objects.create(city_code ="2515500",
                                city_name ="Serra Branca")
            
        CityCode.objects.create(city_code ="2515609",
                                city_name ="Serra da Raiz")
            
        CityCode.objects.create(city_code ="2515708",
                                city_name ="Serra Grande")
            
        CityCode.objects.create(city_code ="2515807",
                                city_name ="Serra Redonda")
            
        CityCode.objects.create(city_code ="2515906",
                                city_name ="Serraria")
            
        CityCode.objects.create(city_code ="2515930",
                                city_name ="Sertãozinho")
            
        CityCode.objects.create(city_code ="2515971",
                                city_name ="Sobrado")
            
        CityCode.objects.create(city_code ="2516003",
                                city_name ="Solânea")
            
        CityCode.objects.create(city_code ="2516102",
                                city_name ="Soledade")
            
        CityCode.objects.create(city_code ="2516151",
                                city_name ="Sossêgo")
            
        CityCode.objects.create(city_code ="2516201",
                                city_name ="Sousa")
            
        CityCode.objects.create(city_code ="2516300",
                                city_name ="Sumé")
            
        CityCode.objects.create(city_code ="2516409",
                                city_name ="Tacima")
            
        CityCode.objects.create(city_code ="2516508",
                                city_name ="Taperoá")
            
        CityCode.objects.create(city_code ="2516607",
                                city_name ="Tavares")
            
        CityCode.objects.create(city_code ="2516706",
                                city_name ="Teixeira")
            
        CityCode.objects.create(city_code ="2516755",
                                city_name ="Tenório")
            
        CityCode.objects.create(city_code ="2516805",
                                city_name ="Triunfo")
            
        CityCode.objects.create(city_code ="2516904",
                                city_name ="Uiraúna")
            
        CityCode.objects.create(city_code ="2517001",
                                city_name ="Umbuzeiro")
            
        CityCode.objects.create(city_code ="2517100",
                                city_name ="Várzea")
            
        CityCode.objects.create(city_code ="2517209",
                                city_name ="Vieirópolis")
            
        CityCode.objects.create(city_code ="2505501",
                                city_name ="Vista Serrana")
            
        CityCode.objects.create(city_code ="2517407",
                                city_name ="Zabelê")
            
        CityCode.objects.create(city_code ="2600054",
                                city_name ="Abreu e Lima")
            
        CityCode.objects.create(city_code ="2600104",
                                city_name ="Afogados da Ingazeira")
            
        CityCode.objects.create(city_code ="2600203",
                                city_name ="Afrânio")
            
        CityCode.objects.create(city_code ="2600302",
                                city_name ="Agrestina")
            
        CityCode.objects.create(city_code ="2600401",
                                city_name ="Água Preta")
            
        CityCode.objects.create(city_code ="2600500",
                                city_name ="Águas Belas")
            
        CityCode.objects.create(city_code ="2600609",
                                city_name ="Alagoinha")
            
        CityCode.objects.create(city_code ="2600708",
                                city_name ="Aliança")
            
        CityCode.objects.create(city_code ="2600807",
                                city_name ="Altinho")
            
        CityCode.objects.create(city_code ="2600906",
                                city_name ="Amaraji")
            
        CityCode.objects.create(city_code ="2601003",
                                city_name ="Angelim")
            
        CityCode.objects.create(city_code ="2601052",
                                city_name ="Araçoiaba")
            
        CityCode.objects.create(city_code ="2601102",
                                city_name ="Araripina")
            
        CityCode.objects.create(city_code ="2601201",
                                city_name ="Arcoverde")
            
        CityCode.objects.create(city_code ="2601300",
                                city_name ="Barra de Guabiraba")
            
        CityCode.objects.create(city_code ="2601409",
                                city_name ="Barreiros")
            
        CityCode.objects.create(city_code ="2601508",
                                city_name ="Belém de Maria")
            
        CityCode.objects.create(city_code ="2601607",
                                city_name ="Belém do São Francisco")
            
        CityCode.objects.create(city_code ="2601706",
                                city_name ="Belo Jardim")
            
        CityCode.objects.create(city_code ="2601805",
                                city_name ="Betânia")
            
        CityCode.objects.create(city_code ="2601904",
                                city_name ="Bezerros")
            
        CityCode.objects.create(city_code ="2602001",
                                city_name ="Bodocó")
            
        CityCode.objects.create(city_code ="2602100",
                                city_name ="Bom Conselho")
            
        CityCode.objects.create(city_code ="2602209",
                                city_name ="Bom Jardim")
            
        CityCode.objects.create(city_code ="2602308",
                                city_name ="Bonito")
            
        CityCode.objects.create(city_code ="2602407",
                                city_name ="Brejão")
            
        CityCode.objects.create(city_code ="2602506",
                                city_name ="Brejinho")
            
        CityCode.objects.create(city_code ="2602605",
                                city_name ="Brejo da Madre de Deus")
            
        CityCode.objects.create(city_code ="2602704",
                                city_name ="Buenos Aires")
            
        CityCode.objects.create(city_code ="2602803",
                                city_name ="Buíque")
            
        CityCode.objects.create(city_code ="2602902",
                                city_name ="Cabo de Santo Agostinho")
            
        CityCode.objects.create(city_code ="2603009",
                                city_name ="Cabrobó")
            
        CityCode.objects.create(city_code ="2603108",
                                city_name ="Cachoeirinha")
            
        CityCode.objects.create(city_code ="2603207",
                                city_name ="Caetés")
            
        CityCode.objects.create(city_code ="2603306",
                                city_name ="Calçado")
            
        CityCode.objects.create(city_code ="2603405",
                                city_name ="Calumbi")
            
        CityCode.objects.create(city_code ="2603454",
                                city_name ="Camaragibe")
            
        CityCode.objects.create(city_code ="2603504",
                                city_name ="Camocim de São Félix")
            
        CityCode.objects.create(city_code ="2603603",
                                city_name ="Camutanga")
            
        CityCode.objects.create(city_code ="2603702",
                                city_name ="Canhotinho")
            
        CityCode.objects.create(city_code ="2603801",
                                city_name ="Capoeiras")
            
        CityCode.objects.create(city_code ="2603900",
                                city_name ="Carnaíba")
            
        CityCode.objects.create(city_code ="2603926",
                                city_name ="Carnaubeira da Penha")
            
        CityCode.objects.create(city_code ="2604007",
                                city_name ="Carpina")
            
        CityCode.objects.create(city_code ="2604106",
                                city_name ="Caruaru")
            
        CityCode.objects.create(city_code ="2604155",
                                city_name ="Casinhas")
            
        CityCode.objects.create(city_code ="2604205",
                                city_name ="Catende")
            
        CityCode.objects.create(city_code ="2604304",
                                city_name ="Cedro")
            
        CityCode.objects.create(city_code ="2604403",
                                city_name ="Chã de Alegria")
            
        CityCode.objects.create(city_code ="2604502",
                                city_name ="Chã Grande")
            
        CityCode.objects.create(city_code ="2604601",
                                city_name ="Condado")
            
        CityCode.objects.create(city_code ="2604700",
                                city_name ="Correntes")
            
        CityCode.objects.create(city_code ="2604809",
                                city_name ="Cortês")
            
        CityCode.objects.create(city_code ="2604908",
                                city_name ="Cumaru")
            
        CityCode.objects.create(city_code ="2605004",
                                city_name ="Cupira")
            
        CityCode.objects.create(city_code ="2605103",
                                city_name ="Custódia")
            
        CityCode.objects.create(city_code ="2605152",
                                city_name ="Dormentes")
            
        CityCode.objects.create(city_code ="2605202",
                                city_name ="Escada")
            
        CityCode.objects.create(city_code ="2605301",
                                city_name ="Exu")
            
        CityCode.objects.create(city_code ="2605400",
                                city_name ="Feira Nova")
            
        CityCode.objects.create(city_code ="2605459",
                                city_name ="Fernando de Noronha")
            
        CityCode.objects.create(city_code ="2605509",
                                city_name ="Ferreiros")
            
        CityCode.objects.create(city_code ="2605608",
                                city_name ="Flores")
            
        CityCode.objects.create(city_code ="2605707",
                                city_name ="Floresta")
            
        CityCode.objects.create(city_code ="2605806",
                                city_name ="Frei Miguelinho")
            
        CityCode.objects.create(city_code ="2605905",
                                city_name ="Gameleira")
            
        CityCode.objects.create(city_code ="2606002",
                                city_name ="Garanhuns")
            
        CityCode.objects.create(city_code ="2606101",
                                city_name ="Glória do Goitá")
            
        CityCode.objects.create(city_code ="2606200",
                                city_name ="Goiana")
            
        CityCode.objects.create(city_code ="2606309",
                                city_name ="Granito")
            
        CityCode.objects.create(city_code ="2606408",
                                city_name ="Gravatá")
            
        CityCode.objects.create(city_code ="2606507",
                                city_name ="Iati")
            
        CityCode.objects.create(city_code ="2606606",
                                city_name ="Ibimirim")
            
        CityCode.objects.create(city_code ="2606705",
                                city_name ="Ibirajuba")
            
        CityCode.objects.create(city_code ="2606804",
                                city_name ="Igarassu")
            
        CityCode.objects.create(city_code ="2606903",
                                city_name ="Iguaracy")
            
        CityCode.objects.create(city_code ="2607604",
                                city_name ="Ilha de Itamaracá")
            
        CityCode.objects.create(city_code ="2607000",
                                city_name ="Inajá")
            
        CityCode.objects.create(city_code ="2607109",
                                city_name ="Ingazeira")
            
        CityCode.objects.create(city_code ="2607208",
                                city_name ="Ipojuca")
            
        CityCode.objects.create(city_code ="2607307",
                                city_name ="Ipubi")
            
        CityCode.objects.create(city_code ="2607406",
                                city_name ="Itacuruba")
            
        CityCode.objects.create(city_code ="2607505",
                                city_name ="Itaíba")
            
        CityCode.objects.create(city_code ="2607653",
                                city_name ="Itambé")
            
        CityCode.objects.create(city_code ="2607703",
                                city_name ="Itapetim")
            
        CityCode.objects.create(city_code ="2607752",
                                city_name ="Itapissuma")
            
        CityCode.objects.create(city_code ="2607802",
                                city_name ="Itaquitinga")
            
        CityCode.objects.create(city_code ="2607901",
                                city_name ="Jaboatão dos Guararapes")
            
        CityCode.objects.create(city_code ="2607950",
                                city_name ="Jaqueira")
            
        CityCode.objects.create(city_code ="2608008",
                                city_name ="Jataúba")
            
        CityCode.objects.create(city_code ="2608057",
                                city_name ="Jatobá")
            
        CityCode.objects.create(city_code ="2608107",
                                city_name ="João Alfredo")
            
        CityCode.objects.create(city_code ="2608206",
                                city_name ="Joaquim Nabuco")
            
        CityCode.objects.create(city_code ="2608255",
                                city_name ="Jucati")
            
        CityCode.objects.create(city_code ="2608305",
                                city_name ="Jupi")
            
        CityCode.objects.create(city_code ="2608404",
                                city_name ="Jurema")
            
        CityCode.objects.create(city_code ="2608503",
                                city_name ="Lagoa de Itaenga")
            
        CityCode.objects.create(city_code ="2608453",
                                city_name ="Lagoa do Carro")
            
        CityCode.objects.create(city_code ="2608602",
                                city_name ="Lagoa do Ouro")
            
        CityCode.objects.create(city_code ="2608701",
                                city_name ="Lagoa dos Gatos")
            
        CityCode.objects.create(city_code ="2608750",
                                city_name ="Lagoa Grande")
            
        CityCode.objects.create(city_code ="2608800",
                                city_name ="Lajedo")
            
        CityCode.objects.create(city_code ="2608909",
                                city_name ="Limoeiro")
            
        CityCode.objects.create(city_code ="2609006",
                                city_name ="Macaparana")
            
        CityCode.objects.create(city_code ="2609105",
                                city_name ="Machados")
            
        CityCode.objects.create(city_code ="2609154",
                                city_name ="Manari")
            
        CityCode.objects.create(city_code ="2609204",
                                city_name ="Maraial")
            
        CityCode.objects.create(city_code ="2609303",
                                city_name ="Mirandiba")
            
        CityCode.objects.create(city_code ="2614303",
                                city_name ="Moreilândia")
            
        CityCode.objects.create(city_code ="2609402",
                                city_name ="Moreno")
            
        CityCode.objects.create(city_code ="2609501",
                                city_name ="Nazaré da Mata")
            
        CityCode.objects.create(city_code ="2609600",
                                city_name ="Olinda")
            
        CityCode.objects.create(city_code ="2609709",
                                city_name ="Orobó")
            
        CityCode.objects.create(city_code ="2609808",
                                city_name ="Orocó")
            
        CityCode.objects.create(city_code ="2609907",
                                city_name ="Ouricuri")
            
        CityCode.objects.create(city_code ="2610004",
                                city_name ="Palmares")
            
        CityCode.objects.create(city_code ="2610103",
                                city_name ="Palmeirina")
            
        CityCode.objects.create(city_code ="2610202",
                                city_name ="Panelas")
            
        CityCode.objects.create(city_code ="2610301",
                                city_name ="Paranatama")
            
        CityCode.objects.create(city_code ="2610400",
                                city_name ="Parnamirim")
            
        CityCode.objects.create(city_code ="2610509",
                                city_name ="Passira")
            
        CityCode.objects.create(city_code ="2610608",
                                city_name ="Paudalho")
            
        CityCode.objects.create(city_code ="2610707",
                                city_name ="Paulista")
            
        CityCode.objects.create(city_code ="2610806",
                                city_name ="Pedra")
            
        CityCode.objects.create(city_code ="2610905",
                                city_name ="Pesqueira")
            
        CityCode.objects.create(city_code ="2611002",
                                city_name ="Petrolândia")
            
        CityCode.objects.create(city_code ="2611101",
                                city_name ="Petrolina")
            
        CityCode.objects.create(city_code ="2611200",
                                city_name ="Poção")
            
        CityCode.objects.create(city_code ="2611309",
                                city_name ="Pombos")
            
        CityCode.objects.create(city_code ="2611408",
                                city_name ="Primavera")
            
        CityCode.objects.create(city_code ="2611507",
                                city_name ="Quipapá")
            
        CityCode.objects.create(city_code ="2611533",
                                city_name ="Quixaba")
            
        CityCode.objects.create(city_code ="2611606",
                                city_name ="Recife")
            
        CityCode.objects.create(city_code ="2611705",
                                city_name ="Riacho das Almas")
            
        CityCode.objects.create(city_code ="2611804",
                                city_name ="Ribeirão")
            
        CityCode.objects.create(city_code ="2611903",
                                city_name ="Rio Formoso")
            
        CityCode.objects.create(city_code ="2612000",
                                city_name ="Sairé")
            
        CityCode.objects.create(city_code ="2612109",
                                city_name ="Salgadinho")
            
        CityCode.objects.create(city_code ="2612208",
                                city_name ="Salgueiro")
            
        CityCode.objects.create(city_code ="2612307",
                                city_name ="Saloá")
            
        CityCode.objects.create(city_code ="2612406",
                                city_name ="Sanharó")
            
        CityCode.objects.create(city_code ="2612455",
                                city_name ="Santa Cruz")
            
        CityCode.objects.create(city_code ="2612471",
                                city_name ="Santa Cruz da Baixa Verde")
            
        CityCode.objects.create(city_code ="2612505",
                                city_name ="Santa Cruz do Capibaribe")
            
        CityCode.objects.create(city_code ="2612554",
                                city_name ="Santa Filomena")
            
        CityCode.objects.create(city_code ="2612604",
                                city_name ="Santa Maria da Boa Vista")
            
        CityCode.objects.create(city_code ="2612703",
                                city_name ="Santa Maria do Cambucá")
            
        CityCode.objects.create(city_code ="2612802",
                                city_name ="Santa Terezinha")
            
        CityCode.objects.create(city_code ="2612901",
                                city_name ="São Benedito do Sul")
            
        CityCode.objects.create(city_code ="2613008",
                                city_name ="São Bento do Una")
            
        CityCode.objects.create(city_code ="2613107",
                                city_name ="São Caitano")
            
        CityCode.objects.create(city_code ="2613206",
                                city_name ="São João")
            
        CityCode.objects.create(city_code ="2613305",
                                city_name ="São Joaquim do Monte")
            
        CityCode.objects.create(city_code ="2613404",
                                city_name ="São José da Coroa Grande")
            
        CityCode.objects.create(city_code ="2613503",
                                city_name ="São José do Belmonte")
            
        CityCode.objects.create(city_code ="2613602",
                                city_name ="São José do Egito")
            
        CityCode.objects.create(city_code ="2613701",
                                city_name ="São Lourenço da Mata")
            
        CityCode.objects.create(city_code ="2613800",
                                city_name ="São Vicente Férrer")
            
        CityCode.objects.create(city_code ="2613909",
                                city_name ="Serra Talhada")
            
        CityCode.objects.create(city_code ="2614006",
                                city_name ="Serrita")
            
        CityCode.objects.create(city_code ="2614105",
                                city_name ="Sertânia")
            
        CityCode.objects.create(city_code ="2614204",
                                city_name ="Sirinhaém")
            
        CityCode.objects.create(city_code ="2614402",
                                city_name ="Solidão")
            
        CityCode.objects.create(city_code ="2614501",
                                city_name ="Surubim")
            
        CityCode.objects.create(city_code ="2614600",
                                city_name ="Tabira")
            
        CityCode.objects.create(city_code ="2614709",
                                city_name ="Tacaimbó")
            
        CityCode.objects.create(city_code ="2614808",
                                city_name ="Tacaratu")
            
        CityCode.objects.create(city_code ="2614857",
                                city_name ="Tamandaré")
            
        CityCode.objects.create(city_code ="2615003",
                                city_name ="Taquaritinga do Norte")
            
        CityCode.objects.create(city_code ="2615102",
                                city_name ="Terezinha")
            
        CityCode.objects.create(city_code ="2615201",
                                city_name ="Terra Nova")
            
        CityCode.objects.create(city_code ="2615300",
                                city_name ="Timbaúba")
            
        CityCode.objects.create(city_code ="2615409",
                                city_name ="Toritama")
            
        CityCode.objects.create(city_code ="2615508",
                                city_name ="Tracunhaém")
            
        CityCode.objects.create(city_code ="2615607",
                                city_name ="Trindade")
            
        CityCode.objects.create(city_code ="2615706",
                                city_name ="Triunfo")
            
        CityCode.objects.create(city_code ="2615805",
                                city_name ="Tupanatinga")
            
        CityCode.objects.create(city_code ="2615904",
                                city_name ="Tuparetama")
            
        CityCode.objects.create(city_code ="2616001",
                                city_name ="Venturosa")
            
        CityCode.objects.create(city_code ="2616100",
                                city_name ="Verdejante")
            
        CityCode.objects.create(city_code ="2616183",
                                city_name ="Vertente do Lério")
            
        CityCode.objects.create(city_code ="2616209",
                                city_name ="Vertentes")
            
        CityCode.objects.create(city_code ="2616308",
                                city_name ="Vicência")
            
        CityCode.objects.create(city_code ="2616407",
                                city_name ="Vitória de Santo Antão")
            
        CityCode.objects.create(city_code ="2616506",
                                city_name ="Xexéu")
            
        CityCode.objects.create(city_code ="2700102",
                                city_name ="Água Branca")
            
        CityCode.objects.create(city_code ="2700201",
                                city_name ="Anadia")
            
        CityCode.objects.create(city_code ="2700300",
                                city_name ="Arapiraca")
            
        CityCode.objects.create(city_code ="2700409",
                                city_name ="Atalaia")
            
        CityCode.objects.create(city_code ="2700508",
                                city_name ="Barra de Santo Antônio")
            
        CityCode.objects.create(city_code ="2700607",
                                city_name ="Barra de São Miguel")
            
        CityCode.objects.create(city_code ="2700706",
                                city_name ="Batalha")
            
        CityCode.objects.create(city_code ="2700805",
                                city_name ="Belém")
            
        CityCode.objects.create(city_code ="2700904",
                                city_name ="Belo Monte")
            
        CityCode.objects.create(city_code ="2701001",
                                city_name ="Boca da Mata")
            
        CityCode.objects.create(city_code ="2701100",
                                city_name ="Branquinha")
            
        CityCode.objects.create(city_code ="2701209",
                                city_name ="Cacimbinhas")
            
        CityCode.objects.create(city_code ="2701308",
                                city_name ="Cajueiro")
            
        CityCode.objects.create(city_code ="2701357",
                                city_name ="Campestre")
            
        CityCode.objects.create(city_code ="2701407",
                                city_name ="Campo Alegre")
            
        CityCode.objects.create(city_code ="2701506",
                                city_name ="Campo Grande")
            
        CityCode.objects.create(city_code ="2701605",
                                city_name ="Canapi")
            
        CityCode.objects.create(city_code ="2701704",
                                city_name ="Capela")
            
        CityCode.objects.create(city_code ="2701803",
                                city_name ="Carneiros")
            
        CityCode.objects.create(city_code ="2701902",
                                city_name ="Chã Preta")
            
        CityCode.objects.create(city_code ="2702009",
                                city_name ="Coité do Nóia")
            
        CityCode.objects.create(city_code ="2702108",
                                city_name ="Colônia Leopoldina")
            
        CityCode.objects.create(city_code ="2702207",
                                city_name ="Coqueiro Seco")
            
        CityCode.objects.create(city_code ="2702306",
                                city_name ="Coruripe")
            
        CityCode.objects.create(city_code ="2702355",
                                city_name ="Craíbas")
            
        CityCode.objects.create(city_code ="2702405",
                                city_name ="Delmiro Gouveia")
            
        CityCode.objects.create(city_code ="2702504",
                                city_name ="Dois Riachos")
            
        CityCode.objects.create(city_code ="2702553",
                                city_name ="Estrela de Alagoas")
            
        CityCode.objects.create(city_code ="2702603",
                                city_name ="Feira Grande")
            
        CityCode.objects.create(city_code ="2702702",
                                city_name ="Feliz Deserto")
            
        CityCode.objects.create(city_code ="2702801",
                                city_name ="Flexeiras")
            
        CityCode.objects.create(city_code ="2702900",
                                city_name ="Girau do Ponciano")
            
        CityCode.objects.create(city_code ="2703007",
                                city_name ="Ibateguara")
            
        CityCode.objects.create(city_code ="2703106",
                                city_name ="Igaci")
            
        CityCode.objects.create(city_code ="2703205",
                                city_name ="Igreja Nova")
            
        CityCode.objects.create(city_code ="2703304",
                                city_name ="Inhapi")
            
        CityCode.objects.create(city_code ="2703403",
                                city_name ="Jacaré dos Homens")
            
        CityCode.objects.create(city_code ="2703502",
                                city_name ="Jacuípe")
            
        CityCode.objects.create(city_code ="2703601",
                                city_name ="Japaratinga")
            
        CityCode.objects.create(city_code ="2703700",
                                city_name ="Jaramataia")
            
        CityCode.objects.create(city_code ="2703759",
                                city_name ="Jequiá da Praia")
            
        CityCode.objects.create(city_code ="2703809",
                                city_name ="Joaquim Gomes")
            
        CityCode.objects.create(city_code ="2703908",
                                city_name ="Jundiá")
            
        CityCode.objects.create(city_code ="2704005",
                                city_name ="Junqueiro")
            
        CityCode.objects.create(city_code ="2704104",
                                city_name ="Lagoa da Canoa")
            
        CityCode.objects.create(city_code ="2704203",
                                city_name ="Limoeiro de Anadia")
            
        CityCode.objects.create(city_code ="2704302",
                                city_name ="Maceió")
            
        CityCode.objects.create(city_code ="2704401",
                                city_name ="Major Isidoro")
            
        CityCode.objects.create(city_code ="2704906",
                                city_name ="Mar Vermelho")
            
        CityCode.objects.create(city_code ="2704500",
                                city_name ="Maragogi")
            
        CityCode.objects.create(city_code ="2704609",
                                city_name ="Maravilha")
            
        CityCode.objects.create(city_code ="2704708",
                                city_name ="Marechal Deodoro")
            
        CityCode.objects.create(city_code ="2704807",
                                city_name ="Maribondo")
            
        CityCode.objects.create(city_code ="2705002",
                                city_name ="Mata Grande")
            
        CityCode.objects.create(city_code ="2705101",
                                city_name ="Matriz de Camaragibe")
            
        CityCode.objects.create(city_code ="2705200",
                                city_name ="Messias")
            
        CityCode.objects.create(city_code ="2705309",
                                city_name ="Minador do Negrão")
            
        CityCode.objects.create(city_code ="2705408",
                                city_name ="Monteirópolis")
            
        CityCode.objects.create(city_code ="2705507",
                                city_name ="Murici")
            
        CityCode.objects.create(city_code ="2705606",
                                city_name ="Novo Lino")
            
        CityCode.objects.create(city_code ="2705705",
                                city_name ="Olho d'Água das Flores")
            
        CityCode.objects.create(city_code ="2705804",
                                city_name ="Olho d'Água do Casado")
            
        CityCode.objects.create(city_code ="2705903",
                                city_name ="Olho d'Água Grande")
            
        CityCode.objects.create(city_code ="2706000",
                                city_name ="Olivença")
            
        CityCode.objects.create(city_code ="2706109",
                                city_name ="Ouro Branco")
            
        CityCode.objects.create(city_code ="2706208",
                                city_name ="Palestina")
            
        CityCode.objects.create(city_code ="2706307",
                                city_name ="Palmeira dos Índios")
            
        CityCode.objects.create(city_code ="2706406",
                                city_name ="Pão de Açúcar")
            
        CityCode.objects.create(city_code ="2706422",
                                city_name ="Pariconha")
            
        CityCode.objects.create(city_code ="2706448",
                                city_name ="Paripueira")
            
        CityCode.objects.create(city_code ="2706505",
                                city_name ="Passo de Camaragibe")
            
        CityCode.objects.create(city_code ="2706604",
                                city_name ="Paulo Jacinto")
            
        CityCode.objects.create(city_code ="2706703",
                                city_name ="Penedo")
            
        CityCode.objects.create(city_code ="2706802",
                                city_name ="Piaçabuçu")
            
        CityCode.objects.create(city_code ="2706901",
                                city_name ="Pilar")
            
        CityCode.objects.create(city_code ="2707008",
                                city_name ="Pindoba")
            
        CityCode.objects.create(city_code ="2707107",
                                city_name ="Piranhas")
            
        CityCode.objects.create(city_code ="2707206",
                                city_name ="Poço das Trincheiras")
            
        CityCode.objects.create(city_code ="2707305",
                                city_name ="Porto Calvo")
            
        CityCode.objects.create(city_code ="2707404",
                                city_name ="Porto de Pedras")
            
        CityCode.objects.create(city_code ="2707503",
                                city_name ="Porto Real do Colégio")
            
        CityCode.objects.create(city_code ="2707602",
                                city_name ="Quebrangulo")
            
        CityCode.objects.create(city_code ="2707701",
                                city_name ="Rio Largo")
            
        CityCode.objects.create(city_code ="2707800",
                                city_name ="Roteiro")
            
        CityCode.objects.create(city_code ="2707909",
                                city_name ="Santa Luzia do Norte")
            
        CityCode.objects.create(city_code ="2708006",
                                city_name ="Santana do Ipanema")
            
        CityCode.objects.create(city_code ="2708105",
                                city_name ="Santana do Mundaú")
            
        CityCode.objects.create(city_code ="2708204",
                                city_name ="São Brás")
            
        CityCode.objects.create(city_code ="2708303",
                                city_name ="São José da Laje")
            
        CityCode.objects.create(city_code ="2708402",
                                city_name ="São José da Tapera")
            
        CityCode.objects.create(city_code ="2708501",
                                city_name ="São Luís do Quitunde")
            
        CityCode.objects.create(city_code ="2708600",
                                city_name ="São Miguel dos Campos")
            
        CityCode.objects.create(city_code ="2708709",
                                city_name ="São Miguel dos Milagres")
            
        CityCode.objects.create(city_code ="2708808",
                                city_name ="São Sebastião")
            
        CityCode.objects.create(city_code ="2708907",
                                city_name ="Satuba")
            
        CityCode.objects.create(city_code ="2708956",
                                city_name ="Senador Rui Palmeira")
            
        CityCode.objects.create(city_code ="2709004",
                                city_name ="Tanque d'Arca")
            
        CityCode.objects.create(city_code ="2709103",
                                city_name ="Taquarana")
            
        CityCode.objects.create(city_code ="2709152",
                                city_name ="Teotônio Vilela")
            
        CityCode.objects.create(city_code ="2709202",
                                city_name ="Traipu")
            
        CityCode.objects.create(city_code ="2709301",
                                city_name ="União dos Palmares")
            
        CityCode.objects.create(city_code ="2709400",
                                city_name ="Viçosa")
            
        CityCode.objects.create(city_code ="2800100",
                                city_name ="Amparo do São Francisco")
            
        CityCode.objects.create(city_code ="2800209",
                                city_name ="Aquidabã")
            
        CityCode.objects.create(city_code ="2800308",
                                city_name ="Aracaju")
            
        CityCode.objects.create(city_code ="2800407",
                                city_name ="Arauá")
            
        CityCode.objects.create(city_code ="2800506",
                                city_name ="Areia Branca")
            
        CityCode.objects.create(city_code ="2800605",
                                city_name ="Barra dos Coqueiros")
            
        CityCode.objects.create(city_code ="2800670",
                                city_name ="Boquim")
            
        CityCode.objects.create(city_code ="2800704",
                                city_name ="Brejo Grande")
            
        CityCode.objects.create(city_code ="2801009",
                                city_name ="Campo do Brito")
            
        CityCode.objects.create(city_code ="2801108",
                                city_name ="Canhoba")
            
        CityCode.objects.create(city_code ="2801207",
                                city_name ="Canindé de São Francisco")
            
        CityCode.objects.create(city_code ="2801306",
                                city_name ="Capela")
            
        CityCode.objects.create(city_code ="2801405",
                                city_name ="Carira")
            
        CityCode.objects.create(city_code ="2801504",
                                city_name ="Carmópolis")
            
        CityCode.objects.create(city_code ="2801603",
                                city_name ="Cedro de São João")
            
        CityCode.objects.create(city_code ="2801702",
                                city_name ="Cristinápolis")
            
        CityCode.objects.create(city_code ="2801900",
                                city_name ="Cumbe")
            
        CityCode.objects.create(city_code ="2802007",
                                city_name ="Divina Pastora")
            
        CityCode.objects.create(city_code ="2802106",
                                city_name ="Estância")
            
        CityCode.objects.create(city_code ="2802205",
                                city_name ="Feira Nova")
            
        CityCode.objects.create(city_code ="2802304",
                                city_name ="Frei Paulo")
            
        CityCode.objects.create(city_code ="2802403",
                                city_name ="Gararu")
            
        CityCode.objects.create(city_code ="2802502",
                                city_name ="General Maynard")
            
        CityCode.objects.create(city_code ="2802601",
                                city_name ="Gracho Cardoso")
            
        CityCode.objects.create(city_code ="2802700",
                                city_name ="Ilha das Flores")
            
        CityCode.objects.create(city_code ="2802809",
                                city_name ="Indiaroba")
            
        CityCode.objects.create(city_code ="2802908",
                                city_name ="Itabaiana")
            
        CityCode.objects.create(city_code ="2803005",
                                city_name ="Itabaianinha")
            
        CityCode.objects.create(city_code ="2803104",
                                city_name ="Itabi")
            
        CityCode.objects.create(city_code ="2803203",
                                city_name ="Itaporanga d'Ajuda")
            
        CityCode.objects.create(city_code ="2803302",
                                city_name ="Japaratuba")
            
        CityCode.objects.create(city_code ="2803401",
                                city_name ="Japoatã")
            
        CityCode.objects.create(city_code ="2803500",
                                city_name ="Lagarto")
            
        CityCode.objects.create(city_code ="2803609",
                                city_name ="Laranjeiras")
            
        CityCode.objects.create(city_code ="2803708",
                                city_name ="Macambira")
            
        CityCode.objects.create(city_code ="2803807",
                                city_name ="Malhada dos Bois")
            
        CityCode.objects.create(city_code ="2803906",
                                city_name ="Malhador")
            
        CityCode.objects.create(city_code ="2804003",
                                city_name ="Maruim")
            
        CityCode.objects.create(city_code ="2804102",
                                city_name ="Moita Bonita")
            
        CityCode.objects.create(city_code ="2804201",
                                city_name ="Monte Alegre de Sergipe")
            
        CityCode.objects.create(city_code ="2804300",
                                city_name ="Muribeca")
            
        CityCode.objects.create(city_code ="2804409",
                                city_name ="Neópolis")
            
        CityCode.objects.create(city_code ="2804458",
                                city_name ="Nossa Senhora Aparecida")
            
        CityCode.objects.create(city_code ="2804508",
                                city_name ="Nossa Senhora da Glória")
            
        CityCode.objects.create(city_code ="2804607",
                                city_name ="Nossa Senhora das Dores")
            
        CityCode.objects.create(city_code ="2804706",
                                city_name ="Nossa Senhora de Lourdes")
            
        CityCode.objects.create(city_code ="2804805",
                                city_name ="Nossa Senhora do Socorro")
            
        CityCode.objects.create(city_code ="2804904",
                                city_name ="Pacatuba")
            
        CityCode.objects.create(city_code ="2805000",
                                city_name ="Pedra Mole")
            
        CityCode.objects.create(city_code ="2805109",
                                city_name ="Pedrinhas")
            
        CityCode.objects.create(city_code ="2805208",
                                city_name ="Pinhão")
            
        CityCode.objects.create(city_code ="2805307",
                                city_name ="Pirambu")
            
        CityCode.objects.create(city_code ="2805406",
                                city_name ="Poço Redondo")
            
        CityCode.objects.create(city_code ="2805505",
                                city_name ="Poço Verde")
            
        CityCode.objects.create(city_code ="2805604",
                                city_name ="Porto da Folha")
            
        CityCode.objects.create(city_code ="2805703",
                                city_name ="Propriá")
            
        CityCode.objects.create(city_code ="2805802",
                                city_name ="Riachão do Dantas")
            
        CityCode.objects.create(city_code ="2805901",
                                city_name ="Riachuelo")
            
        CityCode.objects.create(city_code ="2806008",
                                city_name ="Ribeirópolis")
            
        CityCode.objects.create(city_code ="2806107",
                                city_name ="Rosário do Catete")
            
        CityCode.objects.create(city_code ="2806206",
                                city_name ="Salgado")
            
        CityCode.objects.create(city_code ="2806305",
                                city_name ="Santa Luzia do Itanhy")
            
        CityCode.objects.create(city_code ="2806503",
                                city_name ="Santa Rosa de Lima")
            
        CityCode.objects.create(city_code ="2806404",
                                city_name ="Santana do São Francisco")
            
        CityCode.objects.create(city_code ="2806602",
                                city_name ="Santo Amaro das Brotas")
            
        CityCode.objects.create(city_code ="2806701",
                                city_name ="São Cristóvão")
            
        CityCode.objects.create(city_code ="2806800",
                                city_name ="São Domingos")
            
        CityCode.objects.create(city_code ="2806909",
                                city_name ="São Francisco")
            
        CityCode.objects.create(city_code ="2807006",
                                city_name ="São Miguel do Aleixo")
            
        CityCode.objects.create(city_code ="2807105",
                                city_name ="Simão Dias")
            
        CityCode.objects.create(city_code ="2807204",
                                city_name ="Siriri")
            
        CityCode.objects.create(city_code ="2807303",
                                city_name ="Telha")
            
        CityCode.objects.create(city_code ="2807402",
                                city_name ="Tobias Barreto")
            
        CityCode.objects.create(city_code ="2807501",
                                city_name ="Tomar do Geru")
            
        CityCode.objects.create(city_code ="2807600",
                                city_name ="Umbaúba")
            
        CityCode.objects.create(city_code ="2900108",
                                city_name ="Abaíra" )
            
        CityCode.objects.create(city_code ="2900207",
                                city_name ="Abaré" )
            
        CityCode.objects.create(city_code ="2900306",
                                city_name ="Acajutiba" )
            
        CityCode.objects.create(city_code ="2900355",
                                city_name ="Adustina" )
            
        CityCode.objects.create(city_code ="2900405",
                                city_name ="Água Fria" )
            
        CityCode.objects.create(city_code ="2900603",
                                city_name ="Aiquara" )
            
        CityCode.objects.create(city_code ="2900702",
                                city_name ="Alagoinhas" )
            
        CityCode.objects.create(city_code ="2900801",
                                city_name ="Alcobaça" )
            
        CityCode.objects.create(city_code ="2900900",
                                city_name ="Almadina" )
            
        CityCode.objects.create(city_code ="2901007",
                                city_name ="Amargosa" )
            
        CityCode.objects.create(city_code ="2901106",
                                city_name ="Amélia Rodrigues" )
            
        CityCode.objects.create(city_code ="2901155",
                                city_name ="América Dourada" )
            
        CityCode.objects.create(city_code ="2901205",
                                city_name ="Anagé" )
            
        CityCode.objects.create(city_code ="2901304",
                                city_name ="Andaraí" )
            
        CityCode.objects.create(city_code ="2901353",
                                city_name ="Andorinha" )
            
        CityCode.objects.create(city_code ="2901403",
                                city_name ="Angical" )
            
        CityCode.objects.create(city_code ="2901502",
                                city_name ="Anguera" )
            
        CityCode.objects.create(city_code ="2901601",
                                city_name ="Antas" )
            
        CityCode.objects.create(city_code ="2901700",
                                city_name ="Antônio Cardoso" )
            
        CityCode.objects.create(city_code ="2901809",
                                city_name ="Antônio Gonçalves" )
            
        CityCode.objects.create(city_code ="2901908",
                                city_name ="Aporá" )
            
        CityCode.objects.create(city_code ="2901957",
                                city_name ="Apuarema" )
            
        CityCode.objects.create(city_code ="2902054",
                                city_name ="Araçás" )
            
        CityCode.objects.create(city_code ="2902005",
                                city_name ="Aracatu" )
            
        CityCode.objects.create(city_code ="2902104",
                                city_name ="Araci" )
            
        CityCode.objects.create(city_code ="2902203",
                                city_name ="Aramari" )
            
        CityCode.objects.create(city_code ="2902252",
                                city_name ="Arataca" )
            
        CityCode.objects.create(city_code ="2902302",
                                city_name ="Aratuípe" )
            
        CityCode.objects.create(city_code ="2902401",
                                city_name ="Aurelino Leal" )
            
        CityCode.objects.create(city_code ="2902500",
                                city_name ="Baianópolis" )
            
        CityCode.objects.create(city_code ="2902609",
                                city_name ="Baixa Grande" )
            
        CityCode.objects.create(city_code ="2902658",
                                city_name ="Banzaê" )
            
        CityCode.objects.create(city_code ="2902708",
                                city_name ="Barra" )
            
        CityCode.objects.create(city_code ="2902807",
                                city_name ="Barra da Estiva" )
            
        CityCode.objects.create(city_code ="2902906",
                                city_name ="Barra do Choça" )
            
        CityCode.objects.create(city_code ="2903003",
                                city_name ="Barra do Mendes" )
            
        CityCode.objects.create(city_code ="2903102",
                                city_name ="Barra do Rocha" )
            
        CityCode.objects.create(city_code ="2903201",
                                city_name ="Barreiras" )
            
        CityCode.objects.create(city_code ="2903235",
                                city_name ="Barro Alto" )
            
        CityCode.objects.create(city_code ="2903300",
                                city_name ="Barro Preto" )
            
        CityCode.objects.create(city_code ="2903276",
                                city_name ="Barrocas" )
            
        CityCode.objects.create(city_code ="2903409",
                                city_name ="Belmonte" )
            
        CityCode.objects.create(city_code ="2903508",
                                city_name ="Belo Campo" )
            
        CityCode.objects.create(city_code ="2903607",
                                city_name ="Biritinga" )
            
        CityCode.objects.create(city_code ="2903706",
                                city_name ="Boa Nova" )
            
        CityCode.objects.create(city_code ="2903805",
                                city_name ="Boa Vista do Tupim" )
            
        CityCode.objects.create(city_code ="2903904",
                                city_name ="Bom Jesus da Lapa" )
            
        CityCode.objects.create(city_code ="2903953",
                                city_name ="Bom Jesus da Serra" )
            
        CityCode.objects.create(city_code ="2904001",
                                city_name ="Boninal" )
            
        CityCode.objects.create(city_code ="2904050",
                                city_name ="Bonito" )
            
        CityCode.objects.create(city_code ="2904100",
                                city_name ="Boquira" )
            
        CityCode.objects.create(city_code ="2904209",
                                city_name ="Botuporã" )
            
        CityCode.objects.create(city_code ="2904308",
                                city_name ="Brejões" )
            
        CityCode.objects.create(city_code ="2904407",
                                city_name ="Brejolândia" )
            
        CityCode.objects.create(city_code ="2904506",
                                city_name ="Brotas de Macaúbas" )
            
        CityCode.objects.create(city_code ="2904605",
                                city_name ="Brumado" )
            
        CityCode.objects.create(city_code ="2904704",
                                city_name ="Buerarema" )
            
        CityCode.objects.create(city_code ="2904753",
                                city_name ="Buritirama" )
            
        CityCode.objects.create(city_code ="2904803",
                                city_name ="Caatiba" )
            
        CityCode.objects.create(city_code ="2904852",
                                city_name ="Cabaceiras do Paraguaçu" )
            
        CityCode.objects.create(city_code ="2904902",
                                city_name ="Cachoeira" )
            
        CityCode.objects.create(city_code ="2905008",
                                city_name ="Caculé" )
            
        CityCode.objects.create(city_code ="2905107",
                                city_name ="Caém" )
            
        CityCode.objects.create(city_code ="2905156",
                                city_name ="Caetanos" )
            
        CityCode.objects.create(city_code ="2905206",
                                city_name ="Caetité" )
            
        CityCode.objects.create(city_code ="2905305",
                                city_name ="Cafarnaum" )
            
        CityCode.objects.create(city_code ="2905404",
                                city_name ="Cairu" )
            
        CityCode.objects.create(city_code ="2905503",
                                city_name ="Caldeirão Grande" )
            
        CityCode.objects.create(city_code ="2905602",
                                city_name ="Camacan" )
            
        CityCode.objects.create(city_code ="2905701",
                                city_name ="Camaçari" )
            
        CityCode.objects.create(city_code ="2905800",
                                city_name ="Camamu" )
            
        CityCode.objects.create(city_code ="2905909",
                                city_name ="Campo Alegre de Lourdes" )
            
        CityCode.objects.create(city_code ="2906006",
                                city_name ="Campo Formoso" )
            
        CityCode.objects.create(city_code ="2906105",
                                city_name ="Canápolis" )
            
        CityCode.objects.create(city_code ="2906204",
                                city_name ="Canarana" )
            
        CityCode.objects.create(city_code ="2906303",
                                city_name ="Canavieiras" )
            
        CityCode.objects.create(city_code ="2906402",
                                city_name ="Candeal" )
            
        CityCode.objects.create(city_code ="2906501",
                                city_name ="Candeias" )
            
        CityCode.objects.create(city_code ="2906600",
                                city_name ="Candiba" )
            
        CityCode.objects.create(city_code ="2906709",
                                city_name ="Cândido Sales" )
            
        CityCode.objects.create(city_code ="2906808",
                                city_name ="Cansanção" )
            
        CityCode.objects.create(city_code ="2906824",
                                city_name ="Canudos" )
            
        CityCode.objects.create(city_code ="2906857",
                                city_name ="Capela do Alto Alegre" )
            
        CityCode.objects.create(city_code ="2906873",
                                city_name ="Capim Grosso" )
            
        CityCode.objects.create(city_code ="2906899",
                                city_name ="Caraíbas" )
            
        CityCode.objects.create(city_code ="2906907",
                                city_name ="Caravelas" )
            
        CityCode.objects.create(city_code ="2907004",
                                city_name ="Cardeal da Silva" )
            
        CityCode.objects.create(city_code ="2907103",
                                city_name ="Carinhanha" )
            
        CityCode.objects.create(city_code ="2907202",
                                city_name ="Casa Nova" )
            
        CityCode.objects.create(city_code ="2907301",
                                city_name ="Castro Alves" )
            
        CityCode.objects.create(city_code ="2907400",
                                city_name ="Catolândia" )
            
        CityCode.objects.create(city_code ="2907509",
                                city_name ="Catu" )
            
        CityCode.objects.create(city_code ="2907558",
                                city_name ="Caturama" )
            
        CityCode.objects.create(city_code ="2907608",
                                city_name ="Central" )
            
        CityCode.objects.create(city_code ="2907707",
                                city_name ="Chorrochó" )
            
        CityCode.objects.create(city_code ="2907806",
                                city_name ="Cícero Dantas" )
            
        CityCode.objects.create(city_code ="2907905",
                                city_name ="Cipó" )
            
        CityCode.objects.create(city_code ="2908002",
                                city_name ="Coaraci" )
            
        CityCode.objects.create(city_code ="2908101",
                                city_name ="Cocos" )
            
        CityCode.objects.create(city_code ="2908200",
                                city_name ="Conceição da Feira" )
            
        CityCode.objects.create(city_code ="2908309",
                                city_name ="Conceição do Almeida" )
            
        CityCode.objects.create(city_code ="2908408",
                                city_name ="Conceição do Coité" )
            
        CityCode.objects.create(city_code ="2908507",
                                city_name ="Conceição do Jacuípe" )
            
        CityCode.objects.create(city_code ="2908606",
                                city_name ="Conde" )
            
        CityCode.objects.create(city_code ="2908705",
                                city_name ="Condeúba" )
            
        CityCode.objects.create(city_code ="2908804",
                                city_name ="Contendas do Sincorá" )
            
        CityCode.objects.create(city_code ="2908903",
                                city_name ="Coração de Maria" )
            
        CityCode.objects.create(city_code ="2909000",
                                city_name ="Cordeiros" )
            
        CityCode.objects.create(city_code ="2909109",
                                city_name ="Coribe" )
            
        CityCode.objects.create(city_code ="2909208",
                                city_name ="Coronel João Sá" )
            
        CityCode.objects.create(city_code ="2909307",
                                city_name ="Correntina" )
            
        CityCode.objects.create(city_code ="2909406",
                                city_name ="Cotegipe" )
            
        CityCode.objects.create(city_code ="2909505",
                                city_name ="Cravolândia" )
            
        CityCode.objects.create(city_code ="2909604",
                                city_name ="Crisópolis" )
            
        CityCode.objects.create(city_code ="2909703",
                                city_name ="Cristópolis" )
            
        CityCode.objects.create(city_code ="2909802",
                                city_name ="Cruz das Almas" )
            
        CityCode.objects.create(city_code ="2909901",
                                city_name ="Curaçá" )
            
        CityCode.objects.create(city_code ="2910008",
                                city_name ="Dário Meira" )
            
        CityCode.objects.create(city_code ="2910057",
                                city_name ="Dias d'Ávila" )
            
        CityCode.objects.create(city_code ="2910107",
                                city_name ="Dom Basílio" )
            
        CityCode.objects.create(city_code ="2910206",
                                city_name ="Dom Macedo Costa" )
            
        CityCode.objects.create(city_code ="2910305",
                                city_name ="Elísio Medrado" )
            
        CityCode.objects.create(city_code ="2910404",
                                city_name ="Encruzilhada" )
            
        CityCode.objects.create(city_code ="2910503",
                                city_name ="Entre Rios" )
            
        CityCode.objects.create(city_code ="2900504",
                                city_name ="Érico Cardoso" )
            
        CityCode.objects.create(city_code ="2910602",
                                city_name ="Esplanada" )
            
        CityCode.objects.create(city_code ="2910701",
                                city_name ="Euclides da Cunha" )
            
        CityCode.objects.create(city_code ="2910727",
                                city_name ="Eunápolis" )
            
        CityCode.objects.create(city_code ="2910750",
                                city_name ="Fátima" )
            
        CityCode.objects.create(city_code ="2910776",
                                city_name ="Feira da Mata" )
            
        CityCode.objects.create(city_code ="2910800",
                                city_name ="Feira de Santana" )
            
        CityCode.objects.create(city_code ="2910859",
                                city_name ="Filadélfia" )
            
        CityCode.objects.create(city_code ="2910909",
                                city_name ="Firmino Alves" )
            
        CityCode.objects.create(city_code ="2911006",
                                city_name ="Floresta Azul" )
            
        CityCode.objects.create(city_code ="2911105",
                                city_name ="Formosa do Rio Preto" )
            
        CityCode.objects.create(city_code ="2911204",
                                city_name ="Gandu" )
            
        CityCode.objects.create(city_code ="2911253",
                                city_name ="Gavião" )
            
        CityCode.objects.create(city_code ="2911303",
                                city_name ="Gentio do Ouro" )
            
        CityCode.objects.create(city_code ="2911402",
                                city_name ="Glória" )
            
        CityCode.objects.create(city_code ="2911501",
                                city_name ="Gongogi" )
            
        CityCode.objects.create(city_code ="2911600",
                                city_name ="Governador Mangabeira" )
            
        CityCode.objects.create(city_code ="2911659",
                                city_name ="Guajeru" )
            
        CityCode.objects.create(city_code ="2911709",
                                city_name ="Guanambi" )
            
        CityCode.objects.create(city_code ="2911808",
                                city_name ="Guaratinga" )
            
        CityCode.objects.create(city_code ="2911857",
                                city_name ="Heliópolis" )
            
        CityCode.objects.create(city_code ="2911907",
                                city_name ="Iaçu" )
            
        CityCode.objects.create(city_code ="2912004",
                                city_name ="Ibiassucê" )
            
        CityCode.objects.create(city_code ="2912103",
                                city_name ="Ibicaraí" )
            
        CityCode.objects.create(city_code ="2912202",
                                city_name ="Ibicoara" )
            
        CityCode.objects.create(city_code ="2912301",
                                city_name ="Ibicuí" )
            
        CityCode.objects.create(city_code ="2912400",
                                city_name ="Ibipeba" )
            
        CityCode.objects.create(city_code ="2912509",
                                city_name ="Ibipitanga" )
            
        CityCode.objects.create(city_code ="2912608",
                                city_name ="Ibiquera" )
            
        CityCode.objects.create(city_code ="2912707",
                                city_name ="Ibirapitanga" )
            
        CityCode.objects.create(city_code ="2912806",
                                city_name ="Ibirapuã" )
            
        CityCode.objects.create(city_code ="2912905",
                                city_name ="Ibirataia" )
            
        CityCode.objects.create(city_code ="2913002",
                                city_name ="Ibitiara" )
            
        CityCode.objects.create(city_code ="2913101",
                                city_name ="Ibititá" )
            
        CityCode.objects.create(city_code ="2913200",
                                city_name ="Ibotirama" )
            
        CityCode.objects.create(city_code ="2913309",
                                city_name ="Ichu" )
            
        CityCode.objects.create(city_code ="2913408",
                                city_name ="Igaporã" )
            
        CityCode.objects.create(city_code ="2913457",
                                city_name ="Igrapiúna" )
            
        CityCode.objects.create(city_code ="2913507",
                                city_name ="Iguaí" )
            
        CityCode.objects.create(city_code ="2913606",
                                city_name ="Ilhéus" )
            
        CityCode.objects.create(city_code ="2913705",
                                city_name ="Inhambupe" )
            
        CityCode.objects.create(city_code ="2913804",
                                city_name ="Ipecaetá" )
            
        CityCode.objects.create(city_code ="2913903",
                                city_name ="Ipiaú" )
            
        CityCode.objects.create(city_code ="2914000",
                                city_name ="Ipirá" )
            
        CityCode.objects.create(city_code ="2914109",
                                city_name ="Ipupiara" )
            
        CityCode.objects.create(city_code ="2914208",
                                city_name ="Irajuba" )
            
        CityCode.objects.create(city_code ="2914307",
                                city_name ="Iramaia" )
            
        CityCode.objects.create(city_code ="2914406",
                                city_name ="Iraquara" )
            
        CityCode.objects.create(city_code ="2914505",
                                city_name ="Irará" )
            
        CityCode.objects.create(city_code ="2914604",
                                city_name ="Irecê" )
            
        CityCode.objects.create(city_code ="2914653",
                                city_name ="Itabela" )
            
        CityCode.objects.create(city_code ="2914703",
                                city_name ="Itaberaba" )
            
        CityCode.objects.create(city_code ="2914802",
                                city_name ="Itabuna" )
            
        CityCode.objects.create(city_code ="2914901",
                                city_name ="Itacaré" )
            
        CityCode.objects.create(city_code ="2915007",
                                city_name ="Itaeté" )
            
        CityCode.objects.create(city_code ="2915106",
                                city_name ="Itagi" )
            
        CityCode.objects.create(city_code ="2915205",
                                city_name ="Itagibá" )
            
        CityCode.objects.create(city_code ="2915304",
                                city_name ="Itagimirim" )
            
        CityCode.objects.create(city_code ="2915353",
                                city_name ="Itaguaçu da Bahia" )
            
        CityCode.objects.create(city_code ="2915403",
                                city_name ="Itaju do Colônia" )
            
        CityCode.objects.create(city_code ="2915502",
                                city_name ="Itajuípe" )
            
        CityCode.objects.create(city_code ="2915601",
                                city_name ="Itamaraju" )
            
        CityCode.objects.create(city_code ="2915700",
                                city_name ="Itamari" )
            
        CityCode.objects.create(city_code ="2915809",
                                city_name ="Itambé" )
            
        CityCode.objects.create(city_code ="2915908",
                                city_name ="Itanagra" )
            
        CityCode.objects.create(city_code ="2916005",
                                city_name ="Itanhém" )
            
        CityCode.objects.create(city_code ="2916104",
                                city_name ="Itaparica" )
            
        CityCode.objects.create(city_code ="2916203",
                                city_name ="Itapé" )
            
        CityCode.objects.create(city_code ="2916302",
                                city_name ="Itapebi" )
            
        CityCode.objects.create(city_code ="2916401",
                                city_name ="Itapetinga" )
            
        CityCode.objects.create(city_code ="2916500",
                                city_name ="Itapicuru" )
            
        CityCode.objects.create(city_code ="2916609",
                                city_name ="Itapitanga" )
            
        CityCode.objects.create(city_code ="2916708",
                                city_name ="Itaquara" )
            
        CityCode.objects.create(city_code ="2916807",
                                city_name ="Itarantim" )
            
        CityCode.objects.create(city_code ="2916856",
                                city_name ="Itatim" )
            
        CityCode.objects.create(city_code ="2916906",
                                city_name ="Itiruçu" )
            
        CityCode.objects.create(city_code ="2917003",
                                city_name ="Itiúba" )
            
        CityCode.objects.create(city_code ="2917102",
                                city_name ="Itororó" )
            
        CityCode.objects.create(city_code ="2917201",
                                city_name ="Ituaçu" )
            
        CityCode.objects.create(city_code ="2917300",
                                city_name ="Ituberá" )
            
        CityCode.objects.create(city_code ="2917334",
                                city_name ="Iuiu" )
            
        CityCode.objects.create(city_code ="2917359",
                                city_name ="Jaborandi" )
            
        CityCode.objects.create(city_code ="2917409",
                                city_name ="Jacaraci" )
            
        CityCode.objects.create(city_code ="2917508",
                                city_name ="Jacobina" )
            
        CityCode.objects.create(city_code ="2917607",
                                city_name ="Jaguaquara" )
            
        CityCode.objects.create(city_code ="2917706",
                                city_name ="Jaguarari" )
            
        CityCode.objects.create(city_code ="2917805",
                                city_name ="Jaguaripe" )
            
        CityCode.objects.create(city_code ="2917904",
                                city_name ="Jandaíra" )
            
        CityCode.objects.create(city_code ="2918001",
                                city_name ="Jequié" )
            
        CityCode.objects.create(city_code ="2918100",
                                city_name ="Jeremoabo" )
            
        CityCode.objects.create(city_code ="2918209",
                                city_name ="Jiquiriçá" )
            
        CityCode.objects.create(city_code ="2918308",
                                city_name ="Jitaúna" )
            
        CityCode.objects.create(city_code ="2918357",
                                city_name ="João Dourado" )
            
        CityCode.objects.create(city_code ="2918407",
                                city_name ="Juazeiro" )
            
        CityCode.objects.create(city_code ="2918456",
                                city_name ="Jucuruçu" )
            
        CityCode.objects.create(city_code ="2918506",
                                city_name ="Jussara" )
            
        CityCode.objects.create(city_code ="2918555",
                                city_name ="Jussari" )
            
        CityCode.objects.create(city_code ="2918605",
                                city_name ="Jussiape" )
            
        CityCode.objects.create(city_code ="2918704",
                                city_name ="Lafaiete Coutinho" )
            
        CityCode.objects.create(city_code ="2918753",
                                city_name ="Lagoa Real" )
            
        CityCode.objects.create(city_code ="2918803",
                                city_name ="Laje" )
            
        CityCode.objects.create(city_code ="2918902",
                                city_name ="Lajedão" )
            
        CityCode.objects.create(city_code ="2919009",
                                city_name ="Lajedinho" )
            
        CityCode.objects.create(city_code ="2919058",
                                city_name ="Lajedo do Tabocal" )
            
        CityCode.objects.create(city_code ="2919108",
                                city_name ="Lamarão" )
            
        CityCode.objects.create(city_code ="2919157",
                                city_name ="Lapão" )
            
        CityCode.objects.create(city_code ="2919207",
                                city_name ="Lauro de Freitas" )
            
        CityCode.objects.create(city_code ="2919306",
                                city_name ="Lençóis" )
            
        CityCode.objects.create(city_code ="2919405",
                                city_name ="Licínio de Almeida" )
            
        CityCode.objects.create(city_code ="2919504",
                                city_name ="Livramento de Nossa Senhora" )
            
        CityCode.objects.create(city_code ="2919553",
                                city_name ="Luís Eduardo Magalhães" )
            
        CityCode.objects.create(city_code ="2919603",
                                city_name ="Macajuba" )
            
        CityCode.objects.create(city_code ="2919702",
                                city_name ="Macarani" )
            
        CityCode.objects.create(city_code ="2919801",
                                city_name ="Macaúbas" )
            
        CityCode.objects.create(city_code ="2919900",
                                city_name ="Macururé" )
            
        CityCode.objects.create(city_code ="2919926",
                                city_name ="Madre de Deus" )
            
        CityCode.objects.create(city_code ="2919959",
                                city_name ="Maetinga" )
            
        CityCode.objects.create(city_code ="2920007",
                                city_name ="Maiquinique" )
            
        CityCode.objects.create(city_code ="2920106",
                                city_name ="Mairi" )
            
        CityCode.objects.create(city_code ="2920205",
                                city_name ="Malhada" )
            
        CityCode.objects.create(city_code ="2920304",
                                city_name ="Malhada de Pedras" )
            
        CityCode.objects.create(city_code ="2920403",
                                city_name ="Manoel Vitorino" )
            
        CityCode.objects.create(city_code ="2920452",
                                city_name ="Mansidão" )
            
        CityCode.objects.create(city_code ="2920502",
                                city_name ="Maracás" )
            
        CityCode.objects.create(city_code ="2920601",
                                city_name ="Maragogipe" )
            
        CityCode.objects.create(city_code ="2920700",
                                city_name ="Maraú" )
            
        CityCode.objects.create(city_code ="2920809",
                                city_name ="Marcionílio Souza" )
            
        CityCode.objects.create(city_code ="2920908",
                                city_name ="Mascote" )
            
        CityCode.objects.create(city_code ="2921005",
                                city_name ="Mata de São João" )
            
        CityCode.objects.create(city_code ="2921054",
                                city_name ="Matina" )
            
        CityCode.objects.create(city_code ="2921104",
                                city_name ="Medeiros Neto" )
            
        CityCode.objects.create(city_code ="2921203",
                                city_name ="Miguel Calmon" )
            
        CityCode.objects.create(city_code ="2921302",
                                city_name ="Milagres" )
            
        CityCode.objects.create(city_code ="2921401",
                                city_name ="Mirangaba" )
            
        CityCode.objects.create(city_code ="2921450",
                                city_name ="Mirante" )
            
        CityCode.objects.create(city_code ="2921500",
                                city_name ="Monte Santo" )
            
        CityCode.objects.create(city_code ="2921609",
                                city_name ="Morpará" )
            
        CityCode.objects.create(city_code ="2921708",
                                city_name ="Morro do Chapéu" )
            
        CityCode.objects.create(city_code ="2921807",
                                city_name ="Mortugaba" )
            
        CityCode.objects.create(city_code ="2921906",
                                city_name ="Mucugê" )
            
        CityCode.objects.create(city_code ="2922003",
                                city_name ="Mucuri" )
            
        CityCode.objects.create(city_code ="2922052",
                                city_name ="Mulungu do Morro" )
            
        CityCode.objects.create(city_code ="2922102",
                                city_name ="Mundo Novo" )
            
        CityCode.objects.create(city_code ="2922201",
                                city_name ="Muniz Ferreira" )
            
        CityCode.objects.create(city_code ="2922250",
                                city_name ="Muquém do São Francisco" )
            
        CityCode.objects.create(city_code ="2922300",
                                city_name ="Muritiba" )
            
        CityCode.objects.create(city_code ="2922409",
                                city_name ="Mutuípe" )
            
        CityCode.objects.create(city_code ="2922508",
                                city_name ="Nazaré" )
            
        CityCode.objects.create(city_code ="2922607",
                                city_name ="Nilo Peçanha" )
            
        CityCode.objects.create(city_code ="2922656",
                                city_name ="Nordestina" )
            
        CityCode.objects.create(city_code ="2922706",
                                city_name ="Nova Canaã" )
            
        CityCode.objects.create(city_code ="2922730",
                                city_name ="Nova Fátima" )
            
        CityCode.objects.create(city_code ="2922755",
                                city_name ="Nova Ibiá" )
            
        CityCode.objects.create(city_code ="2922805",
                                city_name ="Nova Itarana" )
            
        CityCode.objects.create(city_code ="2922854",
                                city_name ="Nova Redenção" )
            
        CityCode.objects.create(city_code ="2922904",
                                city_name ="Nova Soure" )
            
        CityCode.objects.create(city_code ="2923001",
                                city_name ="Nova Viçosa" )
            
        CityCode.objects.create(city_code ="2923035",
                                city_name ="Novo Horizonte" )
            
        CityCode.objects.create(city_code ="2923050",
                                city_name ="Novo Triunfo" )
            
        CityCode.objects.create(city_code ="2923100",
                                city_name ="Olindina" )
            
        CityCode.objects.create(city_code ="2923209",
                                city_name ="Oliveira dos Brejinhos" )
            
        CityCode.objects.create(city_code ="2923308",
                                city_name ="Ouriçangas" )
            
        CityCode.objects.create(city_code ="2923357",
                                city_name ="Ourolândia" )
            
        CityCode.objects.create(city_code ="2923407",
                                city_name ="Palmas de Monte Alto" )
            
        CityCode.objects.create(city_code ="2923506",
                                city_name ="Palmeiras" )
            
        CityCode.objects.create(city_code ="2923605",
                                city_name ="Paramirim" )
            
        CityCode.objects.create(city_code ="2923704",
                                city_name ="Paratinga" )
            
        CityCode.objects.create(city_code ="2923803",
                                city_name ="Paripiranga" )
            
        CityCode.objects.create(city_code ="2923902",
                                city_name ="Pau Brasil" )
            
        CityCode.objects.create(city_code ="2924009",
                                city_name ="Paulo Afonso" )
            
        CityCode.objects.create(city_code ="2924058",
                                city_name ="Pé de Serra" )
            
        CityCode.objects.create(city_code ="2924108",
                                city_name ="Pedrão" )
            
        CityCode.objects.create(city_code ="2924207",
                                city_name ="Pedro Alexandre" )
            
        CityCode.objects.create(city_code ="2924306",
                                city_name ="Piatã" )
            
        CityCode.objects.create(city_code ="2924405",
                                city_name ="Pilão Arcado" )
            
        CityCode.objects.create(city_code ="2924504",
                                city_name ="Pindaí" )
            
        CityCode.objects.create(city_code ="2924603",
                                city_name ="Pindobaçu" )
            
        CityCode.objects.create(city_code ="2924652",
                                city_name ="Pintadas" )
            
        CityCode.objects.create(city_code ="2924678",
                                city_name ="Piraí do Norte" )
            
        CityCode.objects.create(city_code ="2924702",
                                city_name ="Piripá" )
            
        CityCode.objects.create(city_code ="2924801",
                                city_name ="Piritiba" )
            
        CityCode.objects.create(city_code ="2924900",
                                city_name ="Planaltino" )
            
        CityCode.objects.create(city_code ="2925006",
                                city_name ="Planalto" )
            
        CityCode.objects.create(city_code ="2925105",
                                city_name ="Poções" )
            
        CityCode.objects.create(city_code ="2925204",
                                city_name ="Pojuca" )
            
        CityCode.objects.create(city_code ="2925253",
                                city_name ="Ponto Novo" )
            
        CityCode.objects.create(city_code ="2925303",
                                city_name ="Porto Seguro" )
            
        CityCode.objects.create(city_code ="2925402",
                                city_name ="Potiraguá" )
            
        CityCode.objects.create(city_code ="2925501",
                                city_name ="Prado" )
            
        CityCode.objects.create(city_code ="2925600",
                                city_name ="Presidente Dutra" )
            
        CityCode.objects.create(city_code ="2925709",
                                city_name ="Presidente Jânio Quadros" )
            
        CityCode.objects.create(city_code ="2925758",
                                city_name ="Presidente Tancredo Neves" )
            
        CityCode.objects.create(city_code ="2925808",
                                city_name ="Queimadas" )
            
        CityCode.objects.create(city_code ="2925907",
                                city_name ="Quijingue" )
            
        CityCode.objects.create(city_code ="2925931",
                                city_name ="Quixabeira" )
            
        CityCode.objects.create(city_code ="2925956",
                                city_name ="Rafael Jambeiro" )
            
        CityCode.objects.create(city_code ="2926004",
                                city_name ="Remanso" )
            
        CityCode.objects.create(city_code ="2926103",
                                city_name ="Retirolândia" )
            
        CityCode.objects.create(city_code ="2926202",
                                city_name ="Riachão das Neves" )
            
        CityCode.objects.create(city_code ="2926301",
                                city_name ="Riachão do Jacuípe" )
            
        CityCode.objects.create(city_code ="2926400",
                                city_name ="Riacho de Santana" )
            
        CityCode.objects.create(city_code ="2926509",
                                city_name ="Ribeira do Amparo" )
            
        CityCode.objects.create(city_code ="2926608",
                                city_name ="Ribeira do Pombal" )
            
        CityCode.objects.create(city_code ="2926657",
                                city_name ="Ribeirão do Largo" )
            
        CityCode.objects.create(city_code ="2926707",
                                city_name ="Rio de Contas" )
            
        CityCode.objects.create(city_code ="2926806",
                                city_name ="Rio do Antônio" )
            
        CityCode.objects.create(city_code ="2926905",
                                city_name ="Rio do Pires" )
            
        CityCode.objects.create(city_code ="2927002",
                                city_name ="Rio Real" )
            
        CityCode.objects.create(city_code ="2927101",
                                city_name ="Rodelas" )
            
        CityCode.objects.create(city_code ="2927200",
                                city_name ="Ruy Barbosa" )
            
        CityCode.objects.create(city_code ="2927309",
                                city_name ="Salinas da Margarida" )
            
        CityCode.objects.create(city_code ="2927408",
                                city_name ="Salvador" )
            
        CityCode.objects.create(city_code ="2927507",
                                city_name ="Santa Bárbara" )
            
        CityCode.objects.create(city_code ="2927606",
                                city_name ="Santa Brígida" )
            
        CityCode.objects.create(city_code ="2927705",
                                city_name ="Santa Cruz Cabrália" )
            
        CityCode.objects.create(city_code ="2927804",
                                city_name ="Santa Cruz da Vitória" )
            
        CityCode.objects.create(city_code ="2927903",
                                city_name ="Santa Inês" )
            
        CityCode.objects.create(city_code ="2928059",
                                city_name ="Santa Luzia" )
            
        CityCode.objects.create(city_code ="2928109",
                                city_name ="Santa Maria da Vitória" )
            
        CityCode.objects.create(city_code ="2928406",
                                city_name ="Santa Rita de Cássia" )
            
        CityCode.objects.create(city_code ="2928505",
                                city_name ="Santa Terezinha" )
            
        CityCode.objects.create(city_code ="2928000",
                                city_name ="Santaluz" )
            
        CityCode.objects.create(city_code ="2928208",
                                city_name ="Santana" )
            
        CityCode.objects.create(city_code ="2928307",
                                city_name ="Santanópolis" )
            
        CityCode.objects.create(city_code ="2928604",
                                city_name ="Santo Amaro" )
            
        CityCode.objects.create(city_code ="2928703",
                                city_name ="Santo Antônio de Jesus" )
            
        CityCode.objects.create(city_code ="2928802",
                                city_name ="Santo Estêvão" )
            
        CityCode.objects.create(city_code ="2928901",
                                city_name ="São Desidério" )
            
        CityCode.objects.create(city_code ="2928950",
                                city_name ="São Domingos" )
            
        CityCode.objects.create(city_code ="2929107",
                                city_name ="São Felipe" )
            
        CityCode.objects.create(city_code ="2929008",
                                city_name ="São Félix" )
            
        CityCode.objects.create(city_code ="2929057",
                                city_name ="São Félix do Coribe" )
            
        CityCode.objects.create(city_code ="2929206",
                                city_name ="São Francisco do Conde" )
            
        CityCode.objects.create(city_code ="2929255",
                                city_name ="São Gabriel" )
            
        CityCode.objects.create(city_code ="2929305",
                                city_name ="São Gonçalo dos Campos" )
            
        CityCode.objects.create(city_code ="2929354",
                                city_name ="São José da Vitória" )
            
        CityCode.objects.create(city_code ="2929370",
                                city_name ="São José do Jacuípe" )
            
        CityCode.objects.create(city_code ="2929404",
                                city_name ="São Miguel das Matas" )
            
        CityCode.objects.create(city_code ="2929503",
                                city_name ="São Sebastião do Passé" )
            
        CityCode.objects.create(city_code ="2929602",
                                city_name ="Sapeaçu" )
            
        CityCode.objects.create(city_code ="2929701",
                                city_name ="Sátiro Dias" )
            
        CityCode.objects.create(city_code ="2929750",
                                city_name ="Saubara" )
            
        CityCode.objects.create(city_code ="2929800",
                                city_name ="Saúde" )
            
        CityCode.objects.create(city_code ="2929909",
                                city_name ="Seabra" )
            
        CityCode.objects.create(city_code ="2930006",
                                city_name ="Sebastião Laranjeiras" )
            
        CityCode.objects.create(city_code ="2930105",
                                city_name ="Senhor do Bonfim" )
            
        CityCode.objects.create(city_code ="2930204",
                                city_name ="Sento Sé" )
            
        CityCode.objects.create(city_code ="2930154",
                                city_name ="Serra do Ramalho" )
            
        CityCode.objects.create(city_code ="2930303",
                                city_name ="Serra Dourada" )
            
        CityCode.objects.create(city_code ="2930402",
                                city_name ="Serra Preta" )
            
        CityCode.objects.create(city_code ="2930501",
                                city_name ="Serrinha" )
            
        CityCode.objects.create(city_code ="2930600",
                                city_name ="Serrolândia" )
            
        CityCode.objects.create(city_code ="2930709",
                                city_name ="Simões Filho" )
            
        CityCode.objects.create(city_code ="2930758",
                                city_name ="Sítio do Mato" )
            
        CityCode.objects.create(city_code ="2930766",
                                city_name ="Sítio do Quinto" )
            
        CityCode.objects.create(city_code ="2930774",
                                city_name ="Sobradinho" )
            
        CityCode.objects.create(city_code ="2930808",
                                city_name ="Souto Soares" )
            
        CityCode.objects.create(city_code ="2930907",
                                city_name ="Tabocas do Brejo Velho" )
            
        CityCode.objects.create(city_code ="2931004",
                                city_name ="Tanhaçu" )
            
        CityCode.objects.create(city_code ="2931053",
                                city_name ="Tanque Novo" )
            
        CityCode.objects.create(city_code ="2931103",
                                city_name ="Tanquinho" )
            
        CityCode.objects.create(city_code ="2931202",
                                city_name ="Taperoá" )
            
        CityCode.objects.create(city_code ="2931301",
                                city_name ="Tapiramutá" )
            
        CityCode.objects.create(city_code ="2931350",
                                city_name ="Teixeira de Freitas" )
            
        CityCode.objects.create(city_code ="2931400",
                                city_name ="Teodoro Sampaio" )
            
        CityCode.objects.create(city_code ="2931509",
                                city_name ="Teofilândia" )
            
        CityCode.objects.create(city_code ="2931608",
                                city_name ="Teolândia" )
            
        CityCode.objects.create(city_code ="2931707",
                                city_name ="Terra Nova" )
            
        CityCode.objects.create(city_code ="2931806",
                                city_name ="Tremedal" )
            
        CityCode.objects.create(city_code ="2931905",
                                city_name ="Tucano" )
            
        CityCode.objects.create(city_code ="2932002",
                                city_name ="Uauá" )
            
        CityCode.objects.create(city_code ="2932101",
                                city_name ="Ubaíra" )
            
        CityCode.objects.create(city_code ="2932200",
                                city_name ="Ubaitaba" )
            
        CityCode.objects.create(city_code ="2932309",
                                city_name ="Ubatã" )
            
        CityCode.objects.create(city_code ="2932408",
                                city_name ="Uibaí" )
            
        CityCode.objects.create(city_code ="2932457",
                                city_name ="Umburanas" )
            
        CityCode.objects.create(city_code ="2932507",
                                city_name ="Una" )
            
        CityCode.objects.create(city_code ="2932606",
                                city_name ="Urandi" )
            
        CityCode.objects.create(city_code ="2932705",
                                city_name ="Uruçuca" )
            
        CityCode.objects.create(city_code ="2932804",
                                city_name ="Utinga" )
            
        CityCode.objects.create(city_code ="2932903",
                                city_name ="Valença" )
            
        CityCode.objects.create(city_code ="2933000",
                                city_name ="Valente" )
            
        CityCode.objects.create(city_code ="2933059",
                                city_name ="Várzea da Roça" )
            
        CityCode.objects.create(city_code ="2933109",
                                city_name ="Várzea do Poço" )
            
        CityCode.objects.create(city_code ="2933158",
                                city_name ="Várzea Nova" )
            
        CityCode.objects.create(city_code ="2933174",
                                city_name ="Varzedo" )
            
        CityCode.objects.create(city_code ="2933208",
                                city_name ="Vera Cruz" )
            
        CityCode.objects.create(city_code ="2933257",
                                city_name ="Vereda" )
            
        CityCode.objects.create(city_code ="2933307",
                                city_name ="Vitória da Conquista" )
            
        CityCode.objects.create(city_code ="2933406",
                                city_name ="Wagner" )
            
        CityCode.objects.create(city_code ="2933455",
                                city_name ="Wanderley" )
            
        CityCode.objects.create(city_code ="2933505",
                                city_name ="Wenceslau Guimarães" )
            
        CityCode.objects.create(city_code ="2933604",
                                city_name ="Xique-Xique")

        CityCode.objects.create(city_code ="3100104",
                                city_name ="Abadia dos Dourados" )
            
        CityCode.objects.create(city_code ="3100203",
                                city_name ="Abaeté" )
            
        CityCode.objects.create(city_code ="3100302",
                                city_name ="Abre Campo" )
            
        CityCode.objects.create(city_code ="3100401",
                                city_name ="Acaiaca" )
            
        CityCode.objects.create(city_code ="3100500",
                                city_name ="Açucena" )
            
        CityCode.objects.create(city_code ="3100609",
                                city_name ="Água Boa" )
            
        CityCode.objects.create(city_code ="3100708",
                                city_name ="Água Comprida" )
            
        CityCode.objects.create(city_code ="3100807",
                                city_name ="Aguanil" )
            
        CityCode.objects.create(city_code ="3100906",
                                city_name ="Águas Formosas" )
            
        CityCode.objects.create(city_code ="3101003",
                                city_name ="Águas Vermelhas" )
            
        CityCode.objects.create(city_code ="3101102",
                                city_name ="Aimorés" )
            
        CityCode.objects.create(city_code ="3101201",
                                city_name ="Aiuruoca" )
            
        CityCode.objects.create(city_code ="3101300",
                                city_name ="Alagoa" )
            
        CityCode.objects.create(city_code ="3101409",
                                city_name ="Albertina" )
            
        CityCode.objects.create(city_code ="3101508",
                                city_name ="Além Paraíba" )
            
        CityCode.objects.create(city_code ="3101607",
                                city_name ="Alfenas" )
            
        CityCode.objects.create(city_code ="3101631",
                                city_name ="Alfredo Vasconcelos" )
            
        CityCode.objects.create(city_code ="3101706",
                                city_name ="Almenara" )
            
        CityCode.objects.create(city_code ="3101805",
                                city_name ="Alpercata" )
            
        CityCode.objects.create(city_code ="3101904",
                                city_name ="Alpinópolis" )
            
        CityCode.objects.create(city_code ="3102001",
                                city_name ="Alterosa" )
            
        CityCode.objects.create(city_code ="3102050",
                                city_name ="Alto Caparaó" )
            
        CityCode.objects.create(city_code ="3153509",
                                city_name ="Alto Jequitibá" )
            
        CityCode.objects.create(city_code ="3102100",
                                city_name ="Alto Rio Doce" )
            
        CityCode.objects.create(city_code ="3102209",
                                city_name ="Alvarenga" )
            
        CityCode.objects.create(city_code ="3102308",
                                city_name ="Alvinópolis" )
            
        CityCode.objects.create(city_code ="3102407",
                                city_name ="Alvorada de Minas" )
            
        CityCode.objects.create(city_code ="3102506",
                                city_name ="Amparo do Serra" )
            
        CityCode.objects.create(city_code ="3102605",
                                city_name ="Andradas" )
            
        CityCode.objects.create(city_code ="3102803",
                                city_name ="Andrelândia" )
            
        CityCode.objects.create(city_code ="3102852",
                                city_name ="Angelândia" )
            
        CityCode.objects.create(city_code ="3102902",
                                city_name ="Antônio Carlos" )
            
        CityCode.objects.create(city_code ="3103009",
                                city_name ="Antônio Dias" )
            
        CityCode.objects.create(city_code ="3103108",
                                city_name ="Antônio Prado de Minas" )
            
        CityCode.objects.create(city_code ="3103207",
                                city_name ="Araçaí" )
            
        CityCode.objects.create(city_code ="3103306",
                                city_name ="Aracitaba" )
            
        CityCode.objects.create(city_code ="3103405",
                                city_name ="Araçuaí" )
            
        CityCode.objects.create(city_code ="3103504",
                                city_name ="Araguari" )
            
        CityCode.objects.create(city_code ="3103603",
                                city_name ="Arantina" )
            
        CityCode.objects.create(city_code ="3103702",
                                city_name ="Araponga" )
            
        CityCode.objects.create(city_code ="3103751",
                                city_name ="Araporã" )
            
        CityCode.objects.create(city_code ="3103801",
                                city_name ="Arapuá" )
            
        CityCode.objects.create(city_code ="3103900",
                                city_name ="Araújos" )
            
        CityCode.objects.create(city_code ="3104007",
                                city_name ="Araxá" )
            
        CityCode.objects.create(city_code ="3104106",
                                city_name ="Arceburgo" )
            
        CityCode.objects.create(city_code ="3104205",
                                city_name ="Arcos" )
            
        CityCode.objects.create(city_code ="3104304",
                                city_name ="Areado" )
            
        CityCode.objects.create(city_code ="3104403",
                                city_name ="Argirita" )
            
        CityCode.objects.create(city_code ="3104452",
                                city_name ="Aricanduva" )
            
        CityCode.objects.create(city_code ="3104502",
                                city_name ="Arinos" )
            
        CityCode.objects.create(city_code ="3104601",
                                city_name ="Astolfo Dutra" )
            
        CityCode.objects.create(city_code ="3104700",
                                city_name ="Ataléia" )
            
        CityCode.objects.create(city_code ="3104809",
                                city_name ="Augusto de Lima" )
            
        CityCode.objects.create(city_code ="3104908",
                                city_name ="Baependi" )
            
        CityCode.objects.create(city_code ="3105004",
                                city_name ="Baldim" )
            
        CityCode.objects.create(city_code ="3105103",
                                city_name ="Bambuí" )
            
        CityCode.objects.create(city_code ="3105202",
                                city_name ="Bandeira" )
            
        CityCode.objects.create(city_code ="3105301",
                                city_name ="Bandeira do Sul" )
            
        CityCode.objects.create(city_code ="3105400",
                                city_name ="Barão de Cocais" )
            
        CityCode.objects.create(city_code ="3105509",
                                city_name ="Barão de Monte Alto" )
            
        CityCode.objects.create(city_code ="3105608",
                                city_name ="Barbacena" )
            
        CityCode.objects.create(city_code ="3105707",
                                city_name ="Barra Longa" )
            
        CityCode.objects.create(city_code ="3105905",
                                city_name ="Barroso" )
            
        CityCode.objects.create(city_code ="3106002",
                                city_name ="Bela Vista de Minas" )
            
        CityCode.objects.create(city_code ="3106101",
                                city_name ="Belmiro Braga" )
            
        CityCode.objects.create(city_code ="3106200",
                                city_name ="Belo Horizonte" )
            
        CityCode.objects.create(city_code ="3106309",
                                city_name ="Belo Oriente" )
            
        CityCode.objects.create(city_code ="3106408",
                                city_name ="Belo Vale" )
            
        CityCode.objects.create(city_code ="3106507",
                                city_name ="Berilo" )
            
        CityCode.objects.create(city_code ="3106655",
                                city_name ="Berizal" )
            
        CityCode.objects.create(city_code ="3106606",
                                city_name ="Bertópolis" )
            
        CityCode.objects.create(city_code ="3106705",
                                city_name ="Betim" )
            
        CityCode.objects.create(city_code ="3106804",
                                city_name ="Bias Fortes" )
            
        CityCode.objects.create(city_code ="3106903",
                                city_name ="Bicas" )
            
        CityCode.objects.create(city_code ="3107000",
                                city_name ="Biquinhas" )
            
        CityCode.objects.create(city_code ="3107109",
                                city_name ="Boa Esperança" )
            
        CityCode.objects.create(city_code ="3107208",
                                city_name ="Bocaina de Minas" )
            
        CityCode.objects.create(city_code ="3107307",
                                city_name ="Bocaiúva" )
            
        CityCode.objects.create(city_code ="3107406",
                                city_name ="Bom Despacho" )
            
        CityCode.objects.create(city_code ="3107505",
                                city_name ="Bom Jardim de Minas" )
            
        CityCode.objects.create(city_code ="3107604",
                                city_name ="Bom Jesus da Penha" )
            
        CityCode.objects.create(city_code ="3107703",
                                city_name ="Bom Jesus do Amparo" )
            
        CityCode.objects.create(city_code ="3107802",
                                city_name ="Bom Jesus do Galho" )
            
        CityCode.objects.create(city_code ="3107901",
                                city_name ="Bom Repouso" )
            
        CityCode.objects.create(city_code ="3108008",
                                city_name ="Bom Sucesso" )
            
        CityCode.objects.create(city_code ="3108107",
                                city_name ="Bonfim" )
            
        CityCode.objects.create(city_code ="3108206",
                                city_name ="Bonfinópolis de Minas" )
            
        CityCode.objects.create(city_code ="3108255",
                                city_name ="Bonito de Minas" )
            
        CityCode.objects.create(city_code ="3108305",
                                city_name ="Borda da Mata" )
            
        CityCode.objects.create(city_code ="3108404",
                                city_name ="Botelhos" )
            
        CityCode.objects.create(city_code ="3108503",
                                city_name ="Botumirim" )
            
        CityCode.objects.create(city_code ="3108701",
                                city_name ="Brás Pires" )
            
        CityCode.objects.create(city_code ="3108552",
                                city_name ="Brasilândia de Minas" )
            
        CityCode.objects.create(city_code ="3108602",
                                city_name ="Brasília de Minas" )
            
        CityCode.objects.create(city_code ="3108800",
                                city_name ="Braúnas" )
            
        CityCode.objects.create(city_code ="3108909",
                                city_name ="Brazópolis" )
            
        CityCode.objects.create(city_code ="3109006",
                                city_name ="Brumadinho" )
            
        CityCode.objects.create(city_code ="3109105",
                                city_name ="Bueno Brandão" )
            
        CityCode.objects.create(city_code ="3109204",
                                city_name ="Buenópolis" )
            
        CityCode.objects.create(city_code ="3109253",
                                city_name ="Bugre" )
            
        CityCode.objects.create(city_code ="3109303",
                                city_name ="Buritis" )
            
        CityCode.objects.create(city_code ="3109402",
                                city_name ="Buritizeiro" )
            
        CityCode.objects.create(city_code ="3109451",
                                city_name ="Cabeceira Grande" )
            
        CityCode.objects.create(city_code ="3109501",
                                city_name ="Cabo Verde" )
            
        CityCode.objects.create(city_code ="3109600",
                                city_name ="Cachoeira da Prata" )
            
        CityCode.objects.create(city_code ="3109709",
                                city_name ="Cachoeira de Minas" )
            
        CityCode.objects.create(city_code ="3102704",
                                city_name ="Cachoeira de Pajeú" )
            
        CityCode.objects.create(city_code ="3109808",
                                city_name ="Cachoeira Dourada" )
            
        CityCode.objects.create(city_code ="3109907",
                                city_name ="Caetanópolis" )
            
        CityCode.objects.create(city_code ="3110004",
                                city_name ="Caeté" )
            
        CityCode.objects.create(city_code ="3110103",
                                city_name ="Caiana" )
            
        CityCode.objects.create(city_code ="3110202",
                                city_name ="Cajuri" )
            
        CityCode.objects.create(city_code ="3110301",
                                city_name ="Caldas" )
            
        CityCode.objects.create(city_code ="3110400",
                                city_name ="Camacho" )
            
        CityCode.objects.create(city_code ="3110509",
                                city_name ="Camanducaia" )
            
        CityCode.objects.create(city_code ="3110608",
                                city_name ="Cambuí" )
            
        CityCode.objects.create(city_code ="3110707",
                                city_name ="Cambuquira" )
            
        CityCode.objects.create(city_code ="3110806",
                                city_name ="Campanário" )
            
        CityCode.objects.create(city_code ="3110905",
                                city_name ="Campanha" )
            
        CityCode.objects.create(city_code ="3111002",
                                city_name ="Campestre" )
            
        CityCode.objects.create(city_code ="3111101",
                                city_name ="Campina Verde" )
            
        CityCode.objects.create(city_code ="3111150",
                                city_name ="Campo Azul" )
            
        CityCode.objects.create(city_code ="3111200",
                                city_name ="Campo Belo" )
            
        CityCode.objects.create(city_code ="3111309",
                                city_name ="Campo do Meio" )
            
        CityCode.objects.create(city_code ="3111408",
                                city_name ="Campo Florido" )
            
        CityCode.objects.create(city_code ="3111507",
                                city_name ="Campos Altos" )
            
        CityCode.objects.create(city_code ="3111606",
                                city_name ="Campos Gerais" )
            
        CityCode.objects.create(city_code ="3111903",
                                city_name ="Cana Verde" )
            
        CityCode.objects.create(city_code ="3111705",
                                city_name ="Canaã" )
            
        CityCode.objects.create(city_code ="3111804",
                                city_name ="Canápolis" )
            
        CityCode.objects.create(city_code ="3112000",
                                city_name ="Candeias" )
            
        CityCode.objects.create(city_code ="3112059",
                                city_name ="Cantagalo" )
            
        CityCode.objects.create(city_code ="3112109",
                                city_name ="Caparaó" )
            
        CityCode.objects.create(city_code ="3112208",
                                city_name ="Capela Nova" )
            
        CityCode.objects.create(city_code ="3112307",
                                city_name ="Capelinha" )
            
        CityCode.objects.create(city_code ="3112406",
                                city_name ="Capetinga" )
            
        CityCode.objects.create(city_code ="3112505",
                                city_name ="Capim Branco" )
            
        CityCode.objects.create(city_code ="3112604",
                                city_name ="Capinópolis" )
            
        CityCode.objects.create(city_code ="3112653",
                                city_name ="Capitão Andrade" )
            
        CityCode.objects.create(city_code ="3112703",
                                city_name ="Capitão Enéas" )
            
        CityCode.objects.create(city_code ="3112802",
                                city_name ="Capitólio" )
            
        CityCode.objects.create(city_code ="3112901",
                                city_name ="Caputira" )
            
        CityCode.objects.create(city_code ="3113008",
                                city_name ="Caraí" )
            
        CityCode.objects.create(city_code ="3113107",
                                city_name ="Caranaíba" )
            
        CityCode.objects.create(city_code ="3113206",
                                city_name ="Carandaí" )
            
        CityCode.objects.create(city_code ="3113305",
                                city_name ="Carangola" )
            
        CityCode.objects.create(city_code ="3113404",
                                city_name ="Caratinga" )
            
        CityCode.objects.create(city_code ="3113503",
                                city_name ="Carbonita" )
            
        CityCode.objects.create(city_code ="3113602",
                                city_name ="Careaçu" )
            
        CityCode.objects.create(city_code ="3113701",
                                city_name ="Carlos Chagas" )
            
        CityCode.objects.create(city_code ="3113800",
                                city_name ="Carmésia" )
            
        CityCode.objects.create(city_code ="3113909",
                                city_name ="Carmo da Cachoeira" )
            
        CityCode.objects.create(city_code ="3114006",
                                city_name ="Carmo da Mata" )
            
        CityCode.objects.create(city_code ="3114105",
                                city_name ="Carmo de Minas" )
            
        CityCode.objects.create(city_code ="3114204",
                                city_name ="Carmo do Cajuru" )
            
        CityCode.objects.create(city_code ="3114303",
                                city_name ="Carmo do Paranaíba" )
            
        CityCode.objects.create(city_code ="3114402",
                                city_name ="Carmo do Rio Claro" )
            
        CityCode.objects.create(city_code ="3114501",
                                city_name ="Carmópolis de Minas" )
            
        CityCode.objects.create(city_code ="3114550",
                                city_name ="Carneirinho" )
            
        CityCode.objects.create(city_code ="3114600",
                                city_name ="Carrancas" )
            
        CityCode.objects.create(city_code ="3114709",
                                city_name ="Carvalhópolis" )
            
        CityCode.objects.create(city_code ="3114808",
                                city_name ="Carvalhos" )
            
        CityCode.objects.create(city_code ="3114907",
                                city_name ="Casa Grande" )
            
        CityCode.objects.create(city_code ="3115003",
                                city_name ="Cascalho Rico" )
            
        CityCode.objects.create(city_code ="3115102",
                                city_name ="Cássia" )
            
        CityCode.objects.create(city_code ="3115300",
                                city_name ="Cataguases" )
            
        CityCode.objects.create(city_code ="3115359",
                                city_name ="Catas Altas" )
            
        CityCode.objects.create(city_code ="3115409",
                                city_name ="Catas Altas da Noruega" )
            
        CityCode.objects.create(city_code ="3115458",
                                city_name ="Catuji" )
            
        CityCode.objects.create(city_code ="3115474",
                                city_name ="Catuti" )
            
        CityCode.objects.create(city_code ="3115508",
                                city_name ="Caxambu" )
            
        CityCode.objects.create(city_code ="3115607",
                                city_name ="Cedro do Abaeté" )
            
        CityCode.objects.create(city_code ="3115706",
                                city_name ="Central de Minas" )
            
        CityCode.objects.create(city_code ="3115805",
                                city_name ="Centralina" )
            
        CityCode.objects.create(city_code ="3115904",
                                city_name ="Chácara" )
            
        CityCode.objects.create(city_code ="3116001",
                                city_name ="Chalé" )
            
        CityCode.objects.create(city_code ="3116100",
                                city_name ="Chapada do Norte" )
            
        CityCode.objects.create(city_code ="3116159",
                                city_name ="Chapada Gaúcha" )
            
        CityCode.objects.create(city_code ="3116209",
                                city_name ="Chiador" )
            
        CityCode.objects.create(city_code ="3116308",
                                city_name ="Cipotânea" )
            
        CityCode.objects.create(city_code ="3116407",
                                city_name ="Claraval" )
            
        CityCode.objects.create(city_code ="3116506",
                                city_name ="Claro dos Poções" )
            
        CityCode.objects.create(city_code ="3116605",
                                city_name ="Cláudio" )
            
        CityCode.objects.create(city_code ="3116704",
                                city_name ="Coimbra" )
            
        CityCode.objects.create(city_code ="3116803",
                                city_name ="Coluna" )
            
        CityCode.objects.create(city_code ="3116902",
                                city_name ="Comendador Gomes" )
            
        CityCode.objects.create(city_code ="3117009",
                                city_name ="Comercinho" )
            
        CityCode.objects.create(city_code ="3117108",
                                city_name ="Conceição da Aparecida" )
            
        CityCode.objects.create(city_code ="3115201",
                                city_name ="Conceição da Barra de Minas" )
            
        CityCode.objects.create(city_code ="3117306",
                                city_name ="Conceição das Alagoas" )
            
        CityCode.objects.create(city_code ="3117207",
                                city_name ="Conceição das Pedras" )
            
        CityCode.objects.create(city_code ="3117405",
                                city_name ="Conceição de Ipanema" )
            
        CityCode.objects.create(city_code ="3117504",
                                city_name ="Conceição do Mato Dentro" )
            
        CityCode.objects.create(city_code ="3117603",
                                city_name ="Conceição do Pará" )
            
        CityCode.objects.create(city_code ="3117702",
                                city_name ="Conceição do Rio Verde" )
            
        CityCode.objects.create(city_code ="3117801",
                                city_name ="Conceição dos Ouros" )
            
        CityCode.objects.create(city_code ="3117836",
                                city_name ="Cônego Marinho" )
            
        CityCode.objects.create(city_code ="3117876",
                                city_name ="Confins" )
            
        CityCode.objects.create(city_code ="3117900",
                                city_name ="Congonhal" )
            
        CityCode.objects.create(city_code ="3118007",
                                city_name ="Congonhas" )
            
        CityCode.objects.create(city_code ="3118106",
                                city_name ="Congonhas do Norte" )
            
        CityCode.objects.create(city_code ="3118205",
                                city_name ="Conquista" )
            
        CityCode.objects.create(city_code ="3118304",
                                city_name ="Conselheiro Lafaiete" )
            
        CityCode.objects.create(city_code ="3118403",
                                city_name ="Conselheiro Pena" )
            
        CityCode.objects.create(city_code ="3118502",
                                city_name ="Consolação" )
            
        CityCode.objects.create(city_code ="3118601",
                                city_name ="Contagem" )
            
        CityCode.objects.create(city_code ="3118700",
                                city_name ="Coqueiral" )
            
        CityCode.objects.create(city_code ="3118809",
                                city_name ="Coração de Jesus" )
            
        CityCode.objects.create(city_code ="3118908",
                                city_name ="Cordisburgo" )
            
        CityCode.objects.create(city_code ="3119005",
                                city_name ="Cordislândia" )
            
        CityCode.objects.create(city_code ="3119104",
                                city_name ="Corinto" )
            
        CityCode.objects.create(city_code ="3119203",
                                city_name ="Coroaci" )
            
        CityCode.objects.create(city_code ="3119302",
                                city_name ="Coromandel" )
            
        CityCode.objects.create(city_code ="3119401",
                                city_name ="Coronel Fabriciano" )
            
        CityCode.objects.create(city_code ="3119500",
                                city_name ="Coronel Murta" )
            
        CityCode.objects.create(city_code ="3119609",
                                city_name ="Coronel Pacheco" )
            
        CityCode.objects.create(city_code ="3119708",
                                city_name ="Coronel Xavier Chaves" )
            
        CityCode.objects.create(city_code ="3119807",
                                city_name ="Córrego Danta" )
            
        CityCode.objects.create(city_code ="3119906",
                                city_name ="Córrego do Bom Jesus" )
            
        CityCode.objects.create(city_code ="3119955",
                                city_name ="Córrego Fundo" )
            
        CityCode.objects.create(city_code ="3120003",
                                city_name ="Córrego Novo" )
            
        CityCode.objects.create(city_code ="3120102",
                                city_name ="Couto de Magalhães de Minas" )
            
        CityCode.objects.create(city_code ="3120151",
                                city_name ="Crisólita" )
            
        CityCode.objects.create(city_code ="3120201",
                                city_name ="Cristais" )
            
        CityCode.objects.create(city_code ="3120300",
                                city_name ="Cristália" )
            
        CityCode.objects.create(city_code ="3120409",
                                city_name ="Cristiano Otoni" )
            
        CityCode.objects.create(city_code ="3120508",
                                city_name ="Cristina" )
            
        CityCode.objects.create(city_code ="3120607",
                                city_name ="Crucilândia" )
            
        CityCode.objects.create(city_code ="3120706",
                                city_name ="Cruzeiro da Fortaleza" )
            
        CityCode.objects.create(city_code ="3120805",
                                city_name ="Cruzília" )
            
        CityCode.objects.create(city_code ="3120839",
                                city_name ="Cuparaque" )
            
        CityCode.objects.create(city_code ="3120870",
                                city_name ="Curral de Dentro" )
            
        CityCode.objects.create(city_code ="3120904",
                                city_name ="Curvelo" )
            
        CityCode.objects.create(city_code ="3121001",
                                city_name ="Datas" )
            
        CityCode.objects.create(city_code ="3121100",
                                city_name ="Delfim Moreira" )
            
        CityCode.objects.create(city_code ="3121209",
                                city_name ="Delfinópolis" )
            
        CityCode.objects.create(city_code ="3121258",
                                city_name ="Delta" )
            
        CityCode.objects.create(city_code ="3121308",
                                city_name ="Descoberto" )
            
        CityCode.objects.create(city_code ="3121407",
                                city_name ="Desterro de Entre Rios" )
            
        CityCode.objects.create(city_code ="3121506",
                                city_name ="Desterro do Melo" )
            
        CityCode.objects.create(city_code ="3121605",
                                city_name ="Diamantina" )
            
        CityCode.objects.create(city_code ="3121704",
                                city_name ="Diogo de Vasconcelos" )
            
        CityCode.objects.create(city_code ="3121803",
                                city_name ="Dionísio" )
            
        CityCode.objects.create(city_code ="3121902",
                                city_name ="Divinésia" )
            
        CityCode.objects.create(city_code ="3122009",
                                city_name ="Divino" )
            
        CityCode.objects.create(city_code ="3122108",
                                city_name ="Divino das Laranjeiras" )
            
        CityCode.objects.create(city_code ="3122207",
                                city_name ="Divinolândia de Minas" )
            
        CityCode.objects.create(city_code ="3122306",
                                city_name ="Divinópolis" )
            
        CityCode.objects.create(city_code ="3122355",
                                city_name ="Divisa Alegre" )
            
        CityCode.objects.create(city_code ="3122405",
                                city_name ="Divisa Nova" )
            
        CityCode.objects.create(city_code ="3122454",
                                city_name ="Divisópolis" )
            
        CityCode.objects.create(city_code ="3122470",
                                city_name ="Dom Bosco" )
            
        CityCode.objects.create(city_code ="3122504",
                                city_name ="Dom Cavati" )
            
        CityCode.objects.create(city_code ="3122603",
                                city_name ="Dom Joaquim" )
            
        CityCode.objects.create(city_code ="3122702",
                                city_name ="Dom Silvério" )
            
        CityCode.objects.create(city_code ="3122801",
                                city_name ="Dom Viçoso" )
            
        CityCode.objects.create(city_code ="3122900",
                                city_name ="Dona Euzébia" )
            
        CityCode.objects.create(city_code ="3123007",
                                city_name ="Dores de Campos" )
            
        CityCode.objects.create(city_code ="3123106",
                                city_name ="Dores de Guanhães" )
            
        CityCode.objects.create(city_code ="3123205",
                                city_name ="Dores do Indaiá" )
            
        CityCode.objects.create(city_code ="3123304",
                                city_name ="Dores do Turvo" )
            
        CityCode.objects.create(city_code ="3123403",
                                city_name ="Doresópolis" )
            
        CityCode.objects.create(city_code ="3123502",
                                city_name ="Douradoquara" )
            
        CityCode.objects.create(city_code ="3123528",
                                city_name ="Durandé" )
            
        CityCode.objects.create(city_code ="3123601",
                                city_name ="Elói Mendes" )
            
        CityCode.objects.create(city_code ="3123700",
                                city_name ="Engenheiro Caldas" )
            
        CityCode.objects.create(city_code ="3123809",
                                city_name ="Engenheiro Navarro" )
            
        CityCode.objects.create(city_code ="3123858",
                                city_name ="Entre Folhas" )
            
        CityCode.objects.create(city_code ="3123908",
                                city_name ="Entre Rios de Minas" )
            
        CityCode.objects.create(city_code ="3124005",
                                city_name ="Ervália" )
            
        CityCode.objects.create(city_code ="3124104",
                                city_name ="Esmeraldas" )
            
        CityCode.objects.create(city_code ="3124203",
                                city_name ="Espera Feliz" )
            
        CityCode.objects.create(city_code ="3124302",
                                city_name ="Espinosa" )
            
        CityCode.objects.create(city_code ="3124401",
                                city_name ="Espírito Santo do Dourado" )
            
        CityCode.objects.create(city_code ="3124500",
                                city_name ="Estiva" )
            
        CityCode.objects.create(city_code ="3124609",
                                city_name ="Estrela Dalva" )
            
        CityCode.objects.create(city_code ="3124708",
                                city_name ="Estrela do Indaiá" )
            
        CityCode.objects.create(city_code ="3124807",
                                city_name ="Estrela do Sul" )
            
        CityCode.objects.create(city_code ="3124906",
                                city_name ="Eugenópolis" )
            
        CityCode.objects.create(city_code ="3125002",
                                city_name ="Ewbank da Câmara" )
            
        CityCode.objects.create(city_code ="3125101",
                                city_name ="Extrema" )
            
        CityCode.objects.create(city_code ="3125200",
                                city_name ="Fama" )
            
        CityCode.objects.create(city_code ="3125309",
                                city_name ="Faria Lemos" )
            
        CityCode.objects.create(city_code ="3125408",
                                city_name ="Felício dos Santos" )
            
        CityCode.objects.create(city_code ="3125606",
                                city_name ="Felisburgo" )
            
        CityCode.objects.create(city_code ="3125705",
                                city_name ="Felixlândia" )
            
        CityCode.objects.create(city_code ="3125804",
                                city_name ="Fernandes Tourinho" )
            
        CityCode.objects.create(city_code ="3125903",
                                city_name ="Ferros" )
            
        CityCode.objects.create(city_code ="3125952",
                                city_name ="Fervedouro" )
            
        CityCode.objects.create(city_code ="3126000",
                                city_name ="Florestal" )
            
        CityCode.objects.create(city_code ="3126109",
                                city_name ="Formiga" )
            
        CityCode.objects.create(city_code ="3126208",
                                city_name ="Formoso" )
            
        CityCode.objects.create(city_code ="3126307",
                                city_name ="Fortaleza de Minas" )
            
        CityCode.objects.create(city_code ="3126406",
                                city_name ="Fortuna de Minas" )
            
        CityCode.objects.create(city_code ="3126505",
                                city_name ="Francisco Badaró" )
            
        CityCode.objects.create(city_code ="3126604",
                                city_name ="Francisco Dumont" )
            
        CityCode.objects.create(city_code ="3126703",
                                city_name ="Francisco Sá" )
            
        CityCode.objects.create(city_code ="3126752",
                                city_name ="Franciscópolis" )
            
        CityCode.objects.create(city_code ="3126802",
                                city_name ="Frei Gaspar" )
            
        CityCode.objects.create(city_code ="3126901",
                                city_name ="Frei Inocêncio" )
            
        CityCode.objects.create(city_code ="3126950",
                                city_name ="Frei Lagonegro" )
            
        CityCode.objects.create(city_code ="3127008",
                                city_name ="Fronteira" )
            
        CityCode.objects.create(city_code ="3127057",
                                city_name ="Fronteira dos Vales" )
            
        CityCode.objects.create(city_code ="3127073",
                                city_name ="Fruta de Leite" )
            
        CityCode.objects.create(city_code ="3127107",
                                city_name ="Frutal" )
            
        CityCode.objects.create(city_code ="3127206",
                                city_name ="Funilândia" )
            
        CityCode.objects.create(city_code ="3127305",
                                city_name ="Galiléia" )
            
        CityCode.objects.create(city_code ="3127339",
                                city_name ="Gameleiras" )
            
        CityCode.objects.create(city_code ="3127354",
                                city_name ="Glaucilândia" )
            
        CityCode.objects.create(city_code ="3127370",
                                city_name ="Goiabeira" )
            
        CityCode.objects.create(city_code ="3127388",
                                city_name ="Goianá" )
            
        CityCode.objects.create(city_code ="3127404",
                                city_name ="Gonçalves" )
            
        CityCode.objects.create(city_code ="3127503",
                                city_name ="Gonzaga" )
            
        CityCode.objects.create(city_code ="3127602",
                                city_name ="Gouveia" )
            
        CityCode.objects.create(city_code ="3127701",
                                city_name ="Governador Valadares" )
            
        CityCode.objects.create(city_code ="3127800",
                                city_name ="Grão Mogol" )
            
        CityCode.objects.create(city_code ="3127909",
                                city_name ="Grupiara" )
            
        CityCode.objects.create(city_code ="3128006",
                                city_name ="Guanhães" )
            
        CityCode.objects.create(city_code ="3128105",
                                city_name ="Guapé" )
            
        CityCode.objects.create(city_code ="3128204",
                                city_name ="Guaraciaba" )
            
        CityCode.objects.create(city_code ="3128253",
                                city_name ="Guaraciama" )
            
        CityCode.objects.create(city_code ="3128303",
                                city_name ="Guaranésia" )
            
        CityCode.objects.create(city_code ="3128402",
                                city_name ="Guarani" )
            
        CityCode.objects.create(city_code ="3128501",
                                city_name ="Guarará" )
            
        CityCode.objects.create(city_code ="3128600",
                                city_name ="Guarda-Mor" )
            
        CityCode.objects.create(city_code ="3128709",
                                city_name ="Guaxupé" )
            
        CityCode.objects.create(city_code ="3128808",
                                city_name ="Guidoval" )
            
        CityCode.objects.create(city_code ="3128907",
                                city_name ="Guimarânia" )
            
        CityCode.objects.create(city_code ="3129004",
                                city_name ="Guiricema" )
            
        CityCode.objects.create(city_code ="3129103",
                                city_name ="Gurinhatã" )
            
        CityCode.objects.create(city_code ="3129202",
                                city_name ="Heliodora" )
            
        CityCode.objects.create(city_code ="3129301",
                                city_name ="Iapu" )
            
        CityCode.objects.create(city_code ="3129400",
                                city_name ="Ibertioga" )
            
        CityCode.objects.create(city_code ="3129509",
                                city_name ="Ibiá" )
            
        CityCode.objects.create(city_code ="3129608",
                                city_name ="Ibiaí" )
            
        CityCode.objects.create(city_code ="3129657",
                                city_name ="Ibiracatu" )
            
        CityCode.objects.create(city_code ="3129707",
                                city_name ="Ibiraci" )
            
        CityCode.objects.create(city_code ="3129806",
                                city_name ="Ibirité" )
            
        CityCode.objects.create(city_code ="3129905",
                                city_name ="Ibitiúra de Minas" )
            
        CityCode.objects.create(city_code ="3130002",
                                city_name ="Ibituruna" )
            
        CityCode.objects.create(city_code ="3130051",
                                city_name ="Icaraí de Minas" )
            
        CityCode.objects.create(city_code ="3130101",
                                city_name ="Igarapé" )
            
        CityCode.objects.create(city_code ="3130200",
                                city_name ="Igaratinga" )
            
        CityCode.objects.create(city_code ="3130309",
                                city_name ="Iguatama" )
            
        CityCode.objects.create(city_code ="3130408",
                                city_name ="Ijaci" )
            
        CityCode.objects.create(city_code ="3130507",
                                city_name ="Ilicínea" )
            
        CityCode.objects.create(city_code ="3130556",
                                city_name ="Imbé de Minas" )
            
        CityCode.objects.create(city_code ="3130606",
                                city_name ="Inconfidentes" )
            
        CityCode.objects.create(city_code ="3130655",
                                city_name ="Indaiabira" )
            
        CityCode.objects.create(city_code ="3130705",
                                city_name ="Indianópolis" )
            
        CityCode.objects.create(city_code ="3130804",
                                city_name ="Ingaí" )
            
        CityCode.objects.create(city_code ="3130903",
                                city_name ="Inhapim" )
            
        CityCode.objects.create(city_code ="3131000",
                                city_name ="Inhaúma" )
            
        CityCode.objects.create(city_code ="3131109",
                                city_name ="Inimutaba" )
            
        CityCode.objects.create(city_code ="3131158",
                                city_name ="Ipaba" )
            
        CityCode.objects.create(city_code ="3131208",
                                city_name ="Ipanema" )
            
        CityCode.objects.create(city_code ="3131307",
                                city_name ="Ipatinga" )
            
        CityCode.objects.create(city_code ="3131406",
                                city_name ="Ipiaçu" )
            
        CityCode.objects.create(city_code ="3131505",
                                city_name ="Ipuiúna" )
            
        CityCode.objects.create(city_code ="3131604",
                                city_name ="Iraí de Minas" )
            
        CityCode.objects.create(city_code ="3131703",
                                city_name ="Itabira" )
            
        CityCode.objects.create(city_code ="3131802",
                                city_name ="Itabirinha" )
            
        CityCode.objects.create(city_code ="3131901",
                                city_name ="Itabirito" )
            
        CityCode.objects.create(city_code ="3132008",
                                city_name ="Itacambira" )
            
        CityCode.objects.create(city_code ="3132107",
                                city_name ="Itacarambi" )
            
        CityCode.objects.create(city_code ="3132206",
                                city_name ="Itaguara" )
            
        CityCode.objects.create(city_code ="3132305",
                                city_name ="Itaipé" )
            
        CityCode.objects.create(city_code ="3132404",
                                city_name ="Itajubá" )
            
        CityCode.objects.create(city_code ="3132503",
                                city_name ="Itamarandiba" )
            
        CityCode.objects.create(city_code ="3132602",
                                city_name ="Itamarati de Minas" )
            
        CityCode.objects.create(city_code ="3132701",
                                city_name ="Itambacuri" )
            
        CityCode.objects.create(city_code ="3132800",
                                city_name ="Itambé do Mato Dentro" )
            
        CityCode.objects.create(city_code ="3132909",
                                city_name ="Itamogi" )
            
        CityCode.objects.create(city_code ="3133006",
                                city_name ="Itamonte" )
            
        CityCode.objects.create(city_code ="3133105",
                                city_name ="Itanhandu" )
            
        CityCode.objects.create(city_code ="3133204",
                                city_name ="Itanhomi" )
            
        CityCode.objects.create(city_code ="3133303",
                                city_name ="Itaobim" )
            
        CityCode.objects.create(city_code ="3133402",
                                city_name ="Itapagipe" )
            
        CityCode.objects.create(city_code ="3133501",
                                city_name ="Itapecerica" )
            
        CityCode.objects.create(city_code ="3133600",
                                city_name ="Itapeva" )
            
        CityCode.objects.create(city_code ="3133709",
                                city_name ="Itatiaiuçu" )
            
        CityCode.objects.create(city_code ="3133758",
                                city_name ="Itaú de Minas" )
            
        CityCode.objects.create(city_code ="3133808",
                                city_name ="Itaúna" )
            
        CityCode.objects.create(city_code ="3133907",
                                city_name ="Itaverava" )
            
        CityCode.objects.create(city_code ="3134004",
                                city_name ="Itinga" )
            
        CityCode.objects.create(city_code ="3134103",
                                city_name ="Itueta" )
            
        CityCode.objects.create(city_code ="3134202",
                                city_name ="Ituiutaba" )
            
        CityCode.objects.create(city_code ="3134301",
                                city_name ="Itumirim" )
            
        CityCode.objects.create(city_code ="3134400",
                                city_name ="Iturama" )
            
        CityCode.objects.create(city_code ="3134509",
                                city_name ="Itutinga" )
            
        CityCode.objects.create(city_code ="3134608",
                                city_name ="Jaboticatubas" )
            
        CityCode.objects.create(city_code ="3134707",
                                city_name ="Jacinto" )
            
        CityCode.objects.create(city_code ="3134806",
                                city_name ="Jacuí" )
            
        CityCode.objects.create(city_code ="3134905",
                                city_name ="Jacutinga" )
            
        CityCode.objects.create(city_code ="3135001",
                                city_name ="Jaguaraçu" )
            
        CityCode.objects.create(city_code ="3135050",
                                city_name ="Jaíba" )
            
        CityCode.objects.create(city_code ="3135076",
                                city_name ="Jampruca" )
            
        CityCode.objects.create(city_code ="3135100",
                                city_name ="Janaúba" )
            
        CityCode.objects.create(city_code ="3135209",
                                city_name ="Januária" )
            
        CityCode.objects.create(city_code ="3135308",
                                city_name ="Japaraíba" )
            
        CityCode.objects.create(city_code ="3135357",
                                city_name ="Japonvar" )
            
        CityCode.objects.create(city_code ="3135407",
                                city_name ="Jeceaba" )
            
        CityCode.objects.create(city_code ="3135456",
                                city_name ="Jenipapo de Minas" )
            
        CityCode.objects.create(city_code ="3135506",
                                city_name ="Jequeri" )
            
        CityCode.objects.create(city_code ="3135605",
                                city_name ="Jequitaí" )
            
        CityCode.objects.create(city_code ="3135704",
                                city_name ="Jequitibá" )
            
        CityCode.objects.create(city_code ="3135803",
                                city_name ="Jequitinhonha" )
            
        CityCode.objects.create(city_code ="3135902",
                                city_name ="Jesuânia" )
            
        CityCode.objects.create(city_code ="3136009",
                                city_name ="Joaíma" )
            
        CityCode.objects.create(city_code ="3136108",
                                city_name ="Joanésia" )
            
        CityCode.objects.create(city_code ="3136207",
                                city_name ="João Monlevade" )
            
        CityCode.objects.create(city_code ="3136306",
                                city_name ="João Pinheiro" )
            
        CityCode.objects.create(city_code ="3136405",
                                city_name ="Joaquim Felício" )
            
        CityCode.objects.create(city_code ="3136504",
                                city_name ="Jordânia" )
            
        CityCode.objects.create(city_code ="3136520",
                                city_name ="José Gonçalves de Minas" )
            
        CityCode.objects.create(city_code ="3136553",
                                city_name ="José Raydan" )
            
        CityCode.objects.create(city_code ="3136579",
                                city_name ="Josenópolis" )
            
        CityCode.objects.create(city_code ="3136652",
                                city_name ="Juatuba" )
            
        CityCode.objects.create(city_code ="3136702",
                                city_name ="Juiz de Fora" )
            
        CityCode.objects.create(city_code ="3136801",
                                city_name ="Juramento" )
            
        CityCode.objects.create(city_code ="3136900",
                                city_name ="Juruaia" )
            
        CityCode.objects.create(city_code ="3136959",
                                city_name ="Juvenília" )
            
        CityCode.objects.create(city_code ="3137007",
                                city_name ="Ladainha" )
            
        CityCode.objects.create(city_code ="3137106",
                                city_name ="Lagamar" )
            
        CityCode.objects.create(city_code ="3137205",
                                city_name ="Lagoa da Prata" )
            
        CityCode.objects.create(city_code ="3137304",
                                city_name ="Lagoa dos Patos" )
            
        CityCode.objects.create(city_code ="3137403",
                                city_name ="Lagoa Dourada" )
            
        CityCode.objects.create(city_code ="3137502",
                                city_name ="Lagoa Formosa" )
            
        CityCode.objects.create(city_code ="3137536",
                                city_name ="Lagoa Grande" )
            
        CityCode.objects.create(city_code ="3137601",
                                city_name ="Lagoa Santa" )
            
        CityCode.objects.create(city_code ="3137700",
                                city_name ="Lajinha" )
            
        CityCode.objects.create(city_code ="3137809",
                                city_name ="Lambari" )
            
        CityCode.objects.create(city_code ="3137908",
                                city_name ="Lamim" )
            
        CityCode.objects.create(city_code ="3138005",
                                city_name ="Laranjal" )
            
        CityCode.objects.create(city_code ="3138104",
                                city_name ="Lassance" )
            
        CityCode.objects.create(city_code ="3138203",
                                city_name ="Lavras" )
            
        CityCode.objects.create(city_code ="3138302",
                                city_name ="Leandro Ferreira" )
            
        CityCode.objects.create(city_code ="3138351",
                                city_name ="Leme do Prado" )
            
        CityCode.objects.create(city_code ="3138401",
                                city_name ="Leopoldina" )
            
        CityCode.objects.create(city_code ="3138500",
                                city_name ="Liberdade" )
            
        CityCode.objects.create(city_code ="3138609",
                                city_name ="Lima Duarte" )
            
        CityCode.objects.create(city_code ="3138625",
                                city_name ="Limeira do Oeste" )
            
        CityCode.objects.create(city_code ="3138658",
                                city_name ="Lontra" )
            
        CityCode.objects.create(city_code ="3138674",
                                city_name ="Luisburgo" )
            
        CityCode.objects.create(city_code ="3138682",
                                city_name ="Luislândia" )
            
        CityCode.objects.create(city_code ="3138708",
                                city_name ="Luminárias" )
            
        CityCode.objects.create(city_code ="3138807",
                                city_name ="Luz" )
            
        CityCode.objects.create(city_code ="3138906",
                                city_name ="Machacalis" )
            
        CityCode.objects.create(city_code ="3139003",
                                city_name ="Machado" )
            
        CityCode.objects.create(city_code ="3139102",
                                city_name ="Madre de Deus de Minas" )
            
        CityCode.objects.create(city_code ="3139201",
                                city_name ="Malacacheta" )
            
        CityCode.objects.create(city_code ="3139250",
                                city_name ="Mamonas" )
            
        CityCode.objects.create(city_code ="3139300",
                                city_name ="Manga" )
            
        CityCode.objects.create(city_code ="3139409",
                                city_name ="Manhuaçu" )
            
        CityCode.objects.create(city_code ="3139508",
                                city_name ="Manhumirim" )
            
        CityCode.objects.create(city_code ="3139607",
                                city_name ="Mantena" )
            
        CityCode.objects.create(city_code ="3139805",
                                city_name ="Mar de Espanha" )
            
        CityCode.objects.create(city_code ="3139706",
                                city_name ="Maravilhas" )
            
        CityCode.objects.create(city_code ="3139904",
                                city_name ="Maria da Fé" )
            
        CityCode.objects.create(city_code ="3140001",
                                city_name ="Mariana" )
            
        CityCode.objects.create(city_code ="3140100",
                                city_name ="Marilac" )
            
        CityCode.objects.create(city_code ="3140159",
                                city_name ="Mário Campos" )
            
        CityCode.objects.create(city_code ="3140209",
                                city_name ="Maripá de Minas" )
            
        CityCode.objects.create(city_code ="3140308",
                                city_name ="Marliéria" )
            
        CityCode.objects.create(city_code ="3140407",
                                city_name ="Marmelópolis" )
            
        CityCode.objects.create(city_code ="3140506",
                                city_name ="Martinho Campos" )
            
        CityCode.objects.create(city_code ="3140530",
                                city_name ="Martins Soares" )
            
        CityCode.objects.create(city_code ="3140555",
                                city_name ="Mata Verde" )
            
        CityCode.objects.create(city_code ="3140605",
                                city_name ="Materlândia" )
            
        CityCode.objects.create(city_code ="3140704",
                                city_name ="Mateus Leme" )
            
        CityCode.objects.create(city_code ="3171501",
                                city_name ="Mathias Lobato" )
            
        CityCode.objects.create(city_code ="3140803",
                                city_name ="Matias Barbosa" )
            
        CityCode.objects.create(city_code ="3140852",
                                city_name ="Matias Cardoso" )
            
        CityCode.objects.create(city_code ="3140902",
                                city_name ="Matipó" )
            
        CityCode.objects.create(city_code ="3141009",
                                city_name ="Mato Verde" )
            
        CityCode.objects.create(city_code ="3141108",
                                city_name ="Matozinhos" )
            
        CityCode.objects.create(city_code ="3141207",
                                city_name ="Matutina" )
            
        CityCode.objects.create(city_code ="3141306",
                                city_name ="Medeiros" )
            
        CityCode.objects.create(city_code ="3141405",
                                city_name ="Medina" )
            
        CityCode.objects.create(city_code ="3141504",
                                city_name ="Mendes Pimentel" )
            
        CityCode.objects.create(city_code ="3141603",
                                city_name ="Mercês" )
            
        CityCode.objects.create(city_code ="3141702",
                                city_name ="Mesquita" )
            
        CityCode.objects.create(city_code ="3141801",
                                city_name ="Minas Novas" )
            
        CityCode.objects.create(city_code ="3141900",
                                city_name ="Minduri" )
            
        CityCode.objects.create(city_code ="3142007",
                                city_name ="Mirabela" )
            
        CityCode.objects.create(city_code ="3142106",
                                city_name ="Miradouro" )
            
        CityCode.objects.create(city_code ="3142205",
                                city_name ="Miraí" )
            
        CityCode.objects.create(city_code ="3142254",
                                city_name ="Miravânia" )
            
        CityCode.objects.create(city_code ="3142304",
                                city_name ="Moeda" )
            
        CityCode.objects.create(city_code ="3142403",
                                city_name ="Moema" )
            
        CityCode.objects.create(city_code ="3142502",
                                city_name ="Monjolos" )
            
        CityCode.objects.create(city_code ="3142601",
                                city_name ="Monsenhor Paulo" )
            
        CityCode.objects.create(city_code ="3142700",
                                city_name ="Montalvânia" )
            
        CityCode.objects.create(city_code ="3142809",
                                city_name ="Monte Alegre de Minas" )
            
        CityCode.objects.create(city_code ="3142908",
                                city_name ="Monte Azul" )
            
        CityCode.objects.create(city_code ="3143005",
                                city_name ="Monte Belo" )
            
        CityCode.objects.create(city_code ="3143104",
                                city_name ="Monte Carmelo" )
            
        CityCode.objects.create(city_code ="3143153",
                                city_name ="Monte Formoso" )
            
        CityCode.objects.create(city_code ="3143203",
                                city_name ="Monte Santo de Minas" )
            
        CityCode.objects.create(city_code ="3143401",
                                city_name ="Monte Sião" )
            
        CityCode.objects.create(city_code ="3143302",
                                city_name ="Montes Claros" )
            
        CityCode.objects.create(city_code ="3143450",
                                city_name ="Montezuma" )
            
        CityCode.objects.create(city_code ="3143500",
                                city_name ="Morada Nova de Minas" )
            
        CityCode.objects.create(city_code ="3143609",
                                city_name ="Morro da Garça" )
            
        CityCode.objects.create(city_code ="3143708",
                                city_name ="Morro do Pilar" )
            
        CityCode.objects.create(city_code ="3143807",
                                city_name ="Munhoz" )
            
        CityCode.objects.create(city_code ="3143906",
                                city_name ="Muriaé" )
            
        CityCode.objects.create(city_code ="3144003",
                                city_name ="Mutum" )
            
        CityCode.objects.create(city_code ="3144102",
                                city_name ="Muzambinho" )
            
        CityCode.objects.create(city_code ="3144201",
                                city_name ="Nacip Raydan" )
            
        CityCode.objects.create(city_code ="3144300",
                                city_name ="Nanuque" )
            
        CityCode.objects.create(city_code ="3144359",
                                city_name ="Naque" )
            
        CityCode.objects.create(city_code ="3144375",
                                city_name ="Natalândia" )
            
        CityCode.objects.create(city_code ="3144409",
                                city_name ="Natércia" )
            
        CityCode.objects.create(city_code ="3144508",
                                city_name ="Nazareno" )
            
        CityCode.objects.create(city_code ="3144607",
                                city_name ="Nepomuceno" )
            
        CityCode.objects.create(city_code ="3144656",
                                city_name ="Ninheira" )
            
        CityCode.objects.create(city_code ="3144672",
                                city_name ="Nova Belém" )
            
        CityCode.objects.create(city_code ="3144706",
                                city_name ="Nova Era" )
            
        CityCode.objects.create(city_code ="3144805",
                                city_name ="Nova Lima" )
            
        CityCode.objects.create(city_code ="3144904",
                                city_name ="Nova Módica" )
            
        CityCode.objects.create(city_code ="3145000",
                                city_name ="Nova Ponte" )
            
        CityCode.objects.create(city_code ="3145059",
                                city_name ="Nova Porteirinha" )
            
        CityCode.objects.create(city_code ="3145109",
                                city_name ="Nova Resende" )
            
        CityCode.objects.create(city_code ="3145208",
                                city_name ="Nova Serrana" )
            
        CityCode.objects.create(city_code ="3136603",
                                city_name ="Nova União" )
            
        CityCode.objects.create(city_code ="3145307",
                                city_name ="Novo Cruzeiro" )
            
        CityCode.objects.create(city_code ="3145356",
                                city_name ="Novo Oriente de Minas" )
            
        CityCode.objects.create(city_code ="3145372",
                                city_name ="Novorizonte" )
            
        CityCode.objects.create(city_code ="3145406",
                                city_name ="Olaria" )
            
        CityCode.objects.create(city_code ="3145455",
                                city_name ="Olhos-d'Água" )
            
        CityCode.objects.create(city_code ="3145505",
                                city_name ="Olímpio Noronha" )
            
        CityCode.objects.create(city_code ="3145604",
                                city_name ="Oliveira" )
            
        CityCode.objects.create(city_code ="3145703",
                                city_name ="Oliveira Fortes" )
            
        CityCode.objects.create(city_code ="3145802",
                                city_name ="Onça de Pitangui" )
            
        CityCode.objects.create(city_code ="3145851",
                                city_name ="Oratórios" )
            
        CityCode.objects.create(city_code ="3145877",
                                city_name ="Orizânia" )
            
        CityCode.objects.create(city_code ="3145901",
                                city_name ="Ouro Branco" )
            
        CityCode.objects.create(city_code ="3146008",
                                city_name ="Ouro Fino" )
            
        CityCode.objects.create(city_code ="3146107",
                                city_name ="Ouro Preto" )
            
        CityCode.objects.create(city_code ="3146206",
                                city_name ="Ouro Verde de Minas" )
            
        CityCode.objects.create(city_code ="3146255",
                                city_name ="Padre Carvalho" )
            
        CityCode.objects.create(city_code ="3146305",
                                city_name ="Padre Paraíso" )
            
        CityCode.objects.create(city_code ="3146552",
                                city_name ="Pai Pedro" )
            
        CityCode.objects.create(city_code ="3146404",
                                city_name ="Paineiras" )
            
        CityCode.objects.create(city_code ="3146503",
                                city_name ="Pains" )
            
        CityCode.objects.create(city_code ="3146602",
                                city_name ="Paiva" )
            
        CityCode.objects.create(city_code ="3146701",
                                city_name ="Palma" )
            
        CityCode.objects.create(city_code ="3146750",
                                city_name ="Palmópolis" )
            
        CityCode.objects.create(city_code ="3146909",
                                city_name ="Papagaios" )
            
        CityCode.objects.create(city_code ="3147105",
                                city_name ="Pará de Minas" )
            
        CityCode.objects.create(city_code ="3147006",
                                city_name ="Paracatu" )
            
        CityCode.objects.create(city_code ="3147204",
                                city_name ="Paraguaçu" )
            
        CityCode.objects.create(city_code ="3147303",
                                city_name ="Paraisópolis" )
            
        CityCode.objects.create(city_code ="3147402",
                                city_name ="Paraopeba" )
            
        CityCode.objects.create(city_code ="3147600",
                                city_name ="Passa Quatro" )
            
        CityCode.objects.create(city_code ="3147709",
                                city_name ="Passa Tempo" )
            
        CityCode.objects.create(city_code ="3147808",
                                city_name ="Passa Vinte" )
            
        CityCode.objects.create(city_code ="3147501",
                                city_name ="Passabém" )
            
        CityCode.objects.create(city_code ="3147907",
                                city_name ="Passos" )
            
        CityCode.objects.create(city_code ="3147956",
                                city_name ="Patis" )
            
        CityCode.objects.create(city_code ="3148004",
                                city_name ="Patos de Minas" )
            
        CityCode.objects.create(city_code ="3148103",
                                city_name ="Patrocínio" )
            
        CityCode.objects.create(city_code ="3148202",
                                city_name ="Patrocínio do Muriaé" )
            
        CityCode.objects.create(city_code ="3148301",
                                city_name ="Paula Cândido" )
            
        CityCode.objects.create(city_code ="3148400",
                                city_name ="Paulistas" )
            
        CityCode.objects.create(city_code ="3148509",
                                city_name ="Pavão" )
            
        CityCode.objects.create(city_code ="3148608",
                                city_name ="Peçanha" )
            
        CityCode.objects.create(city_code ="3148707",
                                city_name ="Pedra Azul" )
            
        CityCode.objects.create(city_code ="3148756",
                                city_name ="Pedra Bonita" )
            
        CityCode.objects.create(city_code ="3148806",
                                city_name ="Pedra do Anta" )
            
        CityCode.objects.create(city_code ="3148905",
                                city_name ="Pedra do Indaiá" )
            
        CityCode.objects.create(city_code ="3149002",
                                city_name ="Pedra Dourada" )
            
        CityCode.objects.create(city_code ="3149101",
                                city_name ="Pedralva" )
            
        CityCode.objects.create(city_code ="3149150",
                                city_name ="Pedras de Maria da Cruz" )
            
        CityCode.objects.create(city_code ="3149200",
                                city_name ="Pedrinópolis" )
            
        CityCode.objects.create(city_code ="3149309",
                                city_name ="Pedro Leopoldo" )
            
        CityCode.objects.create(city_code ="3149408",
                                city_name ="Pedro Teixeira" )
            
        CityCode.objects.create(city_code ="3149507",
                                city_name ="Pequeri" )
            
        CityCode.objects.create(city_code ="3149606",
                                city_name ="Pequi" )
            
        CityCode.objects.create(city_code ="3149705",
                                city_name ="Perdigão" )
            
        CityCode.objects.create(city_code ="3149804",
                                city_name ="Perdizes" )
            
        CityCode.objects.create(city_code ="3149903",
                                city_name ="Perdões" )
            
        CityCode.objects.create(city_code ="3149952",
                                city_name ="Periquito" )
            
        CityCode.objects.create(city_code ="3150000",
                                city_name ="Pescador" )
            
        CityCode.objects.create(city_code ="3150109",
                                city_name ="Piau" )
            
        CityCode.objects.create(city_code ="3150158",
                                city_name ="Piedade de Caratinga" )
            
        CityCode.objects.create(city_code ="3150208",
                                city_name ="Piedade de Ponte Nova" )
            
        CityCode.objects.create(city_code ="3150307",
                                city_name ="Piedade do Rio Grande" )
            
        CityCode.objects.create(city_code ="3150406",
                                city_name ="Piedade dos Gerais" )
            
        CityCode.objects.create(city_code ="3150505",
                                city_name ="Pimenta" )
            
        CityCode.objects.create(city_code ="3150539",
                                city_name ="Pingo-d'Água" )
            
        CityCode.objects.create(city_code ="3150570",
                                city_name ="Pintópolis" )
            
        CityCode.objects.create(city_code ="3150604",
                                city_name ="Piracema" )
            
        CityCode.objects.create(city_code ="3150703",
                                city_name ="Pirajuba" )
            
        CityCode.objects.create(city_code ="3150802",
                                city_name ="Piranga" )
            
        CityCode.objects.create(city_code ="3150901",
                                city_name ="Piranguçu" )
            
        CityCode.objects.create(city_code ="3151008",
                                city_name ="Piranguinho" )
            
        CityCode.objects.create(city_code ="3151107",
                                city_name ="Pirapetinga" )
            
        CityCode.objects.create(city_code ="3151206",
                                city_name ="Pirapora" )
            
        CityCode.objects.create(city_code ="3151305",
                                city_name ="Piraúba" )
            
        CityCode.objects.create(city_code ="3151404",
                                city_name ="Pitangui" )
            
        CityCode.objects.create(city_code ="3151503",
                                city_name ="Piumhi" )
            
        CityCode.objects.create(city_code ="3151602",
                                city_name ="Planura" )
            
        CityCode.objects.create(city_code ="3151701",
                                city_name ="Poço Fundo" )
            
        CityCode.objects.create(city_code ="3151800",
                                city_name ="Poços de Caldas" )
            
        CityCode.objects.create(city_code ="3151909",
                                city_name ="Pocrane" )
            
        CityCode.objects.create(city_code ="3152006",
                                city_name ="Pompéu" )
            
        CityCode.objects.create(city_code ="3152105",
                                city_name ="Ponte Nova" )
            
        CityCode.objects.create(city_code ="3152131",
                                city_name ="Ponto Chique" )
            
        CityCode.objects.create(city_code ="3152170",
                                city_name ="Ponto dos Volantes" )
            
        CityCode.objects.create(city_code ="3152204",
                                city_name ="Porteirinha" )
            
        CityCode.objects.create(city_code ="3152303",
                                city_name ="Porto Firme" )
            
        CityCode.objects.create(city_code ="3152402",
                                city_name ="Poté" )
            
        CityCode.objects.create(city_code ="3152501",
                                city_name ="Pouso Alegre" )
            
        CityCode.objects.create(city_code ="3152600",
                                city_name ="Pouso Alto" )
            
        CityCode.objects.create(city_code ="3152709",
                                city_name ="Prados" )
            
        CityCode.objects.create(city_code ="3152808",
                                city_name ="Prata" )
            
        CityCode.objects.create(city_code ="3152907",
                                city_name ="Pratápolis" )
            
        CityCode.objects.create(city_code ="3153004",
                                city_name ="Pratinha" )
            
        CityCode.objects.create(city_code ="3153103",
                                city_name ="Presidente Bernardes" )
            
        CityCode.objects.create(city_code ="3153202",
                                city_name ="Presidente Juscelino" )
            
        CityCode.objects.create(city_code ="3153301",
                                city_name ="Presidente Kubitschek" )
            
        CityCode.objects.create(city_code ="3153400",
                                city_name ="Presidente Olegário" )
            
        CityCode.objects.create(city_code ="3153608",
                                city_name ="Prudente de Morais" )
            
        CityCode.objects.create(city_code ="3153707",
                                city_name ="Quartel Geral" )
            
        CityCode.objects.create(city_code ="3153806",
                                city_name ="Queluzito" )
            
        CityCode.objects.create(city_code ="3153905",
                                city_name ="Raposos" )
            
        CityCode.objects.create(city_code ="3154002",
                                city_name ="Raul Soares" )
            
        CityCode.objects.create(city_code ="3154101",
                                city_name ="Recreio" )
            
        CityCode.objects.create(city_code ="3154150",
                                city_name ="Reduto" )
            
        CityCode.objects.create(city_code ="3154200",
                                city_name ="Resende Costa" )
            
        CityCode.objects.create(city_code ="3154309",
                                city_name ="Resplendor" )
            
        CityCode.objects.create(city_code ="3154408",
                                city_name ="Ressaquinha" )
            
        CityCode.objects.create(city_code ="3154457",
                                city_name ="Riachinho" )
            
        CityCode.objects.create(city_code ="3154507",
                                city_name ="Riacho dos Machados" )
            
        CityCode.objects.create(city_code ="3154606",
                                city_name ="Ribeirão das Neves" )
            
        CityCode.objects.create(city_code ="3154705",
                                city_name ="Ribeirão Vermelho" )
            
        CityCode.objects.create(city_code ="3154804",
                                city_name ="Rio Acima" )
            
        CityCode.objects.create(city_code ="3154903",
                                city_name ="Rio Casca" )
            
        CityCode.objects.create(city_code ="3155108",
                                city_name ="Rio do Prado" )
            
        CityCode.objects.create(city_code ="3155009",
                                city_name ="Rio Doce" )
            
        CityCode.objects.create(city_code ="3155207",
                                city_name ="Rio Espera" )
            
        CityCode.objects.create(city_code ="3155306",
                                city_name ="Rio Manso" )
            
        CityCode.objects.create(city_code ="3155405",
                                city_name ="Rio Novo" )
            
        CityCode.objects.create(city_code ="3155504",
                                city_name ="Rio Paranaíba" )
            
        CityCode.objects.create(city_code ="3155603",
                                city_name ="Rio Pardo de Minas" )
            
        CityCode.objects.create(city_code ="3155702",
                                city_name ="Rio Piracicaba" )
            
        CityCode.objects.create(city_code ="3155801",
                                city_name ="Rio Pomba" )
            
        CityCode.objects.create(city_code ="3155900",
                                city_name ="Rio Preto" )
            
        CityCode.objects.create(city_code ="3156007",
                                city_name ="Rio Vermelho" )
            
        CityCode.objects.create(city_code ="3156106",
                                city_name ="Ritápolis" )
            
        CityCode.objects.create(city_code ="3156205",
                                city_name ="Rochedo de Minas" )
            
        CityCode.objects.create(city_code ="3156304",
                                city_name ="Rodeiro" )
            
        CityCode.objects.create(city_code ="3156403",
                                city_name ="Romaria" )
            
        CityCode.objects.create(city_code ="3156452",
                                city_name ="Rosário da Limeira" )
            
        CityCode.objects.create(city_code ="3156502",
                                city_name ="Rubelita" )
            
        CityCode.objects.create(city_code ="3156601",
                                city_name ="Rubim" )
            
        CityCode.objects.create(city_code ="3156700",
                                city_name ="Sabará" )
            
        CityCode.objects.create(city_code ="3156809",
                                city_name ="Sabinópolis" )
            
        CityCode.objects.create(city_code ="3156908",
                                city_name ="Sacramento" )
            
        CityCode.objects.create(city_code ="3157005",
                                city_name ="Salinas" )
            
        CityCode.objects.create(city_code ="3157104",
                                city_name ="Salto da Divisa" )
            
        CityCode.objects.create(city_code ="3157203",
                                city_name ="Santa Bárbara" )
            
        CityCode.objects.create(city_code ="3157252",
                                city_name ="Santa Bárbara do Leste" )
            
        CityCode.objects.create(city_code ="3157278",
                                city_name ="Santa Bárbara do Monte Verde" )
            
        CityCode.objects.create(city_code ="3157302",
                                city_name ="Santa Bárbara do Tugúrio" )
            
        CityCode.objects.create(city_code ="3157336",
                                city_name ="Santa Cruz de Minas" )
            
        CityCode.objects.create(city_code ="3157377",
                                city_name ="Santa Cruz de Salinas" )
            
        CityCode.objects.create(city_code ="3157401",
                                city_name ="Santa Cruz do Escalvado" )
            
        CityCode.objects.create(city_code ="3157500",
                                city_name ="Santa Efigênia de Minas" )
            
        CityCode.objects.create(city_code ="3157609",
                                city_name ="Santa Fé de Minas" )
            
        CityCode.objects.create(city_code ="3157658",
                                city_name ="Santa Helena de Minas" )
            
        CityCode.objects.create(city_code ="3157708",
                                city_name ="Santa Juliana" )
            
        CityCode.objects.create(city_code ="3157807",
                                city_name ="Santa Luzia" )
            
        CityCode.objects.create(city_code ="3157906",
                                city_name ="Santa Margarida" )
            
        CityCode.objects.create(city_code ="3158003",
                                city_name ="Santa Maria de Itabira" )
            
        CityCode.objects.create(city_code ="3158102",
                                city_name ="Santa Maria do Salto" )
            
        CityCode.objects.create(city_code ="3158201",
                                city_name ="Santa Maria do Suaçuí" )
            
        CityCode.objects.create(city_code ="3159209",
                                city_name ="Santa Rita de Caldas" )
            
        CityCode.objects.create(city_code ="3159407",
                                city_name ="Santa Rita de Ibitipoca" )
            
        CityCode.objects.create(city_code ="3159308",
                                city_name ="Santa Rita de Jacutinga" )
            
        CityCode.objects.create(city_code ="3159357",
                                city_name ="Santa Rita de Minas" )
            
        CityCode.objects.create(city_code ="3159506",
                                city_name ="Santa Rita do Itueto" )
            
        CityCode.objects.create(city_code ="3159605",
                                city_name ="Santa Rita do Sapucaí" )
            
        CityCode.objects.create(city_code ="3159704",
                                city_name ="Santa Rosa da Serra" )
            
        CityCode.objects.create(city_code ="3159803",
                                city_name ="Santa Vitória" )
            
        CityCode.objects.create(city_code ="3158300",
                                city_name ="Santana da Vargem" )
            
        CityCode.objects.create(city_code ="3158409",
                                city_name ="Santana de Cataguases" )
            
        CityCode.objects.create(city_code ="3158508",
                                city_name ="Santana de Pirapama" )
            
        CityCode.objects.create(city_code ="3158607",
                                city_name ="Santana do Deserto" )
            
        CityCode.objects.create(city_code ="3158706",
                                city_name ="Santana do Garambéu" )
            
        CityCode.objects.create(city_code ="3158805",
                                city_name ="Santana do Jacaré" )
            
        CityCode.objects.create(city_code ="3158904",
                                city_name ="Santana do Manhuaçu" )
            
        CityCode.objects.create(city_code ="3158953",
                                city_name ="Santana do Paraíso" )
            
        CityCode.objects.create(city_code ="3159001",
                                city_name ="Santana do Riacho" )
            
        CityCode.objects.create(city_code ="3159100",
                                city_name ="Santana dos Montes" )
            
        CityCode.objects.create(city_code ="3159902",
                                city_name ="Santo Antônio do Amparo" )
            
        CityCode.objects.create(city_code ="3160009",
                                city_name ="Santo Antônio do Aventureiro" )
            
        CityCode.objects.create(city_code ="3160108",
                                city_name ="Santo Antônio do Grama" )
            
        CityCode.objects.create(city_code ="3160207",
                                city_name ="Santo Antônio do Itambé" )
            
        CityCode.objects.create(city_code ="3160306",
                                city_name ="Santo Antônio do Jacinto" )
            
        CityCode.objects.create(city_code ="3160405",
                                city_name ="Santo Antônio do Monte" )
            
        CityCode.objects.create(city_code ="3160454",
                                city_name ="Santo Antônio do Retiro" )
            
        CityCode.objects.create(city_code ="3160504",
                                city_name ="Santo Antônio do Rio Abaixo" )
            
        CityCode.objects.create(city_code ="3160603",
                                city_name ="Santo Hipólito" )
            
        CityCode.objects.create(city_code ="3160702",
                                city_name ="Santos Dumont" )
            
        CityCode.objects.create(city_code ="3160801",
                                city_name ="São Bento Abade" )
            
        CityCode.objects.create(city_code ="3160900",
                                city_name ="São Brás do Suaçuí" )
            
        CityCode.objects.create(city_code ="3160959",
                                city_name ="São Domingos das Dores" )
            
        CityCode.objects.create(city_code ="3161007",
                                city_name ="São Domingos do Prata" )
            
        CityCode.objects.create(city_code ="3161056",
                                city_name ="São Félix de Minas" )
            
        CityCode.objects.create(city_code ="3161106",
                                city_name ="São Francisco" )
            
        CityCode.objects.create(city_code ="3161205",
                                city_name ="São Francisco de Paula" )
            
        CityCode.objects.create(city_code ="3161304",
                                city_name ="São Francisco de Sales" )
            
        CityCode.objects.create(city_code ="3161403",
                                city_name ="São Francisco do Glória" )
            
        CityCode.objects.create(city_code ="3161502",
                                city_name ="São Geraldo" )
            
        CityCode.objects.create(city_code ="3161601",
                                city_name ="São Geraldo da Piedade" )
            
        CityCode.objects.create(city_code ="3161650",
                                city_name ="São Geraldo do Baixio" )
            
        CityCode.objects.create(city_code ="3161700",
                                city_name ="São Gonçalo do Abaeté" )
            
        CityCode.objects.create(city_code ="3161809",
                                city_name ="São Gonçalo do Pará" )
            
        CityCode.objects.create(city_code ="3161908",
                                city_name ="São Gonçalo do Rio Abaixo" )
            
        CityCode.objects.create(city_code ="3125507",
                                city_name ="São Gonçalo do Rio Preto" )
            
        CityCode.objects.create(city_code ="3162005",
                                city_name ="São Gonçalo do Sapucaí" )
            
        CityCode.objects.create(city_code ="3162104",
                                city_name ="São Gotardo" )
            
        CityCode.objects.create(city_code ="3162203",
                                city_name ="São João Batista do Glória" )
            
        CityCode.objects.create(city_code ="3162252",
                                city_name ="São João da Lagoa" )
            
        CityCode.objects.create(city_code ="3162302",
                                city_name ="São João da Mata" )
            
        CityCode.objects.create(city_code ="3162401",
                                city_name ="São João da Ponte" )
            
        CityCode.objects.create(city_code ="3162450",
                                city_name ="São João das Missões" )
            
        CityCode.objects.create(city_code ="3162500",
                                city_name ="São João del Rei" )
            
        CityCode.objects.create(city_code ="3162559",
                                city_name ="São João do Manhuaçu" )
            
        CityCode.objects.create(city_code ="3162575",
                                city_name ="São João do Manteninha" )
            
        CityCode.objects.create(city_code ="3162609",
                                city_name ="São João do Oriente" )
            
        CityCode.objects.create(city_code ="3162658",
                                city_name ="São João do Pacuí" )
            
        CityCode.objects.create(city_code ="3162708",
                                city_name ="São João do Paraíso" )
            
        CityCode.objects.create(city_code ="3162807",
                                city_name ="São João Evangelista" )
            
        CityCode.objects.create(city_code ="3162906",
                                city_name ="São João Nepomuceno" )
            
        CityCode.objects.create(city_code ="3162922",
                                city_name ="São Joaquim de Bicas" )
            
        CityCode.objects.create(city_code ="3162948",
                                city_name ="São José da Barra" )
            
        CityCode.objects.create(city_code ="3162955",
                                city_name ="São José da Lapa" )
            
        CityCode.objects.create(city_code ="3163003",
                                city_name ="São José da Safira" )
            
        CityCode.objects.create(city_code ="3163102",
                                city_name ="São José da Varginha" )
            
        CityCode.objects.create(city_code ="3163201",
                                city_name ="São José do Alegre" )
            
        CityCode.objects.create(city_code ="3163300",
                                city_name ="São José do Divino" )
            
        CityCode.objects.create(city_code ="3163409",
                                city_name ="São José do Goiabal" )
            
        CityCode.objects.create(city_code ="3163508",
                                city_name ="São José do Jacuri" )
            
        CityCode.objects.create(city_code ="3163607",
                                city_name ="São José do Mantimento" )
            
        CityCode.objects.create(city_code ="3163706",
                                city_name ="São Lourenço" )
            
        CityCode.objects.create(city_code ="3163805",
                                city_name ="São Miguel do Anta" )
            
        CityCode.objects.create(city_code ="3163904",
                                city_name ="São Pedro da União" )
            
        CityCode.objects.create(city_code ="3164100",
                                city_name ="São Pedro do Suaçuí" )
            
        CityCode.objects.create(city_code ="3164001",
                                city_name ="São Pedro dos Ferros" )
            
        CityCode.objects.create(city_code ="3164209",
                                city_name ="São Romão" )
            
        CityCode.objects.create(city_code ="3164308",
                                city_name ="São Roque de Minas" )
            
        CityCode.objects.create(city_code ="3164407",
                                city_name ="São Sebastião da Bela Vista" )
            
        CityCode.objects.create(city_code ="3164431",
                                city_name ="São Sebastião da Vargem Alegre" )
            
        CityCode.objects.create(city_code ="3164472",
                                city_name ="São Sebastião do Anta" )
            
        CityCode.objects.create(city_code ="3164506",
                                city_name ="São Sebastião do Maranhão" )
            
        CityCode.objects.create(city_code ="3164605",
                                city_name ="São Sebastião do Oeste" )
            
        CityCode.objects.create(city_code ="3164704",
                                city_name ="São Sebastião do Paraíso" )
            
        CityCode.objects.create(city_code ="3164803",
                                city_name ="São Sebastião do Rio Preto" )
            
        CityCode.objects.create(city_code ="3164902",
                                city_name ="São Sebastião do Rio Verde" )
            
        CityCode.objects.create(city_code ="3165008",
                                city_name ="São Tiago" )
            
        CityCode.objects.create(city_code ="3165107",
                                city_name ="São Tomás de Aquino" )
            
        CityCode.objects.create(city_code ="3165206",
                                city_name ="São Tomé das Letras" )
            
        CityCode.objects.create(city_code ="3165305",
                                city_name ="São Vicente de Minas" )
            
        CityCode.objects.create(city_code ="3165404",
                                city_name ="Sapucaí-Mirim" )
            
        CityCode.objects.create(city_code ="3165503",
                                city_name ="Sardoá" )
            
        CityCode.objects.create(city_code ="3165537",
                                city_name ="Sarzedo" )
            
        CityCode.objects.create(city_code ="3165560",
                                city_name ="Sem-Peixe" )
            
        CityCode.objects.create(city_code ="3165578",
                                city_name ="Senador Amaral" )
            
        CityCode.objects.create(city_code ="3165602",
                                city_name ="Senador Cortes" )
            
        CityCode.objects.create(city_code ="3165701",
                                city_name ="Senador Firmino" )
            
        CityCode.objects.create(city_code ="3165800",
                                city_name ="Senador José Bento" )
            
        CityCode.objects.create(city_code ="3165909",
                                city_name ="Senador Modestino Gonçalves" )
            
        CityCode.objects.create(city_code ="3166006",
                                city_name ="Senhora de Oliveira" )
            
        CityCode.objects.create(city_code ="3166105",
                                city_name ="Senhora do Porto" )
            
        CityCode.objects.create(city_code ="3166204",
                                city_name ="Senhora dos Remédios" )
            
        CityCode.objects.create(city_code ="3166303",
                                city_name ="Sericita" )
            
        CityCode.objects.create(city_code ="3166402",
                                city_name ="Seritinga" )
            
        CityCode.objects.create(city_code ="3166501",
                                city_name ="Serra Azul de Minas" )
            
        CityCode.objects.create(city_code ="3166600",
                                city_name ="Serra da Saudade" )
            
        CityCode.objects.create(city_code ="3166808",
                                city_name ="Serra do Salitre" )
            
        CityCode.objects.create(city_code ="3166709",
                                city_name ="Serra dos Aimorés" )
            
        CityCode.objects.create(city_code ="3166907",
                                city_name ="Serrania" )
            
        CityCode.objects.create(city_code ="3166956",
                                city_name ="Serranópolis de Minas" )
            
        CityCode.objects.create(city_code ="3167004",
                                city_name ="Serranos" )
            
        CityCode.objects.create(city_code ="3167103",
                                city_name ="Serro" )
            
        CityCode.objects.create(city_code ="3167202",
                                city_name ="Sete Lagoas" )
            
        CityCode.objects.create(city_code ="3165552",
                                city_name ="Setubinha" )
            
        CityCode.objects.create(city_code ="3167301",
                                city_name ="Silveirânia" )
            
        CityCode.objects.create(city_code ="3167400",
                                city_name ="Silvianópolis" )
            
        CityCode.objects.create(city_code ="3167509",
                                city_name ="Simão Pereira" )
            
        CityCode.objects.create(city_code ="3167608",
                                city_name ="Simonésia" )
            
        CityCode.objects.create(city_code ="3167707",
                                city_name ="Sobrália" )
            
        CityCode.objects.create(city_code ="3167806",
                                city_name ="Soledade de Minas" )
            
        CityCode.objects.create(city_code ="3167905",
                                city_name ="Tabuleiro" )
            
        CityCode.objects.create(city_code ="3168002",
                                city_name ="Taiobeiras" )
            
        CityCode.objects.create(city_code ="3168051",
                                city_name ="Taparuba" )
            
        CityCode.objects.create(city_code ="3168101",
                                city_name ="Tapira" )
            
        CityCode.objects.create(city_code ="3168200",
                                city_name ="Tapiraí" )
            
        CityCode.objects.create(city_code ="3168309",
                                city_name ="Taquaraçu de Minas" )
            
        CityCode.objects.create(city_code ="3168408",
                                city_name ="Tarumirim" )
            
        CityCode.objects.create(city_code ="3168507",
                                city_name ="Teixeiras" )
            
        CityCode.objects.create(city_code ="3168606",
                                city_name ="Teófilo Otoni" )
            
        CityCode.objects.create(city_code ="3168705",
                                city_name ="Timóteo" )
            
        CityCode.objects.create(city_code ="3168804",
                                city_name ="Tiradentes" )
            
        CityCode.objects.create(city_code ="3168903",
                                city_name ="Tiros" )
            
        CityCode.objects.create(city_code ="3169000",
                                city_name ="Tocantins" )
            
        CityCode.objects.create(city_code ="3169059",
                                city_name ="Tocos do Moji" )
            
        CityCode.objects.create(city_code ="3169109",
                                city_name ="Toledo" )
            
        CityCode.objects.create(city_code ="3169208",
                                city_name ="Tombos" )
            
        CityCode.objects.create(city_code ="3169307",
                                city_name ="Três Corações" )
            
        CityCode.objects.create(city_code ="3169356",
                                city_name ="Três Marias" )
            
        CityCode.objects.create(city_code ="3169406",
                                city_name ="Três Pontas" )
            
        CityCode.objects.create(city_code ="3169505",
                                city_name ="Tumiritinga" )
            
        CityCode.objects.create(city_code ="3169604",
                                city_name ="Tupaciguara" )
            
        CityCode.objects.create(city_code ="3169703",
                                city_name ="Turmalina" )
            
        CityCode.objects.create(city_code ="3169802",
                                city_name ="Turvolândia" )
            
        CityCode.objects.create(city_code ="3169901",
                                city_name ="Ubá" )
            
        CityCode.objects.create(city_code ="3170008",
                                city_name ="Ubaí" )
            
        CityCode.objects.create(city_code ="3170057",
                                city_name ="Ubaporanga" )
            
        CityCode.objects.create(city_code ="3170107",
                                city_name ="Uberaba" )
            
        CityCode.objects.create(city_code ="3170206",
                                city_name ="Uberlândia" )
            
        CityCode.objects.create(city_code ="3170305",
                                city_name ="Umburatiba" )
            
        CityCode.objects.create(city_code ="3170404",
                                city_name ="Unaí" )
            
        CityCode.objects.create(city_code ="3170438",
                                city_name ="União de Minas" )
            
        CityCode.objects.create(city_code ="3170479",
                                city_name ="Uruana de Minas" )
            
        CityCode.objects.create(city_code ="3170503",
                                city_name ="Urucânia" )
            
        CityCode.objects.create(city_code ="3170529",
                                city_name ="Urucuia" )
            
        CityCode.objects.create(city_code ="3170578",
                                city_name ="Vargem Alegre" )
            
        CityCode.objects.create(city_code ="3170602",
                                city_name ="Vargem Bonita" )
            
        CityCode.objects.create(city_code ="3170651",
                                city_name ="Vargem Grande do Rio Pardo" )
            
        CityCode.objects.create(city_code ="3170701",
                                city_name ="Varginha" )
            
        CityCode.objects.create(city_code ="3170750",
                                city_name ="Varjão de Minas" )
            
        CityCode.objects.create(city_code ="3170800",
                                city_name ="Várzea da Palma" )
            
        CityCode.objects.create(city_code ="3170909",
                                city_name ="Varzelândia" )
            
        CityCode.objects.create(city_code ="3171006",
                                city_name ="Vazante" )
            
        CityCode.objects.create(city_code ="3171030",
                                city_name ="Verdelândia" )
            
        CityCode.objects.create(city_code ="3171071",
                                city_name ="Veredinha" )
            
        CityCode.objects.create(city_code ="3171105",
                                city_name ="Veríssimo" )
            
        CityCode.objects.create(city_code ="3171154",
                                city_name ="Vermelho Novo" )
            
        CityCode.objects.create(city_code ="3171204",
                                city_name ="Vespasiano" )
            
        CityCode.objects.create(city_code ="3171303",
                                city_name ="Viçosa" )
            
        CityCode.objects.create(city_code ="3171402",
                                city_name ="Vieiras" )
            
        CityCode.objects.create(city_code ="3171600",
                                city_name ="Virgem da Lapa" )
            
        CityCode.objects.create(city_code ="3171709",
                                city_name ="Virgínia" )
            
        CityCode.objects.create(city_code ="3171808",
                                city_name ="Virginópolis" )
            
        CityCode.objects.create(city_code ="3171907",
                                city_name ="Virgolândia" )
            
        CityCode.objects.create(city_code ="3172004",
                                city_name ="Visconde do Rio Branco" )
            
        CityCode.objects.create(city_code ="3172103",
                                city_name ="Volta Grande" )
            
        CityCode.objects.create(city_code ="3172202",
                                city_name ="Wenceslau Braz" )
            
        CityCode.objects.create(city_code ="3200102",
                                city_name ="Afonso Cláudio" )
            
        CityCode.objects.create(city_code ="3200169",
                                city_name ="Água Doce do Norte" )
            
        CityCode.objects.create(city_code ="3200136",
                                city_name ="Águia Branca" )
            
        CityCode.objects.create(city_code ="3200201",
                                city_name ="Alegre" )
            
        CityCode.objects.create(city_code ="3200300",
                                city_name ="Alfredo Chaves" )
            
        CityCode.objects.create(city_code ="3200359",
                                city_name ="Alto Rio Novo" )
            
        CityCode.objects.create(city_code ="3200409",
                                city_name ="Anchieta" )
            
        CityCode.objects.create(city_code ="3200508",
                                city_name ="Apiacá" )
            
        CityCode.objects.create(city_code ="3200607",
                                city_name ="Aracruz" )
            
        CityCode.objects.create(city_code ="3200706",
                                city_name ="Atílio Vivácqua" )
            
        CityCode.objects.create(city_code ="3200805",
                                city_name ="Baixo Guandu" )
            
        CityCode.objects.create(city_code ="3200904",
                                city_name ="Barra de São Francisco" )
            
        CityCode.objects.create(city_code ="3201001",
                                city_name ="Boa Esperança" )
            
        CityCode.objects.create(city_code ="3201100",
                                city_name ="Bom Jesus do Norte" )
            
        CityCode.objects.create(city_code ="3201159",
                                city_name ="Brejetuba" )
            
        CityCode.objects.create(city_code ="3201209",
                                city_name ="Cachoeiro de Itapemirim" )
            
        CityCode.objects.create(city_code ="3201308",
                                city_name ="Cariacica" )
            
        CityCode.objects.create(city_code ="3201407",
                                city_name ="Castelo" )
            
        CityCode.objects.create(city_code ="3201506",
                                city_name ="Colatina" )
            
        CityCode.objects.create(city_code ="3201605",
                                city_name ="Conceição da Barra" )
            
        CityCode.objects.create(city_code ="3201704",
                                city_name ="Conceição do Castelo" )
            
        CityCode.objects.create(city_code ="3201803",
                                city_name ="Divino de São Lourenço" )
            
        CityCode.objects.create(city_code ="3201902",
                                city_name ="Domingos Martins" )
            
        CityCode.objects.create(city_code ="3202009",
                                city_name ="Dores do Rio Preto" )
            
        CityCode.objects.create(city_code ="3202108",
                                city_name ="Ecoporanga" )
            
        CityCode.objects.create(city_code ="3202207",
                                city_name ="Fundão" )
            
        CityCode.objects.create(city_code ="3202256",
                                city_name ="Governador Lindenberg" )
            
        CityCode.objects.create(city_code ="3202306",
                                city_name ="Guaçuí" )
            
        CityCode.objects.create(city_code ="3202405",
                                city_name ="Guarapari" )
            
        CityCode.objects.create(city_code ="3202454",
                                city_name ="Ibatiba" )
            
        CityCode.objects.create(city_code ="3202504",
                                city_name ="Ibiraçu" )
            
        CityCode.objects.create(city_code ="3202553",
                                city_name ="Ibitirama" )
            
        CityCode.objects.create(city_code ="3202603",
                                city_name ="Iconha" )
            
        CityCode.objects.create(city_code ="3202652",
                                city_name ="Irupi" )
            
        CityCode.objects.create(city_code ="3202702",
                                city_name ="Itaguaçu" )
            
        CityCode.objects.create(city_code ="3202801",
                                city_name ="Itapemirim" )
            
        CityCode.objects.create(city_code ="3202900",
                                city_name ="Itarana" )
            
        CityCode.objects.create(city_code ="3203007",
                                city_name ="Iúna" )
            
        CityCode.objects.create(city_code ="3203056",
                                city_name ="Jaguaré" )
            
        CityCode.objects.create(city_code ="3203106",
                                city_name ="Jerônimo Monteiro" )
            
        CityCode.objects.create(city_code ="3203130",
                                city_name ="João Neiva" )
            
        CityCode.objects.create(city_code ="3203163",
                                city_name ="Laranja da Terra" )
            
        CityCode.objects.create(city_code ="3203205",
                                city_name ="Linhares" )
            
        CityCode.objects.create(city_code ="3203304",
                                city_name ="Mantenópolis" )
            
        CityCode.objects.create(city_code ="3203320",
                                city_name ="Marataízes" )
            
        CityCode.objects.create(city_code ="3203346",
                                city_name ="Marechal Floriano" )
            
        CityCode.objects.create(city_code ="3203353",
                                city_name ="Marilândia" )
            
        CityCode.objects.create(city_code ="3203403",
                                city_name ="Mimoso do Sul" )
            
        CityCode.objects.create(city_code ="3203502",
                                city_name ="Montanha" )
            
        CityCode.objects.create(city_code ="3203601",
                                city_name ="Mucurici" )
            
        CityCode.objects.create(city_code ="3203700",
                                city_name ="Muniz Freire" )
            
        CityCode.objects.create(city_code ="3203809",
                                city_name ="Muqui" )
            
        CityCode.objects.create(city_code ="3203908",
                                city_name ="Nova Venécia" )
            
        CityCode.objects.create(city_code ="3204005",
                                city_name ="Pancas" )
            
        CityCode.objects.create(city_code ="3204054",
                                city_name ="Pedro Canário" )
            
        CityCode.objects.create(city_code ="3204104",
                                city_name ="Pinheiros" )
            
        CityCode.objects.create(city_code ="3204203",
                                city_name ="Piúma" )
            
        CityCode.objects.create(city_code ="3204252",
                                city_name ="Ponto Belo" )
            
        CityCode.objects.create(city_code ="3204302",
                                city_name ="Presidente Kennedy" )
            
        CityCode.objects.create(city_code ="3204351",
                                city_name ="Rio Bananal" )
            
        CityCode.objects.create(city_code ="3204401",
                                city_name ="Rio Novo do Sul" )
            
        CityCode.objects.create(city_code ="3204500",
                                city_name ="Santa Leopoldina" )
            
        CityCode.objects.create(city_code ="3204559",
                                city_name ="Santa Maria de Jetibá" )
            
        CityCode.objects.create(city_code ="3204609",
                                city_name ="Santa Teresa" )
            
        CityCode.objects.create(city_code ="3204658",
                                city_name ="São Domingos do Norte" )
            
        CityCode.objects.create(city_code ="3204708",
                                city_name ="São Gabriel da Palha" )
            
        CityCode.objects.create(city_code ="3204807",
                                city_name ="São José do Calçado" )
            
        CityCode.objects.create(city_code ="3204906",
                                city_name ="São Mateus" )
            
        CityCode.objects.create(city_code ="3204955",
                                city_name ="São Roque do Canaã" )
            
        CityCode.objects.create(city_code ="3205002",
                                city_name ="Serra" )
            
        CityCode.objects.create(city_code ="3205010",
                                city_name ="Sooretama" )
            
        CityCode.objects.create(city_code ="3205036",
                                city_name ="Vargem Alta" )
            
        CityCode.objects.create(city_code ="3205069",
                                city_name ="Venda Nova do Imigrante" )
            
        CityCode.objects.create(city_code ="3205101",
                                city_name ="Viana" )
            
        CityCode.objects.create(city_code ="3205150",
                                city_name ="Vila Pavão" )
            
        CityCode.objects.create(city_code ="3205176",
                                city_name ="Vila Valério" )
            
        CityCode.objects.create(city_code ="3205200",
                                city_name ="Vila Velha" )
            
        CityCode.objects.create(city_code ="3205309",
                                city_name ="Vitória" )
            
        CityCode.objects.create(city_code ="3300100",
                                city_name ="Angra dos Reis" )
            
        CityCode.objects.create(city_code ="3300159",
                                city_name ="Aperibé" )
            
        CityCode.objects.create(city_code ="3300209",
                                city_name ="Araruama" )
            
        CityCode.objects.create(city_code ="3300225",
                                city_name ="Areal" )
            
        CityCode.objects.create(city_code ="3300233",
                                city_name ="Armação dos Búzios" )
            
        CityCode.objects.create(city_code ="3300258",
                                city_name ="Arraial do Cabo" )
            
        CityCode.objects.create(city_code ="3300308",
                                city_name ="Barra do Piraí" )
            
        CityCode.objects.create(city_code ="3300407",
                                city_name ="Barra Mansa" )
            
        CityCode.objects.create(city_code ="3300456",
                                city_name ="Belford Roxo" )
            
        CityCode.objects.create(city_code ="3300506",
                                city_name ="Bom Jardim" )
            
        CityCode.objects.create(city_code ="3300605",
                                city_name ="Bom Jesus do Itabapoana" )
            
        CityCode.objects.create(city_code ="3300704",
                                city_name ="Cabo Frio" )
            
        CityCode.objects.create(city_code ="3300803",
                                city_name ="Cachoeiras de Macacu" )
            
        CityCode.objects.create(city_code ="3300902",
                                city_name ="Cambuci" )
            
        CityCode.objects.create(city_code ="3301009",
                                city_name ="Campos dos Goytacazes" )
            
        CityCode.objects.create(city_code ="3301108",
                                city_name ="Cantagalo" )
            
        CityCode.objects.create(city_code ="3300936",
                                city_name ="Carapebus" )
            
        CityCode.objects.create(city_code ="3301157",
                                city_name ="Cardoso Moreira" )
            
        CityCode.objects.create(city_code ="3301207",
                                city_name ="Carmo" )
            
        CityCode.objects.create(city_code ="3301306",
                                city_name ="Casimiro de Abreu" )
            
        CityCode.objects.create(city_code ="3300951",
                                city_name ="Comendador Levy Gasparian" )
            
        CityCode.objects.create(city_code ="3301405",
                                city_name ="Conceição de Macabu" )
            
        CityCode.objects.create(city_code ="3301504",
                                city_name ="Cordeiro" )
            
        CityCode.objects.create(city_code ="3301603",
                                city_name ="Duas Barras" )
            
        CityCode.objects.create(city_code ="3301702",
                                city_name ="Duque de Caxias" )
            
        CityCode.objects.create(city_code ="3301801",
                                city_name ="Engenheiro Paulo de Frontin" )
            
        CityCode.objects.create(city_code ="3301850",
                                city_name ="Guapimirim" )
            
        CityCode.objects.create(city_code ="3301876",
                                city_name ="Iguaba Grande" )
            
        CityCode.objects.create(city_code ="3301900",
                                city_name ="Itaboraí" )
            
        CityCode.objects.create(city_code ="3302007",
                                city_name ="Itaguaí" )
            
        CityCode.objects.create(city_code ="3302056",
                                city_name ="Italva" )
            
        CityCode.objects.create(city_code ="3302106",
                                city_name ="Itaocara" )
            
        CityCode.objects.create(city_code ="3302205",
                                city_name ="Itaperuna" )
            
        CityCode.objects.create(city_code ="3302254",
                                city_name ="Itatiaia" )
            
        CityCode.objects.create(city_code ="3302270",
                                city_name ="Japeri" )
            
        CityCode.objects.create(city_code ="3302304",
                                city_name ="Laje do Muriaé" )
            
        CityCode.objects.create(city_code ="3302403",
                                city_name ="Macaé" )
            
        CityCode.objects.create(city_code ="3302452",
                                city_name ="Macuco" )
            
        CityCode.objects.create(city_code ="3302502",
                                city_name ="Magé" )
            
        CityCode.objects.create(city_code ="3302601",
                                city_name ="Mangaratiba" )
            
        CityCode.objects.create(city_code ="3302700",
                                city_name ="Maricá" )
            
        CityCode.objects.create(city_code ="3302809",
                                city_name ="Mendes" )
            
        CityCode.objects.create(city_code ="3302858",
                                city_name ="Mesquita" )
            
        CityCode.objects.create(city_code ="3302908",
                                city_name ="Miguel Pereira" )
            
        CityCode.objects.create(city_code ="3303005",
                                city_name ="Miracema" )
            
        CityCode.objects.create(city_code ="3303104",
                                city_name ="Natividade" )
            
        CityCode.objects.create(city_code ="3303203",
                                city_name ="Nilópolis" )
            
        CityCode.objects.create(city_code ="3303302",
                                city_name ="Niterói" )
            
        CityCode.objects.create(city_code ="3303401",
                                city_name ="Nova Friburgo" )
            
        CityCode.objects.create(city_code ="3303500",
                                city_name ="Nova Iguaçu" )
            
        CityCode.objects.create(city_code ="3303609",
                                city_name ="Paracambi" )
            
        CityCode.objects.create(city_code ="3303708",
                                city_name ="Paraíba do Sul" )
            
        CityCode.objects.create(city_code ="3303807",
                                city_name ="Paraty" )
            
        CityCode.objects.create(city_code ="3303856",
                                city_name ="Paty do Alferes" )
            
        CityCode.objects.create(city_code ="3303906",
                                city_name ="Petrópolis" )
            
        CityCode.objects.create(city_code ="3303955",
                                city_name ="Pinheiral" )
            
        CityCode.objects.create(city_code ="3304003",
                                city_name ="Piraí" )
            
        CityCode.objects.create(city_code ="3304102",
                                city_name ="Porciúncula" )
            
        CityCode.objects.create(city_code ="3304110",
                                city_name ="Porto Real" )
            
        CityCode.objects.create(city_code ="3304128",
                                city_name ="Quatis" )
            
        CityCode.objects.create(city_code ="3304144",
                                city_name ="Queimados" )
            
        CityCode.objects.create(city_code ="3304151",
                                city_name ="Quissamã" )
            
        CityCode.objects.create(city_code ="3304201",
                                city_name ="Resende" )
            
        CityCode.objects.create(city_code ="3304300",
                                city_name ="Rio Bonito" )
            
        CityCode.objects.create(city_code ="3304409",
                                city_name ="Rio Claro" )
            
        CityCode.objects.create(city_code ="3304508",
                                city_name ="Rio das Flores" )
            
        CityCode.objects.create(city_code ="3304524",
                                city_name ="Rio das Ostras" )
            
        CityCode.objects.create(city_code ="3304557",
                                city_name ="Rio de Janeiro" )
            
        CityCode.objects.create(city_code ="3304607",
                                city_name ="Santa Maria Madalena" )
            
        CityCode.objects.create(city_code ="3304706",
                                city_name ="Santo Antônio de Pádua" )
            
        CityCode.objects.create(city_code ="3304805",
                                city_name ="São Fidélis" )
            
        CityCode.objects.create(city_code ="3304755",
                                city_name ="São Francisco de Itabapoana" )
            
        CityCode.objects.create(city_code ="3304904",
                                city_name ="São Gonçalo" )
            
        CityCode.objects.create(city_code ="3305000",
                                city_name ="São João da Barra" )
            
        CityCode.objects.create(city_code ="3305109",
                                city_name ="São João de Meriti" )
            
        CityCode.objects.create(city_code ="3305133",
                                city_name ="São José de Ubá" )
            
        CityCode.objects.create(city_code ="3305158",
                                city_name ="São José do Vale do Rio Preto" )
            
        CityCode.objects.create(city_code ="3305208",
                                city_name ="São Pedro da Aldeia" )
            
        CityCode.objects.create(city_code ="3305307",
                                city_name ="São Sebastião do Alto" )
            
        CityCode.objects.create(city_code ="3305406",
                                city_name ="Sapucaia" )
            
        CityCode.objects.create(city_code ="3305505",
                                city_name ="Saquarema" )
            
        CityCode.objects.create(city_code ="3305554",
                                city_name ="Seropédica" )
            
        CityCode.objects.create(city_code ="3305604",
                                city_name ="Silva Jardim" )
            
        CityCode.objects.create(city_code ="3305703",
                                city_name ="Sumidouro" )
            
        CityCode.objects.create(city_code ="3305752",
                                city_name ="Tanguá" )
            
        CityCode.objects.create(city_code ="3305802",
                                city_name ="Teresópolis" )
            
        CityCode.objects.create(city_code ="3305901",
                                city_name ="Trajano de Moraes" )
            
        CityCode.objects.create(city_code ="3306008",
                                city_name ="Três Rios" )
            
        CityCode.objects.create(city_code ="3306107",
                                city_name ="Valença" )
            
        CityCode.objects.create(city_code ="3306156",
                                city_name ="Varre-Sai" )
            
        CityCode.objects.create(city_code ="3306206",
                                city_name ="Vassouras" )
            
        CityCode.objects.create(city_code ="3306305",
                                city_name ="Volta Redonda" )
            
        CityCode.objects.create(city_code ="3500105",
                                city_name ="Adamantina" )
            
        CityCode.objects.create(city_code ="3500204",
                                city_name ="Adolfo" )
            
        CityCode.objects.create(city_code ="3500303",
                                city_name ="Aguaí" )
            
        CityCode.objects.create(city_code ="3500402",
                                city_name ="Águas da Prata" )
            
        CityCode.objects.create(city_code ="3500501",
                                city_name ="Águas de Lindóia" )
            
        CityCode.objects.create(city_code ="3500550",
                                city_name ="Águas de Santa Bárbara" )
            
        CityCode.objects.create(city_code ="3500600",
                                city_name ="Águas de São Pedro" )
            
        CityCode.objects.create(city_code ="3500709",
                                city_name ="Agudos" )
            
        CityCode.objects.create(city_code ="3500758",
                                city_name ="Alambari" )
            
        CityCode.objects.create(city_code ="3500808",
                                city_name ="Alfredo Marcondes" )
            
        CityCode.objects.create(city_code ="3500907",
                                city_name ="Altair" )
            
        CityCode.objects.create(city_code ="3501004",
                                city_name ="Altinópolis" )
            
        CityCode.objects.create(city_code ="3501103",
                                city_name ="Alto Alegre" )
            
        CityCode.objects.create(city_code ="3501152",
                                city_name ="Alumínio" )
            
        CityCode.objects.create(city_code ="3501202",
                                city_name ="Álvares Florence" )
            
        CityCode.objects.create(city_code ="3501301",
                                city_name ="Álvares Machado" )
            
        CityCode.objects.create(city_code ="3501400",
                                city_name ="Álvaro de Carvalho" )
            
        CityCode.objects.create(city_code ="3501509",
                                city_name ="Alvinlândia" )
            
        CityCode.objects.create(city_code ="3501608",
                                city_name ="Americana" )
            
        CityCode.objects.create(city_code ="3501707",
                                city_name ="Américo Brasiliense" )
            
        CityCode.objects.create(city_code ="3501806",
                                city_name ="Américo de Campos" )
            
        CityCode.objects.create(city_code ="3501905",
                                city_name ="Amparo" )
            
        CityCode.objects.create(city_code ="3502002",
                                city_name ="Analândia" )
            
        CityCode.objects.create(city_code ="3502101",
                                city_name ="Andradina" )
            
        CityCode.objects.create(city_code ="3502200",
                                city_name ="Angatuba" )
            
        CityCode.objects.create(city_code ="3502309",
                                city_name ="Anhembi" )
            
        CityCode.objects.create(city_code ="3502408",
                                city_name ="Anhumas" )
            
        CityCode.objects.create(city_code ="3502507",
                                city_name ="Aparecida" )
            
        CityCode.objects.create(city_code ="3502606",
                                city_name ="Aparecida d'Oeste" )
            
        CityCode.objects.create(city_code ="3502705",
                                city_name ="Apiaí" )
            
        CityCode.objects.create(city_code ="3502754",
                                city_name ="Araçariguama" )
            
        CityCode.objects.create(city_code ="3502804",
                                city_name ="Araçatuba" )
            
        CityCode.objects.create(city_code ="3502903",
                                city_name ="Araçoiaba da Serra" )
            
        CityCode.objects.create(city_code ="3503000",
                                city_name ="Aramina" )
            
        CityCode.objects.create(city_code ="3503109",
                                city_name ="Arandu" )
            
        CityCode.objects.create(city_code ="3503158",
                                city_name ="Arapeí" )
            
        CityCode.objects.create(city_code ="3503208",
                                city_name ="Araraquara" )
            
        CityCode.objects.create(city_code ="3503307",
                                city_name ="Araras" )
            
        CityCode.objects.create(city_code ="3503356",
                                city_name ="Arco-Íris" )
            
        CityCode.objects.create(city_code ="3503406",
                                city_name ="Arealva" )
            
        CityCode.objects.create(city_code ="3503505",
                                city_name ="Areias" )
            
        CityCode.objects.create(city_code ="3503604",
                                city_name ="Areiópolis" )
            
        CityCode.objects.create(city_code ="3503703",
                                city_name ="Ariranha" )
            
        CityCode.objects.create(city_code ="3503802",
                                city_name ="Artur Nogueira" )
            
        CityCode.objects.create(city_code ="3503901",
                                city_name ="Arujá" )
            
        CityCode.objects.create(city_code ="3503950",
                                city_name ="Aspásia" )
            
        CityCode.objects.create(city_code ="3504008",
                                city_name ="Assis" )
            
        CityCode.objects.create(city_code ="3504107",
                                city_name ="Atibaia" )
            
        CityCode.objects.create(city_code ="3504206",
                                city_name ="Auriflama" )
            
        CityCode.objects.create(city_code ="3504305",
                                city_name ="Avaí" )
            
        CityCode.objects.create(city_code ="3504404",
                                city_name ="Avanhandava" )
            
        CityCode.objects.create(city_code ="3504503",
                                city_name ="Avaré" )
            
        CityCode.objects.create(city_code ="3504602",
                                city_name ="Bady Bassitt" )
            
        CityCode.objects.create(city_code ="3504701",
                                city_name ="Balbinos" )
            
        CityCode.objects.create(city_code ="3504800",
                                city_name ="Bálsamo" )
            
        CityCode.objects.create(city_code ="3504909",
                                city_name ="Bananal" )
            
        CityCode.objects.create(city_code ="3505005",
                                city_name ="Barão de Antonina" )
            
        CityCode.objects.create(city_code ="3505104",
                                city_name ="Barbosa" )
            
        CityCode.objects.create(city_code ="3505203",
                                city_name ="Bariri" )
            
        CityCode.objects.create(city_code ="3505302",
                                city_name ="Barra Bonita" )
            
        CityCode.objects.create(city_code ="3505351",
                                city_name ="Barra do Chapéu" )
            
        CityCode.objects.create(city_code ="3505401",
                                city_name ="Barra do Turvo" )
            
        CityCode.objects.create(city_code ="3505500",
                                city_name ="Barretos" )
            
        CityCode.objects.create(city_code ="3505609",
                                city_name ="Barrinha" )
            
        CityCode.objects.create(city_code ="3505708",
                                city_name ="Barueri" )
            
        CityCode.objects.create(city_code ="3505807",
                                city_name ="Bastos" )
            
        CityCode.objects.create(city_code ="3505906",
                                city_name ="Batatais" )
            
        CityCode.objects.create(city_code ="3506003",
                                city_name ="Bauru" )
            
        CityCode.objects.create(city_code ="3506102",
                                city_name ="Bebedouro" )
            
        CityCode.objects.create(city_code ="3506201",
                                city_name ="Bento de Abreu" )
            
        CityCode.objects.create(city_code ="3506300",
                                city_name ="Bernardino de Campos" )
            
        CityCode.objects.create(city_code ="3506359",
                                city_name ="Bertioga" )
            
        CityCode.objects.create(city_code ="3506409",
                                city_name ="Bilac" )
            
        CityCode.objects.create(city_code ="3506508",
                                city_name ="Birigui" )
            
        CityCode.objects.create(city_code ="3506607",
                                city_name ="Biritiba Mirim" )
            
        CityCode.objects.create(city_code ="3506706",
                                city_name ="Boa Esperança do Sul" )
            
        CityCode.objects.create(city_code ="3506805",
                                city_name ="Bocaina" )
            
        CityCode.objects.create(city_code ="3506904",
                                city_name ="Bofete" )
            
        CityCode.objects.create(city_code ="3507001",
                                city_name ="Boituva" )
            
        CityCode.objects.create(city_code ="3507100",
                                city_name ="Bom Jesus dos Perdões" )
            
        CityCode.objects.create(city_code ="3507159",
                                city_name ="Bom Sucesso de Itararé" )
            
        CityCode.objects.create(city_code ="3507209",
                                city_name ="Borá" )
            
        CityCode.objects.create(city_code ="3507308",
                                city_name ="Boracéia" )
            
        CityCode.objects.create(city_code ="3507407",
                                city_name ="Borborema" )
            
        CityCode.objects.create(city_code ="3507456",
                                city_name ="Borebi" )
            
        CityCode.objects.create(city_code ="3507506",
                                city_name ="Botucatu" )
            
        CityCode.objects.create(city_code ="3507605",
                                city_name ="Bragança Paulista" )
            
        CityCode.objects.create(city_code ="3507704",
                                city_name ="Braúna" )
            
        CityCode.objects.create(city_code ="3507753",
                                city_name ="Brejo Alegre" )
            
        CityCode.objects.create(city_code ="3507803",
                                city_name ="Brodowski" )
            
        CityCode.objects.create(city_code ="3507902",
                                city_name ="Brotas" )
            
        CityCode.objects.create(city_code ="3508009",
                                city_name ="Buri" )
            
        CityCode.objects.create(city_code ="3508108",
                                city_name ="Buritama" )
            
        CityCode.objects.create(city_code ="3508207",
                                city_name ="Buritizal" )
            
        CityCode.objects.create(city_code ="3508306",
                                city_name ="Cabrália Paulista" )
            
        CityCode.objects.create(city_code ="3508405",
                                city_name ="Cabreúva" )
            
        CityCode.objects.create(city_code ="3508504",
                                city_name ="Caçapava" )
            
        CityCode.objects.create(city_code ="3508603",
                                city_name ="Cachoeira Paulista" )
            
        CityCode.objects.create(city_code ="3508702",
                                city_name ="Caconde" )
            
        CityCode.objects.create(city_code ="3508801",
                                city_name ="Cafelândia" )
            
        CityCode.objects.create(city_code ="3508900",
                                city_name ="Caiabu" )
            
        CityCode.objects.create(city_code ="3509007",
                                city_name ="Caieiras" )
            
        CityCode.objects.create(city_code ="3509106",
                                city_name ="Caiuá" )
            
        CityCode.objects.create(city_code ="3509205",
                                city_name ="Cajamar" )
            
        CityCode.objects.create(city_code ="3509254",
                                city_name ="Cajati" )
            
        CityCode.objects.create(city_code ="3509304",
                                city_name ="Cajobi" )
            
        CityCode.objects.create(city_code ="3509403",
                                city_name ="Cajuru" )
            
        CityCode.objects.create(city_code ="3509452",
                                city_name ="Campina do Monte Alegre" )
            
        CityCode.objects.create(city_code ="3509502",
                                city_name ="Campinas" )
            
        CityCode.objects.create(city_code ="3509601",
                                city_name ="Campo Limpo Paulista" )
            
        CityCode.objects.create(city_code ="3509700",
                                city_name ="Campos do Jordão" )
            
        CityCode.objects.create(city_code ="3509809",
                                city_name ="Campos Novos Paulista" )
            
        CityCode.objects.create(city_code ="3509908",
                                city_name ="Cananéia" )
            
        CityCode.objects.create(city_code ="3509957",
                                city_name ="Canas" )
            
        CityCode.objects.create(city_code ="3510005",
                                city_name ="Cândido Mota" )
            
        CityCode.objects.create(city_code ="3510104",
                                city_name ="Cândido Rodrigues" )
            
        CityCode.objects.create(city_code ="3510153",
                                city_name ="Canitar" )
            
        CityCode.objects.create(city_code ="3510203",
                                city_name ="Capão Bonito" )
            
        CityCode.objects.create(city_code ="3510302",
                                city_name ="Capela do Alto" )
            
        CityCode.objects.create(city_code ="3510401",
                                city_name ="Capivari" )
            
        CityCode.objects.create(city_code ="3510500",
                                city_name ="Caraguatatuba" )
            
        CityCode.objects.create(city_code ="3510609",
                                city_name ="Carapicuíba" )
            
        CityCode.objects.create(city_code ="3510708",
                                city_name ="Cardoso" )
            
        CityCode.objects.create(city_code ="3510807",
                                city_name ="Casa Branca" )
            
        CityCode.objects.create(city_code ="3510906",
                                city_name ="Cássia dos Coqueiros" )
            
        CityCode.objects.create(city_code ="3511003",
                                city_name ="Castilho" )
            
        CityCode.objects.create(city_code ="3511102",
                                city_name ="Catanduva" )
            
        CityCode.objects.create(city_code ="3511201",
                                city_name ="Catiguá" )
            
        CityCode.objects.create(city_code ="3511300",
                                city_name ="Cedral" )
            
        CityCode.objects.create(city_code ="3511409",
                                city_name ="Cerqueira César" )
            
        CityCode.objects.create(city_code ="3511508",
                                city_name ="Cerquilho" )
            
        CityCode.objects.create(city_code ="3511607",
                                city_name ="Cesário Lange" )
            
        CityCode.objects.create(city_code ="3511706",
                                city_name ="Charqueada" )
            
        CityCode.objects.create(city_code ="3557204",
                                city_name ="Chavantes" )
            
        CityCode.objects.create(city_code ="3511904",
                                city_name ="Clementina" )
            
        CityCode.objects.create(city_code ="3512001",
                                city_name ="Colina" )
            
        CityCode.objects.create(city_code ="3512100",
                                city_name ="Colômbia" )
            
        CityCode.objects.create(city_code ="3512209",
                                city_name ="Conchal" )
            
        CityCode.objects.create(city_code ="3512308",
                                city_name ="Conchas" )
            
        CityCode.objects.create(city_code ="3512407",
                                city_name ="Cordeirópolis" )
            
        CityCode.objects.create(city_code ="3512506",
                                city_name ="Coroados" )
            
        CityCode.objects.create(city_code ="3512605",
                                city_name ="Coronel Macedo" )
            
        CityCode.objects.create(city_code ="3512704",
                                city_name ="Corumbataí" )
            
        CityCode.objects.create(city_code ="3512803",
                                city_name ="Cosmópolis" )
            
        CityCode.objects.create(city_code ="3512902",
                                city_name ="Cosmorama" )
            
        CityCode.objects.create(city_code ="3513009",
                                city_name ="Cotia" )
            
        CityCode.objects.create(city_code ="3513108",
                                city_name ="Cravinhos" )
            
        CityCode.objects.create(city_code ="3513207",
                                city_name ="Cristais Paulista" )
            
        CityCode.objects.create(city_code ="3513306",
                                city_name ="Cruzália" )
            
        CityCode.objects.create(city_code ="3513405",
                                city_name ="Cruzeiro" )
            
        CityCode.objects.create(city_code ="3513504",
                                city_name ="Cubatão" )
            
        CityCode.objects.create(city_code ="3513603",
                                city_name ="Cunha" )
            
        CityCode.objects.create(city_code ="3513702",
                                city_name ="Descalvado" )
            
        CityCode.objects.create(city_code ="3513801",
                                city_name ="Diadema" )
            
        CityCode.objects.create(city_code ="3513850",
                                city_name ="Dirce Reis" )
            
        CityCode.objects.create(city_code ="3513900",
                                city_name ="Divinolândia" )
            
        CityCode.objects.create(city_code ="3514007",
                                city_name ="Dobrada" )
            
        CityCode.objects.create(city_code ="3514106",
                                city_name ="Dois Córregos" )
            
        CityCode.objects.create(city_code ="3514205",
                                city_name ="Dolcinópolis" )
            
        CityCode.objects.create(city_code ="3514304",
                                city_name ="Dourado" )
            
        CityCode.objects.create(city_code ="3514403",
                                city_name ="Dracena" )
            
        CityCode.objects.create(city_code ="3514502",
                                city_name ="Duartina" )
            
        CityCode.objects.create(city_code ="3514601",
                                city_name ="Dumont" )
            
        CityCode.objects.create(city_code ="3514700",
                                city_name ="Echaporã" )
            
        CityCode.objects.create(city_code ="3514809",
                                city_name ="Eldorado" )
            
        CityCode.objects.create(city_code ="3514908",
                                city_name ="Elias Fausto" )
            
        CityCode.objects.create(city_code ="3514924",
                                city_name ="Elisiário" )
            
        CityCode.objects.create(city_code ="3514957",
                                city_name ="Embaúba" )
            
        CityCode.objects.create(city_code ="3515004",
                                city_name ="Embu das Artes" )
            
        CityCode.objects.create(city_code ="3515103",
                                city_name ="Embu-Guaçu" )
            
        CityCode.objects.create(city_code ="3515129",
                                city_name ="Emilianópolis" )
            
        CityCode.objects.create(city_code ="3515152",
                                city_name ="Engenheiro Coelho" )
            
        CityCode.objects.create(city_code ="3515186",
                                city_name ="Espírito Santo do Pinhal" )
            
        CityCode.objects.create(city_code ="3515194",
                                city_name ="Espírito Santo do Turvo" )
            
        CityCode.objects.create(city_code ="3557303",
                                city_name ="Estiva Gerbi" )
            
        CityCode.objects.create(city_code ="3515301",
                                city_name ="Estrela do Norte" )
            
        CityCode.objects.create(city_code ="3515202",
                                city_name ="Estrela d'Oeste" )
            
        CityCode.objects.create(city_code ="3515350",
                                city_name ="Euclides da Cunha Paulista" )
            
        CityCode.objects.create(city_code ="3515400",
                                city_name ="Fartura" )
            
        CityCode.objects.create(city_code ="3515608",
                                city_name ="Fernando Prestes" )
            
        CityCode.objects.create(city_code ="3515509",
                                city_name ="Fernandópolis" )
            
        CityCode.objects.create(city_code ="3515657",
                                city_name ="Fernão" )
            
        CityCode.objects.create(city_code ="3515707",
                                city_name ="Ferraz de Vasconcelos" )
            
        CityCode.objects.create(city_code ="3515806",
                                city_name ="Flora Rica" )
            
        CityCode.objects.create(city_code ="3515905",
                                city_name ="Floreal" )
            
        CityCode.objects.create(city_code ="3516002",
                                city_name ="Flórida Paulista" )
            
        CityCode.objects.create(city_code ="3516101",
                                city_name ="Florínea" )
            
        CityCode.objects.create(city_code ="3516200",
                                city_name ="Franca" )
            
        CityCode.objects.create(city_code ="3516309",
                                city_name ="Francisco Morato" )
            
        CityCode.objects.create(city_code ="3516408",
                                city_name ="Franco da Rocha" )
            
        CityCode.objects.create(city_code ="3516507",
                                city_name ="Gabriel Monteiro" )
            
        CityCode.objects.create(city_code ="3516606",
                                city_name ="Gália" )
            
        CityCode.objects.create(city_code ="3516705",
                                city_name ="Garça" )
            
        CityCode.objects.create(city_code ="3516804",
                                city_name ="Gastão Vidigal" )
            
        CityCode.objects.create(city_code ="3516853",
                                city_name ="Gavião Peixoto" )
            
        CityCode.objects.create(city_code ="3516903",
                                city_name ="General Salgado" )
            
        CityCode.objects.create(city_code ="3517000",
                                city_name ="Getulina" )
            
        CityCode.objects.create(city_code ="3517109",
                                city_name ="Glicério" )
            
        CityCode.objects.create(city_code ="3517208",
                                city_name ="Guaiçara" )
            
        CityCode.objects.create(city_code ="3517307",
                                city_name ="Guaimbê" )
            
        CityCode.objects.create(city_code ="3517406",
                                city_name ="Guaíra" )
            
        CityCode.objects.create(city_code ="3517505",
                                city_name ="Guapiaçu" )
            
        CityCode.objects.create(city_code ="3517604",
                                city_name ="Guapiara" )
            
        CityCode.objects.create(city_code ="3517703",
                                city_name ="Guará" )
            
        CityCode.objects.create(city_code ="3517802",
                                city_name ="Guaraçaí" )
            
        CityCode.objects.create(city_code ="3517901",
                                city_name ="Guaraci" )
            
        CityCode.objects.create(city_code ="3518008",
                                city_name ="Guarani d'Oeste" )
            
        CityCode.objects.create(city_code ="3518107",
                                city_name ="Guarantã" )
            
        CityCode.objects.create(city_code ="3518206",
                                city_name ="Guararapes" )
            
        CityCode.objects.create(city_code ="3518305",
                                city_name ="Guararema" )
            
        CityCode.objects.create(city_code ="3518404",
                                city_name ="Guaratinguetá" )
            
        CityCode.objects.create(city_code ="3518503",
                                city_name ="Guareí" )
            
        CityCode.objects.create(city_code ="3518602",
                                city_name ="Guariba" )
            
        CityCode.objects.create(city_code ="3518701",
                                city_name ="Guarujá" )
            
        CityCode.objects.create(city_code ="3518800",
                                city_name ="Guarulhos" )
            
        CityCode.objects.create(city_code ="3518859",
                                city_name ="Guatapará" )
            
        CityCode.objects.create(city_code ="3518909",
                                city_name ="Guzolândia" )
            
        CityCode.objects.create(city_code ="3519006",
                                city_name ="Herculândia" )
            
        CityCode.objects.create(city_code ="3519055",
                                city_name ="Holambra" )
            
        CityCode.objects.create(city_code ="3519071",
                                city_name ="Hortolândia" )
            
        CityCode.objects.create(city_code ="3519105",
                                city_name ="Iacanga" )
            
        CityCode.objects.create(city_code ="3519204",
                                city_name ="Iacri" )
            
        CityCode.objects.create(city_code ="3519253",
                                city_name ="Iaras" )
            
        CityCode.objects.create(city_code ="3519303",
                                city_name ="Ibaté" )
            
        CityCode.objects.create(city_code ="3519402",
                                city_name ="Ibirá" )
            
        CityCode.objects.create(city_code ="3519501",
                                city_name ="Ibirarema" )
            
        CityCode.objects.create(city_code ="3519600",
                                city_name ="Ibitinga" )
            
        CityCode.objects.create(city_code ="3519709",
                                city_name ="Ibiúna" )
            
        CityCode.objects.create(city_code ="3519808",
                                city_name ="Icém" )
            
        CityCode.objects.create(city_code ="3519907",
                                city_name ="Iepê" )
            
        CityCode.objects.create(city_code ="3520004",
                                city_name ="Igaraçu do Tietê" )
            
        CityCode.objects.create(city_code ="3520103",
                                city_name ="Igarapava" )
            
        CityCode.objects.create(city_code ="3520202",
                                city_name ="Igaratá" )
            
        CityCode.objects.create(city_code ="3520301",
                                city_name ="Iguape" )
            
        CityCode.objects.create(city_code ="3520426",
                                city_name ="Ilha Comprida" )
            
        CityCode.objects.create(city_code ="3520442",
                                city_name ="Ilha Solteira" )
            
        CityCode.objects.create(city_code ="3520400",
                                city_name ="Ilhabela" )
            
        CityCode.objects.create(city_code ="3520509",
                                city_name ="Indaiatuba" )
            
        CityCode.objects.create(city_code ="3520608",
                                city_name ="Indiana" )
            
        CityCode.objects.create(city_code ="3520707",
                                city_name ="Indiaporã" )
            
        CityCode.objects.create(city_code ="3520806",
                                city_name ="Inúbia Paulista" )
            
        CityCode.objects.create(city_code ="3520905",
                                city_name ="Ipaussu" )
            
        CityCode.objects.create(city_code ="3521002",
                                city_name ="Iperó" )
            
        CityCode.objects.create(city_code ="3521101",
                                city_name ="Ipeúna" )
            
        CityCode.objects.create(city_code ="3521150",
                                city_name ="Ipiguá" )
            
        CityCode.objects.create(city_code ="3521200",
                                city_name ="Iporanga" )
            
        CityCode.objects.create(city_code ="3521309",
                                city_name ="Ipuã" )
            
        CityCode.objects.create(city_code ="3521408",
                                city_name ="Iracemápolis" )
            
        CityCode.objects.create(city_code ="3521507",
                                city_name ="Irapuã" )
            
        CityCode.objects.create(city_code ="3521606",
                                city_name ="Irapuru" )
            
        CityCode.objects.create(city_code ="3521705",
                                city_name ="Itaberá" )
            
        CityCode.objects.create(city_code ="3521804",
                                city_name ="Itaí" )
            
        CityCode.objects.create(city_code ="3521903",
                                city_name ="Itajobi" )
            
        CityCode.objects.create(city_code ="3522000",
                                city_name ="Itaju" )
            
        CityCode.objects.create(city_code ="3522109",
                                city_name ="Itanhaém" )
            
        CityCode.objects.create(city_code ="3522158",
                                city_name ="Itaoca" )
            
        CityCode.objects.create(city_code ="3522208",
                                city_name ="Itapecerica da Serra" )
            
        CityCode.objects.create(city_code ="3522307",
                                city_name ="Itapetininga" )
            
        CityCode.objects.create(city_code ="3522406",
                                city_name ="Itapeva" )
            
        CityCode.objects.create(city_code ="3522505",
                                city_name ="Itapevi" )
            
        CityCode.objects.create(city_code ="3522604",
                                city_name ="Itapira" )
            
        CityCode.objects.create(city_code ="3522653",
                                city_name ="Itapirapuã Paulista" )
            
        CityCode.objects.create(city_code ="3522703",
                                city_name ="Itápolis" )
            
        CityCode.objects.create(city_code ="3522802",
                                city_name ="Itaporanga" )
            
        CityCode.objects.create(city_code ="3522901",
                                city_name ="Itapuí" )
            
        CityCode.objects.create(city_code ="3523008",
                                city_name ="Itapura" )
            
        CityCode.objects.create(city_code ="3523107",
                                city_name ="Itaquaquecetuba" )
            
        CityCode.objects.create(city_code ="3523206",
                                city_name ="Itararé" )
            
        CityCode.objects.create(city_code ="3523305",
                                city_name ="Itariri" )
            
        CityCode.objects.create(city_code ="3523404",
                                city_name ="Itatiba" )
            
        CityCode.objects.create(city_code ="3523503",
                                city_name ="Itatinga" )
            
        CityCode.objects.create(city_code ="3523602",
                                city_name ="Itirapina" )
            
        CityCode.objects.create(city_code ="3523701",
                                city_name ="Itirapuã" )
            
        CityCode.objects.create(city_code ="3523800",
                                city_name ="Itobi" )
            
        CityCode.objects.create(city_code ="3523909",
                                city_name ="Itu" )
            
        CityCode.objects.create(city_code ="3524006",
                                city_name ="Itupeva" )
            
        CityCode.objects.create(city_code ="3524105",
                                city_name ="Ituverava" )
            
        CityCode.objects.create(city_code ="3524204",
                                city_name ="Jaborandi" )
            
        CityCode.objects.create(city_code ="3524303",
                                city_name ="Jaboticabal" )
            
        CityCode.objects.create(city_code ="3524402",
                                city_name ="Jacareí" )
            
        CityCode.objects.create(city_code ="3524501",
                                city_name ="Jaci" )
            
        CityCode.objects.create(city_code ="3524600",
                                city_name ="Jacupiranga" )
            
        CityCode.objects.create(city_code ="3524709",
                                city_name ="Jaguariúna" )
            
        CityCode.objects.create(city_code ="3524808",
                                city_name ="Jales" )
            
        CityCode.objects.create(city_code ="3524907",
                                city_name ="Jambeiro" )
            
        CityCode.objects.create(city_code ="3525003",
                                city_name ="Jandira" )
            
        CityCode.objects.create(city_code ="3525102",
                                city_name ="Jardinópolis" )
            
        CityCode.objects.create(city_code ="3525201",
                                city_name ="Jarinu" )
            
        CityCode.objects.create(city_code ="3525300",
                                city_name ="Jaú" )
            
        CityCode.objects.create(city_code ="3525409",
                                city_name ="Jeriquara" )
            
        CityCode.objects.create(city_code ="3525508",
                                city_name ="Joanópolis" )
            
        CityCode.objects.create(city_code ="3525607",
                                city_name ="João Ramalho" )
            
        CityCode.objects.create(city_code ="3525706",
                                city_name ="José Bonifácio" )
            
        CityCode.objects.create(city_code ="3525805",
                                city_name ="Júlio Mesquita" )
            
        CityCode.objects.create(city_code ="3525854",
                                city_name ="Jumirim" )
            
        CityCode.objects.create(city_code ="3525904",
                                city_name ="Jundiaí" )
            
        CityCode.objects.create(city_code ="3526001",
                                city_name ="Junqueirópolis" )
            
        CityCode.objects.create(city_code ="3526100",
                                city_name ="Juquiá" )
            
        CityCode.objects.create(city_code ="3526209",
                                city_name ="Juquitiba" )
            
        CityCode.objects.create(city_code ="3526308",
                                city_name ="Lagoinha" )
            
        CityCode.objects.create(city_code ="3526407",
                                city_name ="Laranjal Paulista" )
            
        CityCode.objects.create(city_code ="3526506",
                                city_name ="Lavínia" )
            
        CityCode.objects.create(city_code ="3526605",
                                city_name ="Lavrinhas" )
            
        CityCode.objects.create(city_code ="3526704",
                                city_name ="Leme" )
            
        CityCode.objects.create(city_code ="3526803",
                                city_name ="Lençóis Paulista" )
            
        CityCode.objects.create(city_code ="3526902",
                                city_name ="Limeira" )
            
        CityCode.objects.create(city_code ="3527009",
                                city_name ="Lindóia" )
            
        CityCode.objects.create(city_code ="3527108",
                                city_name ="Lins" )
            
        CityCode.objects.create(city_code ="3527207",
                                city_name ="Lorena" )
            
        CityCode.objects.create(city_code ="3527256",
                                city_name ="Lourdes" )
            
        CityCode.objects.create(city_code ="3527306",
                                city_name ="Louveira" )
            
        CityCode.objects.create(city_code ="3527405",
                                city_name ="Lucélia" )
            
        CityCode.objects.create(city_code ="3527504",
                                city_name ="Lucianópolis" )
            
        CityCode.objects.create(city_code ="3527603",
                                city_name ="Luís Antônio" )
            
        CityCode.objects.create(city_code ="3527702",
                                city_name ="Luiziânia" )
            
        CityCode.objects.create(city_code ="3527801",
                                city_name ="Lupércio" )
            
        CityCode.objects.create(city_code ="3527900",
                                city_name ="Lutécia" )
            
        CityCode.objects.create(city_code ="3528007",
                                city_name ="Macatuba" )
            
        CityCode.objects.create(city_code ="3528106",
                                city_name ="Macaubal" )
            
        CityCode.objects.create(city_code ="3528205",
                                city_name ="Macedônia" )
            
        CityCode.objects.create(city_code ="3528304",
                                city_name ="Magda" )
            
        CityCode.objects.create(city_code ="3528403",
                                city_name ="Mairinque" )
            
        CityCode.objects.create(city_code ="3528502",
                                city_name ="Mairiporã" )
            
        CityCode.objects.create(city_code ="3528601",
                                city_name ="Manduri" )
            
        CityCode.objects.create(city_code ="3528700",
                                city_name ="Marabá Paulista" )
            
        CityCode.objects.create(city_code ="3528809",
                                city_name ="Maracaí" )
            
        CityCode.objects.create(city_code ="3528858",
                                city_name ="Marapoama" )
            
        CityCode.objects.create(city_code ="3528908",
                                city_name ="Mariápolis" )
            
        CityCode.objects.create(city_code ="3529005",
                                city_name ="Marília" )
            
        CityCode.objects.create(city_code ="3529104",
                                city_name ="Marinópolis" )
            
        CityCode.objects.create(city_code ="3529203",
                                city_name ="Martinópolis" )
            
        CityCode.objects.create(city_code ="3529302",
                                city_name ="Matão" )
            
        CityCode.objects.create(city_code ="3529401",
                                city_name ="Mauá" )
            
        CityCode.objects.create(city_code ="3529500",
                                city_name ="Mendonça" )
            
        CityCode.objects.create(city_code ="3529609",
                                city_name ="Meridiano" )
            
        CityCode.objects.create(city_code ="3529658",
                                city_name ="Mesópolis" )
            
        CityCode.objects.create(city_code ="3529708",
                                city_name ="Miguelópolis" )
            
        CityCode.objects.create(city_code ="3529807",
                                city_name ="Mineiros do Tietê" )
            
        CityCode.objects.create(city_code ="3530003",
                                city_name ="Mira Estrela" )
            
        CityCode.objects.create(city_code ="3529906",
                                city_name ="Miracatu" )
            
        CityCode.objects.create(city_code ="3530102",
                                city_name ="Mirandópolis" )
            
        CityCode.objects.create(city_code ="3530201",
                                city_name ="Mirante do Paranapanema" )
            
        CityCode.objects.create(city_code ="3530300",
                                city_name ="Mirassol" )
            
        CityCode.objects.create(city_code ="3530409",
                                city_name ="Mirassolândia" )
            
        CityCode.objects.create(city_code ="3530508",
                                city_name ="Mococa" )
            
        CityCode.objects.create(city_code ="3530607",
                                city_name ="Mogi das Cruzes" )
            
        CityCode.objects.create(city_code ="3530706",
                                city_name ="Mogi Guaçu" )
            
        CityCode.objects.create(city_code ="3530805",
                                city_name ="Mogi Mirim" )
            
        CityCode.objects.create(city_code ="3530904",
                                city_name ="Mombuca" )
            
        CityCode.objects.create(city_code ="3531001",
                                city_name ="Monções" )
            
        CityCode.objects.create(city_code ="3531100",
                                city_name ="Mongaguá" )
            
        CityCode.objects.create(city_code ="3531209",
                                city_name ="Monte Alegre do Sul" )
            
        CityCode.objects.create(city_code ="3531308",
                                city_name ="Monte Alto" )
            
        CityCode.objects.create(city_code ="3531407",
                                city_name ="Monte Aprazível" )
            
        CityCode.objects.create(city_code ="3531506",
                                city_name ="Monte Azul Paulista" )
            
        CityCode.objects.create(city_code ="3531605",
                                city_name ="Monte Castelo" )
            
        CityCode.objects.create(city_code ="3531803",
                                city_name ="Monte Mor" )
            
        CityCode.objects.create(city_code ="3531704",
                                city_name ="Monteiro Lobato" )
            
        CityCode.objects.create(city_code ="3531902",
                                city_name ="Morro Agudo" )
            
        CityCode.objects.create(city_code ="3532009",
                                city_name ="Morungaba" )
            
        CityCode.objects.create(city_code ="3532058",
                                city_name ="Motuca" )
            
        CityCode.objects.create(city_code ="3532108",
                                city_name ="Murutinga do Sul" )
            
        CityCode.objects.create(city_code ="3532157",
                                city_name ="Nantes" )
            
        CityCode.objects.create(city_code ="3532207",
                                city_name ="Narandiba" )
            
        CityCode.objects.create(city_code ="3532306",
                                city_name ="Natividade da Serra" )
            
        CityCode.objects.create(city_code ="3532405",
                                city_name ="Nazaré Paulista" )
            
        CityCode.objects.create(city_code ="3532504",
                                city_name ="Neves Paulista" )
            
        CityCode.objects.create(city_code ="3532603",
                                city_name ="Nhandeara" )
            
        CityCode.objects.create(city_code ="3532702",
                                city_name ="Nipoã" )
            
        CityCode.objects.create(city_code ="3532801",
                                city_name ="Nova Aliança" )
            
        CityCode.objects.create(city_code ="3532827",
                                city_name ="Nova Campina" )
            
        CityCode.objects.create(city_code ="3532843",
                                city_name ="Nova Canaã Paulista" )
            
        CityCode.objects.create(city_code ="3532868",
                                city_name ="Nova Castilho" )
            
        CityCode.objects.create(city_code ="3532900",
                                city_name ="Nova Europa" )
            
        CityCode.objects.create(city_code ="3533007",
                                city_name ="Nova Granada" )
            
        CityCode.objects.create(city_code ="3533106",
                                city_name ="Nova Guataporanga" )
            
        CityCode.objects.create(city_code ="3533205",
                                city_name ="Nova Independência" )
            
        CityCode.objects.create(city_code ="3533304",
                                city_name ="Nova Luzitânia" )
            
        CityCode.objects.create(city_code ="3533403",
                                city_name ="Nova Odessa" )
            
        CityCode.objects.create(city_code ="3533254",
                                city_name ="Novais" )
            
        CityCode.objects.create(city_code ="3533502",
                                city_name ="Novo Horizonte" )
            
        CityCode.objects.create(city_code ="3533601",
                                city_name ="Nuporanga" )
            
        CityCode.objects.create(city_code ="3533700",
                                city_name ="Ocauçu" )
            
        CityCode.objects.create(city_code ="3533809",
                                city_name ="Óleo" )
            
        CityCode.objects.create(city_code ="3533908",
                                city_name ="Olímpia" )
            
        CityCode.objects.create(city_code ="3534005",
                                city_name ="Onda Verde" )
            
        CityCode.objects.create(city_code ="3534104",
                                city_name ="Oriente" )
            
        CityCode.objects.create(city_code ="3534203",
                                city_name ="Orindiúva" )
            
        CityCode.objects.create(city_code ="3534302",
                                city_name ="Orlândia" )
            
        CityCode.objects.create(city_code ="3534401",
                                city_name ="Osasco" )
            
        CityCode.objects.create(city_code ="3534500",
                                city_name ="Oscar Bressane" )
            
        CityCode.objects.create(city_code ="3534609",
                                city_name ="Osvaldo Cruz" )
            
        CityCode.objects.create(city_code ="3534708",
                                city_name ="Ourinhos" )
            
        CityCode.objects.create(city_code ="3534807",
                                city_name ="Ouro Verde" )
            
        CityCode.objects.create(city_code ="3534757",
                                city_name ="Ouroeste" )
            
        CityCode.objects.create(city_code ="3534906",
                                city_name ="Pacaembu" )
            
        CityCode.objects.create(city_code ="3535002",
                                city_name ="Palestina" )
            
        CityCode.objects.create(city_code ="3535101",
                                city_name ="Palmares Paulista" )
            
        CityCode.objects.create(city_code ="3535200",
                                city_name ="Palmeira d'Oeste" )
            
        CityCode.objects.create(city_code ="3535309",
                                city_name ="Palmital" )
            
        CityCode.objects.create(city_code ="3535408",
                                city_name ="Panorama" )
            
        CityCode.objects.create(city_code ="3535507",
                                city_name ="Paraguaçu Paulista" )
            
        CityCode.objects.create(city_code ="3535606",
                                city_name ="Paraibuna" )
            
        CityCode.objects.create(city_code ="3535705",
                                city_name ="Paraíso" )
            
        CityCode.objects.create(city_code ="3535804",
                                city_name ="Paranapanema" )
            
        CityCode.objects.create(city_code ="3535903",
                                city_name ="Paranapuã" )
            
        CityCode.objects.create(city_code ="3536000",
                                city_name ="Parapuã" )
            
        CityCode.objects.create(city_code ="3536109",
                                city_name ="Pardinho" )
            
        CityCode.objects.create(city_code ="3536208",
                                city_name ="Pariquera-Açu" )
            
        CityCode.objects.create(city_code ="3536257",
                                city_name ="Parisi" )
            
        CityCode.objects.create(city_code ="3536307",
                                city_name ="Patrocínio Paulista" )
            
        CityCode.objects.create(city_code ="3536406",
                                city_name ="Paulicéia" )
            
        CityCode.objects.create(city_code ="3536505",
                                city_name ="Paulínia" )
            
        CityCode.objects.create(city_code ="3536570",
                                city_name ="Paulistânia" )
            
        CityCode.objects.create(city_code ="3536604",
                                city_name ="Paulo de Faria" )
            
        CityCode.objects.create(city_code ="3536703",
                                city_name ="Pederneiras" )
            
        CityCode.objects.create(city_code ="3536802",
                                city_name ="Pedra Bela" )
            
        CityCode.objects.create(city_code ="3536901",
                                city_name ="Pedranópolis" )
            
        CityCode.objects.create(city_code ="3537008",
                                city_name ="Pedregulho" )
            
        CityCode.objects.create(city_code ="3537107",
                                city_name ="Pedreira" )
            
        CityCode.objects.create(city_code ="3537156",
                                city_name ="Pedrinhas Paulista" )
            
        CityCode.objects.create(city_code ="3537206",
                                city_name ="Pedro de Toledo" )
            
        CityCode.objects.create(city_code ="3537305",
                                city_name ="Penápolis" )
            
        CityCode.objects.create(city_code ="3537404",
                                city_name ="Pereira Barreto" )
            
        CityCode.objects.create(city_code ="3537503",
                                city_name ="Pereiras" )
            
        CityCode.objects.create(city_code ="3537602",
                                city_name ="Peruíbe" )
            
        CityCode.objects.create(city_code ="3537701",
                                city_name ="Piacatu" )
            
        CityCode.objects.create(city_code ="3537800",
                                city_name ="Piedade" )
            
        CityCode.objects.create(city_code ="3537909",
                                city_name ="Pilar do Sul" )
            
        CityCode.objects.create(city_code ="3538006",
                                city_name ="Pindamonhangaba" )
            
        CityCode.objects.create(city_code ="3538105",
                                city_name ="Pindorama" )
            
        CityCode.objects.create(city_code ="3538204",
                                city_name ="Pinhalzinho" )
            
        CityCode.objects.create(city_code ="3538303",
                                city_name ="Piquerobi" )
            
        CityCode.objects.create(city_code ="3538501",
                                city_name ="Piquete" )
            
        CityCode.objects.create(city_code ="3538600",
                                city_name ="Piracaia" )
            
        CityCode.objects.create(city_code ="3538709",
                                city_name ="Piracicaba" )
            
        CityCode.objects.create(city_code ="3538808",
                                city_name ="Piraju" )
            
        CityCode.objects.create(city_code ="3538907",
                                city_name ="Pirajuí" )
            
        CityCode.objects.create(city_code ="3539004",
                                city_name ="Pirangi" )
            
        CityCode.objects.create(city_code ="3539103",
                                city_name ="Pirapora do Bom Jesus" )
            
        CityCode.objects.create(city_code ="3539202",
                                city_name ="Pirapozinho" )
            
        CityCode.objects.create(city_code ="3539301",
                                city_name ="Pirassununga" )
            
        CityCode.objects.create(city_code ="3539400",
                                city_name ="Piratininga" )
            
        CityCode.objects.create(city_code ="3539509",
                                city_name ="Pitangueiras" )
            
        CityCode.objects.create(city_code ="3539608",
                                city_name ="Planalto" )
            
        CityCode.objects.create(city_code ="3539707",
                                city_name ="Platina" )
            
        CityCode.objects.create(city_code ="3539806",
                                city_name ="Poá" )
            
        CityCode.objects.create(city_code ="3539905",
                                city_name ="Poloni" )
            
        CityCode.objects.create(city_code ="3540002",
                                city_name ="Pompéia" )
            
        CityCode.objects.create(city_code ="3540101",
                                city_name ="Pongaí" )
            
        CityCode.objects.create(city_code ="3540200",
                                city_name ="Pontal" )
            
        CityCode.objects.create(city_code ="3540259",
                                city_name ="Pontalinda" )
            
        CityCode.objects.create(city_code ="3540309",
                                city_name ="Pontes Gestal" )
            
        CityCode.objects.create(city_code ="3540408",
                                city_name ="Populina" )
            
        CityCode.objects.create(city_code ="3540507",
                                city_name ="Porangaba" )
            
        CityCode.objects.create(city_code ="3540606",
                                city_name ="Porto Feliz" )
            
        CityCode.objects.create(city_code ="3540705",
                                city_name ="Porto Ferreira" )
            
        CityCode.objects.create(city_code ="3540754",
                                city_name ="Potim" )
            
        CityCode.objects.create(city_code ="3540804",
                                city_name ="Potirendaba" )
            
        CityCode.objects.create(city_code ="3540853",
                                city_name ="Pracinha" )
            
        CityCode.objects.create(city_code ="3540903",
                                city_name ="Pradópolis" )
            
        CityCode.objects.create(city_code ="3541000",
                                city_name ="Praia Grande" )
            
        CityCode.objects.create(city_code ="3541059",
                                city_name ="Pratânia" )
            
        CityCode.objects.create(city_code ="3541109",
                                city_name ="Presidente Alves" )
            
        CityCode.objects.create(city_code ="3541208",
                                city_name ="Presidente Bernardes" )
            
        CityCode.objects.create(city_code ="3541307",
                                city_name ="Presidente Epitácio" )
            
        CityCode.objects.create(city_code ="3541406",
                                city_name ="Presidente Prudente" )
            
        CityCode.objects.create(city_code ="3541505",
                                city_name ="Presidente Venceslau" )
            
        CityCode.objects.create(city_code ="3541604",
                                city_name ="Promissão" )
            
        CityCode.objects.create(city_code ="3541653",
                                city_name ="Quadra" )
            
        CityCode.objects.create(city_code ="3541703",
                                city_name ="Quatá" )
            
        CityCode.objects.create(city_code ="3541802",
                                city_name ="Queiroz" )
            
        CityCode.objects.create(city_code ="3541901",
                                city_name ="Queluz" )
            
        CityCode.objects.create(city_code ="3542008",
                                city_name ="Quintana" )
            
        CityCode.objects.create(city_code ="3542107",
                                city_name ="Rafard" )
            
        CityCode.objects.create(city_code ="3542206",
                                city_name ="Rancharia" )
            
        CityCode.objects.create(city_code ="3542305",
                                city_name ="Redenção da Serra" )
            
        CityCode.objects.create(city_code ="3542404",
                                city_name ="Regente Feijó" )
            
        CityCode.objects.create(city_code ="3542503",
                                city_name ="Reginópolis" )
            
        CityCode.objects.create(city_code ="3542602",
                                city_name ="Registro" )
            
        CityCode.objects.create(city_code ="3542701",
                                city_name ="Restinga" )
            
        CityCode.objects.create(city_code ="3542800",
                                city_name ="Ribeira" )
            
        CityCode.objects.create(city_code ="3542909",
                                city_name ="Ribeirão Bonito" )
            
        CityCode.objects.create(city_code ="3543006",
                                city_name ="Ribeirão Branco" )
            
        CityCode.objects.create(city_code ="3543105",
                                city_name ="Ribeirão Corrente" )
            
        CityCode.objects.create(city_code ="3543204",
                                city_name ="Ribeirão do Sul" )
            
        CityCode.objects.create(city_code ="3543238",
                                city_name ="Ribeirão dos Índios" )
            
        CityCode.objects.create(city_code ="3543253",
                                city_name ="Ribeirão Grande" )
            
        CityCode.objects.create(city_code ="3543303",
                                city_name ="Ribeirão Pires" )
            
        CityCode.objects.create(city_code ="3543402",
                                city_name ="Ribeirão Preto" )
            
        CityCode.objects.create(city_code ="3543600",
                                city_name ="Rifaina" )
            
        CityCode.objects.create(city_code ="3543709",
                                city_name ="Rincão" )
            
        CityCode.objects.create(city_code ="3543808",
                                city_name ="Rinópolis" )
            
        CityCode.objects.create(city_code ="3543907",
                                city_name ="Rio Claro" )
            
        CityCode.objects.create(city_code ="3544004",
                                city_name ="Rio das Pedras" )
            
        CityCode.objects.create(city_code ="3544103",
                                city_name ="Rio Grande da Serra" )
            
        CityCode.objects.create(city_code ="3544202",
                                city_name ="Riolândia" )
            
        CityCode.objects.create(city_code ="3543501",
                                city_name ="Riversul" )
            
        CityCode.objects.create(city_code ="3544251",
                                city_name ="Rosana" )
            
        CityCode.objects.create(city_code ="3544301",
                                city_name ="Roseira" )
            
        CityCode.objects.create(city_code ="3544400",
                                city_name ="Rubiácea" )
            
        CityCode.objects.create(city_code ="3544509",
                                city_name ="Rubinéia" )
            
        CityCode.objects.create(city_code ="3544608",
                                city_name ="Sabino" )
            
        CityCode.objects.create(city_code ="3544707",
                                city_name ="Sagres" )
            
        CityCode.objects.create(city_code ="3544806",
                                city_name ="Sales" )
            
        CityCode.objects.create(city_code ="3544905",
                                city_name ="Sales Oliveira" )
            
        CityCode.objects.create(city_code ="3545001",
                                city_name ="Salesópolis" )
            
        CityCode.objects.create(city_code ="3545100",
                                city_name ="Salmourão" )
            
        CityCode.objects.create(city_code ="3545159",
                                city_name ="Saltinho" )
            
        CityCode.objects.create(city_code ="3545209",
                                city_name ="Salto" )
            
        CityCode.objects.create(city_code ="3545308",
                                city_name ="Salto de Pirapora" )
            
        CityCode.objects.create(city_code ="3545407",
                                city_name ="Salto Grande" )
            
        CityCode.objects.create(city_code ="3545506",
                                city_name ="Sandovalina" )
            
        CityCode.objects.create(city_code ="3545605",
                                city_name ="Santa Adélia" )
            
        CityCode.objects.create(city_code ="3545704",
                                city_name ="Santa Albertina" )
            
        CityCode.objects.create(city_code ="3545803",
                                city_name ="Santa Bárbara d'Oeste" )
            
        CityCode.objects.create(city_code ="3546009",
                                city_name ="Santa Branca" )
            
        CityCode.objects.create(city_code ="3546108",
                                city_name ="Santa Clara d'Oeste" )
            
        CityCode.objects.create(city_code ="3546207",
                                city_name ="Santa Cruz da Conceição" )
            
        CityCode.objects.create(city_code ="3546256",
                                city_name ="Santa Cruz da Esperança" )
            
        CityCode.objects.create(city_code ="3546306",
                                city_name ="Santa Cruz das Palmeiras" )
            
        CityCode.objects.create(city_code ="3546405",
                                city_name ="Santa Cruz do Rio Pardo" )
            
        CityCode.objects.create(city_code ="3546504",
                                city_name ="Santa Ernestina" )
            
        CityCode.objects.create(city_code ="3546603",
                                city_name ="Santa Fé do Sul" )
            
        CityCode.objects.create(city_code ="3546702",
                                city_name ="Santa Gertrudes" )
            
        CityCode.objects.create(city_code ="3546801",
                                city_name ="Santa Isabel" )
            
        CityCode.objects.create(city_code ="3546900",
                                city_name ="Santa Lúcia" )
            
        CityCode.objects.create(city_code ="3547007",
                                city_name ="Santa Maria da Serra" )
            
        CityCode.objects.create(city_code ="3547106",
                                city_name ="Santa Mercedes" )
            
        CityCode.objects.create(city_code ="3547502",
                                city_name ="Santa Rita do Passa Quatro" )
            
        CityCode.objects.create(city_code ="3547403",
                                city_name ="Santa Rita d'Oeste" )
            
        CityCode.objects.create(city_code ="3547601",
                                city_name ="Santa Rosa de Viterbo" )
            
        CityCode.objects.create(city_code ="3547650",
                                city_name ="Santa Salete" )
            
        CityCode.objects.create(city_code ="3547205",
                                city_name ="Santana da Ponte Pensa" )
            
        CityCode.objects.create(city_code ="3547304",
                                city_name ="Santana de Parnaíba" )
            
        CityCode.objects.create(city_code ="3547700",
                                city_name ="Santo Anastácio" )
            
        CityCode.objects.create(city_code ="3547809",
                                city_name ="Santo André" )
            
        CityCode.objects.create(city_code ="3547908",
                                city_name ="Santo Antônio da Alegria" )
            
        CityCode.objects.create(city_code ="3548005",
                                city_name ="Santo Antônio de Posse" )
            
        CityCode.objects.create(city_code ="3548054",
                                city_name ="Santo Antônio do Aracanguá" )
            
        CityCode.objects.create(city_code ="3548104",
                                city_name ="Santo Antônio do Jardim" )
            
        CityCode.objects.create(city_code ="3548203",
                                city_name ="Santo Antônio do Pinhal" )
            
        CityCode.objects.create(city_code ="3548302",
                                city_name ="Santo Expedito" )
            
        CityCode.objects.create(city_code ="3548401",
                                city_name ="Santópolis do Aguapeí" )
            
        CityCode.objects.create(city_code ="3548500",
                                city_name ="Santos" )
            
        CityCode.objects.create(city_code ="3548609",
                                city_name ="São Bento do Sapucaí" )
            
        CityCode.objects.create(city_code ="3548708",
                                city_name ="São Bernardo do Campo" )
            
        CityCode.objects.create(city_code ="3548807",
                                city_name ="São Caetano do Sul" )
            
        CityCode.objects.create(city_code ="3548906",
                                city_name ="São Carlos" )
            
        CityCode.objects.create(city_code ="3549003",
                                city_name ="São Francisco" )
            
        CityCode.objects.create(city_code ="3549102",
                                city_name ="São João da Boa Vista" )
            
        CityCode.objects.create(city_code ="3549201",
                                city_name ="São João das Duas Pontes" )
            
        CityCode.objects.create(city_code ="3549250",
                                city_name ="São João de Iracema" )
            
        CityCode.objects.create(city_code ="3549300",
                                city_name ="São João do Pau d'Alho" )
            
        CityCode.objects.create(city_code ="3549409",
                                city_name ="São Joaquim da Barra" )
            
        CityCode.objects.create(city_code ="3549508",
                                city_name ="São José da Bela Vista" )
            
        CityCode.objects.create(city_code ="3549607",
                                city_name ="São José do Barreiro" )
            
        CityCode.objects.create(city_code ="3549706",
                                city_name ="São José do Rio Pardo" )
            
        CityCode.objects.create(city_code ="3549805",
                                city_name ="São José do Rio Preto" )
            
        CityCode.objects.create(city_code ="3549904",
                                city_name ="São José dos Campos" )
            
        CityCode.objects.create(city_code ="3549953",
                                city_name ="São Lourenço da Serra" )
            
        CityCode.objects.create(city_code ="3550001",
                                city_name ="São Luiz do Paraitinga" )
            
        CityCode.objects.create(city_code ="3550100",
                                city_name ="São Manuel" )
            
        CityCode.objects.create(city_code ="3550209",
                                city_name ="São Miguel Arcanjo" )
            
        CityCode.objects.create(city_code ="3550308",
                                city_name ="São Paulo" )
            
        CityCode.objects.create(city_code ="3550407",
                                city_name ="São Pedro" )
            
        CityCode.objects.create(city_code ="3550506",
                                city_name ="São Pedro do Turvo" )
            
        CityCode.objects.create(city_code ="3550605",
                                city_name ="São Roque" )
            
        CityCode.objects.create(city_code ="3550704",
                                city_name ="São Sebastião" )
            
        CityCode.objects.create(city_code ="3550803",
                                city_name ="São Sebastião da Grama" )
            
        CityCode.objects.create(city_code ="3550902",
                                city_name ="São Simão" )
            
        CityCode.objects.create(city_code ="3551009",
                                city_name ="São Vicente" )
            
        CityCode.objects.create(city_code ="3551108",
                                city_name ="Sarapuí" )
            
        CityCode.objects.create(city_code ="3551207",
                                city_name ="Sarutaiá" )
            
        CityCode.objects.create(city_code ="3551306",
                                city_name ="Sebastianópolis do Sul" )
            
        CityCode.objects.create(city_code ="3551405",
                                city_name ="Serra Azul" )
            
        CityCode.objects.create(city_code ="3551603",
                                city_name ="Serra Negra" )
            
        CityCode.objects.create(city_code ="3551504",
                                city_name ="Serrana" )
            
        CityCode.objects.create(city_code ="3551702",
                                city_name ="Sertãozinho" )
            
        CityCode.objects.create(city_code ="3551801",
                                city_name ="Sete Barras" )
            
        CityCode.objects.create(city_code ="3551900",
                                city_name ="Severínia" )
            
        CityCode.objects.create(city_code ="3552007",
                                city_name ="Silveiras" )
            
        CityCode.objects.create(city_code ="3552106",
                                city_name ="Socorro" )
            
        CityCode.objects.create(city_code ="3552205",
                                city_name ="Sorocaba" )
            
        CityCode.objects.create(city_code ="3552304",
                                city_name ="Sud Mennucci" )
            
        CityCode.objects.create(city_code ="3552403",
                                city_name ="Sumaré" )
            
        CityCode.objects.create(city_code ="3552551",
                                city_name ="Suzanápolis" )
            
        CityCode.objects.create(city_code ="3552502",
                                city_name ="Suzano" )
            
        CityCode.objects.create(city_code ="3552601",
                                city_name ="Tabapuã" )
            
        CityCode.objects.create(city_code ="3552700",
                                city_name ="Tabatinga" )
            
        CityCode.objects.create(city_code ="3552809",
                                city_name ="Taboão da Serra" )
            
        CityCode.objects.create(city_code ="3552908",
                                city_name ="Taciba" )
            
        CityCode.objects.create(city_code ="3553005",
                                city_name ="Taguaí" )
            
        CityCode.objects.create(city_code ="3553104",
                                city_name ="Taiaçu" )
            
        CityCode.objects.create(city_code ="3553203",
                                city_name ="Taiúva" )
            
        CityCode.objects.create(city_code ="3553302",
                                city_name ="Tambaú" )
            
        CityCode.objects.create(city_code ="3553401",
                                city_name ="Tanabi" )
            
        CityCode.objects.create(city_code ="3553500",
                                city_name ="Tapiraí" )
            
        CityCode.objects.create(city_code ="3553609",
                                city_name ="Tapiratiba" )
            
        CityCode.objects.create(city_code ="3553658",
                                city_name ="Taquaral" )
            
        CityCode.objects.create(city_code ="3553708",
                                city_name ="Taquaritinga" )
            
        CityCode.objects.create(city_code ="3553807",
                                city_name ="Taquarituba" )
            
        CityCode.objects.create(city_code ="3553856",
                                city_name ="Taquarivaí" )
            
        CityCode.objects.create(city_code ="3553906",
                                city_name ="Tarabai" )
            
        CityCode.objects.create(city_code ="3553955",
                                city_name ="Tarumã" )
            
        CityCode.objects.create(city_code ="3554003",
                                city_name ="Tatuí" )
            
        CityCode.objects.create(city_code ="3554102",
                                city_name ="Taubaté" )
            
        CityCode.objects.create(city_code ="3554201",
                                city_name ="Tejupá" )
            
        CityCode.objects.create(city_code ="3554300",
                                city_name ="Teodoro Sampaio" )
            
        CityCode.objects.create(city_code ="3554409",
                                city_name ="Terra Roxa" )
            
        CityCode.objects.create(city_code ="3554508",
                                city_name ="Tietê" )
            
        CityCode.objects.create(city_code ="3554607",
                                city_name ="Timburi" )
            
        CityCode.objects.create(city_code ="3554656",
                                city_name ="Torre de Pedra" )
            
        CityCode.objects.create(city_code ="3554706",
                                city_name ="Torrinha" )
            
        CityCode.objects.create(city_code ="3554755",
                                city_name ="Trabiju" )
            
        CityCode.objects.create(city_code ="3554805",
                                city_name ="Tremembé" )
            
        CityCode.objects.create(city_code ="3554904",
                                city_name ="Três Fronteiras" )
            
        CityCode.objects.create(city_code ="3554953",
                                city_name ="Tuiuti" )
            
        CityCode.objects.create(city_code ="3555000",
                                city_name ="Tupã" )
            
        CityCode.objects.create(city_code ="3555109",
                                city_name ="Tupi Paulista" )
            
        CityCode.objects.create(city_code ="3555208",
                                city_name ="Turiúba" )
            
        CityCode.objects.create(city_code ="3555307",
                                city_name ="Turmalina" )
            
        CityCode.objects.create(city_code ="3555356",
                                city_name ="Ubarana" )
            
        CityCode.objects.create(city_code ="3555406",
                                city_name ="Ubatuba" )
            
        CityCode.objects.create(city_code ="3555505",
                                city_name ="Ubirajara" )
            
        CityCode.objects.create(city_code ="3555604",
                                city_name ="Uchoa" )
            
        CityCode.objects.create(city_code ="3555703",
                                city_name ="União Paulista" )
            
        CityCode.objects.create(city_code ="3555802",
                                city_name ="Urânia" )
            
        CityCode.objects.create(city_code ="3555901",
                                city_name ="Uru" )
            
        CityCode.objects.create(city_code ="3556008",
                                city_name ="Urupês" )
            
        CityCode.objects.create(city_code ="3556107",
                                city_name ="Valentim Gentil" )
            
        CityCode.objects.create(city_code ="3556206",
                                city_name ="Valinhos" )
            
        CityCode.objects.create(city_code ="3556305",
                                city_name ="Valparaíso" )
            
        CityCode.objects.create(city_code ="3556354",
                                city_name ="Vargem" )
            
        CityCode.objects.create(city_code ="3556404",
                                city_name ="Vargem Grande do Sul" )
            
        CityCode.objects.create(city_code ="3556453",
                                city_name ="Vargem Grande Paulista" )
            
        CityCode.objects.create(city_code ="3556503",
                                city_name ="Várzea Paulista" )
            
        CityCode.objects.create(city_code ="3556602",
                                city_name ="Vera Cruz" )
            
        CityCode.objects.create(city_code ="3556701",
                                city_name ="Vinhedo" )
            
        CityCode.objects.create(city_code ="3556800",
                                city_name ="Viradouro" )
            
        CityCode.objects.create(city_code ="3556909",
                                city_name ="Vista Alegre do Alto" )
            
        CityCode.objects.create(city_code ="3556958",
                                city_name ="Vitória Brasil" )
            
        CityCode.objects.create(city_code ="3557006",
                                city_name ="Votorantim" )
            
        CityCode.objects.create(city_code ="3557105",
                                city_name ="Votuporanga" )
            
        CityCode.objects.create(city_code ="3557154",
                                city_name ="Zacarias")

        CityCode.objects.create(city_code ="4100103", 
                                city_name ="Abatiá" )

        CityCode.objects.create(city_code ="4100202", 
                                city_name ="Adrianópolis")
            
        CityCode.objects.create(city_code ="4100301", 
                                city_name ="Agudos do Sul")

        CityCode.objects.create(city_code ="4100400", 
                                city_name ="Almirante Tamandaré")

        CityCode.objects.create(city_code ="4100459", 
                                city_name ="Altamira do Paraná")

        CityCode.objects.create(city_code ="4128625", 
                                city_name ="Alto Paraíso")

        CityCode.objects.create(city_code ="4100608", 
                                city_name ="Alto Paraná")

        CityCode.objects.create(city_code ="4100707", 
                                city_name ="Alto Piquiri")

        CityCode.objects.create(city_code ="4100509", 
                                city_name ="Altônia")

        CityCode.objects.create(city_code ="4100806", 
                                city_name ="Alvorada do Sul")

        CityCode.objects.create(city_code ="4100905", 
                                city_name ="Amaporã")

        CityCode.objects.create(city_code ="4101002", 
                                city_name ="Ampére")

        CityCode.objects.create(city_code ="4101051", 
                                city_name ="Anahy")

        CityCode.objects.create(city_code ="4101101", 
                                city_name ="Andirá")

        CityCode.objects.create(city_code ="4101150", 
                                city_name ="Ângulo")

        CityCode.objects.create(city_code ="4101200", 
                                city_name ="Antonina")

        CityCode.objects.create(city_code ="4101309", 
                                city_name ="Antônio Olinto")

        CityCode.objects.create(city_code ="4101408", 
                                city_name ="Apucarana")

        CityCode.objects.create(city_code ="4101507", 
                                city_name ="Arapongas")

        CityCode.objects.create(city_code ="4101606", 
                                city_name ="Arapoti")

        CityCode.objects.create(city_code ="4101655", 
                                city_name ="Arapuã")

        CityCode.objects.create(city_code ="4101705", 
                                city_name ="Araruna")

        CityCode.objects.create(city_code ="4101804", 
                                city_name ="Araucária")

        CityCode.objects.create(city_code ="4101853", 
                                city_name ="Ariranha do Ivaí")

        CityCode.objects.create(city_code ="4101903", 
                                city_name ="Assaí")

        CityCode.objects.create(city_code ="4102000", 
                                city_name ="Assis Chateaubriand")

        CityCode.objects.create(city_code ="4102109", 
                                city_name ="Astorga")

        CityCode.objects.create(city_code ="4102208", 
                                city_name ="Atalaia")

        CityCode.objects.create(city_code ="4102307", 
                                city_name ="Balsa Nova")

        CityCode.objects.create(city_code ="4102406", 
                                city_name ="Bandeirantes")

        CityCode.objects.create(city_code ="4102505", 
                                city_name ="Barbosa Ferraz")

        CityCode.objects.create(city_code ="4102703", 
                                city_name ="Barra do Jacaré")

        CityCode.objects.create(city_code ="4102604", 
                                city_name ="Barracão")

        CityCode.objects.create(city_code ="4102752", 
                                city_name ="Bela Vista da Caroba")

        CityCode.objects.create(city_code ="4102802", 
                                city_name ="Bela Vista do Paraíso")

        CityCode.objects.create(city_code ="4102901", 
                                city_name ="Bituruna")

        CityCode.objects.create(city_code ="4103008", 
                                city_name ="Boa Esperança")

        CityCode.objects.create(city_code ="4103024", 
                                city_name ="Boa Esperança do Iguaçu")

        CityCode.objects.create(city_code ="4103040", 
                                city_name ="Boa Ventura de São Roque")

        CityCode.objects.create(city_code ="4103057", 
                                city_name ="Boa Vista da Aparecida")

        CityCode.objects.create(city_code ="4103107", 
                                city_name ="Bocaiúva do Sul")

        CityCode.objects.create(city_code ="4103156", 
                                city_name ="Bom Jesus do Sul")

        CityCode.objects.create(city_code ="4103206", 
                                city_name ="Bom Sucesso")

        CityCode.objects.create(city_code ="4103222", 
                                city_name ="Bom Sucesso do Sul")

        CityCode.objects.create(city_code ="4103305", 
                                city_name ="Borrazópolis")

        CityCode.objects.create(city_code ="4103354", 
                                city_name ="Braganey")

        CityCode.objects.create(city_code ="4103370", 
                                city_name ="Brasilândia do Sul")

        CityCode.objects.create(city_code ="4103404", 
                                city_name ="Cafeara")

        CityCode.objects.create(city_code ="4103453", 
                                city_name ="Cafelândia")

        CityCode.objects.create(city_code ="4103479", 
                                city_name ="Cafezal do Sul")

        CityCode.objects.create(city_code ="4103503", 
                                city_name ="Califórnia")

        CityCode.objects.create(city_code ="4103602", 
                                city_name ="Cambará")

        CityCode.objects.create(city_code ="4103701", 
                                city_name ="Cambé")

        CityCode.objects.create(city_code ="4103800", 
                                city_name ="Cambira")

        CityCode.objects.create(city_code ="4103909", 
                                city_name ="Campina da Lagoa")

        CityCode.objects.create(city_code ="4103958", 
                                city_name ="Campina do Simão")

        CityCode.objects.create(city_code ="4104006", 
                                city_name ="Campina Grande do Sul")

        CityCode.objects.create(city_code ="4104055", 
                                city_name ="Campo Bonito")

        CityCode.objects.create(city_code ="4104105", 
                                city_name ="Campo do Tenente")

        CityCode.objects.create(city_code ="4104204", 
                                city_name ="Campo Largo")

        CityCode.objects.create(city_code ="4104253", 
                                city_name ="Campo Magro")

        CityCode.objects.create(city_code ="4104303", 
                                city_name ="Campo Mourão")

        CityCode.objects.create(city_code ="4104402", 
                                city_name ="Cândido de Abreu")

        CityCode.objects.create(city_code ="4104428", 
                                city_name ="Candói")

        CityCode.objects.create(city_code ="4104451", 
                                city_name ="Cantagalo")

        CityCode.objects.create(city_code ="4104501", 
                                city_name ="Capanema")

        CityCode.objects.create(city_code ="4104600", 
                                city_name ="Capitão Leônidas Marques")

        CityCode.objects.create(city_code ="4104659", 
                                city_name ="Carambeí")

        CityCode.objects.create(city_code ="4104709", 
                                city_name ="Carlópolis")

        CityCode.objects.create(city_code ="4104808", 
                                city_name ="Cascavel")

        CityCode.objects.create(city_code ="4104907", 
                                city_name ="Castro")

        CityCode.objects.create(city_code ="4105003", 
                                city_name ="Catanduvas")

        CityCode.objects.create(city_code ="4105102", 
                                city_name ="Centenário do Sul")

        CityCode.objects.create(city_code ="4105201", 
                                city_name ="Cerro Azul")

        CityCode.objects.create(city_code ="4105300", 
                                city_name ="Céu Azul")

        CityCode.objects.create(city_code ="4105409", 
                                city_name ="Chopinzinho")

        CityCode.objects.create(city_code ="4105508", 
                                city_name ="Cianorte")

        CityCode.objects.create(city_code ="4105607", 
                                city_name ="Cidade Gaúcha")

        CityCode.objects.create(city_code ="4105706", 
                                city_name ="Clevelândia")

        CityCode.objects.create(city_code ="4105805", 
                                city_name ="Colombo")

        CityCode.objects.create(city_code ="4105904", 
                                city_name ="Colorado")

        CityCode.objects.create(city_code ="4106001", 
                                city_name ="Congonhinhas")

        CityCode.objects.create(city_code ="4106100", 
                                city_name ="Conselheiro Mairinck")

        CityCode.objects.create(city_code ="4106209", 
                                city_name ="Contenda")

        CityCode.objects.create(city_code ="4106308", 
                                city_name ="Corbélia")

        CityCode.objects.create(city_code ="4106407", 
                                city_name ="Cornélio Procópio")

        CityCode.objects.create(city_code ="4106456", 
                                city_name ="Coronel Domingos Soares")

        CityCode.objects.create(city_code ="4106506", 
                                city_name ="Coronel Vivida")

        CityCode.objects.create(city_code ="4106555", 
                                city_name ="Corumbataí do Sul")

        CityCode.objects.create(city_code ="4106803", 
                                city_name ="Cruz Machado")

        CityCode.objects.create(city_code ="4106571", 
                                city_name ="Cruzeiro do Iguaçu")

        CityCode.objects.create(city_code ="4106605", 
                                city_name ="Cruzeiro do Oeste")

        CityCode.objects.create(city_code ="4106704", 
                                city_name ="Cruzeiro do Sul")

        CityCode.objects.create(city_code ="4106852", 
                                city_name ="Cruzmaltina")

        CityCode.objects.create(city_code ="4106902", 
                                city_name ="Curitiba")

        CityCode.objects.create(city_code ="4107009", 
                                city_name ="Curiúva")

        CityCode.objects.create(city_code ="4107108", 
                                city_name ="Diamante do Norte")

        CityCode.objects.create(city_code ="4107124", 
                                city_name ="Diamante do Sul")

        CityCode.objects.create(city_code ="4107157", 
                                city_name ="Diamante D'Oeste")

        CityCode.objects.create(city_code ="4107207", 
                                city_name ="Dois Vizinhos")

        CityCode.objects.create(city_code ="4107256", 
                                city_name ="Douradina")

        CityCode.objects.create(city_code ="4107306", 
                                city_name ="Doutor Camargo")

        CityCode.objects.create(city_code ="4128633", 
                                city_name ="Doutor Ulysses")

        CityCode.objects.create(city_code ="4107405", 
                                city_name ="Enéas Marques")

        CityCode.objects.create(city_code ="4107504", 
                                city_name ="Engenheiro Beltrão")

        CityCode.objects.create(city_code ="4107538", 
                                city_name ="Entre Rios do Oeste")

        CityCode.objects.create(city_code ="4107520", 
                                city_name ="Esperança Nova")

        CityCode.objects.create(city_code ="4107546", 
                                city_name ="Espigão Alto do Iguaçu")

        CityCode.objects.create(city_code ="4107553", 
                                city_name ="Farol")

        CityCode.objects.create(city_code ="4107603", 
                                city_name ="Faxinal")

        CityCode.objects.create(city_code ="4107652", 
                                city_name ="Fazenda Rio Grande")

        CityCode.objects.create(city_code ="4107702", 
                                city_name ="Fênix")

        CityCode.objects.create(city_code ="4107736", 
                                city_name ="Fernandes Pinheiro")

        CityCode.objects.create(city_code ="4107751", 
                                city_name ="Figueira")

        CityCode.objects.create(city_code ="4107850", 
                                city_name ="Flor da Serra do Sul")

        CityCode.objects.create(city_code ="4107801", 
                                city_name ="Floraí")

        CityCode.objects.create(city_code ="4107900", 
                                city_name ="Floresta")

        CityCode.objects.create(city_code ="4108007", 
                                city_name ="Florestópolis")

        CityCode.objects.create(city_code ="4108106", 
                                city_name ="Flórida")

        CityCode.objects.create(city_code ="4108205", 
                                city_name ="Formosa do Oeste")

        CityCode.objects.create(city_code ="4108304", 
                                city_name ="Foz do Iguaçu")

        CityCode.objects.create(city_code ="4108452", 
                                city_name ="Foz do Jordão")

        CityCode.objects.create(city_code ="4108320", 
                                city_name ="Francisco Alves")

        CityCode.objects.create(city_code ="4108403", 
                                city_name ="Francisco Beltrão")

        CityCode.objects.create(city_code ="4108502", 
                                city_name ="General Carneiro")

        CityCode.objects.create(city_code ="4108551", 
                                city_name ="Godoy Moreira")

        CityCode.objects.create(city_code ="4108601", 
                                city_name ="Goioerê")

        CityCode.objects.create(city_code ="4108650", 
                                city_name ="Goioxim")

        CityCode.objects.create(city_code ="4108700", 
                                city_name ="Grandes Rios")

        CityCode.objects.create(city_code ="4108809", 
                                city_name ="Guaíra")

        CityCode.objects.create(city_code ="4108908", 
                                city_name ="Guairaçá")

        CityCode.objects.create(city_code ="4108957", 
                                city_name ="Guamiranga")

        CityCode.objects.create(city_code ="4109005", 
                                city_name ="Guapirama")

        CityCode.objects.create(city_code ="4109104", 
                                city_name ="Guaporema")

        CityCode.objects.create(city_code ="4109203", 
                                city_name ="Guaraci")

        CityCode.objects.create(city_code ="4109302", 
                                city_name ="Guaraniaçu")

        CityCode.objects.create(city_code ="4109401", 
                                city_name ="Guarapuava")

        CityCode.objects.create(city_code ="4109500", 
                                city_name ="Guaraqueçaba")

        CityCode.objects.create(city_code ="4109609", 
                                city_name ="Guaratuba")

        CityCode.objects.create(city_code ="4109658", 
                                city_name ="Honório Serpa")

        CityCode.objects.create(city_code ="4109708", 
                                city_name ="Ibaiti")

        CityCode.objects.create(city_code ="4109757", 
                                city_name ="Ibema")

        CityCode.objects.create(city_code ="4109807", 
                                city_name ="Ibiporã")

        CityCode.objects.create(city_code ="4109906", 
                                city_name ="Icaraíma")

        CityCode.objects.create(city_code ="4110003", 
                                city_name ="Iguaraçu")

        CityCode.objects.create(city_code ="4110052", 
                                city_name ="Iguatu")

        CityCode.objects.create(city_code ="4110078", 
                                city_name ="Imbaú")

        CityCode.objects.create(city_code ="4110102", 
                                city_name ="Imbituva")

        CityCode.objects.create(city_code ="4110201", 
                                city_name ="Inácio Martins")

        CityCode.objects.create(city_code ="4110300", 
                                city_name ="Inajá")

        CityCode.objects.create(city_code ="4110409", 
                                city_name ="Indianópolis")

        CityCode.objects.create(city_code ="4110508", 
                                city_name ="Ipiranga")

        CityCode.objects.create(city_code ="4110607", 
                                city_name ="Iporã")

        CityCode.objects.create(city_code ="4110656", 
                                city_name ="Iracema do Oeste")

        CityCode.objects.create(city_code ="4110706", 
                                city_name ="Irati")

        CityCode.objects.create(city_code ="4110805", 
                                city_name ="Iretama")

        CityCode.objects.create(city_code ="4110904", 
                                city_name ="Itaguajé")

        CityCode.objects.create(city_code ="4110953", 
                                city_name ="Itaipulândia")

        CityCode.objects.create(city_code ="4111001", 
                                city_name ="Itambaracá")

        CityCode.objects.create(city_code ="4111100", 
                                city_name ="Itambé")

        CityCode.objects.create(city_code ="4111209", 
                                city_name ="Itapejara d'Oeste")

        CityCode.objects.create(city_code ="4111258", 
                                city_name ="Itaperuçu")

        CityCode.objects.create(city_code ="4111308", 
                                city_name ="Itaúna do Sul")

        CityCode.objects.create(city_code ="4111407", 
                                city_name ="Ivaí")

        CityCode.objects.create(city_code ="4111506", 
                                city_name ="Ivaiporã")

        CityCode.objects.create(city_code ="4111555", 
                                city_name ="Ivaté")

        CityCode.objects.create(city_code ="4111605", 
                                city_name ="Ivatuba")

        CityCode.objects.create(city_code ="4111704", 
                                city_name ="Jaboti")

        CityCode.objects.create(city_code ="4111803", 
                                city_name ="Jacarezinho")

        CityCode.objects.create(city_code ="4111902", 
                                city_name ="Jaguapitã")

        CityCode.objects.create(city_code ="4112009", 
                                city_name ="Jaguariaíva")

        CityCode.objects.create(city_code ="4112108", 
                                city_name ="Jandaia do Sul")

        CityCode.objects.create(city_code ="4112207", 
                                city_name ="Janiópolis")

        CityCode.objects.create(city_code ="4112306", 
                                city_name ="Japira")

        CityCode.objects.create(city_code ="4112405", 
                                city_name ="Japurá")

        CityCode.objects.create(city_code ="4112504", 
                                city_name ="Jardim Alegre")

        CityCode.objects.create(city_code ="4112603", 
                                city_name ="Jardim Olinda")

        CityCode.objects.create(city_code ="4112702", 
                                city_name ="Jataizinho")

        CityCode.objects.create(city_code ="4112751", 
                                city_name ="Jesuítas")

        CityCode.objects.create(city_code ="4112801", 
                                city_name ="Joaquim Távora")

        CityCode.objects.create(city_code ="4112900", 
                                city_name ="Jundiaí do Sul")

        CityCode.objects.create(city_code ="4112959", 
                                city_name ="Juranda")

        CityCode.objects.create(city_code ="4113007", 
                                city_name ="Jussara")

        CityCode.objects.create(city_code ="4113106", 
                                city_name ="Kaloré")

        CityCode.objects.create(city_code ="4113205", 
                                city_name ="Lapa")

        CityCode.objects.create(city_code ="4113254", 
                                city_name ="Laranjal")

        CityCode.objects.create(city_code ="4113304", 
                                city_name ="Laranjeiras do Sul")

        CityCode.objects.create(city_code ="4113403", 
                                city_name ="Leópolis")

        CityCode.objects.create(city_code ="4113429", 
                                city_name ="Lidianópolis")

        CityCode.objects.create(city_code ="4113452", 
                                city_name ="Lindoeste")

        CityCode.objects.create(city_code ="4113502", 
                                city_name ="Loanda")

        CityCode.objects.create(city_code ="4113601", 
                                city_name ="Lobato")

        CityCode.objects.create(city_code ="4113700", 
                                city_name ="Londrina")

        CityCode.objects.create(city_code ="4113734", 
                                city_name ="Luiziana")

        CityCode.objects.create(city_code ="4113759", 
                                city_name ="Lunardelli")

        CityCode.objects.create(city_code ="4113809", 
                                city_name ="Lupionópolis")

        CityCode.objects.create(city_code ="4113908", 
                                city_name ="Mallet")

        CityCode.objects.create(city_code ="4114005", 
                                city_name ="Mamborê")

        CityCode.objects.create(city_code ="4114104", 
                                city_name ="Mandaguaçu")

        CityCode.objects.create(city_code ="4114203", 
                                city_name ="Mandaguari")

        CityCode.objects.create(city_code ="4114302", 
                                city_name ="Mandirituba")

        CityCode.objects.create(city_code ="4114351", 
                                city_name ="Manfrinópolis")

        CityCode.objects.create(city_code ="4114401", 
                                city_name ="Mangueirinha")

        CityCode.objects.create(city_code ="4114500", 
                                city_name ="Manoel Ribas")

        CityCode.objects.create(city_code ="4114609", 
                                city_name ="Marechal Cândido Rondon")

        CityCode.objects.create(city_code ="4114708", 
                                city_name ="Maria Helena")

        CityCode.objects.create(city_code ="4114807", 
                                city_name ="Marialva")

        CityCode.objects.create(city_code ="4114906", 
                                city_name ="Marilândia do Sul")

        CityCode.objects.create(city_code ="4115002", 
                                city_name ="Marilena")

        CityCode.objects.create(city_code ="4115101", 
                                city_name ="Mariluz")

        CityCode.objects.create(city_code ="4115200", 
                                city_name ="Maringá")

        CityCode.objects.create(city_code ="4115309", 
                                city_name ="Mariópolis")

        CityCode.objects.create(city_code ="4115358", 
                                city_name ="Maripá")

        CityCode.objects.create(city_code ="4115408", 
                                city_name ="Marmeleiro")

        CityCode.objects.create(city_code ="4115457", 
                                city_name ="Marquinho")

        CityCode.objects.create(city_code ="4115507", 
                                city_name ="Marumbi")

        CityCode.objects.create(city_code ="4115606", 
                                city_name ="Matelândia")

        CityCode.objects.create(city_code ="4115705", 
                                city_name ="Matinhos")

        CityCode.objects.create(city_code ="4115739", 
                                city_name ="Mato Rico")

        CityCode.objects.create(city_code ="4115754", 
                                city_name ="Mauá da Serra")

        CityCode.objects.create(city_code ="4115804", 
                                city_name ="Medianeira")

        CityCode.objects.create(city_code ="4115853", 
                                city_name ="Mercedes")

        CityCode.objects.create(city_code ="4115903", 
                                city_name ="Mirador")

        CityCode.objects.create(city_code ="4116000", 
                                city_name ="Miraselva")

        CityCode.objects.create(city_code ="4116059", 
                                city_name ="Missal")

        CityCode.objects.create(city_code ="4116109", 
                                city_name ="Moreira Sales")

        CityCode.objects.create(city_code ="4116208", 
                                city_name ="Morretes")

        CityCode.objects.create(city_code ="4116307", 
                                city_name ="Munhoz de Melo")

        CityCode.objects.create(city_code ="4116406", 
                                city_name ="Nossa Senhora das Graças")

        CityCode.objects.create(city_code ="4116505", 
                                city_name ="Nova Aliança do Ivaí")

        CityCode.objects.create(city_code ="4116604", 
                                city_name ="Nova América da Colina")

        CityCode.objects.create(city_code ="4116703", 
                                city_name ="Nova Aurora")

        CityCode.objects.create(city_code ="4116802", 
                                city_name ="Nova Cantu")

        CityCode.objects.create(city_code ="4116901", 
                                city_name ="Nova Esperança")

        CityCode.objects.create(city_code ="4116950", 
                                city_name ="Nova Esperança do Sudoeste")

        CityCode.objects.create(city_code ="4117008", 
                                city_name ="Nova Fátima")

        CityCode.objects.create(city_code ="4117057", 
                                city_name ="Nova Laranjeiras")

        CityCode.objects.create(city_code ="4117107", 
                                city_name ="Nova Londrina")

        CityCode.objects.create(city_code ="4117206", 
                                city_name ="Nova Olímpia")

        CityCode.objects.create(city_code ="4117255", 
                                city_name ="Nova Prata do Iguaçu")

        CityCode.objects.create(city_code ="4117214", 
                                city_name ="Nova Santa Bárbara")

        CityCode.objects.create(city_code ="4117222", 
                                city_name ="Nova Santa Rosa")

        CityCode.objects.create(city_code ="4117271", 
                                city_name ="Nova Tebas")

        CityCode.objects.create(city_code ="4117297", 
                                city_name ="Novo Itacolomi")

        CityCode.objects.create(city_code ="4117305", 
                                city_name ="Ortigueira")

        CityCode.objects.create(city_code ="4117404", 
                                city_name ="Ourizona")

        CityCode.objects.create(city_code ="4117453", 
                                city_name ="Ouro Verde do Oeste")

        CityCode.objects.create(city_code ="4117503", 
                                city_name ="Paiçandu")

        CityCode.objects.create(city_code ="4117602", 
                                city_name ="Palmas")

        CityCode.objects.create(city_code ="4117701", 
                                city_name ="Palmeira")

        CityCode.objects.create(city_code ="4117800", 
                                city_name ="Palmital")

        CityCode.objects.create(city_code ="4117909", 
                                city_name ="Palotina")

        CityCode.objects.create(city_code ="4118006", 
                                city_name ="Paraíso do Norte")

        CityCode.objects.create(city_code ="4118105", 
                                city_name ="Paranacity")

        CityCode.objects.create(city_code ="4118204", 
                                city_name ="Paranaguá")

        CityCode.objects.create(city_code ="4118303", 
                                city_name ="Paranapoema")

        CityCode.objects.create(city_code ="4118402", 
                                city_name ="Paranavaí")

        CityCode.objects.create(city_code ="4118451", 
                                city_name ="Pato Bragado")

        CityCode.objects.create(city_code ="4118501", 
                                city_name ="Pato Branco")

        CityCode.objects.create(city_code ="4118600", 
                                city_name ="Paula Freitas")

        CityCode.objects.create(city_code ="4118709", 
                                city_name ="Paulo Frontin")

        CityCode.objects.create(city_code ="4118808", 
                                city_name ="Peabiru")

        CityCode.objects.create(city_code ="4118857", 
                                city_name ="Perobal")

        CityCode.objects.create(city_code ="4118907", 
                                city_name ="Pérola")

        CityCode.objects.create(city_code ="4119004", 
                                city_name ="Pérola d'Oeste")

        CityCode.objects.create(city_code ="4119103", 
                                city_name ="Piên")

        CityCode.objects.create(city_code ="4119152", 
                                city_name ="Pinhais")

        CityCode.objects.create(city_code ="4119251", 
                                city_name ="Pinhal de São Bento")

        CityCode.objects.create(city_code ="4119202", 
                                city_name ="Pinhalão")

        CityCode.objects.create(city_code ="4119301", 
                                city_name ="Pinhão")

        CityCode.objects.create(city_code ="4119400", 
                                city_name ="Piraí do Sul")

        CityCode.objects.create(city_code ="4119509", 
                                city_name ="Piraquara")

        CityCode.objects.create(city_code ="4119608", 
                                city_name ="Pitanga")

        CityCode.objects.create(city_code ="4119657", 
                                city_name ="Pitangueiras")

        CityCode.objects.create(city_code ="4119707", 
                                city_name ="Planaltina do Paraná")

        CityCode.objects.create(city_code ="4119806", 
                                city_name ="Planalto")

        CityCode.objects.create(city_code ="4119905", 
                                city_name ="Ponta Grossa")

        CityCode.objects.create(city_code ="4119954", 
                                city_name ="Pontal do Paraná")

        CityCode.objects.create(city_code ="4120002", 
                                city_name ="Porecatu")

        CityCode.objects.create(city_code ="4120101", 
                                city_name ="Porto Amazonas")

        CityCode.objects.create(city_code ="4120150", 
                                city_name ="Porto Barreiro")

        CityCode.objects.create(city_code ="4120200", 
                                city_name ="Porto Rico")

        CityCode.objects.create(city_code ="4120309", 
                                city_name ="Porto Vitória")

        CityCode.objects.create(city_code ="4120333", 
                                city_name ="Prado Ferreira")

        CityCode.objects.create(city_code ="4120358", 
                                city_name ="Pranchita")

        CityCode.objects.create(city_code ="4120408", 
                                city_name ="Presidente Castelo Branco")

        CityCode.objects.create(city_code ="4120507", 
                                city_name ="Primeiro de Maio")

        CityCode.objects.create(city_code ="4120606", 
                                city_name ="Prudentópolis")

        CityCode.objects.create(city_code ="4120655", 
                                city_name ="Quarto Centenário")

        CityCode.objects.create(city_code ="4120705", 
                                city_name ="Quatiguá")

        CityCode.objects.create(city_code ="4120804", 
                                city_name ="Quatro Barras")

        CityCode.objects.create(city_code ="4120853", 
                                city_name ="Quatro Pontes")

        CityCode.objects.create(city_code ="4120903", 
                                city_name ="Quedas do Iguaçu")

        CityCode.objects.create(city_code ="4121000", 
                                city_name ="Querência do Norte")

        CityCode.objects.create(city_code ="4121109", 
                                city_name ="Quinta do Sol")

        CityCode.objects.create(city_code ="4121208", 
                                city_name ="Quitandinha")

        CityCode.objects.create(city_code ="4121257", 
                                city_name ="Ramilândia")

        CityCode.objects.create(city_code ="4121307", 
                                city_name ="Rancho Alegre")

        CityCode.objects.create(city_code ="4121356", 
                                city_name ="Rancho Alegre D'Oeste")

        CityCode.objects.create(city_code ="4121406", 
                                city_name ="Realeza")

        CityCode.objects.create(city_code ="4121505", 
                                city_name ="Rebouças")

        CityCode.objects.create(city_code ="4121604", 
                                city_name ="Renascença")

        CityCode.objects.create(city_code ="4121703", 
                                city_name ="Reserva")

        CityCode.objects.create(city_code ="4121752", 
                                city_name ="Reserva do Iguaçu")

        CityCode.objects.create(city_code ="4121802", 
                                city_name ="Ribeirão Claro")

        CityCode.objects.create(city_code ="4121901", 
                                city_name ="Ribeirão do Pinhal")

        CityCode.objects.create(city_code ="4122008", 
                                city_name ="Rio Azul")

        CityCode.objects.create(city_code ="4122107", 
                                city_name ="Rio Bom")

        CityCode.objects.create(city_code ="4122156", 
                                city_name ="Rio Bonito do Iguaçu")

        CityCode.objects.create(city_code ="4122172", 
                                city_name ="Rio Branco do Ivaí")

        CityCode.objects.create(city_code ="4122206", 
                                city_name ="Rio Branco do Sul")

        CityCode.objects.create(city_code ="4122305", 
                                city_name ="Rio Negro")

        CityCode.objects.create(city_code ="4122404", 
                                city_name ="Rolândia")

        CityCode.objects.create(city_code ="4122503", 
                                city_name ="Roncador")

        CityCode.objects.create(city_code ="4122602", 
                                city_name ="Rondon")

        CityCode.objects.create(city_code ="4122651", 
                                city_name ="Rosário do Ivaí")

        CityCode.objects.create(city_code ="4122701", 
                                city_name ="Sabáudia")

        CityCode.objects.create(city_code ="4122800", 
                                city_name ="Salgado Filho")

        CityCode.objects.create(city_code ="4122909", 
                                city_name ="Salto do Itararé")

        CityCode.objects.create(city_code ="4123006", 
                                city_name ="Salto do Lontra")

        CityCode.objects.create(city_code ="4123105", 
                                city_name ="Santa Amélia")

        CityCode.objects.create(city_code ="4123204", 
                                city_name ="Santa Cecília do Pavão")

        CityCode.objects.create(city_code ="4123303", 
                                city_name ="Santa Cruz de Monte Castelo")

        CityCode.objects.create(city_code ="4123402", 
                                city_name ="Santa Fé")

        CityCode.objects.create(city_code ="4123501", 
                                city_name ="Santa Helena")

        CityCode.objects.create(city_code ="4123600", 
                                city_name ="Santa Inês")

        CityCode.objects.create(city_code ="4123709", 
                                city_name ="Santa Isabel do Ivaí")

        CityCode.objects.create(city_code ="4123808", 
                                city_name ="Santa Izabel do Oeste")

        CityCode.objects.create(city_code ="4123824", 
                                city_name ="Santa Lúcia")

        CityCode.objects.create(city_code ="4123857", 
                                city_name ="Santa Maria do Oeste")

        CityCode.objects.create(city_code ="4123907", 
                                city_name ="Santa Mariana")

        CityCode.objects.create(city_code ="4123956", 
                                city_name ="Santa Mônica")

        CityCode.objects.create(city_code ="4124020", 
                                city_name ="Santa Tereza do Oeste")

        CityCode.objects.create(city_code ="4124053", 
                                city_name ="Santa Terezinha de Itaipu")

        CityCode.objects.create(city_code ="4124004", 
                                city_name ="Santana do Itararé")

        CityCode.objects.create(city_code ="4124103", 
                                city_name ="Santo Antônio da Platina")

        CityCode.objects.create(city_code ="4124202", 
                                city_name ="Santo Antônio do Caiuá")

        CityCode.objects.create(city_code ="4124301", 
                                city_name ="Santo Antônio do Paraíso")

        CityCode.objects.create(city_code ="4124400", 
                                city_name ="Santo Antônio do Sudoeste")

        CityCode.objects.create(city_code ="4124509", 
                                city_name ="Santo Inácio")

        CityCode.objects.create(city_code ="4124608", 
                                city_name ="São Carlos do Ivaí")

        CityCode.objects.create(city_code ="4124707", 
                                city_name ="São Jerônimo da Serra")

        CityCode.objects.create(city_code ="4124806", 
                                city_name ="São João")

        CityCode.objects.create(city_code ="4124905", 
                                city_name ="São João do Caiuá")

        CityCode.objects.create(city_code ="4125001", 
                                city_name ="São João do Ivaí")

        CityCode.objects.create(city_code ="4125100", 
                                city_name ="São João do Triunfo")

        CityCode.objects.create(city_code ="4125308", 
                                city_name ="São Jorge do Ivaí")

        CityCode.objects.create(city_code ="4125357", 
                                city_name ="São Jorge do Patrocínio")

        CityCode.objects.create(city_code ="4125209", 
                                city_name ="São Jorge d'Oeste")

        CityCode.objects.create(city_code ="4125407", 
                                city_name ="São José da Boa Vista")

        CityCode.objects.create(city_code ="4125456", 
                                city_name ="São José das Palmeiras")

        CityCode.objects.create(city_code ="4125506", 
                                city_name ="São José dos Pinhais")

        CityCode.objects.create(city_code ="4125555", 
                                city_name ="São Manoel do Paraná")

        CityCode.objects.create(city_code ="4125605", 
                                city_name ="São Mateus do Sul")

        CityCode.objects.create(city_code ="4125704", 
                                city_name ="São Miguel do Iguaçu")

        CityCode.objects.create(city_code ="4125753", 
                                city_name ="São Pedro do Iguaçu")

        CityCode.objects.create(city_code ="4125803", 
                                city_name ="São Pedro do Ivaí")

        CityCode.objects.create(city_code ="4125902", 
                                city_name ="São Pedro do Paraná")

        CityCode.objects.create(city_code ="4126009", 
                                city_name ="São Sebastião da Amoreira")

        CityCode.objects.create(city_code ="4126108", 
                                city_name ="São Tomé")

        CityCode.objects.create(city_code ="4126207", 
                                city_name ="Sapopema")

        CityCode.objects.create(city_code ="4126256", 
                                city_name ="Sarandi")

        CityCode.objects.create(city_code ="4126272", 
                                city_name ="Saudade do Iguaçu")

        CityCode.objects.create(city_code ="4126306", 
                                city_name ="Sengés")

        CityCode.objects.create(city_code ="4126355", 
                                city_name ="Serranópolis do Iguaçu")

        CityCode.objects.create(city_code ="4126405", 
                                city_name ="Sertaneja")

        CityCode.objects.create(city_code ="4126504", 
                                city_name ="Sertanópolis")

        CityCode.objects.create(city_code ="4126603", 
                                city_name ="Siqueira Campos")

        CityCode.objects.create(city_code ="4126652", 
                                city_name ="Sulina")

        CityCode.objects.create(city_code ="4126678", 
                                city_name ="Tamarana")

        CityCode.objects.create(city_code ="4126702", 
                                city_name ="Tamboara")

        CityCode.objects.create(city_code ="4126801", 
                                city_name ="Tapejara")

        CityCode.objects.create(city_code ="4126900", 
                                city_name ="Tapira")

        CityCode.objects.create(city_code ="4127007", 
                                city_name ="Teixeira Soares")

        CityCode.objects.create(city_code ="4127106", 
                                city_name ="Telêmaco Borba")

        CityCode.objects.create(city_code ="4127205", 
                                city_name ="Terra Boa")

        CityCode.objects.create(city_code ="4127304", 
                                city_name ="Terra Rica")

        CityCode.objects.create(city_code ="4127403", 
                                city_name ="Terra Roxa")

        CityCode.objects.create(city_code ="4127502", 
                                city_name ="Tibagi")

        CityCode.objects.create(city_code ="4127601", 
                                city_name ="Tijucas do Sul")

        CityCode.objects.create(city_code ="4127700", 
                                city_name ="Toledo")

        CityCode.objects.create(city_code ="4127809", 
                                city_name ="Tomazina")

        CityCode.objects.create(city_code ="4127858", 
                                city_name ="Três Barras do Paraná")

        CityCode.objects.create(city_code ="4127882", 
                                city_name ="Tunas do Paraná")

        CityCode.objects.create(city_code ="4127908", 
                                city_name ="Tuneiras do Oeste")

        CityCode.objects.create(city_code ="4127957", 
                                city_name ="Tupãssi")

        CityCode.objects.create(city_code ="4127965", 
                                city_name ="Turvo")

        CityCode.objects.create(city_code ="4128005", 
                                city_name ="Ubiratã")

        CityCode.objects.create(city_code ="4128104", 
                                city_name ="Umuarama")

        CityCode.objects.create(city_code ="4128203", 
                                city_name ="União da Vitória")

        CityCode.objects.create(city_code ="4128302", 
                                city_name ="Uniflor")

        CityCode.objects.create(city_code ="4128401", 
                                city_name ="Uraí")

        CityCode.objects.create(city_code ="4128534", 
                                city_name ="Ventania")

        CityCode.objects.create(city_code ="4128559", 
                                city_name ="Vera Cruz do Oeste")

        CityCode.objects.create(city_code ="4128609", 
                                city_name ="Verê")

        CityCode.objects.create(city_code ="4128658", 
                                city_name ="Virmond")

        CityCode.objects.create(city_code ="4128708", 
                                city_name ="Vitorino")

        CityCode.objects.create(city_code ="4128500", 
                                city_name ="Wenceslau Braz")

        CityCode.objects.create(city_code ="4128807", 
                                city_name ="Xambrê")

        CityCode.objects.create(city_code ="4200051", 
                                city_name ="Abdon Batista")

        CityCode.objects.create(city_code ="4200101", 
                                city_name ="Abelardo Luz")

        CityCode.objects.create(city_code ="4200200", 
                                city_name ="Agrolândia")

        CityCode.objects.create(city_code ="4200309", 
                                city_name ="Agronômica")

        CityCode.objects.create(city_code ="4200408", 
                                city_name ="Água Doce")

        CityCode.objects.create(city_code ="4200507", 
                                city_name ="Águas de Chapecó")

        CityCode.objects.create(city_code ="4200556", 
                                city_name ="Águas Frias")

        CityCode.objects.create(city_code ="4200606", 
                                city_name ="Águas Mornas")

        CityCode.objects.create(city_code ="4200705", 
                                city_name ="Alfredo Wagner")

        CityCode.objects.create(city_code ="4200754", 
                                city_name ="Alto Bela Vista")

        CityCode.objects.create(city_code ="4200804", 
                                city_name ="Anchieta")

        CityCode.objects.create(city_code ="4200903", 
                                city_name ="Angelina")

        CityCode.objects.create(city_code ="4201000", 
                                city_name ="Anita Garibaldi")

        CityCode.objects.create(city_code ="4201109", 
                                city_name ="Anitápolis")

        CityCode.objects.create(city_code ="4201208", 
                                city_name ="Antônio Carlos")

        CityCode.objects.create(city_code ="4201257", 
                                city_name ="Apiúna")

        CityCode.objects.create(city_code ="4201273", 
                                city_name ="Arabutã")

        CityCode.objects.create(city_code ="4201307", 
                                city_name ="Araquari")

        CityCode.objects.create(city_code ="4201406", 
                                city_name ="Araranguá")

        CityCode.objects.create(city_code ="4201505", 
                                city_name ="Armazém")

        CityCode.objects.create(city_code ="4201604", 
                                city_name ="Arroio Trinta")

        CityCode.objects.create(city_code ="4201653", 
                                city_name ="Arvoredo")

        CityCode.objects.create(city_code ="4201703", 
                                city_name ="Ascurra")

        CityCode.objects.create(city_code ="4201802", 
                                city_name ="Atalanta")

        CityCode.objects.create(city_code ="4201901", 
                                city_name ="Aurora")

        CityCode.objects.create(city_code ="4201950", 
                                city_name ="Balneário Arroio do Silva")

        CityCode.objects.create(city_code ="4202057", 
                                city_name ="Balneário Barra do Sul")

        CityCode.objects.create(city_code ="4202008", 
                                city_name ="Balneário Camboriú")

        CityCode.objects.create(city_code ="4202073", 
                                city_name ="Balneário Gaivota")

        CityCode.objects.create(city_code ="4212809", 
                                city_name ="Balneário Piçarras")

        CityCode.objects.create(city_code ="4220000", 
                                city_name ="Balneário Rincão")

        CityCode.objects.create(city_code ="4202081", 
                                city_name ="Bandeirante")

        CityCode.objects.create(city_code ="4202099", 
                                city_name ="Barra Bonita")

        CityCode.objects.create(city_code ="4202107", 
                                city_name ="Barra Velha")

        CityCode.objects.create(city_code ="4202131", 
                                city_name ="Bela Vista do Toldo")

        CityCode.objects.create(city_code ="4202156", 
                                city_name ="Belmonte")

        CityCode.objects.create(city_code ="4202206", 
                                city_name ="Benedito Novo")

        CityCode.objects.create(city_code ="4202305", 
                                city_name ="Biguaçu")

        CityCode.objects.create(city_code ="4202404", 
                                city_name ="Blumenau")

        CityCode.objects.create(city_code ="4202438", 
                                city_name ="Bocaina do Sul")

        CityCode.objects.create(city_code ="4202503", 
                                city_name ="Bom Jardim da Serra")

        CityCode.objects.create(city_code ="4202537", 
                                city_name ="Bom Jesus")

        CityCode.objects.create(city_code ="4202578", 
                                city_name ="Bom Jesus do Oeste")

        CityCode.objects.create(city_code ="4202602", 
                                city_name ="Bom Retiro")

        CityCode.objects.create(city_code ="4202453", 
                                city_name ="Bombinhas")

        CityCode.objects.create(city_code ="4202701", 
                                city_name ="Botuverá")

        CityCode.objects.create(city_code ="4202800", 
                                city_name ="Braço do Norte")

        CityCode.objects.create(city_code ="4202859", 
                                city_name ="Braço do Trombudo")

        CityCode.objects.create(city_code ="4202875", 
                                city_name ="Brunópolis")

        CityCode.objects.create(city_code ="4202909", 
                                city_name ="Brusque")

        CityCode.objects.create(city_code ="4203006", 
                                city_name ="Caçador")

        CityCode.objects.create(city_code ="4203105", 
                                city_name ="Caibi")

        CityCode.objects.create(city_code ="4203154", 
                                city_name ="Calmon")

        CityCode.objects.create(city_code ="4203204", 
                                city_name ="Camboriú")

        CityCode.objects.create(city_code ="4203303", 
                                city_name ="Campo Alegre")

        CityCode.objects.create(city_code ="4203402", 
                                city_name ="Campo Belo do Sul")

        CityCode.objects.create(city_code ="4203501", 
                                city_name ="Campo Erê")

        CityCode.objects.create(city_code ="4203600", 
                                city_name ="Campos Novos")

        CityCode.objects.create(city_code ="4203709", 
                                city_name ="Canelinha")

        CityCode.objects.create(city_code ="4203808", 
                                city_name ="Canoinhas")

        CityCode.objects.create(city_code ="4203253", 
                                city_name ="Capão Alto")

        CityCode.objects.create(city_code ="4203907", 
                                city_name ="Capinzal")

        CityCode.objects.create(city_code ="4203956", 
                                city_name ="Capivari de Baixo")

        CityCode.objects.create(city_code ="4204004", 
                                city_name ="Catanduvas")

        CityCode.objects.create(city_code ="4204103", 
                                city_name ="Caxambu do Sul")

        CityCode.objects.create(city_code ="4204152", 
                                city_name ="Celso Ramos")

        CityCode.objects.create(city_code ="4204178", 
                                city_name ="Cerro Negro")

        CityCode.objects.create(city_code ="4204194", 
                                city_name ="Chapadão do Lageado")

        CityCode.objects.create(city_code ="4204202", 
                                city_name ="Chapecó")

        CityCode.objects.create(city_code ="4204251", 
                                city_name ="Cocal do Sul")

        CityCode.objects.create(city_code ="4204301", 
                                city_name ="Concórdia")

        CityCode.objects.create(city_code ="4204350", 
                                city_name ="Cordilheira Alta")

        CityCode.objects.create(city_code ="4204400", 
                                city_name ="Coronel Freitas")

        CityCode.objects.create(city_code ="4204459", 
                                city_name ="Coronel Martins")

        CityCode.objects.create(city_code ="4204558", 
                                city_name ="Correia Pinto")

        CityCode.objects.create(city_code ="4204509", 
                                city_name ="Corupá")

        CityCode.objects.create(city_code ="4204608", 
                                city_name ="Criciúma")

        CityCode.objects.create(city_code ="4204707", 
                                city_name ="Cunha Porã")

        CityCode.objects.create(city_code ="4204756", 
                                city_name ="Cunhataí")

        CityCode.objects.create(city_code ="4204806", 
                                city_name ="Curitibanos")

        CityCode.objects.create(city_code ="4204905", 
                                city_name ="Descanso")

        CityCode.objects.create(city_code ="4205001", 
                                city_name ="Dionísio Cerqueira")

        CityCode.objects.create(city_code ="4205100", 
                                city_name ="Dona Emma")

        CityCode.objects.create(city_code ="4205159", 
                                city_name ="Doutor Pedrinho")

        CityCode.objects.create(city_code ="4205175", 
                                city_name ="Entre Rios")

        CityCode.objects.create(city_code ="4205191", 
                                city_name ="Ermo")

        CityCode.objects.create(city_code ="4205209", 
                                city_name ="Erval Velho")

        CityCode.objects.create(city_code ="4205308", 
                                city_name ="Faxinal dos Guedes")

        CityCode.objects.create(city_code ="4205357", 
                                city_name ="Flor do Sertão")

        CityCode.objects.create(city_code ="4205407", 
                                city_name ="Florianópolis")

        CityCode.objects.create(city_code ="4205431", 
                                city_name ="Formosa do Sul")

        CityCode.objects.create(city_code ="4205456", 
                                city_name ="Forquilhinha")

        CityCode.objects.create(city_code ="4205506", 
                                city_name ="Fraiburgo")

        CityCode.objects.create(city_code ="4205555", 
                                city_name ="Frei Rogério")

        CityCode.objects.create(city_code ="4205605", 
                                city_name ="Galvão")

        CityCode.objects.create(city_code ="4205704", 
                                city_name ="Garopaba")

        CityCode.objects.create(city_code ="4205803", 
                                city_name ="Garuva")

        CityCode.objects.create(city_code ="4205902", 
                                city_name ="Gaspar")

        CityCode.objects.create(city_code ="4206009", 
                                city_name ="Governador Celso Ramos")

        CityCode.objects.create(city_code ="4206108", 
                                city_name ="Grão-Pará")

        CityCode.objects.create(city_code ="4206207", 
                                city_name ="Gravatal")

        CityCode.objects.create(city_code ="4206306", 
                                city_name ="Guabiruba")

        CityCode.objects.create(city_code ="4206405", 
                                city_name ="Guaraciaba")

        CityCode.objects.create(city_code ="4206504", 
                                city_name ="Guaramirim")

        CityCode.objects.create(city_code ="4206603", 
                                city_name ="Guarujá do Sul")

        CityCode.objects.create(city_code ="4206652", 
                                city_name ="Guatambú")

        CityCode.objects.create(city_code ="4206702", 
                                city_name ="Herval d'Oeste")

        CityCode.objects.create(city_code ="4206751", 
                                city_name ="Ibiam")

        CityCode.objects.create(city_code ="4206801", 
                                city_name ="Ibicaré")

        CityCode.objects.create(city_code ="4206900", 
                                city_name ="Ibirama")

        CityCode.objects.create(city_code ="4207007", 
                                city_name ="Içara")

        CityCode.objects.create(city_code ="4207106", 
                                city_name ="Ilhota")

        CityCode.objects.create(city_code ="4207205", 
                                city_name ="Imaruí")

        CityCode.objects.create(city_code ="4207304", 
                                city_name ="Imbituba")

        CityCode.objects.create(city_code ="4207403", 
                                city_name ="Imbuia")

        CityCode.objects.create(city_code ="4207502", 
                                city_name ="Indaial")

        CityCode.objects.create(city_code ="4207577", 
                                city_name ="Iomerê")

        CityCode.objects.create(city_code ="4207601", 
                                city_name ="Ipira")

        CityCode.objects.create(city_code ="4207650", 
                                city_name ="Iporã do Oeste")

        CityCode.objects.create(city_code ="4207684", 
                                city_name ="Ipuaçu")

        CityCode.objects.create(city_code ="4207700", 
                                city_name ="Ipumirim")

        CityCode.objects.create(city_code ="4207759", 
                                city_name ="Iraceminha")

        CityCode.objects.create(city_code ="4207809", 
                                city_name ="Irani")

        CityCode.objects.create(city_code ="4207858", 
                                city_name ="Irati")

        CityCode.objects.create(city_code ="4207908", 
                                city_name ="Irineópolis")

        CityCode.objects.create(city_code ="4208005", 
                                city_name ="Itá")

        CityCode.objects.create(city_code ="4208104", 
                                city_name ="Itaiópolis")

        CityCode.objects.create(city_code ="4208203", 
                                city_name ="Itajaí")

        CityCode.objects.create(city_code ="4208302", 
                                city_name ="Itapema")

        CityCode.objects.create(city_code ="4208401", 
                                city_name ="Itapiranga")

        CityCode.objects.create(city_code ="4208450", 
                                city_name ="Itapoá")

        CityCode.objects.create(city_code ="4208500", 
                                city_name ="Ituporanga")

        CityCode.objects.create(city_code ="4208609", 
                                city_name ="Jaborá")

        CityCode.objects.create(city_code ="4208708", 
                                city_name ="Jacinto Machado")

        CityCode.objects.create(city_code ="4208807", 
                                city_name ="Jaguaruna")

        CityCode.objects.create(city_code ="4208906", 
                                city_name ="Jaraguá do Sul")

        CityCode.objects.create(city_code ="4208955", 
                                city_name ="Jardinópolis")

        CityCode.objects.create(city_code ="4209003", 
                                city_name ="Joaçaba")

        CityCode.objects.create(city_code ="4209102", 
                                city_name ="Joinville")

        CityCode.objects.create(city_code ="4209151", 
                                city_name ="José Boiteux")

        CityCode.objects.create(city_code ="4209177", 
                                city_name ="Jupiá")

        CityCode.objects.create(city_code ="4209201", 
                                city_name ="Lacerdópolis")

        CityCode.objects.create(city_code ="4209300", 
                                city_name ="Lages")

        CityCode.objects.create(city_code ="4209409", 
                                city_name ="Laguna")

        CityCode.objects.create(city_code ="4209458", 
                                city_name ="Lajeado Grande")

        CityCode.objects.create(city_code ="4209508", 
                                city_name ="Laurentino")

        CityCode.objects.create(city_code ="4209607", 
                                city_name ="Lauro Müller")

        CityCode.objects.create(city_code ="4209706", 
                                city_name ="Lebon Régis")

        CityCode.objects.create(city_code ="4209805", 
                                city_name ="Leoberto Leal")

        CityCode.objects.create(city_code ="4209854", 
                                city_name ="Lindóia do Sul")

        CityCode.objects.create(city_code ="4209904", 
                                city_name ="Lontras")

        CityCode.objects.create(city_code ="4210001", 
                                city_name ="Luiz Alves")

        CityCode.objects.create(city_code ="4210035", 
                                city_name ="Luzerna")

        CityCode.objects.create(city_code ="4210050", 
                                city_name ="Macieira")

        CityCode.objects.create(city_code ="4210100", 
                                city_name ="Mafra")

        CityCode.objects.create(city_code ="4210209", 
                                city_name ="Major Gercino")

        CityCode.objects.create(city_code ="4210308", 
                                city_name ="Major Vieira")

        CityCode.objects.create(city_code ="4210407", 
                                city_name ="Maracajá")

        CityCode.objects.create(city_code ="4210506", 
                                city_name ="Maravilha")

        CityCode.objects.create(city_code ="4210555", 
                                city_name ="Marema")

        CityCode.objects.create(city_code ="4210605", 
                                city_name ="Massaranduba")

        CityCode.objects.create(city_code ="4210704", 
                                city_name ="Matos Costa")

        CityCode.objects.create(city_code ="4210803", 
                                city_name ="Meleiro")

        CityCode.objects.create(city_code ="4210852", 
                                city_name ="Mirim Doce")

        CityCode.objects.create(city_code ="4210902", 
                                city_name ="Modelo")

        CityCode.objects.create(city_code ="4211009", 
                                city_name ="Mondaí")

        CityCode.objects.create(city_code ="4211058", 
                                city_name ="Monte Carlo")

        CityCode.objects.create(city_code ="4211108", 
                                city_name ="Monte Castelo")

        CityCode.objects.create(city_code ="4211207", 
                                city_name ="Morro da Fumaça")

        CityCode.objects.create(city_code ="4211256", 
                                city_name ="Morro Grande")

        CityCode.objects.create(city_code ="4211306", 
                                city_name ="Navegantes")

        CityCode.objects.create(city_code ="4211405", 
                                city_name ="Nova Erechim")

        CityCode.objects.create(city_code ="4211454", 
                                city_name ="Nova Itaberaba")

        CityCode.objects.create(city_code ="4211504", 
                                city_name ="Nova Trento")

        CityCode.objects.create(city_code ="4211603", 
                                city_name ="Nova Veneza")

        CityCode.objects.create(city_code ="4211652", 
                                city_name ="Novo Horizonte")

        CityCode.objects.create(city_code ="4211702", 
                                city_name ="Orleans")

        CityCode.objects.create(city_code ="4211751", 
                                city_name ="Otacílio Costa")

        CityCode.objects.create(city_code ="4211801", 
                                city_name ="Ouro")

        CityCode.objects.create(city_code ="4211850", 
                                city_name ="Ouro Verde")

        CityCode.objects.create(city_code ="4211876", 
                                city_name ="Paial")

        CityCode.objects.create(city_code ="4211892", 
                                city_name ="Painel")

        CityCode.objects.create(city_code ="4211900", 
                                city_name ="Palhoça")

        CityCode.objects.create(city_code ="4212007", 
                                city_name ="Palma Sola")

        CityCode.objects.create(city_code ="4212056", 
                                city_name ="Palmeira")

        CityCode.objects.create(city_code ="4212106", 
                                city_name ="Palmitos")

        CityCode.objects.create(city_code ="4212205", 
                                city_name ="Papanduva")

        CityCode.objects.create(city_code ="4212239", 
                                city_name ="Paraíso")

        CityCode.objects.create(city_code ="4212254", 
                                city_name ="Passo de Torres")

        CityCode.objects.create(city_code ="4212270", 
                                city_name ="Passos Maia")

        CityCode.objects.create(city_code ="4212304", 
                                city_name ="Paulo Lopes")

        CityCode.objects.create(city_code ="4212403", 
                                city_name ="Pedras Grandes")

        CityCode.objects.create(city_code ="4212502", 
                                city_name ="Penha")

        CityCode.objects.create(city_code ="4212601", 
                                city_name ="Peritiba")

        CityCode.objects.create(city_code ="4212650", 
                                city_name ="Pescaria Brava")

        CityCode.objects.create(city_code ="4212700", 
                                city_name ="Petrolândia")

        CityCode.objects.create(city_code ="4212908", 
                                city_name ="Pinhalzinho")

        CityCode.objects.create(city_code ="4213005", 
                                city_name ="Pinheiro Preto")

        CityCode.objects.create(city_code ="4213104", 
                                city_name ="Piratuba")

        CityCode.objects.create(city_code ="4213153", 
                                city_name ="Planalto Alegre")

        CityCode.objects.create(city_code ="4213203", 
                                city_name ="Pomerode")

        CityCode.objects.create(city_code ="4213302", 
                                city_name ="Ponte Alta")

        CityCode.objects.create(city_code ="4213351", 
                                city_name ="Ponte Alta do Norte")

        CityCode.objects.create(city_code ="4213401", 
                                city_name ="Ponte Serrada")

        CityCode.objects.create(city_code ="4213500", 
                                city_name ="Porto Belo")

        CityCode.objects.create(city_code ="4213609", 
                                city_name ="Porto União")

        CityCode.objects.create(city_code ="4213708", 
                                city_name ="Pouso Redondo")

        CityCode.objects.create(city_code ="4213807", 
                                city_name ="Praia Grande")

        CityCode.objects.create(city_code ="4213906", 
                                city_name ="Presidente Castello Branco")

        CityCode.objects.create(city_code ="4214003", 
                                city_name ="Presidente Getúlio")

        CityCode.objects.create(city_code ="4214102", 
                                city_name ="Presidente Nereu")

        CityCode.objects.create(city_code ="4214151", 
                                city_name ="Princesa")

        CityCode.objects.create(city_code ="4214201", 
                                city_name ="Quilombo")

        CityCode.objects.create(city_code ="4214300", 
                                city_name ="Rancho Queimado")

        CityCode.objects.create(city_code ="4214409", 
                                city_name ="Rio das Antas")

        CityCode.objects.create(city_code ="4214508", 
                                city_name ="Rio do Campo")

        CityCode.objects.create(city_code ="4214607", 
                                city_name ="Rio do Oeste")

        CityCode.objects.create(city_code ="4214805", 
                                city_name ="Rio do Sul")

        CityCode.objects.create(city_code ="4214706", 
                                city_name ="Rio dos Cedros")

        CityCode.objects.create(city_code ="4214904", 
                                city_name ="Rio Fortuna")

        CityCode.objects.create(city_code ="4215000", 
                                city_name ="Rio Negrinho")

        CityCode.objects.create(city_code ="4215059", 
                                city_name ="Rio Rufino")

        CityCode.objects.create(city_code ="4215075", 
                                city_name ="Riqueza")

        CityCode.objects.create(city_code ="4215109", 
                                city_name ="Rodeio")

        CityCode.objects.create(city_code ="4215208", 
                                city_name ="Romelândia")

        CityCode.objects.create(city_code ="4215307", 
                                city_name ="Salete")

        CityCode.objects.create(city_code ="4215356", 
                                city_name ="Saltinho")

        CityCode.objects.create(city_code ="4215406", 
                                city_name ="Salto Veloso")

        CityCode.objects.create(city_code ="4215455", 
                                city_name ="Sangão")

        CityCode.objects.create(city_code ="4215505", 
                                city_name ="Santa Cecília")

        CityCode.objects.create(city_code ="4215554", 
                                city_name ="Santa Helena")

        CityCode.objects.create(city_code ="4215604", 
                                city_name ="Santa Rosa de Lima")

        CityCode.objects.create(city_code ="4215653", 
                                city_name ="Santa Rosa do Sul")

        CityCode.objects.create(city_code ="4215679", 
                                city_name ="Santa Terezinha")

        CityCode.objects.create(city_code ="4215687", 
                                city_name ="Santa Terezinha do Progresso")

        CityCode.objects.create(city_code ="4215695", 
                                city_name ="Santiago do Sul")

        CityCode.objects.create(city_code ="4215703", 
                                city_name ="Santo Amaro da Imperatriz")

        CityCode.objects.create(city_code ="4215802", 
                                city_name ="São Bento do Sul")

        CityCode.objects.create(city_code ="4215752", 
                                city_name ="São Bernardino")

        CityCode.objects.create(city_code ="4215901", 
                                city_name ="São Bonifácio")

        CityCode.objects.create(city_code ="4216008", 
                                city_name ="São Carlos")

        CityCode.objects.create(city_code ="4216057", 
                                city_name ="São Cristóvão do Sul")

        CityCode.objects.create(city_code ="4216107", 
                                city_name ="São Domingos")

        CityCode.objects.create(city_code ="4216206", 
                                city_name ="São Francisco do Sul")

        CityCode.objects.create(city_code ="4216305", 
                                city_name ="São João Batista")

        CityCode.objects.create(city_code ="4216354", 
                                city_name ="São João do Itaperiú")

        CityCode.objects.create(city_code ="4216255", 
                                city_name ="São João do Oeste")

        CityCode.objects.create(city_code ="4216404", 
                                city_name ="São João do Sul")

        CityCode.objects.create(city_code ="4216503", 
                                city_name ="São Joaquim")

        CityCode.objects.create(city_code ="4216602", 
                                city_name ="São José")

        CityCode.objects.create(city_code ="4216701", 
                                city_name ="São José do Cedro")

        CityCode.objects.create(city_code ="4216800", 
                                city_name ="São José do Cerrito")

        CityCode.objects.create(city_code ="4216909", 
                                city_name ="São Lourenço do Oeste")

        CityCode.objects.create(city_code ="4217006", 
                                city_name ="São Ludgero")

        CityCode.objects.create(city_code ="4217105", 
                                city_name ="São Martinho")

        CityCode.objects.create(city_code ="4217154", 
                                city_name ="São Miguel da Boa Vista")

        CityCode.objects.create(city_code ="4217204", 
                                city_name ="São Miguel do Oeste")

        CityCode.objects.create(city_code ="4217253", 
                                city_name ="São Pedro de Alcântara")

        CityCode.objects.create(city_code ="4217303", 
                                city_name ="Saudades")

        CityCode.objects.create(city_code ="4217402", 
                                city_name ="Schroeder")

        CityCode.objects.create(city_code ="4217501", 
                                city_name ="Seara")

        CityCode.objects.create(city_code ="4217550", 
                                city_name ="Serra Alta")

        CityCode.objects.create(city_code ="4217600", 
                                city_name ="Siderópolis")

        CityCode.objects.create(city_code ="4217709", 
                                city_name ="Sombrio")

        CityCode.objects.create(city_code ="4217758", 
                                city_name ="Sul Brasil")

        CityCode.objects.create(city_code ="4217808", 
                                city_name ="Taió")

        CityCode.objects.create(city_code ="4217907", 
                                city_name ="Tangará")

        CityCode.objects.create(city_code ="4217956", 
                                city_name ="Tigrinhos")

        CityCode.objects.create(city_code ="4218004", 
                                city_name ="Tijucas")

        CityCode.objects.create(city_code ="4218103", 
                                city_name ="Timbé do Sul")

        CityCode.objects.create(city_code ="4218202", 
                                city_name ="Timbó")

        CityCode.objects.create(city_code ="4218251", 
                                city_name ="Timbó Grande")

        CityCode.objects.create(city_code ="4218301", 
                                city_name ="Três Barras")

        CityCode.objects.create(city_code ="4218350", 
                                city_name ="Treviso")

        CityCode.objects.create(city_code ="4218400", 
                                city_name ="Treze de Maio")

        CityCode.objects.create(city_code ="4218509", 
                                city_name ="Treze Tílias")

        CityCode.objects.create(city_code ="4218608", 
                                city_name ="Trombudo Central")

        CityCode.objects.create(city_code ="4218707", 
                                city_name ="Tubarão")

        CityCode.objects.create(city_code ="4218756", 
                                city_name ="Tunápolis")

        CityCode.objects.create(city_code ="4218806", 
                                city_name ="Turvo")

        CityCode.objects.create(city_code ="4218855", 
                                city_name ="União do Oeste")

        CityCode.objects.create(city_code ="4218905", 
                                city_name ="Urubici")

        CityCode.objects.create(city_code ="4218954", 
                                city_name ="Urupema")

        CityCode.objects.create(city_code ="4219002", 
                                city_name ="Urussanga")

        CityCode.objects.create(city_code ="4219101", 
                                city_name ="Vargeão")

        CityCode.objects.create(city_code ="4219150", 
                                city_name ="Vargem")

        CityCode.objects.create(city_code ="4219176", 
                                city_name ="Vargem Bonita")

        CityCode.objects.create(city_code ="4219200", 
                                city_name ="Vidal Ramos")

        CityCode.objects.create(city_code ="4219309", 
                                city_name ="Videira")

        CityCode.objects.create(city_code ="4219358", 
                                city_name ="Vitor Meireles")

        CityCode.objects.create(city_code ="4219408", 
                                city_name ="Witmarsum")

        CityCode.objects.create(city_code ="4219507", 
                                city_name ="Xanxerê")

        CityCode.objects.create(city_code ="4219606", 
                                city_name ="Xavantina")

        CityCode.objects.create(city_code ="4219705", 
                                city_name ="Xaxim")

        CityCode.objects.create(city_code ="4219853", 
                                city_name ="Zortéa")

        CityCode.objects.create(city_code ="4300034", 
                                city_name ="Aceguá")

        CityCode.objects.create(city_code ="4300059", 
                                city_name ="Água Santa")

        CityCode.objects.create(city_code ="4300109", 
                                city_name ="Agudo")

        CityCode.objects.create(city_code ="4300208", 
                                city_name ="Ajuricaba")

        CityCode.objects.create(city_code ="4300307", 
                                city_name ="Alecrim")

        CityCode.objects.create(city_code ="4300406", 
                                city_name ="Alegrete")

        CityCode.objects.create(city_code ="4300455", 
                                city_name ="Alegria")

        CityCode.objects.create(city_code ="4300471", 
                                city_name ="Almirante Tamandaré do Sul")

        CityCode.objects.create(city_code ="4300505", 
                                city_name ="Alpestre")

        CityCode.objects.create(city_code ="4300554", 
                                city_name ="Alto Alegre")

        CityCode.objects.create(city_code ="4300570", 
                                city_name ="Alto Feliz")

        CityCode.objects.create(city_code ="4300604", 
                                city_name ="Alvorada")

        CityCode.objects.create(city_code ="4300638", 
                                city_name ="Amaral Ferrador")

        CityCode.objects.create(city_code ="4300646", 
                                city_name ="Ametista do Sul")

        CityCode.objects.create(city_code ="4300661", 
                                city_name ="André da Rocha")

        CityCode.objects.create(city_code ="4300703", 
                                city_name ="Anta Gorda")

        CityCode.objects.create(city_code ="4300802", 
                                city_name ="Antônio Prado")

        CityCode.objects.create(city_code ="4300851", 
                                city_name ="Arambaré")

        CityCode.objects.create(city_code ="4300877", 
                                city_name ="Araricá")

        CityCode.objects.create(city_code ="4300901", 
                                city_name ="Aratiba")

        CityCode.objects.create(city_code ="4301008", 
                                city_name ="Arroio do Meio")

        CityCode.objects.create(city_code ="4301073", 
                                city_name ="Arroio do Padre")

        CityCode.objects.create(city_code ="4301057", 
                                city_name ="Arroio do Sal")

        CityCode.objects.create(city_code ="4301206", 
                                city_name ="Arroio do Tigre")

        CityCode.objects.create(city_code ="4301107", 
                                city_name ="Arroio dos Ratos")

        CityCode.objects.create(city_code ="4301305", 
                                city_name ="Arroio Grande")

        CityCode.objects.create(city_code ="4301404", 
                                city_name ="Arvorezinha")

        CityCode.objects.create(city_code ="4301503", 
                                city_name ="Augusto Pestana")

        CityCode.objects.create(city_code ="4301552", 
                                city_name ="Áurea")

        CityCode.objects.create(city_code ="4301602", 
                                city_name ="Bagé")

        CityCode.objects.create(city_code ="4301636", 
                                city_name ="Balneário Pinhal")

        CityCode.objects.create(city_code ="4301651", 
                                city_name ="Barão")

        CityCode.objects.create(city_code ="4301701", 
                                city_name ="Barão de Cotegipe")

        CityCode.objects.create(city_code ="4301750", 
                                city_name ="Barão do Triunfo")

        CityCode.objects.create(city_code ="4301859", 
                                city_name ="Barra do Guarita")

        CityCode.objects.create(city_code ="4301875", 
                                city_name ="Barra do Quaraí")

        CityCode.objects.create(city_code ="4301909", 
                                city_name ="Barra do Ribeiro")

        CityCode.objects.create(city_code ="4301925", 
                                city_name ="Barra do Rio Azul")

        CityCode.objects.create(city_code ="4301958", 
                                city_name ="Barra Funda")

        CityCode.objects.create(city_code ="4301800", 
                                city_name ="Barracão")

        CityCode.objects.create(city_code ="4302006", 
                                city_name ="Barros Cassal")

        CityCode.objects.create(city_code ="4302055", 
                                city_name ="Benjamin Constant do Sul")

        CityCode.objects.create(city_code ="4302105", 
                                city_name ="Bento Gonçalves")

        CityCode.objects.create(city_code ="4302154", 
                                city_name ="Boa Vista das Missões")

        CityCode.objects.create(city_code ="4302204", 
                                city_name ="Boa Vista do Buricá")

        CityCode.objects.create(city_code ="4302220", 
                                city_name ="Boa Vista do Cadeado")

        CityCode.objects.create(city_code ="4302238", 
                                city_name ="Boa Vista do Incra")

        CityCode.objects.create(city_code ="4302253", 
                                city_name ="Boa Vista do Sul")

        CityCode.objects.create(city_code ="4302303", 
                                city_name ="Bom Jesus")

        CityCode.objects.create(city_code ="4302352", 
                                city_name ="Bom Princípio")

        CityCode.objects.create(city_code ="4302378", 
                                city_name ="Bom Progresso")

        CityCode.objects.create(city_code ="4302402", 
                                city_name ="Bom Retiro do Sul")

        CityCode.objects.create(city_code ="4302451", 
                                city_name ="Boqueirão do Leão")

        CityCode.objects.create(city_code ="4302501", 
                                city_name ="Bossoroca")

        CityCode.objects.create(city_code ="4302584", 
                                city_name ="Bozano")

        CityCode.objects.create(city_code ="4302600", 
                                city_name ="Braga")

        CityCode.objects.create(city_code ="4302659", 
                                city_name ="Brochier")

        CityCode.objects.create(city_code ="4302709", 
                                city_name ="Butiá")

        CityCode.objects.create(city_code ="4302808", 
                                city_name ="Caçapava do Sul")

        CityCode.objects.create(city_code ="4302907", 
                                city_name ="Cacequi")

        CityCode.objects.create(city_code ="4303004", 
                                city_name ="Cachoeira do Sul")

        CityCode.objects.create(city_code ="4303103", 
                                city_name ="Cachoeirinha")

        CityCode.objects.create(city_code ="4303202", 
                                city_name ="Cacique Doble")

        CityCode.objects.create(city_code ="4303301", 
                                city_name ="Caibaté")

        CityCode.objects.create(city_code ="4303400", 
                                city_name ="Caiçara")

        CityCode.objects.create(city_code ="4303509", 
                                city_name ="Camaquã")

        CityCode.objects.create(city_code ="4303558", 
                                city_name ="Camargo")

        CityCode.objects.create(city_code ="4303608", 
                                city_name ="Cambará do Sul")

        CityCode.objects.create(city_code ="4303673", 
                                city_name ="Campestre da Serra")

        CityCode.objects.create(city_code ="4303707", 
                                city_name ="Campina das Missões")

        CityCode.objects.create(city_code ="4303806", 
                                city_name ="Campinas do Sul")

        CityCode.objects.create(city_code ="4303905", 
                                city_name ="Campo Bom")

        CityCode.objects.create(city_code ="4304002", 
                                city_name ="Campo Novo")

        CityCode.objects.create(city_code ="4304101", 
                                city_name ="Campos Borges")

        CityCode.objects.create(city_code ="4304200", 
                                city_name ="Candelária")

        CityCode.objects.create(city_code ="4304309", 
                                city_name ="Cândido Godói")

        CityCode.objects.create(city_code ="4304358", 
                                city_name ="Candiota")

        CityCode.objects.create(city_code ="4304408", 
                                city_name ="Canela")

        CityCode.objects.create(city_code ="4304507", 
                                city_name ="Canguçu")

        CityCode.objects.create(city_code ="4304606", 
                                city_name ="Canoas")

        CityCode.objects.create(city_code ="4304614", 
                                city_name ="Canudos do Vale")

        CityCode.objects.create(city_code ="4304622", 
                                city_name ="Capão Bonito do Sul")

        CityCode.objects.create(city_code ="4304630", 
                                city_name ="Capão da Canoa")

        CityCode.objects.create(city_code ="4304655", 
                                city_name ="Capão do Cipó")

        CityCode.objects.create(city_code ="4304663", 
                                city_name ="Capão do Leão")

        CityCode.objects.create(city_code ="4304689", 
                                city_name ="Capela de Santana")

        CityCode.objects.create(city_code ="4304697", 
                                city_name ="Capitão")

        CityCode.objects.create(city_code ="4304671", 
                                city_name ="Capivari do Sul")

        CityCode.objects.create(city_code ="4304713", 
                                city_name ="Caraá")

        CityCode.objects.create(city_code ="4304705", 
                                city_name ="Carazinho")

        CityCode.objects.create(city_code ="4304804", 
                                city_name ="Carlos Barbosa")

        CityCode.objects.create(city_code ="4304853", 
                                city_name ="Carlos Gomes")

        CityCode.objects.create(city_code ="4304903", 
                                city_name ="Casca")

        CityCode.objects.create(city_code ="4304952", 
                                city_name ="Caseiros")

        CityCode.objects.create(city_code ="4305009", 
                                city_name ="Catuípe")

        CityCode.objects.create(city_code ="4305108", 
                                city_name ="Caxias do Sul")

        CityCode.objects.create(city_code ="4305116", 
                                city_name ="Centenário")

        CityCode.objects.create(city_code ="4305124", 
                                city_name ="Cerrito")

        CityCode.objects.create(city_code ="4305132", 
                                city_name ="Cerro Branco")

        CityCode.objects.create(city_code ="4305157", 
                                city_name ="Cerro Grande")

        CityCode.objects.create(city_code ="4305173", 
                                city_name ="Cerro Grande do Sul")

        CityCode.objects.create(city_code ="4305207", 
                                city_name ="Cerro Largo")

        CityCode.objects.create(city_code ="4305306", 
                                city_name ="Chapada")

        CityCode.objects.create(city_code ="4305355", 
                                city_name ="Charqueadas")

        CityCode.objects.create(city_code ="4305371", 
                                city_name ="Charrua")

        CityCode.objects.create(city_code ="4305405", 
                                city_name ="Chiapetta")

        CityCode.objects.create(city_code ="4305439", 
                                city_name ="Chuí")

        CityCode.objects.create(city_code ="4305447", 
                                city_name ="Chuvisca")

        CityCode.objects.create(city_code ="4305454", 
                                city_name ="Cidreira")

        CityCode.objects.create(city_code ="4305504", 
                                city_name ="Ciríaco")

        CityCode.objects.create(city_code ="4305587", 
                                city_name ="Colinas")

        CityCode.objects.create(city_code ="4305603", 
                                city_name ="Colorado")

        CityCode.objects.create(city_code ="4305702", 
                                city_name ="Condor")

        CityCode.objects.create(city_code ="4305801", 
                                city_name ="Constantina")

        CityCode.objects.create(city_code ="4305835", 
                                city_name ="Coqueiro Baixo")

        CityCode.objects.create(city_code ="4305850", 
                                city_name ="Coqueiros do Sul")

        CityCode.objects.create(city_code ="4305871", 
                                city_name ="Coronel Barros")

        CityCode.objects.create(city_code ="4305900", 
                                city_name ="Coronel Bicaco")

        CityCode.objects.create(city_code ="4305934", 
                                city_name ="Coronel Pilar")

        CityCode.objects.create(city_code ="4305959", 
                                city_name ="Cotiporã")

        CityCode.objects.create(city_code ="4305975", 
                                city_name ="Coxilha")

        CityCode.objects.create(city_code ="4306007", 
                                city_name ="Crissiumal")

        CityCode.objects.create(city_code ="4306056", 
                                city_name ="Cristal")

        CityCode.objects.create(city_code ="4306072", 
                                city_name ="Cristal do Sul")

        CityCode.objects.create(city_code ="4306106", 
                                city_name ="Cruz Alta")

        CityCode.objects.create(city_code ="4306130", 
                                city_name ="Cruzaltense")

        CityCode.objects.create(city_code ="4306205", 
                                city_name ="Cruzeiro do Sul")

        CityCode.objects.create(city_code ="4306304", 
                                city_name ="David Canabarro")

        CityCode.objects.create(city_code ="4306320", 
                                city_name ="Derrubadas")

        CityCode.objects.create(city_code ="4306353", 
                                city_name ="Dezesseis de Novembro")

        CityCode.objects.create(city_code ="4306379", 
                                city_name ="Dilermando de Aguiar")

        CityCode.objects.create(city_code ="4306403", 
                                city_name ="Dois Irmãos")

        CityCode.objects.create(city_code ="4306429", 
                                city_name ="Dois Irmãos das Missões")

        CityCode.objects.create(city_code ="4306452", 
                                city_name ="Dois Lajeados")

        CityCode.objects.create(city_code ="4306502", 
                                city_name ="Dom Feliciano")

        CityCode.objects.create(city_code ="4306601", 
                                city_name ="Dom Pedrito")

        CityCode.objects.create(city_code ="4306551", 
                                city_name ="Dom Pedro de Alcântara")

        CityCode.objects.create(city_code ="4306700", 
                                city_name ="Dona Francisca")

        CityCode.objects.create(city_code ="4306734", 
                                city_name ="Doutor Maurício Cardoso")

        CityCode.objects.create(city_code ="4306759", 
                                city_name ="Doutor Ricardo")

        CityCode.objects.create(city_code ="4306767", 
                                city_name ="Eldorado do Sul")

        CityCode.objects.create(city_code ="4306809", 
                                city_name ="Encantado")

        CityCode.objects.create(city_code ="4306908", 
                                city_name ="Encruzilhada do Sul")

        CityCode.objects.create(city_code ="4306924", 
                                city_name ="Engenho Velho")

        CityCode.objects.create(city_code ="4306957", 
                                city_name ="Entre Rios do Sul")

        CityCode.objects.create(city_code ="4306932", 
                                city_name ="Entre-Ijuís")

        CityCode.objects.create(city_code ="4306973", 
                                city_name ="Erebango")

        CityCode.objects.create(city_code ="4307005", 
                                city_name ="Erechim")

        CityCode.objects.create(city_code ="4307054", 
                                city_name ="Ernestina")

        CityCode.objects.create(city_code ="4307203", 
                                city_name ="Erval Grande")

        CityCode.objects.create(city_code ="4307302", 
                                city_name ="Erval Seco")

        CityCode.objects.create(city_code ="4307401", 
                                city_name ="Esmeralda")

        CityCode.objects.create(city_code ="4307450", 
                                city_name ="Esperança do Sul")

        CityCode.objects.create(city_code ="4307500", 
                                city_name ="Espumoso")

        CityCode.objects.create(city_code ="4307559", 
                                city_name ="Estação")

        CityCode.objects.create(city_code ="4307609", 
                                city_name ="Estância Velha")

        CityCode.objects.create(city_code ="4307708", 
                                city_name ="Esteio")

        CityCode.objects.create(city_code ="4307807", 
                                city_name ="Estrela")

        CityCode.objects.create(city_code ="4307815", 
                                city_name ="Estrela Velha")

        CityCode.objects.create(city_code ="4307831", 
                                city_name ="Eugênio de Castro")

        CityCode.objects.create(city_code ="4307864", 
                                city_name ="Fagundes Varela")

        CityCode.objects.create(city_code ="4307906", 
                                city_name ="Farroupilha")

        CityCode.objects.create(city_code ="4308003", 
                                city_name ="Faxinal do Soturno")

        CityCode.objects.create(city_code ="4308052", 
                                city_name ="Faxinalzinho")

        CityCode.objects.create(city_code ="4308078", 
                                city_name ="Fazenda Vilanova")

        CityCode.objects.create(city_code ="4308102", 
                                city_name ="Feliz")

        CityCode.objects.create(city_code ="4308201", 
                                city_name ="Flores da Cunha")

        CityCode.objects.create(city_code ="4308250", 
                                city_name ="Floriano Peixoto")

        CityCode.objects.create(city_code ="4308300", 
                                city_name ="Fontoura Xavier")

        CityCode.objects.create(city_code ="4308409", 
                                city_name ="Formigueiro")

        CityCode.objects.create(city_code ="4308433", 
                                city_name ="Forquetinha")

        CityCode.objects.create(city_code ="4308458", 
                                city_name ="Fortaleza dos Valos")

        CityCode.objects.create(city_code ="4308508", 
                                city_name ="Frederico Westphalen")

        CityCode.objects.create(city_code ="4308607", 
                                city_name ="Garibaldi")

        CityCode.objects.create(city_code ="4308656", 
                                city_name ="Garruchos")

        CityCode.objects.create(city_code ="4308706", 
                                city_name ="Gaurama")

        CityCode.objects.create(city_code ="4308805", 
                                city_name ="General Câmara")

        CityCode.objects.create(city_code ="4308854", 
                                city_name ="Gentil")

        CityCode.objects.create(city_code ="4308904", 
                                city_name ="Getúlio Vargas")

        CityCode.objects.create(city_code ="4309001", 
                                city_name ="Giruá")

        CityCode.objects.create(city_code ="4309050", 
                                city_name ="Glorinha")

        CityCode.objects.create(city_code ="4309100", 
                                city_name ="Gramado")

        CityCode.objects.create(city_code ="4309126", 
                                city_name ="Gramado dos Loureiros")

        CityCode.objects.create(city_code ="4309159", 
                                city_name ="Gramado Xavier")

        CityCode.objects.create(city_code ="4309209", 
                                city_name ="Gravataí")

        CityCode.objects.create(city_code ="4309258", 
                                city_name ="Guabiju")

        CityCode.objects.create(city_code ="4309308", 
                                city_name ="Guaíba")

        CityCode.objects.create(city_code ="4309407", 
                                city_name ="Guaporé")

        CityCode.objects.create(city_code ="4309506", 
                                city_name ="Guarani das Missões")

        CityCode.objects.create(city_code ="4309555", 
                                city_name ="Harmonia")

        CityCode.objects.create(city_code ="4307104", 
                                city_name ="Herval")

        CityCode.objects.create(city_code ="4309571", 
                                city_name ="Herveiras")

        CityCode.objects.create(city_code ="4309605", 
                                city_name ="Horizontina")

        CityCode.objects.create(city_code ="4309654", 
                                city_name ="Hulha Negra")

        CityCode.objects.create(city_code ="4309704", 
                                city_name ="Humaitá")

        CityCode.objects.create(city_code ="4309753", 
                                city_name ="Ibarama")

        CityCode.objects.create(city_code ="4309803", 
                                city_name ="Ibiaçá")

        CityCode.objects.create(city_code ="4309902", 
                                city_name ="Ibiraiaras")

        CityCode.objects.create(city_code ="4309951", 
                                city_name ="Ibirapuitã")

        CityCode.objects.create(city_code ="4310009", 
                                city_name ="Ibirubá")

        CityCode.objects.create(city_code ="4310108", 
                                city_name ="Igrejinha")

        CityCode.objects.create(city_code ="4310207", 
                                city_name ="Ijuí")

        CityCode.objects.create(city_code ="4310306", 
                                city_name ="Ilópolis")

        CityCode.objects.create(city_code ="4310330", 
                                city_name ="Imbé")

        CityCode.objects.create(city_code ="4310363", 
                                city_name ="Imigrante")

        CityCode.objects.create(city_code ="4310405", 
                                city_name ="Independência")

        CityCode.objects.create(city_code ="4310413", 
                                city_name ="Inhacorá")

        CityCode.objects.create(city_code ="4310439", 
                                city_name ="Ipê")

        CityCode.objects.create(city_code ="4310462", 
                                city_name ="Ipiranga do Sul")

        CityCode.objects.create(city_code ="4310504", 
                                city_name ="Iraí")

        CityCode.objects.create(city_code ="4310538", 
                                city_name ="Itaara")

        CityCode.objects.create(city_code ="4310553", 
                                city_name ="Itacurubi")

        CityCode.objects.create(city_code ="4310579", 
                                city_name ="Itapuca")

        CityCode.objects.create(city_code ="4310603", 
                                city_name ="Itaqui")

        CityCode.objects.create(city_code ="4310652", 
                                city_name ="Itati")

        CityCode.objects.create(city_code ="4310702", 
                                city_name ="Itatiba do Sul")

        CityCode.objects.create(city_code ="4310751", 
                                city_name ="Ivorá")

        CityCode.objects.create(city_code ="4310801", 
                                city_name ="Ivoti")

        CityCode.objects.create(city_code ="4310850", 
                                city_name ="Jaboticaba")

        CityCode.objects.create(city_code ="4310876", 
                                city_name ="Jacuizinho")

        CityCode.objects.create(city_code ="4310900", 
                                city_name ="Jacutinga")

        CityCode.objects.create(city_code ="4311007", 
                                city_name ="Jaguarão")

        CityCode.objects.create(city_code ="4311106", 
                                city_name ="Jaguari")

        CityCode.objects.create(city_code ="4311122", 
                                city_name ="Jaquirana")

        CityCode.objects.create(city_code ="4311130", 
                                city_name ="Jari")

        CityCode.objects.create(city_code ="4311155", 
                                city_name ="Jóia")

        CityCode.objects.create(city_code ="4311205", 
                                city_name ="Júlio de Castilhos")

        CityCode.objects.create(city_code ="4311239", 
                                city_name ="Lagoa Bonita do Sul")

        CityCode.objects.create(city_code ="4311270", 
                                city_name ="Lagoa dos Três Cantos")

        CityCode.objects.create(city_code ="4311304", 
                                city_name ="Lagoa Vermelha")

        CityCode.objects.create(city_code ="4311254", 
                                city_name ="Lagoão")

        CityCode.objects.create(city_code ="4311403", 
                                city_name ="Lajeado")

        CityCode.objects.create(city_code ="4311429", 
                                city_name ="Lajeado do Bugre")

        CityCode.objects.create(city_code ="4311502", 
                                city_name ="Lavras do Sul")

        CityCode.objects.create(city_code ="4311601", 
                                city_name ="Liberato Salzano")

        CityCode.objects.create(city_code ="4311627", 
                                city_name ="Lindolfo Collor")

        CityCode.objects.create(city_code ="4311643", 
                                city_name ="Linha Nova")

        CityCode.objects.create(city_code ="4311718", 
                                city_name ="Maçambará")

        CityCode.objects.create(city_code ="4311700", 
                                city_name ="Machadinho")

        CityCode.objects.create(city_code ="4311734", 
                                city_name ="Mampituba")

        CityCode.objects.create(city_code ="4311759", 
                                city_name ="Manoel Viana")

        CityCode.objects.create(city_code ="4311775", 
                                city_name ="Maquiné")

        CityCode.objects.create(city_code ="4311791", 
                                city_name ="Maratá")

        CityCode.objects.create(city_code ="4311809", 
                                city_name ="Marau")

        CityCode.objects.create(city_code ="4311908", 
                                city_name ="Marcelino Ramos")

        CityCode.objects.create(city_code ="4311981", 
                                city_name ="Mariana Pimentel")

        CityCode.objects.create(city_code ="4312005", 
                                city_name ="Mariano Moro")

        CityCode.objects.create(city_code ="4312054", 
                                city_name ="Marques de Souza")

        CityCode.objects.create(city_code ="4312104", 
                                city_name ="Mata")

        CityCode.objects.create(city_code ="4312138", 
                                city_name ="Mato Castelhano")

        CityCode.objects.create(city_code ="4312153", 
                                city_name ="Mato Leitão")

        CityCode.objects.create(city_code ="4312179", 
                                city_name ="Mato Queimado")

        CityCode.objects.create(city_code ="4312203", 
                                city_name ="Maximiliano de Almeida")

        CityCode.objects.create(city_code ="4312252", 
                                city_name ="Minas do Leão")

        CityCode.objects.create(city_code ="4312302", 
                                city_name ="Miraguaí")

        CityCode.objects.create(city_code ="4312351", 
                                city_name ="Montauri")

        CityCode.objects.create(city_code ="4312377", 
                                city_name ="Monte Alegre dos Campos")

        CityCode.objects.create(city_code ="4312385", 
                                city_name ="Monte Belo do Sul")

        CityCode.objects.create(city_code ="4312401", 
                                city_name ="Montenegro")

        CityCode.objects.create(city_code ="4312427", 
                                city_name ="Mormaço")

        CityCode.objects.create(city_code ="4312443", 
                                city_name ="Morrinhos do Sul")

        CityCode.objects.create(city_code ="4312450", 
                                city_name ="Morro Redondo")

        CityCode.objects.create(city_code ="4312476", 
                                city_name ="Morro Reuter")

        CityCode.objects.create(city_code ="4312500", 
                                city_name ="Mostardas")

        CityCode.objects.create(city_code ="4312609", 
                                city_name ="Muçum")

        CityCode.objects.create(city_code ="4312617", 
                                city_name ="Muitos Capões")

        CityCode.objects.create(city_code ="4312625", 
                                city_name ="Muliterno")

        CityCode.objects.create(city_code ="4312658", 
                                city_name ="Não-Me-Toque")

        CityCode.objects.create(city_code ="4312674", 
                                city_name ="Nicolau Vergueiro")

        CityCode.objects.create(city_code ="4312708", 
                                city_name ="Nonoai")

        CityCode.objects.create(city_code ="4312757", 
                                city_name ="Nova Alvorada")

        CityCode.objects.create(city_code ="4312807", 
                                city_name ="Nova Araçá")

        CityCode.objects.create(city_code ="4312906", 
                                city_name ="Nova Bassano")

        CityCode.objects.create(city_code ="4312955", 
                                city_name ="Nova Boa Vista")

        CityCode.objects.create(city_code ="4313003", 
                                city_name ="Nova Bréscia")

        CityCode.objects.create(city_code ="4313011", 
                                city_name ="Nova Candelária")

        CityCode.objects.create(city_code ="4313037", 
                                city_name ="Nova Esperança do Sul")

        CityCode.objects.create(city_code ="4313060", 
                                city_name ="Nova Hartz")

        CityCode.objects.create(city_code ="4313086", 
                                city_name ="Nova Pádua")

        CityCode.objects.create(city_code ="4313102", 
                                city_name ="Nova Palma")

        CityCode.objects.create(city_code ="4313201", 
                                city_name ="Nova Petrópolis")

        CityCode.objects.create(city_code ="4313300", 
                                city_name ="Nova Prata")

        CityCode.objects.create(city_code ="4313334", 
                                city_name ="Nova Ramada")

        CityCode.objects.create(city_code ="4313359", 
                                city_name ="Nova Roma do Sul")

        CityCode.objects.create(city_code ="4313375", 
                                city_name ="Nova Santa Rita")

        CityCode.objects.create(city_code ="4313490", 
                                city_name ="Novo Barreiro")

        CityCode.objects.create(city_code ="4313391", 
                                city_name ="Novo Cabrais")

        CityCode.objects.create(city_code ="4313409", 
                                city_name ="Novo Hamburgo")

        CityCode.objects.create(city_code ="4313425", 
                                city_name ="Novo Machado")

        CityCode.objects.create(city_code ="4313441", 
                                city_name ="Novo Tiradentes")

        CityCode.objects.create(city_code ="4313466", 
                                city_name ="Novo Xingu")

        CityCode.objects.create(city_code ="4313508", 
                                city_name ="Osório")

        CityCode.objects.create(city_code ="4313607", 
                                city_name ="Paim Filho")

        CityCode.objects.create(city_code ="4313656", 
                                city_name ="Palmares do Sul")

        CityCode.objects.create(city_code ="4313706", 
                                city_name ="Palmeira das Missões")

        CityCode.objects.create(city_code ="4313805", 
                                city_name ="Palmitinho")

        CityCode.objects.create(city_code ="4313904", 
                                city_name ="Panambi")

        CityCode.objects.create(city_code ="4313953", 
                                city_name ="Pantano Grande")

        CityCode.objects.create(city_code ="4314001", 
                                city_name ="Paraí")

        CityCode.objects.create(city_code ="4314027", 
                                city_name ="Paraíso do Sul")

        CityCode.objects.create(city_code ="4314035", 
                                city_name ="Pareci Novo")

        CityCode.objects.create(city_code ="4314050", 
                                city_name ="Parobé")

        CityCode.objects.create(city_code ="4314068", 
                                city_name ="Passa Sete")

        CityCode.objects.create(city_code ="4314076", 
                                city_name ="Passo do Sobrado")

        CityCode.objects.create(city_code ="4314100", 
                                city_name ="Passo Fundo")

        CityCode.objects.create(city_code ="4314134", 
                                city_name ="Paulo Bento")

        CityCode.objects.create(city_code ="4314159", 
                                city_name ="Paverama")

        CityCode.objects.create(city_code ="4314175", 
                                city_name ="Pedras Altas")

        CityCode.objects.create(city_code ="4314209", 
                                city_name ="Pedro Osório")

        CityCode.objects.create(city_code ="4314308", 
                                city_name ="Pejuçara")

        CityCode.objects.create(city_code ="4314407", 
                                city_name ="Pelotas")

        CityCode.objects.create(city_code ="4314423", 
                                city_name ="Picada Café")

        CityCode.objects.create(city_code ="4314456", 
                                city_name ="Pinhal")

        CityCode.objects.create(city_code ="4314464", 
                                city_name ="Pinhal da Serra")

        CityCode.objects.create(city_code ="4314472", 
                                city_name ="Pinhal Grande")

        CityCode.objects.create(city_code ="4314498", 
                                city_name ="Pinheirinho do Vale")

        CityCode.objects.create(city_code ="4314506", 
                                city_name ="Pinheiro Machado")

        CityCode.objects.create(city_code ="4314548", 
                                city_name ="Pinto Bandeira")

        CityCode.objects.create(city_code ="4314555", 
                                city_name ="Pirapó")

        CityCode.objects.create(city_code ="4314605", 
                                city_name ="Piratini")

        CityCode.objects.create(city_code ="4314704", 
                                city_name ="Planalto")

        CityCode.objects.create(city_code ="4314753", 
                                city_name ="Poço das Antas")

        CityCode.objects.create(city_code ="4314779", 
                                city_name ="Pontão")

        CityCode.objects.create(city_code ="4314787", 
                                city_name ="Ponte Preta")

        CityCode.objects.create(city_code ="4314803", 
                                city_name ="Portão")

        CityCode.objects.create(city_code ="4314902", 
                                city_name ="Porto Alegre")

        CityCode.objects.create(city_code ="4315008", 
                                city_name ="Porto Lucena")

        CityCode.objects.create(city_code ="4315057", 
                                city_name ="Porto Mauá")

        CityCode.objects.create(city_code ="4315073", 
                                city_name ="Porto Vera Cruz")

        CityCode.objects.create(city_code ="4315107", 
                                city_name ="Porto Xavier")

        CityCode.objects.create(city_code ="4315131", 
                                city_name ="Pouso Novo")

        CityCode.objects.create(city_code ="4315149", 
                                city_name ="Presidente Lucena")

        CityCode.objects.create(city_code ="4315156", 
                                city_name ="Progresso")

        CityCode.objects.create(city_code ="4315172", 
                                city_name ="Protásio Alves")

        CityCode.objects.create(city_code ="4315206", 
                                city_name ="Putinga")

        CityCode.objects.create(city_code ="4315305", 
                                city_name ="Quaraí")

        CityCode.objects.create(city_code ="4315313", 
                                city_name ="Quatro Irmãos")

        CityCode.objects.create(city_code ="4315321", 
                                city_name ="Quevedos")

        CityCode.objects.create(city_code ="4315354", 
                                city_name ="Quinze de Novembro")

        CityCode.objects.create(city_code ="4315404", 
                                city_name ="Redentora")

        CityCode.objects.create(city_code ="4315453", 
                                city_name ="Relvado")

        CityCode.objects.create(city_code ="4315503", 
                                city_name ="Restinga Sêca")

        CityCode.objects.create(city_code ="4315552", 
                                city_name ="Rio dos Índios")

        CityCode.objects.create(city_code ="4315602", 
                                city_name ="Rio Grande")

        CityCode.objects.create(city_code ="4315701", 
                                city_name ="Rio Pardo")

        CityCode.objects.create(city_code ="4315750", 
                                city_name ="Riozinho")

        CityCode.objects.create(city_code ="4315800", 
                                city_name ="Roca Sales")

        CityCode.objects.create(city_code ="4315909", 
                                city_name ="Rodeio Bonito")

        CityCode.objects.create(city_code ="4315958", 
                                city_name ="Rolador")

        CityCode.objects.create(city_code ="4316006", 
                                city_name ="Rolante")

        CityCode.objects.create(city_code ="4316105", 
                                city_name ="Ronda Alta")

        CityCode.objects.create(city_code ="4316204", 
                                city_name ="Rondinha")

        CityCode.objects.create(city_code ="4316303", 
                                city_name ="Roque Gonzales")

        CityCode.objects.create(city_code ="4316402", 
                                city_name ="Rosário do Sul")

        CityCode.objects.create(city_code ="4316428", 
                                city_name ="Sagrada Família")

        CityCode.objects.create(city_code ="4316436", 
                                city_name ="Saldanha Marinho")

        CityCode.objects.create(city_code ="4316451", 
                                city_name ="Salto do Jacuí")

        CityCode.objects.create(city_code ="4316477", 
                                city_name ="Salvador das Missões")

        CityCode.objects.create(city_code ="4316501", 
                                city_name ="Salvador do Sul")

        CityCode.objects.create(city_code ="4316600", 
                                city_name ="Sananduva")

        CityCode.objects.create(city_code ="4316709", 
                                city_name ="Santa Bárbara do Sul")

        CityCode.objects.create(city_code ="4316733", 
                                city_name ="Santa Cecília do Sul")

        CityCode.objects.create(city_code ="4316758", 
                                city_name ="Santa Clara do Sul")

        CityCode.objects.create(city_code ="4316808", 
                                city_name ="Santa Cruz do Sul")

        CityCode.objects.create(city_code ="4316972", 
                                city_name ="Santa Margarida do Sul")

        CityCode.objects.create(city_code ="4316907", 
                                city_name ="Santa Maria")

        CityCode.objects.create(city_code ="4316956", 
                                city_name ="Santa Maria do Herval")

        CityCode.objects.create(city_code ="4317202", 
                                city_name ="Santa Rosa")

        CityCode.objects.create(city_code ="4317251", 
                                city_name ="Santa Tereza")

        CityCode.objects.create(city_code ="4317301", 
                                city_name ="Santa Vitória do Palmar")

        CityCode.objects.create(city_code ="4317004", 
                                city_name ="Santana da Boa Vista")

        CityCode.objects.create(city_code ="4317103", 
                                city_name ="Sant'Ana do Livramento")

        CityCode.objects.create(city_code ="4317400", 
                                city_name ="Santiago")

        CityCode.objects.create(city_code ="4317509", 
                                city_name ="Santo Ângelo")

        CityCode.objects.create(city_code ="4317608", 
                                city_name ="Santo Antônio da Patrulha")

        CityCode.objects.create(city_code ="4317707", 
                                city_name ="Santo Antônio das Missões")

        CityCode.objects.create(city_code ="4317558", 
                                city_name ="Santo Antônio do Palma")

        CityCode.objects.create(city_code ="4317756", 
                                city_name ="Santo Antônio do Planalto")

        CityCode.objects.create(city_code ="4317806", 
                                city_name ="Santo Augusto")

        CityCode.objects.create(city_code ="4317905", 
                                city_name ="Santo Cristo")

        CityCode.objects.create(city_code ="4317954", 
                                city_name ="Santo Expedito do Sul")

        CityCode.objects.create(city_code ="4318002", 
                                city_name ="São Borja")

        CityCode.objects.create(city_code ="4318051", 
                                city_name ="São Domingos do Sul")

        CityCode.objects.create(city_code ="4318101", 
                                city_name ="São Francisco de Assis")

        CityCode.objects.create(city_code ="4318200", 
                                city_name ="São Francisco de Paula")

        CityCode.objects.create(city_code ="4318309", 
                                city_name ="São Gabriel")

        CityCode.objects.create(city_code ="4318408", 
                                city_name ="São Jerônimo")

        CityCode.objects.create(city_code ="4318424", 
                                city_name ="São João da Urtiga")

        CityCode.objects.create(city_code ="4318432", 
                                city_name ="São João do Polêsine")

        CityCode.objects.create(city_code ="4318440", 
                                city_name ="São Jorge")

        CityCode.objects.create(city_code ="4318457", 
                                city_name ="São José das Missões")

        CityCode.objects.create(city_code ="4318465", 
                                city_name ="São José do Herval")

        CityCode.objects.create(city_code ="4318481", 
                                city_name ="São José do Hortêncio")

        CityCode.objects.create(city_code ="4318499", 
                                city_name ="São José do Inhacorá")

        CityCode.objects.create(city_code ="4318507", 
                                city_name ="São José do Norte")

        CityCode.objects.create(city_code ="4318606", 
                                city_name ="São José do Ouro")

        CityCode.objects.create(city_code ="4318614", 
                                city_name ="São José do Sul")

        CityCode.objects.create(city_code ="4318622", 
                                city_name ="São José dos Ausentes")

        CityCode.objects.create(city_code ="4318705", 
                                city_name ="São Leopoldo")

        CityCode.objects.create(city_code ="4318804", 
                                city_name ="São Lourenço do Sul")

        CityCode.objects.create(city_code ="4318903", 
                                city_name ="São Luiz Gonzaga")

        CityCode.objects.create(city_code ="4319000", 
                                city_name ="São Marcos")

        CityCode.objects.create(city_code ="4319109", 
                                city_name ="São Martinho")

        CityCode.objects.create(city_code ="4319125", 
                                city_name ="São Martinho da Serra")

        CityCode.objects.create(city_code ="4319158", 
                                city_name ="São Miguel das Missões")

        CityCode.objects.create(city_code ="4319208", 
                                city_name ="São Nicolau")

        CityCode.objects.create(city_code ="4319307", 
                                city_name ="São Paulo das Missões")

        CityCode.objects.create(city_code ="4319356", 
                                city_name ="São Pedro da Serra")

        CityCode.objects.create(city_code ="4319364", 
                                city_name ="São Pedro das Missões")

        CityCode.objects.create(city_code ="4319372", 
                                city_name ="São Pedro do Butiá")

        CityCode.objects.create(city_code ="4319406", 
                                city_name ="São Pedro do Sul")

        CityCode.objects.create(city_code ="4319505", 
                                city_name ="São Sebastião do Caí")

        CityCode.objects.create(city_code ="4319604", 
                                city_name ="São Sepé")

        CityCode.objects.create(city_code ="4319703", 
                                city_name ="São Valentim")

        CityCode.objects.create(city_code ="4319711", 
                                city_name ="São Valentim do Sul")

        CityCode.objects.create(city_code ="4319737", 
                                city_name ="São Valério do Sul")

        CityCode.objects.create(city_code ="4319752", 
                                city_name ="São Vendelino")

        CityCode.objects.create(city_code ="4319802", 
                                city_name ="São Vicente do Sul")

        CityCode.objects.create(city_code ="4319901", 
                                city_name ="Sapiranga")

        CityCode.objects.create(city_code ="4320008", 
                                city_name ="Sapucaia do Sul")

        CityCode.objects.create(city_code ="4320107", 
                                city_name ="Sarandi")

        CityCode.objects.create(city_code ="4320206", 
                                city_name ="Seberi")

        CityCode.objects.create(city_code ="4320230", 
                                city_name ="Sede Nova")

        CityCode.objects.create(city_code ="4320263", 
                                city_name ="Segredo")

        CityCode.objects.create(city_code ="4320305", 
                                city_name ="Selbach")

        CityCode.objects.create(city_code ="4320321", 
                                city_name ="Senador Salgado Filho")

        CityCode.objects.create(city_code ="4320354", 
                                city_name ="Sentinela do Sul")

        CityCode.objects.create(city_code ="4320404", 
                                city_name ="Serafina Corrêa")

        CityCode.objects.create(city_code ="4320453", 
                                city_name ="Sério")

        CityCode.objects.create(city_code ="4320503", 
                                city_name ="Sertão")

        CityCode.objects.create(city_code ="4320552", 
                                city_name ="Sertão Santana")

        CityCode.objects.create(city_code ="4320578", 
                                city_name ="Sete de Setembro")

        CityCode.objects.create(city_code ="4320602", 
                                city_name ="Severiano de Almeida")

        CityCode.objects.create(city_code ="4320651", 
                                city_name ="Silveira Martins")

        CityCode.objects.create(city_code ="4320677", 
                                city_name ="Sinimbu")

        CityCode.objects.create(city_code ="4320701", 
                                city_name ="Sobradinho")

        CityCode.objects.create(city_code ="4320800", 
                                city_name ="Soledade")

        CityCode.objects.create(city_code ="4320859", 
                                city_name ="Tabaí")

        CityCode.objects.create(city_code ="4320909", 
                                city_name ="Tapejara")

        CityCode.objects.create(city_code ="4321006", 
                                city_name ="Tapera")

        CityCode.objects.create(city_code ="4321105", 
                                city_name ="Tapes")

        CityCode.objects.create(city_code ="4321204", 
                                city_name ="Taquara")

        CityCode.objects.create(city_code ="4321303", 
                                city_name ="Taquari")

        CityCode.objects.create(city_code ="4321329", 
                                city_name ="Taquaruçu do Sul")

        CityCode.objects.create(city_code ="4321352", 
                                city_name ="Tavares")

        CityCode.objects.create(city_code ="4321402", 
                                city_name ="Tenente Portela")

        CityCode.objects.create(city_code ="4321436", 
                                city_name ="Terra de Areia")

        CityCode.objects.create(city_code ="4321451", 
                                city_name ="Teutônia")

        CityCode.objects.create(city_code ="4321469", 
                                city_name ="Tio Hugo")

        CityCode.objects.create(city_code ="4321477", 
                                city_name ="Tiradentes do Sul")

        CityCode.objects.create(city_code ="4321493", 
                                city_name ="Toropi")

        CityCode.objects.create(city_code ="4321501", 
                                city_name ="Torres")

        CityCode.objects.create(city_code ="4321600", 
                                city_name ="Tramandaí")

        CityCode.objects.create(city_code ="4321626", 
                                city_name ="Travesseiro")

        CityCode.objects.create(city_code ="4321634", 
                                city_name ="Três Arroios")

        CityCode.objects.create(city_code ="4321667", 
                                city_name ="Três Cachoeiras")

        CityCode.objects.create(city_code ="4321709", 
                                city_name ="Três Coroas")

        CityCode.objects.create(city_code ="4321808", 
                                city_name ="Três de Maio")

        CityCode.objects.create(city_code ="4321832", 
                                city_name ="Três Forquilhas")

        CityCode.objects.create(city_code ="4321857", 
                                city_name ="Três Palmeiras")

        CityCode.objects.create(city_code ="4321907", 
                                city_name ="Três Passos")

        CityCode.objects.create(city_code ="4321956", 
                                city_name ="Trindade do Sul")

        CityCode.objects.create(city_code ="4322004", 
                                city_name ="Triunfo")

        CityCode.objects.create(city_code ="4322103", 
                                city_name ="Tucunduva")

        CityCode.objects.create(city_code ="4322152", 
                                city_name ="Tunas")

        CityCode.objects.create(city_code ="4322186", 
                                city_name ="Tupanci do Sul")

        CityCode.objects.create(city_code ="4322202", 
                                city_name ="Tupanciretã")

        CityCode.objects.create(city_code ="4322251", 
                                city_name ="Tupandi")

        CityCode.objects.create(city_code ="4322301", 
                                city_name ="Tuparendi")

        CityCode.objects.create(city_code ="4322327", 
                                city_name ="Turuçu")

        CityCode.objects.create(city_code ="4322343", 
                                city_name ="Ubiretama")

        CityCode.objects.create(city_code ="4322350", 
                                city_name ="União da Serra")

        CityCode.objects.create(city_code ="4322376", 
                                city_name ="Unistalda")

        CityCode.objects.create(city_code ="4322400", 
                                city_name ="Uruguaiana")

        CityCode.objects.create(city_code ="4322509", 
                                city_name ="Vacaria")

        CityCode.objects.create(city_code ="4322533", 
                                city_name ="Vale do Sol")

        CityCode.objects.create(city_code ="4322541", 
                                city_name ="Vale Real")

        CityCode.objects.create(city_code ="4322525", 
                                city_name ="Vale Verde")

        CityCode.objects.create(city_code ="4322558", 
                                city_name ="Vanini")

        CityCode.objects.create(city_code ="4322608", 
                                city_name ="Venâncio Aires")

        CityCode.objects.create(city_code ="4322707", 
                                city_name ="Vera Cruz")

        CityCode.objects.create(city_code ="4322806", 
                                city_name ="Veranópolis")

        CityCode.objects.create(city_code ="4322855", 
                                city_name ="Vespasiano Corrêa")

        CityCode.objects.create(city_code ="4322905", 
                                city_name ="Viadutos")

        CityCode.objects.create(city_code ="4323002", 
                                city_name ="Viamão")

        CityCode.objects.create(city_code ="4323101", 
                                city_name ="Vicente Dutra")

        CityCode.objects.create(city_code ="4323200", 
                                city_name ="Victor Graeff")

        CityCode.objects.create(city_code ="4323309", 
                                city_name ="Vila Flores")

        CityCode.objects.create(city_code ="4323358", 
                                city_name ="Vila Lângaro")

        CityCode.objects.create(city_code ="4323408", 
                                city_name ="Vila Maria")

        CityCode.objects.create(city_code ="4323457", 
                                city_name ="Vila Nova do Sul")

        CityCode.objects.create(city_code ="4323507", 
                                city_name ="Vista Alegre")

        CityCode.objects.create(city_code ="4323606", 
                                city_name ="Vista Alegre do Prata")

        CityCode.objects.create(city_code ="4323705", 
                                city_name ="Vista Gaúcha")

        CityCode.objects.create(city_code ="4323754", 
                                city_name ="Vitória das Missões")

        CityCode.objects.create(city_code ="4323770", 
                                city_name ="Westfália")

        CityCode.objects.create(city_code ="4323804", 
                                city_name ="Xangri-lá")

        CityCode.objects.create(city_code ="5000203", 
                                city_name = "Água Clara")    
        	
        CityCode.objects.create(city_code ="5000609", 
                                city_name ="Amamba")
         
        CityCode.objects.create(city_code ="5000252", 
                                city_name ="Alcinópolis")
        	
        CityCode.objects.create(city_code ="5000708", 
                                city_name = "Anastácio")    
        	
        CityCode.objects.create(city_code ="5000807", 
                                city_name = "Anaurilândia")    
        	
        CityCode.objects.create(city_code ="5000856", 
                                city_name = "Angélica")    
        	
        CityCode.objects.create(city_code ="5000906", 
                                city_name = "Antônio João")    
        	
        CityCode.objects.create(city_code ="5001003", 
                                city_name = "Aparecida do Taboado")    
        	
        CityCode.objects.create(city_code ="5001102", 
                                city_name = "Aquidauana")    
        	
        CityCode.objects.create(city_code ="5001243", 
                                city_name = "Aral Moreira")    
        	
        CityCode.objects.create(city_code ="5001508", 
                                city_name = "Bandeirantes")    
        	
        CityCode.objects.create(city_code ="5001904", 
                                city_name = "Bataguassu")    
        	
        CityCode.objects.create(city_code ="5002001", 
                                city_name = "Batayporã")    
        	
        CityCode.objects.create(city_code ="5002100", 
                                city_name = "Bela Vista")    
        	
        CityCode.objects.create(city_code ="5002159", 
                                city_name = "Bodoquena")    
        	
        CityCode.objects.create(city_code ="5002209", 
                                city_name = "Bonito")    
        	
        CityCode.objects.create(city_code ="5002308", 
                                city_name = "Brasilândia")    
        	
        CityCode.objects.create(city_code ="5002407", 
                                city_name = "Caarapó")    
        	
        CityCode.objects.create(city_code ="5002605", 
                                city_name = "Camapuã")    
        	
        CityCode.objects.create(city_code ="5002704", 
                                city_name = "Campo Grande")    
        	
        CityCode.objects.create(city_code ="5002803", 
                                city_name = "Caracol")    
        	
        CityCode.objects.create(city_code ="5002902", 
                                city_name = "Cassilândia")    
        	
        CityCode.objects.create(city_code ="5002951", 
                                city_name = "Chapadão do Sul")    
        	
        CityCode.objects.create(city_code ="5003108", 
                                city_name = "Corguinho")    
        	
        CityCode.objects.create(city_code ="5003157", 
                                city_name = "Coronel Sapucaia")    
        	
        CityCode.objects.create(city_code ="5003207", 
                                city_name = "Corumbá")    
        	
        CityCode.objects.create(city_code ="5003256", 
                                city_name = "Costa Rica")    
        	
        CityCode.objects.create(city_code ="5003306", 
                                city_name = "Coxim")    
        	
        CityCode.objects.create(city_code ="5003454", 
                                city_name = "Deodápolis")    
        	
        CityCode.objects.create(city_code ="5003488", 
                                city_name = "Dois Irmãos do Buriti")    
        	
        CityCode.objects.create(city_code ="5003504", 
                                city_name = "Douradina")    
        	
        CityCode.objects.create(city_code ="5003702", 
                                city_name = "Dourados")    
        	
        CityCode.objects.create(city_code ="5003751", 
                                city_name = "Eldorado")    
        	
        CityCode.objects.create(city_code ="5003801", 
                                city_name = "Fátima do Sul")    
        	
        CityCode.objects.create(city_code ="5003900", 
                                city_name = "Figueirão")    
        	
        CityCode.objects.create(city_code ="5004007", 
                                city_name = "Glória de Dourados")    
        	
        CityCode.objects.create(city_code ="5004106", 
                                city_name = "Guia Lopes da Laguna")    
        	
        CityCode.objects.create(city_code ="5004304", 
                                city_name = "Iguatemi")    
        	
        CityCode.objects.create(city_code ="5004403", 
                                city_name = "Inocência")    
        	
        CityCode.objects.create(city_code ="5004502", 
                                city_name = "Itaporã")    
        	
        CityCode.objects.create(city_code ="5004601", 
                                city_name = "Itaquiraí")    
        	
        CityCode.objects.create(city_code ="5004700", 
                                city_name = "Ivinhema")    
        	
        CityCode.objects.create(city_code ="5004809", 
                                city_name = "Japorã")    
        	
        CityCode.objects.create(city_code ="5004908", 
                                city_name = "Jaraguari")    
        	
        CityCode.objects.create(city_code ="5005004", 
                                city_name = "Jardim")    
        	
        CityCode.objects.create(city_code ="5005103", 
                                city_name = "Jateí")    
        	
        CityCode.objects.create(city_code ="5005152", 
                                city_name = "Juti")    
        	
        CityCode.objects.create(city_code ="5005202", 
                                city_name = "Ladário")    
        	
        CityCode.objects.create(city_code ="5005251", 
                                city_name = "Laguna Carapã")    
        	
        CityCode.objects.create(city_code ="5005400", 
                                city_name = "Maracaju")    
        	
        CityCode.objects.create(city_code ="5005608", 
                                city_name = "Miranda")    
        	
        CityCode.objects.create(city_code ="5005681", 
                                city_name = "Mundo Novo")    
        	
        CityCode.objects.create(city_code ="5005707", 
                                city_name = "Naviraí")    
        	
        CityCode.objects.create(city_code ="5005806", 
                                city_name = "Nioaque")    
        	
        CityCode.objects.create(city_code ="5006002", 
                                city_name = "Nova Alvorada do Sul")    
        	
        CityCode.objects.create(city_code ="5006200", 
                                city_name = "Nova Andradina")    
        	
        CityCode.objects.create(city_code ="5006259", 
                                city_name = "Novo Horizonte do Sul")    
        	
        CityCode.objects.create(city_code ="5006275", 
                                city_name = "Paraíso das Águas")    
        	
        CityCode.objects.create(city_code ="5006309", 
                                city_name = "Paranaíba")    
        	
        CityCode.objects.create(city_code ="5006358", 
                                city_name = "Paranhos")    
        	
        CityCode.objects.create(city_code ="5006408", 
                                city_name = "Pedro Gomes")    
        	
        CityCode.objects.create(city_code ="5006606", 
                                city_name = "Ponta Porã")    
        	
        CityCode.objects.create(city_code ="5006903", 
                                city_name = "Porto Murtinho")    
        	
        CityCode.objects.create(city_code ="5007109", 
                                city_name = "Ribas do Rio Pardo")    
        	
        CityCode.objects.create(city_code ="5007208", 
                                city_name = "Rio Brilhante")    
        	
        CityCode.objects.create(city_code ="5007307", 
                                city_name = "Rio Negro")    
        	
        CityCode.objects.create(city_code ="5007406", 
                                city_name = "Rio Verde de Mato Grosso")    
        	
        CityCode.objects.create(city_code ="5007505", 
                                city_name = "Rochedo")    
        	
        CityCode.objects.create(city_code ="5007554", 
                                city_name = "Santa Rita do Pardo")    
        	
        CityCode.objects.create(city_code ="5007695", 
                                city_name = "São Gabriel do Oeste")    
        	
        CityCode.objects.create(city_code ="5007802", 
                                city_name = "Selvíria")    
        	
        CityCode.objects.create(city_code ="5007703", 
                                city_name = "Sete Quedas")    
        	
        CityCode.objects.create(city_code ="5007901", 
                                city_name = "Sidrolândia")    
        	
        CityCode.objects.create(city_code ="5007935", 
                                city_name = "Sonora")    
        	
        CityCode.objects.create(city_code ="5007950", 
                                city_name = "Tacuru")    
        	
        CityCode.objects.create(city_code ="5007976", 
                                city_name = "Taquarussu")    
        	
        CityCode.objects.create(city_code ="5008008", 
                                city_name = "Terenos")    
        	
        CityCode.objects.create(city_code ="5008305", 
                                city_name = "Três Lagoas")    
        	
        CityCode.objects.create(city_code ="5008404", 
                                city_name = "Vicentina")    
        	
        CityCode.objects.create(city_code ="5100102", 
                                city_name = "Acorizal")    
        	
        CityCode.objects.create(city_code ="5100201", 
                                city_name = "Água Boa")    
        	
        CityCode.objects.create(city_code ="5100250", 
                                city_name = "Alta Floresta")    
        	
        CityCode.objects.create(city_code ="5100300", 
                                city_name = "Alto Araguaia")    
        	
        CityCode.objects.create(city_code ="5100359", 
                                city_name = "Alto Boa Vista")    
        	
        CityCode.objects.create(city_code ="5100409", 
                                city_name = "Alto Garças")    
        	
        CityCode.objects.create(city_code ="5100508", 
                                city_name = "Alto Paraguai")    
        	
        CityCode.objects.create(city_code ="5100607", 
                                city_name = "Alto Taquari")    
        	
        CityCode.objects.create(city_code ="5100805", 
                                city_name = "Apiacás")    
        	
        CityCode.objects.create(city_code ="5101001", 
                                city_name = "Araguaiana")    
        	
        CityCode.objects.create(city_code ="5101209", 
                                city_name = "Araguainha")    
        	
        CityCode.objects.create(city_code ="5101258", 
                                city_name = "Araputanga")    
        	
        CityCode.objects.create(city_code ="5101308", 
                                city_name = "Arenápolis")    
        	
        CityCode.objects.create(city_code ="5101407", 
                                city_name = "Aripuanã")    
        	
        CityCode.objects.create(city_code ="5101605", 
                                city_name = "Barão de Melgaço")    
        	
        CityCode.objects.create(city_code ="5101704", 
                                city_name = "Barra do Bugres")    
        	
        CityCode.objects.create(city_code ="5101803", 
                                city_name = "Barra do Garças")    
        	
        CityCode.objects.create(city_code ="5101852", 
                                city_name = "Bom Jesus do Araguaia")    
        	
        CityCode.objects.create(city_code ="5101902", 
                                city_name = "Brasnorte")    
        	
        CityCode.objects.create(city_code ="5102504", 
                                city_name = "Cáceres")    
        	
        CityCode.objects.create(city_code ="5102603", 
                                city_name = "Campinápolis")    
        	
        CityCode.objects.create(city_code ="5102637", 
                                city_name = "Campo Novo do Parecis")    
        	
        CityCode.objects.create(city_code ="5102678", 
                                city_name = "Campo Verde")    
        	
        CityCode.objects.create(city_code ="5102686", 
                                city_name = "Campos de Júlio")    
        	
        CityCode.objects.create(city_code ="5102694", 
                                city_name = "Canabrava do Norte")    
        	
        CityCode.objects.create(city_code ="5102702", 
                                city_name = "Canarana")    
        	
        CityCode.objects.create(city_code ="5102793", 
                                city_name = "Carlinda")    
        	
        CityCode.objects.create(city_code ="5102850", 
                                city_name = "Castanheira")    
        	
        CityCode.objects.create(city_code ="5103007", 
                                city_name = "Chapada dos Guimarães")    
        	
        CityCode.objects.create(city_code ="5103056", 
                                city_name = "Cláudia")    
        	
        CityCode.objects.create(city_code ="5103106", 
                                city_name = "Cocalinho")    
        	
        CityCode.objects.create(city_code ="5103205", 
                                city_name = "Colíder")    
        	
        CityCode.objects.create(city_code ="5103254", 
                                city_name = "Colniza")    
        	
        CityCode.objects.create(city_code ="5103304", 
                                city_name = "Comodoro")    
        	
        CityCode.objects.create(city_code ="5103353", 
                                city_name = "Confresa")    
        	
        CityCode.objects.create(city_code ="5103361", 
                                city_name = "Conquista D'Oeste")    
        	
        CityCode.objects.create(city_code ="5103379", 
                                city_name = "Cotriguaçu")    
        	
        CityCode.objects.create(city_code ="5103403", 
                                city_name = "Cuiabá")    
        	
        CityCode.objects.create(city_code ="5103437", 
                                city_name = "Curvelândia")    
        	
        CityCode.objects.create(city_code ="5103452", 
                                city_name = "Denise")    
        	
        CityCode.objects.create(city_code ="5103502", 
                                city_name = "Diamantino")    
        	
        CityCode.objects.create(city_code ="5103601", 
                                city_name = "Dom Aquino")    
        	
        CityCode.objects.create(city_code ="5103700", 
                                city_name = "Feliz Natal")    
        	
        CityCode.objects.create(city_code ="5103809", 
                                city_name = "Figueirópolis D'Oeste")    
        	
        CityCode.objects.create(city_code ="5103858", 
                                city_name = "Gaúcha do Norte")    
        	
        CityCode.objects.create(city_code ="5103908", 
                                city_name = "General Carneiro")    
        	
        CityCode.objects.create(city_code ="5103957", 
                                city_name = "Glória D'Oeste")    
        	
        CityCode.objects.create(city_code ="5104104", 
                                city_name = "Guarantã do Norte")    
        	
        CityCode.objects.create(city_code ="5104203", 
                                city_name = "Guiratinga")    
        	
        CityCode.objects.create(city_code ="5104500", 
                                city_name = "Indiavaí")    
        	
        CityCode.objects.create(city_code ="5104526", 
                                city_name = "Ipiranga do Norte")    
        	
        CityCode.objects.create(city_code ="5104542", 
                                city_name = "Itanhangá")    
        	
        CityCode.objects.create(city_code ="5104559", 
                                city_name = "Itaúba")    
        	
        CityCode.objects.create(city_code ="5104609", 
                                city_name = "Itiquira")    
        	
        CityCode.objects.create(city_code ="5104807", 
                                city_name = "Jaciara")    
        	
        CityCode.objects.create(city_code ="5104906", 
                                city_name = "Jangada")    
        	
        CityCode.objects.create(city_code ="5105002", 
                                city_name = "Jauru")    
        	
        CityCode.objects.create(city_code ="5105101", 
                                city_name = "Juara")    
        	
        CityCode.objects.create(city_code ="5105150", 
                                city_name = "Juína")    
        	
        CityCode.objects.create(city_code ="5105176", 
                                city_name = "Juruena")    
        	
        CityCode.objects.create(city_code ="5105200", 
                                city_name = "Juscimeira")    
        	
        CityCode.objects.create(city_code ="5105234", 
                                city_name = "Lambari D'Oeste")    
        	
        CityCode.objects.create(city_code ="5105259", 
                                city_name = "Lucas do Rio Verde")    
        	
        CityCode.objects.create(city_code ="5105309", 
                                city_name = "Luciara")    
        	
        CityCode.objects.create(city_code ="5105580", 
                                city_name = "Marcelândia")    
        	
        CityCode.objects.create(city_code ="5105606", 
                                city_name = "Matupá")    
        	
        CityCode.objects.create(city_code ="5105622", 
                                city_name = "Mirassol d'Oeste")    
        	
        CityCode.objects.create(city_code ="5105903", 
                                city_name = "Nobres")    
        	
        CityCode.objects.create(city_code ="5106000", 
                                city_name = "Nortelândia")    
        	
        CityCode.objects.create(city_code ="5106109", 
                                city_name = "Nossa Senhora do Livramento")    
        	
        CityCode.objects.create(city_code ="5106158", 
                                city_name = "Nova Bandeirantes")    
        	
        CityCode.objects.create(city_code ="5106208", 
                                city_name = "Nova Brasilândia")    
        	
        CityCode.objects.create(city_code ="5106216", 
                                city_name = "Nova Canaã do Norte")    
        	
        CityCode.objects.create(city_code ="5108808", 
                                city_name = "Nova Guarita")    
        	
        CityCode.objects.create(city_code ="5106182", 
                                city_name = "Nova Lacerda")    
        	
        CityCode.objects.create(city_code ="5108857", 
                                city_name = "Nova Marilândia")    
        	
        CityCode.objects.create(city_code ="5108907", 
                                city_name = "Nova Maringá")    
        	
        CityCode.objects.create(city_code ="5108956", 
                                city_name = "Nova Monte Verde")    
        	
        CityCode.objects.create(city_code ="5106224", 
                                city_name = "Nova Mutum")    
        	
        CityCode.objects.create(city_code ="5106174", 
                                city_name = "Nova Nazaré")    
        	
        CityCode.objects.create(city_code ="5106232", 
                                city_name = "Nova Olímpia")    
        	
        CityCode.objects.create(city_code ="5106190", 
                                city_name = "Nova Santa Helena")    
        	
        CityCode.objects.create(city_code ="5106240", 
                                city_name = "Nova Ubiratã")    
        	
        CityCode.objects.create(city_code ="5106257", 
                                city_name = "Nova Xavantina")    
        	
        CityCode.objects.create(city_code ="5106273", 
                                city_name = "Novo Horizonte do Norte")    
        	
        CityCode.objects.create(city_code ="5106265", 
                                city_name = "Novo Mundo")    
        	
        CityCode.objects.create(city_code ="5106315", 
                                city_name = "Novo Santo Antônio")    
        	
        CityCode.objects.create(city_code ="5106281", 
                                city_name = "Novo São Joaquim")    
        	
        CityCode.objects.create(city_code ="5106299", 
                                city_name = "Paranaíta")    
        	
        CityCode.objects.create(city_code ="5106307", 
                                city_name = "Paranatinga")    
        	
        CityCode.objects.create(city_code ="5106372", 
                                city_name = "Pedra Preta")    
        	
        CityCode.objects.create(city_code ="5106422", 
                                city_name = "Peixoto de Azevedo")    
        	
        CityCode.objects.create(city_code ="5106455", 
                                city_name = "Planalto da Serra")    
        	
        CityCode.objects.create(city_code ="5106505", 
                                city_name = "Poconé")    
        	
        CityCode.objects.create(city_code ="5106653", 
                                city_name = "Pontal do Araguaia")    
        	
        CityCode.objects.create(city_code ="5106703", 
                                city_name = "Ponte Branca")    
        	
        CityCode.objects.create(city_code ="5106752", 
                                city_name = "Pontes e Lacerda")    
        	
        CityCode.objects.create(city_code ="5106778", 
                                city_name = "Porto Alegre do Norte")    
        	
        CityCode.objects.create(city_code ="5106802", 
                                city_name = "Porto dos Gaúchos")    
        	
        CityCode.objects.create(city_code ="5106828", 
                                city_name = "Porto Esperidião")    
        	
        CityCode.objects.create(city_code ="5106851", 
                                city_name = "Porto Estrela")    
        	
        CityCode.objects.create(city_code ="5107008", 
                                city_name = "Poxoréu")    
        	
        CityCode.objects.create(city_code ="5107040", 
                                city_name = "Primavera do Leste")    
        	
        CityCode.objects.create(city_code ="5107065", 
                                city_name = "Querência")    
        	
        CityCode.objects.create(city_code ="5107156", 
                                city_name = "Reserva do Cabaçal")    
        	
        CityCode.objects.create(city_code ="5107180", 
                                city_name = "Ribeirão Cascalheira")    
        	
        CityCode.objects.create(city_code ="5107198", 
                                city_name = "Ribeirãozinho")    
        	
        CityCode.objects.create(city_code ="5107206", 
                                city_name = "Rio Branco")    
        	
        CityCode.objects.create(city_code ="5107578", 
                                city_name = "Rondolândia")    
        	
        CityCode.objects.create(city_code ="5107602", 
                                city_name = "Rondonópolis")    
        	
        CityCode.objects.create(city_code ="5107701", 
                                city_name = "Rosário Oeste")    
        	
        CityCode.objects.create(city_code ="5107750", 
                                city_name = "Salto do Céu")    
        	
        CityCode.objects.create(city_code ="5107248", 
                                city_name = "Santa Carmem")    
        	
        CityCode.objects.create(city_code ="5107743", 
                                city_name = "Santa Cruz do Xingu")    
        	
        CityCode.objects.create(city_code ="5107768", 
                                city_name = "Santa Rita do Trivelato")    
        	
        CityCode.objects.create(city_code ="5107776", 
                                city_name = "Santa Terezinha")    
        	
        CityCode.objects.create(city_code ="5107263", 
                                city_name = "Santo Afonso")    
        	
        CityCode.objects.create(city_code ="5107792", 
                                city_name = "Santo Antônio do Leste")    
        	
        CityCode.objects.create(city_code ="5107800", 
                                city_name = "Santo Antônio do Leverger")    
        	
        CityCode.objects.create(city_code ="5107859", 
                                city_name = "São Félix do Araguaia")    
        	
        CityCode.objects.create(city_code ="5107297", 
                                city_name = "São José do Povo")    
        	
        CityCode.objects.create(city_code ="5107305", 
                                city_name = "São José do Rio Claro")    
        	
        CityCode.objects.create(city_code ="5107354", 
                                city_name = "São José do Xingu")    
        	
        CityCode.objects.create(city_code ="5107107", 
                                city_name = "São José dos Quatro Marcos")    
        	
        CityCode.objects.create(city_code ="5107404", 
                                city_name = "São Pedro da Cipa")    
        	
        CityCode.objects.create(city_code ="5107875", 
                                city_name = "Sapezal")    
        	
        CityCode.objects.create(city_code ="5107883", 
                                city_name = "Serra Nova Dourada")    
        	
        CityCode.objects.create(city_code ="5107909", 
                                city_name = "Sinop")    
        	
        CityCode.objects.create(city_code ="5107925", 
                                city_name = "Sorriso")    
        	
        CityCode.objects.create(city_code ="5107941", 
                                city_name = "Tabaporã")    
        	
        CityCode.objects.create(city_code ="5107958", 
                                city_name = "Tangará da Serra")    
        	
        CityCode.objects.create(city_code ="5108006", 
                                city_name = "Tapurah")    
        	
        CityCode.objects.create(city_code ="5108055", 
                                city_name = "Terra Nova do Norte")    
        	
        CityCode.objects.create(city_code ="5108105", 
                                city_name = "Tesouro")    
        	
        CityCode.objects.create(city_code ="5108204", 
                                city_name = "Torixoréu")    
        	
        CityCode.objects.create(city_code ="5108303", 
                                city_name = "União do Sul")    
        	
        CityCode.objects.create(city_code ="5108352", 
                                city_name = "Vale de São Domingos")    
        	
        CityCode.objects.create(city_code ="5108402", 
                                city_name = "Várzea Grande")    
        	
        CityCode.objects.create(city_code ="5108501", 
                                city_name = "Vera")    
        	
        CityCode.objects.create(city_code ="5105507", 
                                city_name = "Vila Bela da Santíssima Trindade")    
        	
        CityCode.objects.create(city_code ="5108600", 
                                city_name = "Vila Rica")    
        	
        CityCode.objects.create(city_code ="5200050", 
                                city_name = "Abadia de Goiás")    
        	
        CityCode.objects.create(city_code ="5200100", 
                                city_name = "Abadiânia")    
        	
        CityCode.objects.create(city_code ="5200134", 
                                city_name = "Acreúna")    
        	
        CityCode.objects.create(city_code ="5200159", 
                                city_name = "Adelândia")    
        	
        CityCode.objects.create(city_code ="5200175", 
                                city_name = "Água Fria de Goiás")    
        	
        CityCode.objects.create(city_code ="5200209", 
                                city_name = "Água Limpa")    
        	
        CityCode.objects.create(city_code ="5200258", 
                                city_name = "Águas Lindas de Goiás")    
        	
        CityCode.objects.create(city_code ="5200308", 
                                city_name = "Alexânia")    
        	
        CityCode.objects.create(city_code ="5200506", 
                                city_name = "Aloândia")    
        	
        CityCode.objects.create(city_code ="5200555", 
                                city_name = "Alto Horizonte")    
        	
        CityCode.objects.create(city_code ="5200605", 
                                city_name = "Alto Paraíso de Goiás")    
        	
        CityCode.objects.create(city_code ="5200803", 
                                city_name = "Alvorada do Norte")    
        	
        CityCode.objects.create(city_code ="5200829", 
                                city_name = "Amaralina")    
        	
        CityCode.objects.create(city_code ="5200852", 
                                city_name = "Americano do Brasil")    
        	
        CityCode.objects.create(city_code ="5200902", 
                                city_name = "Amorinópolis")    
        	
        CityCode.objects.create(city_code ="5201108", 
                                city_name = "Anápolis")    
        	
        CityCode.objects.create(city_code ="5201207", 
                                city_name = "Anhanguera")    
        	
        CityCode.objects.create(city_code ="5201306", 
                                city_name = "Anicuns")    
        	
        CityCode.objects.create(city_code ="5201405", 
                                city_name = "Aparecida de Goiânia")    
        	
        CityCode.objects.create(city_code ="5201454", 
                                city_name = "Aparecida do Rio Doce")    
        	
        CityCode.objects.create(city_code ="5201504", 
                                city_name = "Aporé")    
        	
        CityCode.objects.create(city_code ="5201603", 
                                city_name = "Araçu")    
        	
        CityCode.objects.create(city_code ="5201702", 
                                city_name = "Aragarças")    
        	
        CityCode.objects.create(city_code ="5201801", 
                                city_name = "Aragoiânia")    
        	
        CityCode.objects.create(city_code ="5202155", 
                                city_name = "Araguapaz")    
        	
        CityCode.objects.create(city_code ="5202353", 
                                city_name = "Arenópolis")    
        	
        CityCode.objects.create(city_code ="5202502", 
                                city_name = "Aruanã")    
        	
        CityCode.objects.create(city_code ="5202601", 
                                city_name = "Aurilândia")    
        	
        CityCode.objects.create(city_code ="5202809", 
                                city_name = "Avelinópolis")    
        	
        CityCode.objects.create(city_code ="5203104", 
                                city_name = "Baliza")    
        	
        CityCode.objects.create(city_code ="5203203", 
                                city_name = "Barro Alto")    
        	
        CityCode.objects.create(city_code ="5203302", 
                                city_name = "Bela Vista de Goiás")    
        	
        CityCode.objects.create(city_code ="5203401", 
                                city_name = "Bom Jardim de Goiás")    
        	
        CityCode.objects.create(city_code ="5203500", 
                                city_name = "Bom Jesus de Goiás")    
        	
        CityCode.objects.create(city_code ="5203559", 
                                city_name = "Bonfinópolis")    
        	
        CityCode.objects.create(city_code ="5203575", 
                                city_name = "Bonópolis")    
        	
        CityCode.objects.create(city_code ="5203609", 
                                city_name = "Brazabrantes")    
        	
        CityCode.objects.create(city_code ="5203807", 
                                city_name = "Britânia")    
        	
        CityCode.objects.create(city_code ="5203906", 
                                city_name = "Buriti Alegre")    
        	
        CityCode.objects.create(city_code ="5203939", 
                                city_name = "Buriti de Goiás")    
        	
        CityCode.objects.create(city_code ="5203962", 
                                city_name = "Buritinópolis")    
        	
        CityCode.objects.create(city_code ="5204003", 
                                city_name = "Cabeceiras")    
        	
        CityCode.objects.create(city_code ="5204102", 
                                city_name = "Cachoeira Alta")    
        	
        CityCode.objects.create(city_code ="5204201", 
                                city_name = "Cachoeira de Goiás")    
        	
        CityCode.objects.create(city_code ="5204250", 
                                city_name = "Cachoeira Dourada")    
        	
        CityCode.objects.create(city_code ="5204300", 
                                city_name = "Caçu")    
        	
        CityCode.objects.create(city_code ="5204409", 
                                city_name = "Caiapônia")    
        	
        CityCode.objects.create(city_code ="5204508", 
                                city_name = "Caldas Novas")    
        	
        CityCode.objects.create(city_code ="5204557", 
                                city_name = "Caldazinha")    
        	
        CityCode.objects.create(city_code ="5204607", 
                                city_name = "Campestre de Goiás")    
        	
        CityCode.objects.create(city_code ="5204656", 
                                city_name = "Campinaçu")    
        	
        CityCode.objects.create(city_code ="5204706", 
                                city_name = "Campinorte")    
        	
        CityCode.objects.create(city_code ="5204805", 
                                city_name = "Campo Alegre de Goiás")    
        	
        CityCode.objects.create(city_code ="5204854", 
                                city_name = "Campo Limpo de Goiás")    
        	
        CityCode.objects.create(city_code ="5204904", 
                                city_name = "Campos Belos")    
        	
        CityCode.objects.create(city_code ="5204953", 
                                city_name = "Campos Verdes")    
        	
        CityCode.objects.create(city_code ="5205000", 
                                city_name = "Carmo do Rio Verde")    
        	
        CityCode.objects.create(city_code ="5205059", 
                                city_name = "Castelândia")    
        	
        CityCode.objects.create(city_code ="5205109", 
                                city_name = "Catalão")    
        	
        CityCode.objects.create(city_code ="5205208", 
                                city_name = "Caturaí")    
        	
        CityCode.objects.create(city_code ="5205307", 
                                city_name = "Cavalcante")    
        	
        CityCode.objects.create(city_code ="5205406", 
                                city_name = "Ceres")    
        	
        CityCode.objects.create(city_code ="5205455", 
                                city_name = "Cezarina")    
        	
        CityCode.objects.create(city_code ="5205471", 
                                city_name = "Chapadão do Céu")    
        	
        CityCode.objects.create(city_code ="5205497", 
                                city_name = "Cidade Ocidental")    
        	
        CityCode.objects.create(city_code ="5205513", 
                                city_name = "Cocalzinho de Goiás")    
        	
        CityCode.objects.create(city_code ="5205521", 
                                city_name = "Colinas do Sul")    
        	
        CityCode.objects.create(city_code ="5205703", 
                                city_name = "Córrego do Ouro")    
        	
        CityCode.objects.create(city_code ="5205802", 
                                city_name = "Corumbá de Goiás")    
        	
        CityCode.objects.create(city_code ="5205901", 
                                city_name = "Corumbaíba")    
        	
        CityCode.objects.create(city_code ="5206206", 
                                city_name = "Cristalina")    
        	
        CityCode.objects.create(city_code ="5206305", 
                                city_name = "Cristianópolis")    
        	
        CityCode.objects.create(city_code ="5206404", 
                                city_name = "Crixás")    
        	
        CityCode.objects.create(city_code ="5206503", 
                                city_name = "Cromínia")    
        	
        CityCode.objects.create(city_code ="5206602", 
                                city_name = "Cumari")    
        	
        CityCode.objects.create(city_code ="5206701", 
                                city_name = "Damianópolis")    
        	
        CityCode.objects.create(city_code ="5206800", 
                                city_name = "Damolândia")    
        	
        CityCode.objects.create(city_code ="5206909", 
                                city_name = "Davinópolis")    
        	
        CityCode.objects.create(city_code ="5207105", 
                                city_name = "Diorama")    
        	
        CityCode.objects.create(city_code ="5208301", 
                                city_name = "Divinópolis de Goiás")    
        	
        CityCode.objects.create(city_code ="5207253", 
                                city_name = "Doverlândia")    
        	
        CityCode.objects.create(city_code ="5207352", 
                                city_name = "Edealina")    
        	
        CityCode.objects.create(city_code ="5207402", 
                                city_name = "Edéia")    
        	
        CityCode.objects.create(city_code ="5207501", 
                                city_name = "Estrela do Norte")    
        	
        CityCode.objects.create(city_code ="5207535", 
                                city_name = "Faina")    
        	
        CityCode.objects.create(city_code ="5207600", 
                                city_name = "Fazenda Nova")    
        	
        CityCode.objects.create(city_code ="5207808", 
                                city_name = "Firminópolis")    
        	
        CityCode.objects.create(city_code ="5207907", 
                                city_name = "Flores de Goiás")    
        	
        CityCode.objects.create(city_code ="5208004", 
                                city_name = "Formosa")    
        	
        CityCode.objects.create(city_code ="5208103", 
                                city_name = "Formoso")    
        	
        CityCode.objects.create(city_code ="5208152", 
                                city_name = "Gameleira de Goiás")    
        	
        CityCode.objects.create(city_code ="5208400", 
                                city_name = "Goianápolis")    
        	
        CityCode.objects.create(city_code ="5208509", 
                                city_name = "Goiandira")    
        	
        CityCode.objects.create(city_code ="5208608", 
                                city_name = "Goianésia")    
        	
        CityCode.objects.create(city_code ="5208707", 
                                city_name = "Goiânia")    
        	
        CityCode.objects.create(city_code ="5208806", 
                                city_name = "Goianira")    
        	
        CityCode.objects.create(city_code ="5208905", 
                                city_name = "Goiás")    
        	
        CityCode.objects.create(city_code ="5209101", 
                                city_name = "Goiatuba")    
        	
        CityCode.objects.create(city_code ="5209150", 
                                city_name = "Gouvelândia")    
        	
        CityCode.objects.create(city_code ="5209200", 
                                city_name = "Guapó")    
        	
        CityCode.objects.create(city_code ="5209291", 
                                city_name = "Guaraíta")    
        	
        CityCode.objects.create(city_code ="5209408", 
                                city_name = "Guarani de Goiás")    
        	
        CityCode.objects.create(city_code ="5209457", 
                                city_name = "Guarinos")    
        	
        CityCode.objects.create(city_code ="5209606", 
                                city_name = "Heitoraí")    
        	
        CityCode.objects.create(city_code ="5209705", 
                                city_name = "Hidrolândia")    
        	
        CityCode.objects.create(city_code ="5209804", 
                                city_name = "Hidrolina")    
        	
        CityCode.objects.create(city_code ="5209903", 
                                city_name = "Iaciara")    
        	
        CityCode.objects.create(city_code ="5209937", 
                                city_name = "Inaciolândia")    
        	
        CityCode.objects.create(city_code ="5209952", 
                                city_name = "Indiara")    
        	
        CityCode.objects.create(city_code ="5210000", 
                                city_name = "Inhumas")    
        	
        CityCode.objects.create(city_code ="5210109", 
                                city_name = "Ipameri")    
        	
        CityCode.objects.create(city_code ="5210158", 
                                city_name = "Ipiranga de Goiás")    
        	
        CityCode.objects.create(city_code ="5210208", 
                                city_name = "Iporá")    
        	
        CityCode.objects.create(city_code ="5210307", 
                                city_name = "Israelândia")    
        	
        CityCode.objects.create(city_code ="5210406", 
                                city_name = "Itaberaí")    
        	
        CityCode.objects.create(city_code ="5210562", 
                                city_name = "Itaguari")    
        	
        CityCode.objects.create(city_code ="5210604", 
                                city_name = "Itaguaru")    
        	
        CityCode.objects.create(city_code ="5210802", 
                                city_name = "Itajá")    
        	
        CityCode.objects.create(city_code ="5210901", 
                                city_name = "Itapaci")    
        	
        CityCode.objects.create(city_code ="5211008", 
                                city_name = "Itapirapuã")    
        	
        CityCode.objects.create(city_code ="5211206", 
                                city_name = "Itapuranga")    
        	
        CityCode.objects.create(city_code ="5211305", 
                                city_name = "Itarumã")    
        	
        CityCode.objects.create(city_code ="5211404", 
                                city_name = "Itauçu")    
        	
        CityCode.objects.create(city_code ="5211503", 
                                city_name = "Itumbiara")    
        	
        CityCode.objects.create(city_code ="5211602", 
                                city_name = "Ivolândia")    
        	
        CityCode.objects.create(city_code ="5211701", 
                                city_name = "Jandaia")    
        	
        CityCode.objects.create(city_code ="5211800", 
                                city_name = "Jaraguá")    
        	
        CityCode.objects.create(city_code ="5211909", 
                                city_name = "Jataí")    
        	
        CityCode.objects.create(city_code ="5212006", 
                                city_name = "Jaupaci")    
        	
        CityCode.objects.create(city_code ="5212055", 
                                city_name = "Jesúpolis")    
        	
        CityCode.objects.create(city_code ="5212105", 
                                city_name = "Joviânia")    
        	
        CityCode.objects.create(city_code ="5212204", 
                                city_name = "Jussara")    
        	
        CityCode.objects.create(city_code ="5212253", 
                                city_name = "Lagoa Santa")    
        	
        CityCode.objects.create(city_code ="5212303", 
                                city_name = "Leopoldo de Bulhões")    
        	
        CityCode.objects.create(city_code ="5212501", 
                                city_name = "Luziânia")    
        	
        CityCode.objects.create(city_code ="5212600", 
                                city_name = "Mairipotaba")    
        	
        CityCode.objects.create(city_code ="5212709", 
                                city_name = "Mambaí")    
        	
        CityCode.objects.create(city_code ="5212808", 
                                city_name = "Mara Rosa")    
        	
        CityCode.objects.create(city_code ="5212907", 
                                city_name = "Marzagão")    
        	
        CityCode.objects.create(city_code ="5212956", 
                                city_name = "Matrinchã")    
        	
        CityCode.objects.create(city_code ="5213004", 
                                city_name = "Maurilândia")    
        	
        CityCode.objects.create(city_code ="5213053", 
                                city_name = "Mimoso de Goiás")    
        	
        CityCode.objects.create(city_code ="5213087", 
                                city_name = "Minaçu")    
        	
        CityCode.objects.create(city_code ="5213103", 
                                city_name = "Mineiros")    
        	
        CityCode.objects.create(city_code ="5213400", 
                                city_name = "Moiporá")    
        	
        CityCode.objects.create(city_code ="5213509", 
                                city_name = "Monte Alegre de Goiás")    
        	
        CityCode.objects.create(city_code ="5213707", 
                                city_name = "Montes Claros de Goiás")    
        	
        CityCode.objects.create(city_code ="5213756", 
                                city_name = "Montividiu")    
        	
        CityCode.objects.create(city_code ="5213772", 
                                city_name = "Montividiu do Norte")    
        	
        CityCode.objects.create(city_code ="5213806", 
                                city_name = "Morrinhos")    
        	
        CityCode.objects.create(city_code ="5213855", 
                                city_name = "Morro Agudo de Goiás")    
        	
        CityCode.objects.create(city_code ="5213905", 
                                city_name = "Mossâmedes")    
        	
        CityCode.objects.create(city_code ="5214002", 
                                city_name = "Mozarlândia")    
        	
        CityCode.objects.create(city_code ="5214051", 
                                city_name = "Mundo Novo")    
        	
        CityCode.objects.create(city_code ="5214101", 
                                city_name = "Mutunópolis")    
        	
        CityCode.objects.create(city_code ="5214408", 
                                city_name = "Nazário")    
        	
        CityCode.objects.create(city_code ="5214507", 
                                city_name = "Nerópolis")    
        	
        CityCode.objects.create(city_code ="5214606", 
                                city_name = "Niquelândia")    
        	
        CityCode.objects.create(city_code ="5214705", 
                                city_name = "Nova América")    
        	
        CityCode.objects.create(city_code ="5214804", 
                                city_name = "Nova Aurora")    
        	
        CityCode.objects.create(city_code ="5214838", 
                                city_name = "Nova Crixás")    
        	
        CityCode.objects.create(city_code ="5214861", 
                                city_name = "Nova Glória")    
        	
        CityCode.objects.create(city_code ="5214879", 
                                city_name = "Nova Iguaçu de Goiás")    
        	
        CityCode.objects.create(city_code ="5214903", 
                                city_name = "Nova Roma")    
        	
        CityCode.objects.create(city_code ="5215009", 
                                city_name = "Nova Veneza")    
        	
        CityCode.objects.create(city_code ="5215207", 
                                city_name = "Novo Brasil")    
        	
        CityCode.objects.create(city_code ="5215231", 
                                city_name = "Novo Gama")    
        	
        CityCode.objects.create(city_code ="5215256", 
                                city_name = "Novo Planalto")    
        	
        CityCode.objects.create(city_code ="5215306", 
                                city_name = "Orizona")    
        	
        CityCode.objects.create(city_code ="5215405", 
                                city_name = "Ouro Verde de Goiás")    
        	
        CityCode.objects.create(city_code ="5215504", 
                                city_name = "Ouvidor")    
        	
        CityCode.objects.create(city_code ="5215603", 
                                city_name = "Padre Bernardo")    
        	
        CityCode.objects.create(city_code ="5215652", 
                                city_name = "Palestina de Goiás")    
        	
        CityCode.objects.create(city_code ="5215702", 
                                city_name = "Palmeiras de Goiás")    
        	
        CityCode.objects.create(city_code ="5215801", 
                                city_name = "Palmelo")    
        	
        CityCode.objects.create(city_code ="5215900", 
                                city_name = "Palminópolis")    
        	
        CityCode.objects.create(city_code ="5216007", 
                                city_name = "Panamá")    
        	
        CityCode.objects.create(city_code ="5216304", 
                                city_name = "Paranaiguara")    
        	
        CityCode.objects.create(city_code ="5216403", 
                                city_name = "Paraúna")    
        	
        CityCode.objects.create(city_code ="5216452", 
                                city_name = "Perolândia")    
        	
        CityCode.objects.create(city_code ="5216809", 
                                city_name = "Petrolina de Goiás")    
        	
        CityCode.objects.create(city_code ="5216908", 
                                city_name = "Pilar de Goiás")    
        	
        CityCode.objects.create(city_code ="5217104", 
                                city_name = "Piracanjuba")    
        	
        CityCode.objects.create(city_code ="5217203", 
                                city_name = "Piranhas")    
        	
        CityCode.objects.create(city_code ="5217302", 
                                city_name = "Pirenópolis")    
        	
        CityCode.objects.create(city_code ="5217401", 
                                city_name = "Pires do Rio")    
        	
        CityCode.objects.create(city_code ="5217609", 
                                city_name = "Planaltina")    
        	
        CityCode.objects.create(city_code ="5217708", 
                                city_name = "Pontalina")    
        	
        CityCode.objects.create(city_code ="5218003", 
                                city_name = "Porangatu")    
        	
        CityCode.objects.create(city_code ="5218052", 
                                city_name = "Porteirão")    
        	
        CityCode.objects.create(city_code ="5218102", 
                                city_name = "Portelândia")    
        	
        CityCode.objects.create(city_code ="5218300", 
                                city_name = "Posse")    
        	
        CityCode.objects.create(city_code ="5218391", 
                                city_name = "Professor Jamil")    
        	
        CityCode.objects.create(city_code ="5218508", 
                                city_name = "Quirinópolis")    
        	
        CityCode.objects.create(city_code ="5218607", 
                                city_name = "Rialma")    
        	
        CityCode.objects.create(city_code ="5218706", 
                                city_name = "Rianápolis")    
        	
        CityCode.objects.create(city_code ="5218789", 
                                city_name = "Rio Quente")    
        	
        CityCode.objects.create(city_code ="5218805", 
                                city_name = "Rio Verde")    
        	
        CityCode.objects.create(city_code ="5218904", 
                                city_name = "Rubiataba")    
        	
        CityCode.objects.create(city_code ="5219001", 
                                city_name = "Sanclerlândia")    
        	
        CityCode.objects.create(city_code ="5219100", 
                                city_name = "Santa Bárbara de Goiás")    
        	
        CityCode.objects.create(city_code ="5219209", 
                                city_name = "Santa Cruz de Goiás")    
        	
        CityCode.objects.create(city_code ="5219258", 
                                city_name = "Santa Fé de Goiás")    
        	
        CityCode.objects.create(city_code ="5219308", 
                                city_name = "Santa Helena de Goiás")    
        	
        CityCode.objects.create(city_code ="5219357", 
                                city_name = "Santa Isabel")    
        	
        CityCode.objects.create(city_code ="5219407", 
                                city_name = "Santa Rita do Araguaia")    
        	
        CityCode.objects.create(city_code ="5219456", 
                                city_name = "Santa Rita do Novo Destino")    
        	
        CityCode.objects.create(city_code ="5219506", 
                                city_name = "Santa Rosa de Goiás")    
        	
        CityCode.objects.create(city_code ="5219605", 
                                city_name = "Santa Tereza de Goiás")    
        	
        CityCode.objects.create(city_code ="5219704", 
                                city_name = "Santa Terezinha de Goiás")    
        	
        CityCode.objects.create(city_code ="5219712", 
                                city_name = "Santo Antônio da Barra")    
        	
        CityCode.objects.create(city_code ="5219738", 
                                city_name = "Santo Antônio de Goiás")    
        	
        CityCode.objects.create(city_code ="5219753", 
                                city_name = "Santo Antônio do Descoberto")    
        	
        CityCode.objects.create(city_code ="5219803", 
                                city_name = "São Domingos")    
        	
        CityCode.objects.create(city_code ="5219902", 
                                city_name = "São Francisco de Goiás")    
        	
        CityCode.objects.create(city_code ="5220058", 
                                city_name = "São João da Paraúna")    
        	
        CityCode.objects.create(city_code ="5220009", 
                                city_name = "São João d'Aliança")    
        	
        CityCode.objects.create(city_code ="5220108", 
                                city_name = "São Luís de Montes Belos")    
        	
        CityCode.objects.create(city_code ="5220157", 
                                city_name = "São Luiz do Norte")    
        	
        CityCode.objects.create(city_code ="5220207", 
                                city_name = "São Miguel do Araguaia")    
        	
        CityCode.objects.create(city_code ="5220264", 
                                city_name = "São Miguel do Passa Quatro")    
        	
        CityCode.objects.create(city_code ="5220280", 
                                city_name = "São Patrício")    
        	
        CityCode.objects.create(city_code ="5220405", 
                                city_name = "São Simão")    
        	
        CityCode.objects.create(city_code ="5220454", 
                                city_name = "Senador Canedo")    
        	
        CityCode.objects.create(city_code ="5220504", 
                                city_name = "Serranópolis")    
        	
        CityCode.objects.create(city_code ="5220603", 
                                city_name = "Silvânia")    
        	
        CityCode.objects.create(city_code ="5220686", 
                                city_name = "Simolândia")    
        	
        CityCode.objects.create(city_code ="5220702", 
                                city_name = "Sítio d'Abadia")    
        	
        CityCode.objects.create(city_code ="5221007", 
                                city_name = "Taquaral de Goiás")    
        	
        CityCode.objects.create(city_code ="5221080", 
                                city_name = "Teresina de Goiás")    
        	
        CityCode.objects.create(city_code ="5221197", 
                                city_name = "Terezópolis de Goiás")    
        	
        CityCode.objects.create(city_code ="5221304", 
                                city_name = "Três Ranchos")    
        	
        CityCode.objects.create(city_code ="5221403", 
                                city_name = "Trindade")    
        	
        CityCode.objects.create(city_code ="5221452", 
                                city_name = "Trombas")    
        	
        CityCode.objects.create(city_code ="5221502", 
                                city_name = "Turvânia")    
        	
        CityCode.objects.create(city_code ="5221551", 
                                city_name = "Turvelândia")    
        	
        CityCode.objects.create(city_code ="5221577", 
                                city_name = "Uirapuru")    
        	
        CityCode.objects.create(city_code ="5221601", 
                                city_name = "Uruaçu")    
        	
        CityCode.objects.create(city_code ="5221700", 
                                city_name = "Uruana")    
        	
        CityCode.objects.create(city_code ="5221809", 
                                city_name = "Urutaí")    
        	
        CityCode.objects.create(city_code ="5221858", 
                                city_name = "Valparaíso de Goiás")    
        	
        CityCode.objects.create(city_code ="5221908", 
                                city_name = "Varjão")    
        	
        CityCode.objects.create(city_code ="5222005", 
                                city_name = "Vianópolis")    
        	
        CityCode.objects.create(city_code ="5222054", 
                                city_name = "Vicentinópolis")    
        	
        CityCode.objects.create(city_code ="5222203", 
                                city_name = "Vila Boa")    
        	
        CityCode.objects.create(city_code ="5222302", 
                                city_name = "Vila Propício")  

        CityCode.objects.create(city_code = "5300108",
                                city_name ="Brasília")