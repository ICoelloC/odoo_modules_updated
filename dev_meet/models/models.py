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

    name = fields.Char(string='Name', required=True, help='Name')
    nickname = fields.Char(string='Nickname', required=True, help='Nickname')
    dni = fields.Char(string='DNI', required=True, help='DNI')
    email = fields.Char(string='Email', help='Email')
    phone = fields.Char(string='Phone number', help='Phone number')
    photo = fields.Image(string='Photo', help='Dev photo')
    category = fields.Selection([('1','JUNIOR'),('2','SENIOR'),('3','PROJECT MANAGER'),('4','ANALIST')],'Category',default='1')
    technologies_learned = fields.Many2many(string='Languages learned', comodel_name='dev_meet.technology', help='Languages learned')
    interested_technologies = fields.Many2many(string='Interested in', comodel_name='dev_meet.technology', relation='interested_technologies', help='Interested in')
    events_as_speaker = fields.Many2many(string='Speaker on', comodel_name='dev_meet.event')
    witnessed_events = fields.Many2many(string='Witnessed events', comodel_name='dev_meet.event', relation='witnessed_events')

    @api.constrains('dni')
    def _check_dni(self):
        regex = re.compile('[0-9]{8}[a-z]\Z', re.I) #re.I ignoreCase
        for student in self:
            # Ahora vamos a validar si se cumple la condición
            if regex.match(student.dni):
                _logger.info('DNI correcto')
            else:
                raise ValidationError('Invalid format: DNI')

    _sql_constraints = [('dni_uniq', 'unique(dni)', 'DNI can\'t be repeated')] #Todos los mensajes los deberíamos poner en inglés y luego traducir


class technology(models.Model):
    _name = 'dev_meet.technology'
    _description = 'Developers'
    name = fields.Char(string='Name', required=True, help='Language name')
    logo = fields.Image(string='Logo', help='Logo')
    official_web = fields.Char(string='Official web', help='Offiiial web')
    developers = fields.Many2many(string ='Developers', comodel_name='dev_meet.developer')
    interested_developers = fields.Many2many(string ='Interested developers', comodel_name='dev_meet.developer', relation='interested_technologies')
    events = fields.Many2many(string='Events', comodel_name='dev_meet.event')


class event(models.Model):
    _name = 'dev_meet.event'
    _description = 'Events'
    name = fields.Char(string='Name', required=True, help='Event name')
    start_date = fields.Date(string='Start date', required=True, help='Start date')
    end_date = fields.Date(string='End date', required=True, help='End date')
    presential = fields.Boolean(string='Presential', help='Presential', required=True, default=False)
    room = fields.Many2one(string='Room', comodel_name='dev_meet.room', help='Event room')
    technologies = fields.Many2many(string='Languages', comodel_name='dev_meet.technology', help='Languajes on event')
    speaker = fields.Many2many(string='Speakers', comodel_name='dev_meet.developer', help='Speakers')
    developers = fields.Many2many(string='Developers', comodel_name='dev_meet.developer', relation='witnessed_events')

    @api.constrains('start_date','end_date')
    def _check_date(self):
        for event in self:
            if event.start_date < event.end_date:
                _logger.info('Invlid date')
            else:
                raise ValidationError('Incorrect date interval, start date could not be after the end date.')

class room(models.Model):
    _name = 'dev_meet.room'
    _description = 'Room'

    name = fields.Char(string='Room name', required=True, help='Room name')
    location = fields.Char(string='Location',help='Location')
    room_number = fields.Integer(string='Room number', help='Room number')
    capacity = fields.Integer(string='Capacity', help='Capacity')
    events = fields.One2many(name='Events', comodel_name='dev_meet.event', help='Events on that room', inverse_name='room')