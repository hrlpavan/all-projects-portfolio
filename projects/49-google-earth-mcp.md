# Google Earth 3D Model Context Protocol (MCP) Server

[![Repository](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)](https://github.com/hrlpavan/google-earth-mcp)
[![GitLab Mirror](https://img.shields.io/badge/GitLab-Mirror-FC6D26?style=for-the-badge&logo=gitlab&logoColor=white)](https://gitlab.com/hrlpavan/google-earth-mcp)
[![Visibility](https://img.shields.io/badge/Visibility-Public-brightgreen?style=for-the-badge)](https://github.com/hrlpavan/google-earth-mcp)
[![Primary Language](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge)](https://github.com/hrlpavan/google-earth-mcp)
[![Created](https://img.shields.io/badge/Created-2026--09--23-informational?style=for-the-badge)](https://github.com/hrlpavan/google-earth-mcp)

> **Back to Index**: [Master Project Showcase](../README.md) | [Projects Catalog](README.md)

---

## Executive Summary
A lightweight geospatial MCP server empowering AI agents in Google Antigravity to control 3D satellite camera views, build KML orbital/surveillance tours, and resolve global coordinates.

## Repository Metadata
| Attribute | Specification |
| :--- | :--- |
| **Repository Name** | [`google-earth-mcp`](https://github.com/hrlpavan/google-earth-mcp) |
| **GitHub URL** | [https://github.com/hrlpavan/google-earth-mcp](https://github.com/hrlpavan/google-earth-mcp) |
| **GitLab Mirror URL** | [https://gitlab.com/hrlpavan/google-earth-mcp](https://gitlab.com/hrlpavan/google-earth-mcp) |
| **Architectural Domain** | `Geospatial Intelligence & Agentic AI` |
| **Primary Language** | `Python` |
| **Ecosystem Stack** | `Python 3.12`, `Model Context Protocol (MCP)`, `OpenGIS KML 2.2`, `Geospatial Math` |
| **Access Level** | `Public` |
| **Date Initiated** | `2026-09-23` |

---

## Core Capabilities & Engineering Highlights
- **Pure**: Pure standard-library JSON-RPC 2.0 stdio MCP server with sub-5ms cold startup
- **Generates**: Generates 3D Google Earth Web fly-to camera links with exact tilt, heading, and altitude
- **Synthesizes**: Synthesizes OpenGIS KML 2.2 tours (gx:Tour, gx:FlyTo) with 3D radar envelopes and flight paths
- **Bi-directional**: Bi-directional Decimal Degrees (DD) and Degrees Minutes Seconds (DMS) coordinate converter

---

## Architectural & System Design
The **Google Earth 3D Model Context Protocol (MCP) Server** initiative is engineered with high fidelity and strict performance constraints, forming an integral tier of the **HRL Ecosystem**. Key engineering vectors include:

1. **Modular Decoupling**: Interfaces designed to operate autonomously while exposing standardized RPC, CLI, or API contracts.
2. **Reliability & Validation**: Incorporates strict validation invariants to avoid state corruption or non-deterministic behavior.
3. **Dual-Platform Synchronization**: Maintained in lockstep across both GitHub and GitLab via HRL's automated dual-sync infrastructure.

---

## Tech Stack & Tooling
- **Primary Languages**: Python, KML / XML
- **Core Technologies**: `Python 3.12`, `Model Context Protocol (MCP)`, `OpenGIS KML 2.2`, `Geospatial Math`
- **Target Platforms**: macOS / Linux / Windows / Distributed Cloud

---

## Ecosystem Integration
This repository integrates seamlessly with the overarching **HRL Technology Suite**, providing robust infrastructure for autonomous intelligence, media automation, and enterprise computing.

For complete source code, documentation, and releases, visit:
- **GitHub**: **[https://github.com/hrlpavan/google-earth-mcp](https://github.com/hrlpavan/google-earth-mcp)**
- **GitLab**: **[https://gitlab.com/hrlpavan/google-earth-mcp](https://gitlab.com/hrlpavan/google-earth-mcp)**
