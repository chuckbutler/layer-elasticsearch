from charms.reactive import when, when_not
from charms import ansible

from charms.reactive.bus import get_states

@when('ansible.available')
@when_not('elasticsearch.available')
def do_something():
    ansible.apply_playbook('playbook.yaml') 
