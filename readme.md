# Tiny Docker learning series

In this tiny docker learning series, I'll be creating a web-based Flasked website that gets content from a database. It will start from a single Dockerfile and step into a Docker Compose case.
 
Step by step guide.
- 

### 0: First steps
Deploy a simple python Flask web server. 

<details>
  <summary>Resources</summary>

```bash
 - Dockerfile (1).
 ```
</details>


### 1: Keep moving
Deploy a tiny containerized MongoDB. (2)
<details>
  <summary>Resources</summary>

```bash
 - Dockerfile (1).
 - Volume (1).
 ```
</details>

### 2: Interacting
Connect to the DB from the web-home-page and interact using a Docker network.

<details>
  <summary>Resources</summary>

```bash
 - Dockerfile (2)
 - Network (1)
 - Volume (1).
 ```
</details>

### 3: Interacting
Idem 2 but using a Compose.

<details>
  <summary>Resources</summary>

```bash
 - Docker-compose (1)
 - Network (1)
 - Volume (1).
 ```
</details>

### 4: Interacting
Idem 3 but using a multiple environments.

<details>
  <summary>Resources</summary>

```bash
 - Docker-compose (1)
 - Network (1)
 - Volume (1).
 - Docker yaml env files (2)
 ```
</details>


