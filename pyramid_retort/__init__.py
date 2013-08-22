from pyramid.scaffolds import PyramidTemplate

class AlembicProjectTemplate(PyramidTemplate):
    _template_dir = 'retort'
    summary = 'Pyramid Alembic project with basic models and views'