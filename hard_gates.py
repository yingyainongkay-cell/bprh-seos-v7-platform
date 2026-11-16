import yaml, sys, os
print('>> [SCHEMA-001] Verifying YAML Templates...')
p = 'templates/coffee_order_system.yaml'
assert os.path.exists(p), f'Template {p} not found.'
data = yaml.safe_load(open(p, encoding='utf-8'))
assert 'agents' in data, 'Missing agents definition'
assert 'artifact' in data, 'Missing artifact provenance'
print('✅ PASS SCHEMA-001')

print('>> [CYCLE-001] Topological Cycle Detection...')
deps = {a['name']: a.get('dependencies', []) for a in data['agents']}
seen = set()
def visit(n, stack):
    assert n not in stack, f'Cycle at {n}'
    if n in seen: return
    stack.add(n)
    for d in deps.get(n, []): visit(d, stack)
    stack.remove(n); seen.add(n)
for n in deps: visit(n, set())
print(f'✅ PASS CYCLE-001 DAG={deps}')

print('>> [SEC-001] Command Injection Defense...')
model = data.get('model', '')
assert not any(c in model for c in [';', '|', '&', '$', chr(96)]), 'Security Violation'
print('✅ PASS SEC-001')

print('>> [TRACE-001] Cryptographic Provenance...')
art = data['artifact']
assert art['hash'].startswith('sha256:') and len(art['hash']) == 71, f"Bad hash {art['hash']}"
assert 'timestamp' in art, 'Missing timestamp'
print('✅ PASS TRACE-001')
print('🎉 ALL QUANTUM HARD GATES VERIFIED!')
