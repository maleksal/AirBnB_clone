#!/bin/bash
# Automating (PEP8, unittests, documentation) checks
# Execution: ./checker.sh

printf "\n\t======== Check PEP8 *.py ========\n\n"

pep8 $(find . -name "*.py")
printf "\n\t======== Check/Run Unittests ========\n"

python3 -m unittest discover tests
echo "[x] Run Doc tests:"

python3 <<END

import importlib

packages = [
    {"models": [{"base_model": ["BaseModel"]},]},
    {"models.engine": [{"file_storage": ["FileStorage"]},]}
    ]

print("\n\t======== Documentation CHECK ========\n")
for package in packages:
    for path, modules in package.items():
        for module in modules:
            for k, v in module.items():
                mod = importlib.import_module('{}.{}'.format(path, k))
                if mod:
                    print("[Found] - {} Module docs".format(k))
                else:
                    print("[Not Found] - {} Module docs".format(k))
                for m_class in v:
                    doc = eval("mod.{}.__doc__".format(m_class))
                    if doc:
                        print("[Found] - {} class docs".format(m_class))
                    else:
                        print("[Not foundFound] - {} class docs".format(m_class))
print()
END