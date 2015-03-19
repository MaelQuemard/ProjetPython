import cherrypy
import json
import service.database as db
 
data = json.loads(open("c:/Users/Mael/Documents/Github/ProjetPython/ressource/installation.json").read())
 
class WebManager(object):

    """
    Exposes web services
    """
    @cherrypy.expose
    def index(self):
        """
        Exposes the service at localhost:8080/
        """
        return "There are {0} items".format(len(data))
 
    @cherrypy.expose
    def show_all(self, table):
        """
        Exposes the service at localhost:8080/show_all/table
        """
        database = db.Database("c:/Users/Mael/Documents/Github/ProjetPython/db/test.db")
        database.selectAll(table)
 
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