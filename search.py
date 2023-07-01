import os, sys
import platform

def pesquisar_arquivos(diretorio, extensao):
	arquivos = []
	for root, dirs, files in os.walk(diretorio):
		for file in files:
			if file.endswith(extensao):
				arquivos.append(os.path.join(root, file))
	return arquivos
def pesquisar_frase(arquivo, frase):
	with open(arquivo, 'r') as f:
		conteudo = f.read()
		if frase.lower() in conteudo.lower():
			return True
		return False
def abrir_arquivo(arquivo):
	os.system(f"featherpad {arquivo}")
def get_snopse(arquivo):
	with open(arquivo, "r") as paragrafo:
		return paragrafo.readline()
def clear():
	if "windows" in platform.platform().lower(): os.system("cls")
	else: os.system("clear")

def conscienceNet():
	arquivos_encontrados = pesquisar_arquivos(os.getcwd(), ".txt")

	consulta = input("\nPesquisa: ")

	arquivos_com_frase = []
	for arquivo in arquivos_encontrados:
		if pesquisar_frase(arquivo, consulta.strip()):
			arquivos_com_frase.append(arquivo)

	if not arquivos_com_frase: return

	clear()
	while True:
		try:
			print(get_snopse(arquivos_com_frase[0]))
			print(f"\nResultados encontrados na pesquisa:\n")
			for i, arquivo in enumerate(arquivos_com_frase):  print(f"{i+1}. {arquivo}")

			escolha = input("\nDigite o número do arquivo que deseja abrir: ").strip()
			if escolha == "": clear()
			
			try:
				indice_arquivo = int(escolha) - 1
				arquivo_escolhido = arquivos_com_frase[indice_arquivo]
				abrir_arquivo(arquivo_escolhido)
			except (ValueError, IndexError): clear()
		except KeyboardInterrupt: break
		except EOFError: break
		except: clear()
		
		clear()

if __name__ == '__main__':
	while True: clear(), conscienceNet(), clear()
