import os


def format_phone_number(value):
    if not value:
        return ''
    if len(value) == 10:
        phone = '({0}){1}-{2}'.format(value[0:3], value[3:6], value[6:10])
    elif len(value) == 11:
        phone = '+{0}({1}){2}-{3}'.format(value[0], value[1:4], value[4:7], value[7:11])
    else:
        phone = value

    return phone


# TODO: file path shoudl be None default, to return as buffer
def generate_commercial_invoice(export_data, exporter_data, cosignee_data, products, flags, importer_data=None,
                                file_path="output_commercial_invoice.pdf"):  # self, request, *args, **kwargs):

    current_directory = os.path.dirname(os.path.realpath(__file__))

    from reportlab.lib.enums import TA_CENTER, TA_RIGHT, TA_LEFT
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

    from reportlab.lib import colors
    from reportlab.lib.units import inch, cm
    # from reportlab.lib.pagesizes import cm
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image, PageBreak

    # TODO: return as buffer vs file
    # if file_path = None then return buffer instead
    doc = SimpleDocTemplate(file_path, rightMargin=.5 * cm, leftMargin=.5 * cm,
                            topMargin=1.5 * cm, bottomMargin=1.5 * cm)

    story = []

    # Styles
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='Right', alignment=TA_RIGHT))
    styles.add(ParagraphStyle(name='Left', alignment=TA_LEFT))
    styles.add(ParagraphStyle(name='Line_Data', alignment=TA_LEFT, fontSize=8, leading=7))
    styles.add(ParagraphStyle(name='Line_Data_Small', alignment=TA_LEFT, fontSize=7, leading=8))
    styles.add(ParagraphStyle(name='Line_Data_Large', alignment=TA_LEFT, fontSize=12, leading=12))
    styles.add(ParagraphStyle(name='Line_Data_medium_Center', alignment=TA_CENTER, fontSize=9, leading=12))
    styles.add(ParagraphStyle(name='Line_Fact_Large_Center', alignment=TA_CENTER, fontSize=12, leading=12))
    styles.add(ParagraphStyle(name='Line_Data_Largest', alignment=TA_LEFT, fontSize=14, leading=15))
    styles.add(ParagraphStyle(name='Line_Label', font='Helvetica-Bold', fontSize=7, leading=6, alignment=TA_LEFT))
    styles.add(ParagraphStyle(name='Line_Label_Center', font='Helvetica-Bold', fontSize=7, alignment=TA_CENTER))

    checked_image_path = os.path.join(current_directory, 'images/heritage.png')
    # Get company information

    comprobantee = '{0}<br/><br/> {1}<br/> <br/>{2}'.format(export_data['title'],
                                                  export_data['num_doc_empresa'],
                                                  export_data['serie_and_correlativo'])

    img = Image(checked_image_path, 12.40 * cm, 2.60 * cm, )
    img.vAlign = 'CENTER'
    img.hAlign = 'CENTER'
    data1 = [
            [
                img,
                Paragraph(comprobantee, styles["Line_Fact_Large_Center"])
            ],
             [
                Paragraph('HERITAGE TEXTILES S.A.C', styles["Line_Data_medium_Center"]),
                ""
             ],
             [
                 Paragraph('Dirección: Cal Horacio Cachay Díaz 2do 242 urb, santa catalina, lima, lima', styles["Line_Label_Center"]),
                 ""
             ]
    ]

    t1 = Table(data1, colWidths=(12.6 * cm, 7 * cm))  # , rowHeights = [.3*cm, .5*cm, .3*cm, .5*cm])

    t1.setStyle(TableStyle([
        ('INNERGRID', (1, 1), (1, 1), 0.25, colors.black),
        ('BOX', (1, 0), (1, 0), 0.25, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    t1.hAlign = 'RIGHT'

    story.append(t1)

    story.append(Spacer(0.1 * cm, .5 * cm))

    data1 = [[Paragraph('Fecha de Emisión', styles["Line_Label"]),
              Paragraph('30/12/2022', styles["Line_Label"]),
              Paragraph('Forma de Pago', styles["Line_Label"]),
              Paragraph('Al Contado', styles["Line_Label"]),
              ],
             [Paragraph('Titular', styles["Line_Label"]),
              Paragraph('EMPRESA LEYMASTER SOCIEDAD ANONIMA CERRADA - LEYMASTER S.A.C.', styles["Line_Label"]),
              Paragraph('Guía Remisión', styles["Line_Label"]),
              Paragraph('T001-1', styles["Line_Label"]),
             ],
             [Paragraph('R.U.C', styles["Line_Label"]),
              Paragraph('20524621186', styles["Line_Label"]),
              "",
              "",
              ],
             [Paragraph('Dirección del Cliente', styles["Line_Label"]),
              Paragraph('JR. PROLONGACIÓN GAMARRA NRO. 774 INT. S4 LIMA LIMA LA VICTORIA', styles["Line_Label"]),
              "",
              "",
              ],
             [Paragraph('Tipo de moneda', styles["Line_Label"]),
              Paragraph('Soles', styles["Line_Label"]),
              "",
              "",
              ]
             ]
    t1 = Table(data1,  colWidths=(3 * cm, 10.7 * cm, 2.9 * cm, 3 * cm))
    t1.setStyle(TableStyle([
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t1)

    # Shipper/Exporter, Cosignee

    data1 = [[Paragraph('CODIGO.', styles["Line_Label"]),
              Paragraph('CANTIDAD', styles["Line_Label"]),
              Paragraph('UND', styles["Line_Label"]),
              Paragraph('DESCRIPCION', styles["Line_Label"]),
              Paragraph('P. UNITARIO', styles["Line_Label"]),
              Paragraph('VALOR VENTA', styles["Line_Label"]),
              ],
    ]

    t1 = Table(data1, colWidths=(3.3 * cm, 2.3 * cm, 2.3 * cm, 7 * cm, 2.3 * cm, 2.4 * cm))
    t1.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t1)

    data1 = [[Paragraph(str(product['codigo']), styles["Line_Data_Small"]),
              Paragraph(str(product['cantidad']), styles["Line_Data_Small"]),
              Paragraph(str(product['unidad_medida']), styles["Line_Data_Small"]),
              Paragraph(str(product['descripcion']), styles["Line_Data_Small"]),
              Paragraph(str(product['precio_unitario']), styles["Line_Data_Small"]),
              Paragraph(str(product['valor_venta']), styles["Line_Data_Small"])
              ] for product in products]

    t1 = Table(data1, colWidths=(3.3 * cm, 2.3 * cm, 2.3 * cm, 7 * cm, 2.3 * cm, 2.4 * cm))
    t1.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t1)

    total_packages = 0
    total_weight = 0.0
    total_value = 0.0

    for product in products:
        total_packages += product['cantidad']
        total_weight += float(product['precio_unitario'])
        total_value += float(product['valor_venta'])

    data1 = [['',
              '',
              '',
              '',
              Paragraph('SUBTOTAL', styles["Line_Data_Small"]),
              Paragraph('S/ 100.00', styles["Line_Data_Small"])
              ],
             ['',
              '',
              '',
              '',
              Paragraph('IGV', styles["Line_Data_Small"]),
              Paragraph('S/ 100.00', styles["Line_Data_Small"]),
              ],
             ['',
              '',
              '',
              '',
              Paragraph('TOTAL', styles["Line_Data_Small"]),
              Paragraph('S/ 100.00', styles["Line_Data_Small"]),
              ]
             ]

    t1 = Table(data1, colWidths=(3.3 * cm, 2.3 * cm, 2.3 * cm, 7 * cm, 2.3 * cm, 2.4 * cm))
    t1.setStyle(TableStyle([
        ('INNERGRID', (4, 0), (4, 3), 0.25, colors.black),
        ('INNERGRID', (5, 0), (5, 3), 0.25, colors.black),
        ('BOX', (4, 0), (5, 3), 0.25, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t1)

    data1 = [[Paragraph(
        'SON MIL NOVECIENTOS Y 00/100 SOLES',
        styles["Line_Label"]), '',
              '']]
    t1 = Table(data1, colWidths=(None, 3.3 * cm, 1.8 * cm))
    t1.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t1)

    story.append(Table([[Paragraph('Forma de pago: '
                                   'Al contado', styles["Line_Label"])]]))

    story.append(Spacer(0.1 * cm, .5 * cm))

    # TODO: signature could be image ? Date could be sign_date ?
    # TODO: signature, date

    detallecredito = '{0}<br/> <br/> {1} <br/><br/>{2}'.format('Información del Crédito',
                                                            'Monto neto pendiente de pago:',
                                                            'Total de cuotas:')


    data1 = [
        [Paragraph('Información del Crédito: ', styles["Line_Data_Small"]),
         Paragraph('Monto neto pendiente de pago: S/ 4300,00', styles["Line_Data_Small"]),
         Paragraph('Total de cuotas: 4', styles["Line_Data_Small"]),
         "",
         ]
    ]

    t1 = Table(data1, colWidths=(4.3 * cm, 5.5 * cm, 5.5 * cm, 4.3 * cm))
    t1.setStyle(TableStyle([
        ('INNERGRID', (1, 1), (1, 1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))

    story.append(t1)

    story.append(Spacer(0.1 * cm, .5 * cm))
    data1 = [
        [Paragraph('Nº Cuota', styles["Line_Data_Small"]),
         Paragraph('Fech. Vencimiento', styles["Line_Data_Small"]),
         Paragraph('Monto', styles["Line_Data_Small"]),
         ]
    ]

    t1 = Table(data1, colWidths=(2 * cm, 2.5 * cm, 2 * cm))

    t1.setStyle(TableStyle([
        ('INNERGRID', (1, 1), (1, 1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))

    story.append(t1)

    letras = [
        {
            'n_cuota': '1',
            'fech_ven': '10/01/2023',
            'mto': 'S/ 100,00',
        },
        {
            'n_cuota': '2',
            'fech_ven': '10/01/2023',
            'mto': 'S/ 100,00',
        },
        {
            'n_cuota': '3',
            'fech_ven': '10/01/2023',
            'mto': 'S/ 100,00',
        },
        {
            'n_cuota': '4',
            'fech_ven': '10/01/2023',
            'mto': 'S/ 100,00',
        }
    ]

    data1 = [
        [Paragraph(letra['n_cuota'], styles["Line_Data_Small"]),
         Paragraph(letra['fech_ven'], styles["Line_Data_Small"]),
         Paragraph(letra['mto'], styles["Line_Data_Small"]),
         ] for letra in letras
    ]

    t1 = Table(data1, colWidths=(2 * cm, 2.5 * cm, 2 * cm))

    t1.setStyle(TableStyle([
        ('INNERGRID', (1, 1), (1, 1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))

    story.append(t1)

    doc.build(story)

