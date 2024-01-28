# Inżynieria Oprogramowania

Mock project for the Inżynieria Oprogramowania class. 

## Running the project

Docker is required. Run the following commands in the project root:

```bash
cp .env.example .env
docker-compose up -d
```  

Frontend should be available under localhost:8000, backend should be available under localhost:80.
The admin panel should be accessible at `/admin/` under the default credentials located in `.env`.
You can view the API docs under `/api/v1/docs` and `/api/v1/redoc`

## Local development

Modified files will be auto-reloaded when working on frontend or backend.

See respective backend and frontend directories' README for more detailed instructions.

### WSL2 and VS Code setup

Install npm and Python 3.10 on the host machine.
Run ```npm ci``` in the frontend directory - installed node-modules will enable linting in VS Code and remove Typescript errors.

Run ```pip install requirements-dev.txt``` in the backend directory - it will install black (a code formatter), pigar (a tool for generating requirements.txt), and pre-commit (a tool for pre-commit hooks). 

Install required extensions in VS Code (Python, Vue, Typescript, ...).

After installing the Python extension, enter Settings, set Black as the "python formatting provider", and enable "format on save".

Configure [Takeover Mode](https://vuejs.org/guide/typescript/overview.html#ide-support) in Volar for frontend editing.

Lastly, run ```pre-commit install``` in the root directory to install pre-commit hooks. 

Note: this setup isn't ideal, as it relies on the host machine. It could utilize dev containers VS Code functionality. 

## Deployment - building the frontend

First, set the env variable VITE_BACKEND_URL to an empty string, as after build frontend will run under the same URL as backend. 
Next, launch the frontend container and run:
```bash
su node
npm run build
```

Frontend builds to the backend dist directory (per vite.config.ts file).
Upon build, the website should be available under the localhost:80 backend URL.


### Style guide 

Commits should be in present-tense, imperative style.

## License

Project is licensed under the MIT License.


