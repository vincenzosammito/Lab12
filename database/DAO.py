from database.DB_connect import DBConnect
from model.retailer import Retailer

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllCountries():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select DISTINCT Country 
                from go_retailers gr """

        cursor.execute(query)

        for row in cursor:
            result.append(row["Country"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllRetailers(country):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select Retailer_code , Retailer_name
from go_retailers gr 
where Country = %s """

        cursor.execute(query,[country])

        for row in cursor:
            result.append(Retailer(row["Retailer_code"], row["Retailer_name"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getPesoArco(r1,r2,year):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select DISTINCT (g.Product_number) as peso
from go_daily_sales g, go_daily_sales g2
where YEAR (g2.`Date`) = YEAR (g.`Date`) and YEAR (g2.`Date`) = %s
and g2.Product_number = g.Product_number 
and g.Retailer_code = %s and g2.Retailer_code = %s
"""

        cursor.execute(query, [year, r1, r2])

        for row in cursor:
            result.append(row["peso"])
        cursor.close()
        conn.close()
        return result

