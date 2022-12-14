# Typing practice in Python through game

This is a practice for type hints in Python by making a simple game.

## Packages - Thinking In Layers

The whole idea behind creating packages is to divide the application into logical sub-components.
These sub-components can be grouped by their type of functionality.

### Layers for our game application

| Sr No | Layer Name     | Particular                   | Visibility | Role      |
| ----- | -------------- | ---------------------------- | ---------- | --------- |
| 1     | Data Layer     | Package `models` & `schemas` | Private    | Internal  |
| 2     | Business Logic | `impl.py`                    | Private    | Internal  |
| 3     | API            | Package `game`               | Public     | Interface |
| 4     | Client         | `main.py`                    |            | Consumer  |
