import os
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL", "postgres://tyiwalhhfasfib:9137c297fceffb13aaf4d79b4c70ad426efc0ae0dd2a2344697ca999f7811c18@ec2-54-228-98-132.eu-west-1.compute.amazonaws.com:5432/d7esq77fgp12p0")
OWNER_ID = list({int(x) for x in os.environ.get("OWNER_ID", "").split()})
