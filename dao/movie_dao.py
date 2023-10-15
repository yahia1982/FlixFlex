from config.db import DbHelper

db = DbHelper()


class MovieDao:

    def get_show_genre(self, serie_id=None, movie_id=None):
        sql = """
            SELECT 
                g.genre
            FROM genre g
                INNER JOIN show_genre sg ON sg.genre_id = g.genre_id 
            WHERE serie_id = ? AND movie_id = ? 
        """
        rows = db.fetch_all(sql, (serie_id, movie_id))
        return [row for row in rows]

    def movie_row_mapper(self, row):
        if row:
            return {
                "movie_id": row[0],
                "title": row[1],
                "description": row[2],
                "release_date": row[3],
                "director": row[4],
                "poster_url": row[5],
                "runtime": row[6],
                "genre": self.get_show_genre(movie_id=row[0]),
                "ranking": row[7],
                "trailer": row[8]
            }

    def serie_row_mapper(self, row):
        if row:
            return {
                "serie_id": row[0],
                "title": row[1],
                "description": row[2],
                "release_date": row[3],
                "director": row[4],
                "poster_url": row[5],
                "average_episode_runtime": row[6],
                "episodes": row[7],
                "genre": self.get_show_genre(serie_id=row[0]),
                "ranking": row[8],
                "trailer": row[9]
            }

    def get_movies(self):
        sql = """
            SELECT 
                movie_id, 
                title, 
                description, 
                release_date, 
                director, 
                poster_url,             
                runtime,                
                ranking,
                trailer
            FROM movies                
        """
        rows = db.fetch_all(sql, ())
        return [self.movie_row_mapper(row) for row in rows]

    def get_top_movies(self, rows_count):
        sql = """
            SELECT 
                movie_id, 
                title, 
                description, 
                release_date, 
                director, 
                poster_url,             
                runtime,                
                ranking,
                trailer
            FROM movies 
            ORDER BY ranking DESC 
            LIMIT ?
        """
        rows = db.fetch_all(sql, (rows_count,))
        return [self.movie_row_mapper(row) for row in rows]

    def get_series(self):
        sql = """
            SELECT 
                serie_id,
                title,
                description,
                release_date,
                director,
                poster_url,		
                average_episode_runtime,
                episodes,                
                ranking,
                trailer
            FROM series 
        """
        rows = db.fetch_all(sql, ())
        return [self.serie_row_mapper(row) for row in rows]

    def get_top_series(self, rows_count):
        sql = """
            SELECT 
                serie_id,
                title,
                description,
                release_date,
                director,
                poster_url,		
                average_episode_runtime,
                episodes,                
                ranking,
                trailer
            FROM series 
            ORDER BY ranking DESC 
            LIMIT ?
        """
        rows = db.fetch_all(sql, (rows_count,))
        return [self.serie_row_mapper(row) for row in rows]

    def get_movies_page(self, page, page_size):
        sql = """
                SELECT 
                    movie_id, 
                    title, 
                    description, 
                    release_date, 
                    director, 
                    poster_url,             
                    runtime,                    
                    ranking,
                    trailer
                FROM movies  
                ORDER BY    
                    release_date
                LIMIT ? OFFSET ?
                """
        rows = db.fetch_all(sql, (page_size, (int(page) - 1) * page_size))
        return [self.movie_row_mapper(row) for row in rows]

    def get_series_page(self, page, page_size):
        sql = """
                SELECT 
                    serie_id,
                    title,
                    description,
                    release_date,
                    director,
                    poster_url,		
                    average_episode_runtime,
                    episodes,                    
                    ranking,
                    trailer
                FROM series 
                ORDER BY    
                    release_date
                LIMIT ? OFFSET ?
                """
        rows = db.fetch_all(sql, (page_size, (int(page) - 1) * page_size))
        return [self.serie_row_mapper(row) for row in rows]

    def add_movie_serie_favorite(self, user_id, serie_id=None, movie_id=None):
        try:
            sql = """
            INSERT OR IGNORE INTO favorite_list (   user_id,
                                                    movie_id,
                                                    serie_id)
            VALUES (?,?,?)
            """
            db.execute_query(sql, (user_id, movie_id, serie_id))
            db.commit()
        finally:
            db.close()

    def remove_movie_serie_favorite(self, user_id, movie_id=None, serie_id=None):
        try:
            params = [user_id]
            sql = """
            DELETE FROM favorite_list 
            WHERE user_id = ?"""
            if movie_id:
                sql+=" AND movie_id = ?"
                params.append(movie_id)
            if serie_id:
                sql+=" AND serie_id = ?"
                params.append(serie_id)
            print(sql, tuple(params))

            db.execute_query(sql, tuple(params))
            db.commit()
        finally:
            db.close()

    def get_favorites_movies(self, user_id):
        sql = """
                    SELECT 
                        m.movie_id, 
                        title, 
                        description, 
                        release_date, 
                        director, 
                        poster_url,             
                        runtime,                
                        ranking,
                        trailer
                    FROM movies m
                        inner join favorite_list fl on fl.movie_id = m.movie_id 
                    WHERE user_id = ?                             
                """
        rows = db.fetch_all(sql, (user_id, ))
        return [self.movie_row_mapper(row) for row in rows]

    def get_favorites_series(self, user_id):
        sql = """
                    SELECT 
                        s.serie_id,
                        title,
                        description,
                        release_date,
                        director,
                        poster_url,		
                        average_episode_runtime,
                        episodes,                
                        ranking,
                        trailer
                    FROM series s
                        inner join favorite_list fl on fl.serie_id = s.serie_id 
                    WHERE user_id = ?      
                """
        rows = db.fetch_all(sql, (user_id, ))
        return [self.serie_row_mapper(row) for row in rows]

    def look_for_movies(self, keyword):
        sql = """
                SELECT 
                    movie_id, 
                    title, 
                    description, 
                    release_date, 
                    director, 
                    poster_url,             
                    runtime,                
                    ranking,
                    trailer
                FROM movies
                WHERE
                    title like ? 
                """
        rows = db.fetch_all(sql, ('%'+keyword+'%',))
        return [self.movie_row_mapper(row) for row in rows]

    def look_for_series(self, keyword):
        sql = """
                SELECT 
                    serie_id,
                    title,
                    description,
                    release_date,
                    director,
                    poster_url,		
                    average_episode_runtime,
                    episodes,                
                    ranking,
                    trailer
                FROM series
                WHERE
                    title like ? 
                """
        rows = db.fetch_all(sql, ('%'+keyword+'%',))
        return [self.serie_row_mapper(row) for row in rows]

    def get_movie(self, movie_id):
        sql = """
                   SELECT 
                       movie_id, 
                       title, 
                       description, 
                       release_date, 
                       director, 
                       poster_url,             
                       runtime,                
                       ranking,
                       trailer
                   FROM movies   
                   WHERE movie_id = ?             
               """

        return self.movie_row_mapper(db.fetch_one(sql, (movie_id, )))

    def get_serie(self, serie_id):
        sql = """
                  SELECT 
                      serie_id,
                      title,
                      description,
                      release_date,
                      director,
                      poster_url,		
                      average_episode_runtime,
                      episodes,                
                      ranking,
                      trailer
                  FROM series 
                  WHERE serie_id = ?
              """
        return self.serie_row_mapper(db.fetch_one(sql, (serie_id, )))

