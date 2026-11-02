# 9. Troubleshooting

* [9.1 First-time self-check](9.4-first-time-self-check.md)
* [9.2 Software issues](9.2-software.md)
* [9.3 Hardware issues](9.3-hardware.md)
* [9.0 Others](9.0-other.md)

## Fastest way to localise a fault

Work outwards from the PC. Each step isolates one link:

| # | Check | Passing means |
|---|---|---|
| 1 | `arduino-cli board list` shows the R4 | USB cable and enumeration are fine |
| 2 | `fe fe 02 c1 fa` -> `fe fe 03 c1 18 fa` | firmware runs; USB data path works |
| 3 | `mc.get_basic_version()` -> `2.4` | pymycobot is talking to the R4 |
| 4 | `mc.get_system_version()` -> a number | the **arm link** works |
| 5 | `mc.get_angles()` -> 6 values | everything works |

Step 2 needs no arm and no arm power — the R4 answers it itself. If steps 1-3
pass but step 4 fails, the fault is strictly between the R4 and the arm:
wiring, arm power, or the connector.
