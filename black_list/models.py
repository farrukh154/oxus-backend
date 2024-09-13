import pypyodbc

from common.abacus.connection import connection_string


class BlackListSearch:
    @staticmethod
    def search_person(name, match_percentage):
        conn = pypyodbc.connect(connection_string)
        cursor = conn.cursor()
        sql = f"EXEC [dbo].[OTJ_SearchBL] @input=N'{name}', @desc={match_percentage}"
        cursor.execute(sql)

        results = []
        columns = [column[0] for column in cursor.description]

        while True:
            row = cursor.fetchone()
            if not row:
                break
            result_dict = {column: row[column] for column in columns}
            results.append(result_dict)

        cursor.close()
        conn.close()
        return results
