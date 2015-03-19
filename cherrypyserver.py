import cherrypy
import json
import service.database as db
 
data = json.loads(open("ressource/installation.json").read())
 
class WebManager(object):

    """
    Exposes web services
    """
    @cherrypy.expose
    def index(self):
        """
        Exposes the service at localhost:8080/
        """
        html = '''<h1>Installations Sportives des Pays de la Loire</h1>\n
        <a href="show_all/installation">Voir les installations</a><br/>\n
        <a href="show_all/equipement">Voir les équipements</a><br/>\n
        <a href="show_all/activite">Voir les activités</a>'''
        return html
 
    @cherrypy.expose
    def show_all(self, table):
        """
        Exposes the service at localhost:8080/show_all/table
        """
        database = db.Database("db/test.db")
        return database.selectAll(table)
 
    @cherrypy.expose
    def show(self, id):
        """
        Exposes the service at localhost:8080/show/[id]/
        """
        try:
            item = data[int(id)]
        except (IndexError, IOError):
            return "Invalid ID"
 
        return json.dumps(item)
 
 
cherrypy.quickstart(WebManager())