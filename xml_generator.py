from random import choice, randint
from common import *
import pandas as pd

NUMBER_OF_ENTRIES = 1


def generate_bacterium(id_) -> str:
    id_string = "<idBacterium>" + str(id_) + "</idBacterium>\n"
    morphology = "<Morphology>" + choice(MORPHOLOGIES) + "</Morphology>\n"
    year = "<Year>" + str(choice(YEARS)) + "</Year>\n"
    metabolism = "<MetabolismType>" + \
        choice(METABOLISM) + "</MetabolismType>\n"
    movement = "<MovementType>" + choice(MOVEMENT) + "</MovementType>\n"
    oxy_demand = "<OxygenDemand>" + choice(OXY_DEMAND) + "</OxygenDemand>\n"
    gram = "<GramStain>" + choice(GRAM) + "</GramStain>\n"

    taxonom = "<Taxonomy>" + generate_taxonomy() + "</Taxonomy>\n"
    diseases_tmp = ["<Disease>\n" + generate_disease() +
                    "</Disease>\n" for _ in range(randint(0, 3))]
    diseases = "<Diseases>\n" + ''.join(diseases_tmp) + "</Diseases>\n"

    genome = "<Genome>\n" + generate_genome(id_) + "</Genome>\n"

    xml_string = id_string + morphology + year + metabolism + \
        movement + oxy_demand + gram + taxonom + diseases + genome
    xml_string = f"<Bacterium>\n{xml_string}</Bacterium>"
    return xml_string


def generate_taxonomy() -> str:
    phylum = "<Phylum>" + choice(PHYLUM) + "</Phylum>\n"
    class_ = "<Class>" + choice(CLASS) + "</Class>\n"
    order = "<Order>" + choice(ORDER) + "</Order>\n"
    family = "<Family>" + choice(FAMILY) + "</Family>\n"
    genus = "<Genus>" + choice(GENUS) + "</Genus>\n"
    specie = "<Specie>" + \
        TAXONOM_SPECIES.pop(randint(0, len(TAXONOM_SPECIES))) + "</Specie>\n"

    xml_string = phylum + class_ + order + family + genus + specie
    return xml_string


def generate_disease() -> str:
    name = "<NameDisease>" + \
        choice(NAME_DISEASE).replace("'", "") + "</NameDisease>\n"
    symptoms = "<Symptoms>" + ', '.join([choice(SYMPTOMS).replace(
        ";", "").replace("'", "") for _ in range(randint(1, 8))]) + "</Symptoms>\n"
    cure = "<HasCure>" + choice(HAS_CURE) + "</HasCure>\n"
    desc = "<Description>Some description about the disease...</Description>\n"

    xml_statement = name + symptoms + cure + desc
    return xml_statement


def generate_genome(id_: int) -> str:
    id_ = "<idGenome>" + str(id_) + "</idGenome>\n"
    cat = "<Category>" + choice(CATEGORY) + "</Category>\n"

    genes_tmp = ["<Gene>\n" +
                 generate_gen(i) + "</Gene>\n" for i in range(randint(1, 2))]
    genes = "<Genes>" + ''.join(genes_tmp) + "</Genes>\n"

    xml_statement = id_ + cat + genes

    return xml_statement


def generate_gen(id_: int) -> str:
    id_ = "<idGen>" + str(id_) + "</idGen>\n"
    seq = "<Sequence>" + ''.join([choice(["A", "C", "G", "T"])
                                  for _ in range(randint(20, 100))]) + "</Sequence>\n"

    xml_statement = id_ + seq

    return xml_statement


def main():
    bacterium_xml = open("xml/data.xml", "w")
    bacterium_xml.write("<?xml version=1.0?>\n\n")
    bacterium_xml.write("<Bacteria>")

    for i in range(NUMBER_OF_ENTRIES):
        bacterium_xml.write(generate_bacterium(i))

    bacterium_xml.write("<Bacteria>")


if __name__ == "__main__":
    main()
