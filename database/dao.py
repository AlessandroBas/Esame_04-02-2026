from database.DB_connect import DBConnect
from model.artist import Artist

class DAO:

    @staticmethod
    def get_roles():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ SELECT distinct role
                    FROM authorship"""
        cursor.execute(query)

        for row in cursor:

            result.append(row["role"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_artists(role):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ SELECT a.artist_id,a.name,sum(o.curator_approved)as num_objects
                    FROM authorship au,artists a, objects o
                    WHERE a.artist_id = au.artist_id and au.role=%s and au.object_id =o.object_id and o.curator_approved=1
                    group by a.artist_id, a.name """

        cursor.execute(query, (role,))

        for row in cursor:
            result.append(Artist(row["artist_id"],row["name"],row["num_objects"]))

        cursor.close()
        conn.close()
        return result