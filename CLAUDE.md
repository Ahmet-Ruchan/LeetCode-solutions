# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

A personal learning repository for CS50 content and LeetCode algorithm practice, using **C** and **Python**.

## Structure

- `C Programming/` — C exercises organized by lecture (e.g., `Lecture-1/main.c`)
- `LeetCode Solutions/With Python/` — LeetCode problems, one subdirectory per problem, each with a `main.py` or similarly named `.py` file

## Building and Running C Programs

The project uses **clang** on macOS (Apple Silicon / arm64).

Compile a C file:
```bash
clang -o output/<name> "C Programming/<Lecture-N>/main.c"
```

Or compile with debug info:
```bash
clang -g -o output/<name> "C Programming/<Lecture-N>/main.c"
```

Run the compiled binary:
```bash
./output/<name>
```

## Running Python Solutions

Each LeetCode solution is a standalone script with test input hardcoded at the top:
```bash
python3 "LeetCode Solutions/With Python/<Problem Name>/main.py"
```

## Conventions

- C files follow the pattern `C Programming/<Lecture-N>/main.c`
- Python LeetCode solutions define a function and call it at the bottom of the file with a hardcoded test case
- Compiled C binaries and `.dSYM` debug bundles go in an `output/` directory (already in use at both root and lecture-level)
