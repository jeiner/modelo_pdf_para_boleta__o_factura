# generate_invoice test
from fedex_invoice.invoice import generate_commercial_invoice

# Includes company info.
export_data = {'title': 'FACTURA ELECTRÓNICA', 'num_doc_empresa': 'RUC: 20552103816',
               'serie_and_correlativo': 'F001-1', 'country_code': 'CA',
               'waybill_no': '9999 9999 9999', 'export_date': '12/20/2015', 'export_refs': '999432423, 14314321423',
               'export_country': 'USA', 'manufacture_country': 'CHINA',
               'destination_country': 'CANADA'}

importer_data = {'first_name': 'Real First Name',
                 'last_name': 'Real Last Name',
                 'postal_code': 'M5A 3C6', 'country_code': 'CA', 'state_code': 'ON',
                 'city': 'North York', 'address': '123 Import St.'}

exporter_data = {'first_name': 'Real First Name',
                 'last_name': 'Real Last Name',
                 'postal_code': 'M5A 3C6', 'country_code': 'CA', 'state_code': 'ON',
                 'city': 'North York', 'address': '123 Export St.'}

cosignee_data = {'first_name': 'Real First Name',
                 'last_name': 'Real Last Name',
                 'postal_code': 'M5A 3C6', 'country_code': 'CA', 'state_code': 'ON',
                 'city': 'North York', 'address': '123 Cosignee St.'}

product1 = {'marks_nos': '1234', 'no_packages': 1, 'package_type': 'BOX',
            'description': 'a description of the goods in a full and up to date way', 'quantity': 1,
            'measure_unit': 'lbs', 'weight': 25, 'unit_value': 23.24, 'total_value': 23.24}

product2 = {'marks_nos': '12', 'no_packages': 1, 'package_type': 'OWN_PACKAGING',
            'description': 'a description of the goods, another product to describe', 'quantity': 2,
            'measure_unit': 'lbs', 'weight': 5, 'unit_value': 43.44, 'total_value': 43.44}

data_products = [
    {
        "codigo": '4456545255',
        "cantidad": 2,
        "unidad_medida": "UNIDAD",
        "descripcion": "ROYAL 20321 COLOR VERDE",
        "precio_unitario": "120.00",
        "valor_venta": "120.00",
    },
    {
        "codigo": '4456545255',
        "cantidad": 3,
        "unidad_medida": "UNIDAD",
        "descripcion": "ROYAL 20321 COLOR VERDE",
        "precio_unitario": "120.00",
        "valor_venta": "120.00",
    },
    {
        "codigo": '4456545255',
        "cantidad": 3,
        "unidad_medida": "UNIDAD",
        "descripcion": "ROYAL 20321 COLOR VERDE",
        "precio_unitario": "120.00",
        "valor_venta": "120.00",
    },
    {
        "codigo": '4456545255',
        "cantidad": 3,
        "unidad_medida": "UNIDAD",
        "descripcion": "ROYAL 20321 COLOR VERDE",
        "precio_unitario": "120.00",
        "valor_venta": "120.00",
    }
]

flags = {'fob': True, 'caf': True, 'cif': False}

products = [product1, product2, product1, product2, product1, product2]

generate_commercial_invoice(export_data, exporter_data, cosignee_data, data_products, flags, importer_data)
