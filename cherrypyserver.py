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
        return Template(filename="view/index.html", lookup=lookup).render()
 
    @cherrypy.expose
    def show_all(self, table):
        """
        Exposes the service at localhost:8080/show_all/table
        """
        view = Template(filename="view/template.html", lookup=lookup)

        database = db.Database("db/test.db")
        results = database.selectAll(table)

        return view.render( 
            rows=results
        )

    @cherrypy.expose
    def form_lieu(self):
        """
        Exposes the service at localhost:8080/form_lieu
        """
        return Template(filename="view/form_lieu.html", lookup=lookup).render()

    @cherrypy.expose
    def form_activity(self):
        """
        Exposes the service at localhost:8080/form_activity
        """
        view = Template(filename="view/template2.html", lookup=lookup)

        database = db.Database("db/test.db")
        results = database.requestCity()

        return view.render( 
            rows=results
        )

    @cherrypy.expose
    def requestActivityCity(self, commune, activite):
        """
        Exposes the service at localhost:8080/requestActivityCity
        """
        view = Template(filename="view/template.html", lookup=lookup)

        database = db.Database("db/test.db")
        results = database.requestActivityCity(commune, activite)

        return view.render( 
            rows=results
        )

    @cherrypy.expose
    def requestActivity(self, commune):
        """
        Exposes the service at localhost:8080/requestActivity
        """
        view = Template(filename="view/template.html", lookup=lookup)

        database = db.Database("db/test.db")
        results = database.requestActivity(commune)

        return view.render( 
            rows=results
        ) 
 
cherrypy.quickstart(WebManager())