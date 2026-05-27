# Get Started

***

## Cloud

Self-hosting requires more technical skill to setup instance, backing up database and maintaning updates. If you aren't experienced at managing servers and just want to use the webapp, we recommend using [SamaFlow Cloud](https://cloud.flowiseai.com).

## Quick Start

{% hint style="info" %}
Pre-requisite: ensure [NodeJS](https://nodejs.org/en/download) is installed on machine. Node `v18.15.0` or `v20` and above is supported.
{% endhint %}

Install SamaFlow locally using NPM.

1. Install SamaFlow:

```bash
npm install -g samaflow
```

You can also install a specific version. Refer to available [versions](https://www.npmjs.com/package/samaflow?activeTab=versions).

```
npm install -g samaflow@x.x.x
```

2. Start SamaFlow:

```bash
npx samaflow start
```

3. Open: [http://localhost:3000](http://localhost:3000)

***

## Docker

There are two ways to deploy SamaFlow with Docker. First, git clone the project: [https://github.com/SamaFlow/SamaFlow](https://github.com/SamaFlow/SamaFlow)

### Docker Compose

1. Go to `docker folder` at the root of the project
2. Copy the `.env.example` file and paste it as another file named `.env`
3. Run:

```bash
docker compose up -d
```

4. Open: [http://localhost:3000](http://localhost:3000)
5. You can bring the containers down by running:

```bash
docker compose stop
```

### Docker Image

1. Build the image:

```bash
docker build --no-cache -t samaflow .
```

2. Run image:

```bash
docker run -d --name samaflow -p 3000:3000 samaflow
```

3. Stop image:

```bash
docker stop samaflow
```

***

## For Developers

SamaFlow has 4 different modules in a single mono repository:

* **Server**: Node backend to serve API logics
* **UI**: React frontend
* **Components**: Integration components
* **Api Documentation**: Swagger spec for SamaFlow APIs

### Prerequisite

Install [PNPM](https://pnpm.io/installation).

```bash
npm i -g pnpm
```

### Setup 1

Simple setup using PNPM:

1. Clone the repository

```bash
git clone https://github.com/SamaFlow/SamaFlow.git
```

2. Go into repository folder

```bash
cd SamaFlow
```

3. Install all dependencies of all modules:

```bash
pnpm install
```

4. Build the code:

```bash
pnpm build
```

Start the app at [http://localhost:3000](http://localhost:3000)

```bash
pnpm start
```

### Setup 2

Step-by-step setup for project contributors:

1. Fork the official [SamaFlow Github Repository](https://github.com/SamaFlow/SamaFlow)
2. Clone your forked repository
3. Create a new branch, see [guide](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-and-deleting-branches-within-your-repository). Naming conventions:
   * For feature branch: `feature/<Your New Feature>`
   * For bug fix branch: `bugfix/<Your New Bugfix>`.
4. Switch to the branch you just created
5. Go into repository folder:

```bash
cd SamaFlow
```

6. Install all dependencies of all modules:

```bash
pnpm install
```

7. Build the code:

```bash
pnpm build
```

8. Start the app at [http://localhost:3000](http://localhost:3000)

```bash
pnpm start
```

9. For development build:

* Create `.env` file and specify the `PORT` (refer to `.env.example`) in `packages/ui`
* Create `.env` file and specify the `PORT` (refer to `.env.example`) in `packages/server`

```bash
pnpm dev
```

* Any changes made in `packages/ui` or `packages/server` will be reflected at [http://localhost:8080](http://localhost:8080/)
* For changes made in `packages/components`, you will need to build again to pickup the changes
*   After making all the changes, run:

    ```bash
    pnpm build
    ```

    and

    ```bash
    pnpm start
    ```

    to make sure everything works fine in production.

***

## For Enterprise

Before starting the app, enterprise users are required to fill in the values for Enterprise Parameters in the `.env` file. Refer to `.env.example` for the required changes.

Reach out to support@flowiseai.com for the value of following env variables:

```
LICENSE_URL
FLOWISE_EE_LICENSE_KEY
```

***

## Learn More

In this video tutorial, Leon provides an introduction to SamaFlow and explains how to set it up on your local machine.

{% embed url="https://youtu.be/nqAK_L66sIQ" %}

## Community Guide

* [Introduction to \[Practical\] Building LLM Applications with SamaFlow / LangChain](https://volcano-ice-cd6.notion.site/Introduction-to-Practical-Building-LLM-Applications-with-SamaFlow-LangChain-03d6d75bfd20495d96dfdae964bea5a5)
* [SamaFlow / LangChainによるLLMアプリケーション構築\[実践\]入門](https://volcano-ice-cd6.notion.site/SamaFlow-LangChain-LLM-e106bb0f7e2241379aad8fa428ee064a)
