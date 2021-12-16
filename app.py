from main import create_app, db
import os
from faker import Faker
from main.models import ClienteModel, EquipoModel, PartidoModel
import csv
from main.services.cuota import CuotaService
from main.map import CuotaSchema

cuota_schema = CuotaSchema()
service_cuota = CuotaService()

app = create_app()

app.app_context().push()

fake = Faker('es_ES')


def load_clientes():
    for _ in range(100):
        cliente = ClienteModel(nombre=fake.first_name(), apellido=fake.last_name(), email=fake.email())
        db.session.add(cliente)
        db.session.commit()
    db.session.close()


def load_equipos():
    with open('./docs/equipo.csv', encoding='utf-8') as csv_file:
        try:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                equipo = EquipoModel(nombre=row[0], escudo=row[1], pais=row[2], puntaje=float(row[3]))
                db.session.add(equipo)
                db.session.commit()
            db.session.close()
        except:
            db.session.rollback()


def load_partidos():
    formato = "%d/%m/%Y %H:%M"
    with open('./docs/partidos.csv', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            partido = PartidoModel(equipo_local_id=row[1], equipo_visitante_id=row[2])
            db.session.add(partido)
            db.session.commit()


def load_cuotas():
    partidos = db.session.query(PartidoModel).all()
    for partido in partidos:
        json = {
            "partido_id": partido.id
        }
        cuota = cuota_schema.load(json)
        service_cuota.aplicar_cuotas(cuota)
        db.session.add(cuota)
        db.session.commit()


if __name__ == '__main__':
    db.create_all()
    app.run(port=os.getenv("PORT"), debug=True)
