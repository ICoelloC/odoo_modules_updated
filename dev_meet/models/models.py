# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import secrets
import logging
import re

_logger = logging.getLogger(__name__)

class developer(models.Model):
    _name = 'dev_meet.developer'
    _description = 'Developers'

    name = fields.Char(string='Nombre', required=True,
                       help='Nombre del desarrollador')
    nickname = fields.Char(string='Apellidos', required=True,
                           help='Apellidos del desarrollador')
    dni = fields.Char(string='DNI', required=True, help='DNI')
    email = fields.Char(string='Email', help='Correo electrónico')
    phone = fields.Char(string='Teléfono', help='Teléfono móvil')

    photo = fields.Image(string='Foto', help='Foto del desarrollador')

    category = fields.Selection([('1','JUNIOR'),('2','SENIOR'),('3','PROYECT MANAGER'),('4','ANALIST')],'Category',default='1')

    technologies_learned = fields.Many2many(string='Lenguajes aprendidos', comodel_name='dev_meet.technology', help='Tecnpologías aprendidas')

    interested_technologies = fields.Many2many(string='Tecnologías interesadas', comodel_name='dev_meet.technology', relation='interested_technologies', help='Tecnpologías interesadas')

    events_as_speaker = fields.Many2many(string='Speaker en', comodel_name='dev_meet.event')

    witnessed_events = fields.Many2many(string='Witnessed events', comodel_name='dev_meet.event', relation='witnessed_events')


    @api.constrains('dni')
    def _check_dni(self):
        regex = re.compile('[0-9]{8}[a-z]\Z', re.I) #re.I ignoreCase
        for student in self:
            # Ahora vamos a validar si se cumple la condición
            if regex.match(student.dni):
                _logger.info('DNI correcto')
            else:
                raise ValidationError('Formato incorrecto: DNI')

    _sql_constraints = [('dni_uniq', 'unique(dni)', 'DNI can\'t be repeated')] #Todos los mensajes los deberíamos poner en inglés y luego traducir


class technology(models.Model):
    _name = 'dev_meet.technology'
    _description = 'Developers'

    name = fields.Char(string='Nombre', required=True,
                       help='Nombre de la tecnología')
    logo = fields.Image(string='Logo', help='Logo de la tecnología')
    official_web = fields.Char(
        string='Página oficial', help='Página web oficial')

    developers = fields.Many2many(string ='Desarrolladores', comodel_name='dev_meet.developer')

    interested_developers = fields.Many2many(string ='Desarrolladores interesados', comodel_name='dev_meet.developer', relation='interested_technologies')

    events = fields.Many2many(string='Eventos', comodel_name='dev_meet.event')


class event(models.Model):
    _name = 'dev_meet.event'
    _description = 'Events'

    name = fields.Char(string='Nombre', required=True, help='Nombre del evento')
    start_date = fields.Date(string='Fecha de inicio', required=True, help='Fecha de inicio del evento')
    end_date = fields.Date(string='Fecha de fin', required=True, help='Fecha de fin del evento')
    presential = fields.Boolean(string='Es presencial', help='Evento presencial', required=True, default=False)

    room = fields.Many2one(string='Sala', comodel_name='dev_meet.room', help='Sala donde se realizará el evento' """ , attrs="{'column-invisible': [('presential','==',False)]}, {'column-visible': [('presential','==',True)]}" """)
    technologies = fields.Many2many(string='Tecnologías', comodel_name='dev_meet.technology', help='Tecnologías vistas en el evento')
    speaker = fields.Many2many(string='Speakers', comodel_name='dev_meet.developer', help='Speaker del evento')

    developers = fields.Many2many(string='Developers', comodel_name='dev_meet.developer', relation='witnessed_events')

    @api.constrains('start_date','end_date')
    def _check_date(self):
        for event in self:
            if event.start_date < event.end_date:
                _logger.info('fecha_válida')
            else:
                raise ValidationError('Intervalo de fechas incorrecto, la fecha de inicio no puede ser posterior a la de finalización.')

class room(models.Model):
    _name = 'dev_meet.room'
    _description = 'Room'

    name = fields.Char(string='Nombre de la sala', required=True, help='Nombre de la sala')
    location = fields.Char(string='Ubicación',help='Ubicación del evento')
    room_number = fields.Integer(string='Número de sala', help='Número de sala')
    capacity = fields.Integer(string='Capacidad', help='Capacidad de la sala')
    
    events = fields.One2many(name='Eventos', comodel_name='dev_meet.event', help='Eventos que se realizarán en la sala', inverse_name='room')