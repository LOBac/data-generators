from common import *
from random import choice, randint
import json
import os

NUMBER_OF_ENTRIES = 1000
OUTPUT_DIR = "data/json"


def generate_bacteria(id_):
    bacterium = {}
    bacterium["BacteriumID"] = id_
    bacterium["Morphology"] = f"{choice(MORPHOLOGIES)}"
    bacterium["Year"] = choice(YEARS)
    bacterium["MetabolismType"] = f"{choice(METABOLISM)}"
    bacterium["MovementType"] = f"{choice(MOVEMENT)}"
    bacterium["OxygenDemand"] = f"{choice(OXY_DEMAND)}"
    bacterium["GramStain"] = choice([True, False])
    bacterium["Taxonomy"] = generate_taxonomy()
    bacterium["Diseases"] = [generate_disease() for _ in range(0, 2)]
    bacterium["Genome"] = generate_genome(id_)

    return bacterium


def generate_taxonomy():
    taxonomy = {}
    taxonomy["Phylum"] = choice(PHYLUM)
    taxonomy["Class"] = choice(CLASS)
    taxonomy["Order"] = choice(ORDER)
    taxonomy["Family"] = choice(FAMILY)
    taxonomy["Genus"] = choice(GENUS)
    taxonomy["Specie"] = TAXONOM_SPECIES.pop(
        randint(0, len(TAXONOM_SPECIES)))

    return taxonomy


def generate_disease():
    disease = {}
    disease["NameDisease"] = choice(NAME_DISEASE)
    disease["Symptoms"] = [choice(SYMPTOMS) for _ in range(randint(0, 8))]
    disease["HasCure"] = choice([True, False])
    disease["Description"] = "Some description about the disease..."

    return disease


def generate_genome(id_):
    genome = {}
    genome["idGenome"] = id_
    genome["Category"] = choice(CATEGORY)
    genome["Genes"] = [generate_gene(i) for i in range(randint(1, 3))]

    return genome


def generate_gene(id_):
    gene = {}
    gene["idGene"] = id_
    gene["Sequence"] = ''.join([choice(["A", "C", "G", "T"])
                               for _ in range(randint(20, 100))])

    return gene


def main(requested_items):
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    with open(f"{OUTPUT_DIR}/data.json", "w") as js:
        for i in range(requested_items):
            json.dump(generate_bacteria(i), js)
            js.write("\n")


if __name__ == "__main__":
    main(NUMBER_OF_ENTRIES)
