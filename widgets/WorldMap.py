import sqlite3

from core.base.model.Widget import Widget
from core.base.model.widgetSizes import WidgetSizes


class WorldMap(Widget):

	SIZE = WidgetSizes.w_extralarge_wide
	OPTIONS: dict = dict()

	def __init__(self, data: sqlite3.Row):
		super().__init__(data)
