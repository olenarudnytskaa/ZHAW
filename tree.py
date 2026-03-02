"""
Context:
Disease classification codes (like ICD codes) can be structured in a hierarchical manner.

Exercise:
Read through this script and make yourself familiar with the tree.
The quiz will ask you about it (e.g., What is the direct parent of "COVID-19"? Answer: "Viral")
"""


class DiseaseNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def display(self, level=0):
        indent = "  " * level
        print(f"{indent}{self.name}")
        for child in self.children:
            child.display(level + 1)


if __name__ == "__main__":
    # Root node for all diseases
    root = DiseaseNode("Diseases")

    # First-level categories
    infectious = DiseaseNode("Infectious")
    non_infectious = DiseaseNode("Non-Infectious")
    root.add_child(infectious)
    root.add_child(non_infectious)

    # Second-level for Infectious diseases
    viral = DiseaseNode("Viral")
    bacterial = DiseaseNode("Bacterial")
    infectious.add_child(viral)
    infectious.add_child(bacterial)

    # Third-level for Viral diseases
    flu = DiseaseNode("Flu")
    covid = DiseaseNode("COVID-19")
    viral.add_child(flu)
    viral.add_child(covid)

    # Third-level for Bacterial diseases
    tuberculosis = DiseaseNode("Tuberculosis")
    strep_throat = DiseaseNode("Strep Throat")
    bacterial.add_child(tuberculosis)
    bacterial.add_child(strep_throat)

    # Second-level for Non-Infectious diseases
    genetic = DiseaseNode("Genetic")
    lifestyle = DiseaseNode("Lifestyle")
    non_infectious.add_child(genetic)
    non_infectious.add_child(lifestyle)

    # Third-level for Genetic diseases
    cystic_fibrosis = DiseaseNode("Cystic Fibrosis")
    hemophilia = DiseaseNode("Hemophilia")
    genetic.add_child(cystic_fibrosis)
    genetic.add_child(hemophilia)

    # Third-level for Lifestyle diseases
    diabetes = DiseaseNode("Diabetes")
    heart_disease = DiseaseNode("Heart Disease")
    lifestyle.add_child(diabetes)
    lifestyle.add_child(heart_disease)

    # Display the hierarchical tree
    root.display()