import json

from django.contrib.gis.geos import GEOSGeometry
from django.core.management.base import BaseCommand, CommandError

from ...infrastructure.models.place import LandUseGeometryModel


class Command(BaseCommand):
    help = "Importa geometrias de uso do solo a partir de um GeoJSON"

    def add_arguments(self, parser) -> None:
        parser.add_argument("--path", required=True, help="Caminho do arquivo .geojson")
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Apaga os registros atuais antes de importar",
        )

    def handle(self, *args, **options) -> None:
        path = options["path"]
        should_clear = options["clear"]

        try:
            with open(path, "r", encoding="utf-8") as f:
                content = json.load(f)
        except FileNotFoundError as exc:
            raise CommandError(f"Arquivo não encontrado: {path}") from exc
        except json.JSONDecodeError as exc:
            raise CommandError(f"GeoJSON inválido: {path}") from exc

        features = content.get("features", [])
        if not features:
            raise CommandError("GeoJSON sem features")

        if should_clear:
            LandUseGeometryModel.objects.all().delete()

        created = 0
        for feature in features:
            props = feature.get("properties", {})
            land_use_geometry = props.get("desc_uso_solo")
            geometry = feature.get("geometry")

            if not land_use_geometry or not geometry:
                continue

            geom = GEOSGeometry(json.dumps(geometry), srid=4326)
            LandUseGeometryModel.objects.create(
                land_use_geometry=land_use_geometry,
                geometry=geom,
            )
            creaetd += 1

        self.stdout.write(
            self.style.SUCCESS(f"Importação concluída. Registros criados: {created}")
        )
