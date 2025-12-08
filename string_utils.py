def split_before_each_uppercases(molecule):
  if len(molecule) == 0:
    return []
  else:
    split_formula = []
    start = 0
    end = 1

    for char in molecule[1:]:
      if char.isupper():
        split_formula.append(molecule[start:end])
        start = end
      end += 1

    split_formula.append(molecule[start:])
    return split_formula


def split_at_digit(atoms):
  digit_location = 1
  for char in atoms[1:]:
    if char.isdigit():
      break
    digit_location += 1

  if digit_location == len(atoms):
    return atoms, 1
  else:
    prefix = atoms[:digit_location]
    numbers_part = atoms[digit_location:]
    return prefix, int(numbers_part)



def count_atoms_in_molecule(molecule):
    """Takes a molecular formula (string) and returns a dictionary of atom counts.
    Example: 'H2O' → {'H': 2, 'O': 1}"""

    # Step 1: Initialize an empty dictionary to store atom counts
    formula_dic = {}

    for atoms in split_before_each_uppercases(molecule):
        atom_name, atom_count = split_at_digit(atoms)

        # Step 2: Update the dictionary with the atom name and count
        formula_dic[atom_name] = atom_count

    # Step 3: Return the completed dictionary
    return formula_dic



def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
