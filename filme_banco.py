
def valor_sequence(conn):
    cursor = conn.cursor()
    cursor.execute("select nextval('movies_sequence')")
    result = cursor.fetchone()
    cursor.close()
    return result


def insere_filme(conn,filme):
    id = valor_sequence(conn)
    params = [id,filme.adult,filme.backdrop_path,filme.original_language,
              filme.original_title,filme.overview,filme.popularity,
              filme.poster_path,filme.release_date,filme.title,
              filme.video,filme.vote_average,filme.vote_count
              ]
   

    sql = """insert into movies (id,adult,backdrop_path,original_language,original_title,overview,
                 popularity,poster_path,release_date,title,video,vote_average,vote_count)
                 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) returning id"""      
       
    try:
        cursor = conn.cursor()
        cursor.execute(sql,params)
        id = cursor.fetchone()[0]
        conn.commit()
        cursor.close() 
    except Exception as error:
        print(str(error))


    return id


def lista_filmes(conn):

    resultado = []
    sql = """select id,adult,backdrop_path,original_language,original_title,
             overview,popularity,poster_path,release_date,title,video,vote_average,
             vote_count from movies"""
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()
        print(type(resultado))  
        return resultado

    except Exception as error:
        print(str(error))    


    conn.close()






