import os
c = get_config()
c.NbConvertApp.export_format = 'pdf'
c.TemplateExporter.template_path = ['.', os.path.normpath(r'../styles/')]
c.PDFExporter.latex_command = ['pdflatex', '{filename}']
c.Exporter.template_file = 'template'