# Word-length case study

Curated from the `longest-word` exercise that lived inside the old `fraud-detection-apps`/`pybox` sandbox.

The original exercise mixed domain logic, FastAPI transport code and state in one module. This version keeps the durable lesson—the parsing and longest/shortest-word logic—as a dependency-free functional core with tests.

## Lessons retained

- normalise external text before analysis
- return structured results rather than sentinel strings
- separate pure domain logic from HTTP/framework concerns
- test ties, empty input and numeric tokens explicitly

If this is exposed through FastAPI later, the API layer should adapt HTTP requests to these functions rather than own the text-processing state.
