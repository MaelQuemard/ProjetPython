# -*- coding: utf-8 -*-

import cherrypy
import json
import service.database as db
from mako.template import Template
from mako.lookup import TemplateLookup 
lookup = TemplateLookup(directories=[""]) 
 
class WebManager(object):

    """
    Exposes web services
    """ 
    @cherrypy.expose
    def index(self):
        """
        Exposes the service at localhost:8080/
        """
        return Template(filename="index.html", lookup=lookup).render()
 
    @cherrypy.expose
    def show_all(self, table):
        """
        Exposes the service at localhost:8080/show_all/table
        """
        view = Template(filename="template.html", lookup=lookup)

        database = db.Database("db/test.db")
        results = database.selectAll(table)

        return view.render( 
            rows=results
        )

    @cherrypy.expose
    def requestActivityCity(self, commune, activite):
        """
        Exposes the service at localhost:8080/requestActivityCity
        """
        view = Template(filename="template.html", lookup=lookup)

        database = db.Database("db/test.db")
        results = database.requestActivityCity(commune, activite)

        return view.render( 
            rows=results
        )

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