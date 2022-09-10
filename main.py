
import fundamentus

df = fundamentus.get_resultado() #  // pega todas os papeis e dados das empresas

#df = fundamentus.get_resultado_raw() // pega os dados do site do jeito que esta com lentras maiusculas e espacos

#df = fundamentus.get_papel('sanb4') # // busca papel expecifico

df = df[df['roe'] > 0] # // busca filtro expecifico do papel
df = df[df['pl'] <= 4]
df = df[df['pvp'] <= 1.5]


print(df)
# pesquisa por setor

#fin = fundamentus.list_papel_setor(35)  # finance
#seg = fundamentus.list_papel_setor(38)  # seguradoras

