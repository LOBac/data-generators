from common import *
from random import choice, randint
from typing import Tuple
import os

NUMBER_OF_ENTRIES = 1
OUTPUT_DIR = "data/sql"


def generate_bacterium() -> Tuple[str, str]:
    """generate_insert generates a single one random SQL INSERT statement like
    the following one:

        INSERT INTO `bacterium`.`Bacterium`
        (`Morphology`, `YearOfDiscovery`, `TypeMetabolism`, `Movement`, `OxygenDemand`, `GramStain`, `Taxonomy_Species`)
        VALUES ('A', '0000', 'B', 'C', 'Aerobic', '1', 'D');


    Returns:
        str: INSERT statement
    """
    morphology = choice(MORPHOLOGIES)
    year = choice(YEARS)
    metabolism = choice(METABOLISM)
    movement = choice(MOVEMENT)
    oxy_demand = choice(OXY_DEMAND)
    gram = choice(GRAM)
    taxonom = TAXONOM_SPECIES.pop(randint(0, len(TAXONOM_SPECIES)))
    taxonom = taxonom.replace('\'', '')[0:150]

    statement = f"INSERT INTO `bacterium`.`Bacterium` (`Morphology`, `YearOfDiscovery`, `TypeMetabolism`, `Movement`, `OxygenDemand`, `GramStain`, `Taxonomy_Species`) " +\
        f"VALUES ('{morphology}','{year}','{metabolism}','{movement}','{oxy_demand}','{gram}','{taxonom}');"

    return (statement, taxonom)


def generate_taxonomy(specie: str) -> str:
    phylum = choice(PHYLUM)
    class_ = choice(CLASS)
    order = choice(ORDER)
    family = choice(FAMILY)
    genus = choice(GENUS)

    return f"INSERT INTO `bacterium`.`Taxonomy` (`Phylum`, `Class`, `Order`, `Family`, `Genus`, `Species`) " +\
        f"VALUES ('{phylum}','{class_}','{order}','{family}','{genus}','{specie}');"


def generate_disease(specie: str, id_: int) -> str:
    name = specie + " " + choice(NAME_DISEASE).replace("'", "")
    symptoms = ', '.join([choice(SYMPTOMS).replace(
        ";", "").replace("'", "") for _ in range(randint(1, 8))])
    cure = choice(HAS_CURE)
    desc = f"Some description about the {name} disease caused by {specie}..."

    return f"INSERT INTO `bacterium`.`Disease` (`NameDisease`, `Symptoms`, `HasCure`, `Description`, `Bacterium_idBacterium`) " +\
        f"VALUES ('{name}', '{symptoms}', '{cure}', '{desc}', '{id_}');"


def generate_genome(id_: int) -> str:
    cat = choice(CATEGORY)
    return f"INSERT INTO `bacterium`.`Genome` (`Category`, `Bacterium_idBacterium`) " +\
        f"VALUES ('{cat}', '{id_}');"


def generate_gen(id_genome: int, id_gen: int) -> str:
    seq = ''.join([choice(["A", "C", "G", "T"])
                  for _ in range(randint(20, 100))])
    return f"INSERT INTO `bacterium`.`Gen` (`Secuence`, `Genome_idGenome1`) " +\
        f"VALUES ('{seq}', '{id_genome}');"


def main(requested_items):
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    bacterium_sql = open(f"{OUTPUT_DIR}/bacterium_table.sql", "w")
    taxonomy_sql = open(f"{OUTPUT_DIR}/taxonomy_table.sql", "w")
    disease_sql = open(f"{OUTPUT_DIR}/disease_table.sql", "w")
    genome_sql = open(f"{OUTPUT_DIR}/genome_table.sql", "w")
    gen_sql = open(f"{OUTPUT_DIR}/gen_table.sql", "w")

    for i in range(requested_items):
        bac, specie = generate_bacterium()
        bacterium_sql.write(bac + "\n")
        taxonomy_sql.write(generate_taxonomy(specie) + "\n")
        if randint(0, 1):
            disease_sql.write(generate_disease(specie, i) + "\n")
        genome_sql.write(generate_genome(i) + "\n")
        for j in range(randint(1, 2)):
            gen_sql.write(generate_gen(i, j) + "\n")


if __name__ == "__main__":
    main(NUMBER_OF_ENTRIES)
