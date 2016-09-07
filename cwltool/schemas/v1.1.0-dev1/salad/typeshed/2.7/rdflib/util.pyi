# Stubs for rdflib.util (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

def list2set(seq): ...
def first(seq): ...
def uniq(sequence, strip=0): ...
def more_than(sequence, number): ...
def to_term(s, default=None): ...
def from_n3(s, default=None, backend=None): ...
def check_context(c): ...
def check_subject(s): ...
def check_predicate(p): ...
def check_object(o): ...
def check_statement(triple): ...
def check_pattern(triple): ...
def date_time(t=None, local_time_zone=False): ...
def parse_date_time(val): ...
def guess_format(fpath, fmap=None): ...
def find_roots(graph, prop, roots=None): ...
def get_tree(graph, root, prop, mapper=..., sortkey=None, done=None, dir=''): ...
