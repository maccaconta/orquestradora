import json
import re
postos = None
with open("postos.json", "r", encoding="utf8") as arqPostos:
    postos = json.load(arqPostos)
    arqPostos.close()

# print(postos)

# with open("teste.txt", "w", encoding="utf8") as out:
#     out.write(postos)
guidePost = ''
servicosPostos = []
with open("output_fixtures.py", "w", encoding="utf8") as saida:
    for posto in postos:
        #created_at, updated_at, id_post_guide, id_8, id_2, id_16, description, address, city, id_1
        #GuidePost.objects.create(city= "São Paulo", id_post_guide=33, id_1= 48, id_8= 0, id_2= 58, id_16= 312, description= 'POUPATEMPO - CIDADE ADEMAR', address= 'Av. Cupecê, 5497 - Jardim Miriam')
        # print(posto)
        cidade = posto.get("descricao").split(" - ")[1]

        pattern = re.compile("poupatempo\s+", re.IGNORECASE)
        cidade = pattern.sub("", cidade)

        if cidade in ["CIDADE ADEMAR", "ITAQUERA", "LAPA", "SANTO AMARO", "SÉ", "ALESP"]:
            cidade = "SÃO PAULO"
        print(cidade.title())
        # break
        guidePost = guidePost +  f'GuidePost.objects.create(city= "{str(cidade.title())}", id_post_guide={str(posto.get("idPostoGuia"))}, id_1= {str(posto.get("id1"))}, id_8= {str(posto.get("id8"))}, id_2= {str(posto.get("id2"))}, id_16= {str(posto.get("id16"))}, description= "{str(posto.get("descricao"))}", address= "{str(posto.get("endereco"))}")\n'
        for servico in posto.get("servicos"):
            # PostService.objects.create(id_service=96, description='Certidão de Prontuario de RG', id_organ=1, validator_ne=False, validator_s=False, validator_sa=True, id_guide_post=33)
            id_service = str(servico.get('id'))
            if str(id_service) == '1602':
                id_service = '16'
            servicoPosto = f"PostService.objects.create(id_service={str(id_service)}, description='{str(servico.get('descricao'))}', id_organ={str(servico.get('idOrgao'))}, validator_ne={str(servico.get('ne')).title()}, validator_s={str(servico.get('s')).title()}, validator_sa={str(servico.get('sa')).title()}, id_guide_post={str(posto.get('idPostoGuia'))})\n"
            servicosPostos.append(servicoPosto)
            # print(servico.get("descricao"))

    saida.write(guidePost)
    saida.writelines(servicosPostos)
    saida.flush()
    saida.close()