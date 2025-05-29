# Cookbook API

A RESTful API for managing cooking recipes, built with Django and Django REST Framework.

## Features

- Create, read, update recipes
- Search and filter recipes
- Pagination support
- Docker support for easy deployment

## Prerequisites

- Docker
- Docker Compose

## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/yourusername/cookbook.git
cd cookbook
```

2. Start the application:
```bash
./run up
```

3. Run migrations:
```bash
./run migrate
```

## API Endpoints

### Recipes

- List/Create recipes:
  ```bash
  # List all recipes
  GET /masterdata/recipies/
  
  # Create a new recipe
  POST /masterdata/recipies/
  ```

- Get/Update a specific recipe:
  ```bash
  # Get a specific recipe
  GET /masterdata/recipies/1/
  
  # Update a recipe
  PATCH /masterdata/recipies/1/
  ```

### Search and Filter

The API supports searching and filtering recipes:

- Search by name, description, ingredients, or instructions:
  ```bash
  GET /masterdata/recipies/?search=chicken
  ```

- Order by any field:
  ```bash
  GET /masterdata/recipies/?ordering=name
  GET /masterdata/recipies/?ordering=-created_at
  ```

## Development

### Available Commands

- Start the application:
  ```bash
  ./run up
  ```

- Stop the application:
  ```bash
  ./run down
  ```

- View logs:
  ```bash
  ./run logs
  ```

- Run migrations:
  ```bash
  ./run migrate
  ```

- Create migrations:
  ```bash
  ./run makemigrations
  ```

- Run tests:
  ```bash
  ./run test
  ```

- Open Django shell:
  ```bash
  ./run shell
  ```

## Project Structure

```
cookbook/
├── cookbook/          # Project settings
├── masterdata/        # Recipe management app
├── profiles/          # User profiles app
├── utils/            # Utility functions and models
├── docker-compose.yml # Docker configuration
└── run               # Development script
```

## License

This project is licensed under the MIT License - see the LICENSE file for details. 