from interface_para_cmd import *

ip1 = itemPergunta("Quantos anos você tem?", **{"1":"Tenho um ano. ", "2":"Tenho dois anos. ", "3":"Minha idade não importa. "})
ip2 = itemPergunta("Que curso você faz?", **{"1":"Faço Engenharia da Computação. ", "2":"Faço Ciência da Computação. ", "3":"Faço Licenciatura em Computação. ", "4":"Faço Engenharia Mecatrônica. ", "5":"Sou de humanas >:]"})

tiposForms["Primeiro parágrafo"] = Formulario(ip1, ip2)

menu_principal()