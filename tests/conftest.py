import sys
import os

# Add /services to PYTHONPATH so we can import `api.app`
base_dir = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)  # points to project root
services_dir = os.path.join(base_dir, "services")
sys.path.insert(0, services_dir)
