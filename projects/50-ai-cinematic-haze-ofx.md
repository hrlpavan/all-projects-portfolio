# AI Cinematic Haze — OpenFX & Fusion Plugin for DaVinci Resolve

[![Repository](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)](https://github.com/hrlpavan/ai-cinematic-haze-ofx)
[![GitLab Mirror](https://img.shields.io/badge/GitLab-Mirror-FC6D26?style=for-the-badge&logo=gitlab&logoColor=white)](https://gitlab.com/hrlpavan/ai-cinematic-haze-ofx)
[![Visibility](https://img.shields.io/badge/Visibility-Public-brightgreen?style=for-the-badge)](https://github.com/hrlpavan/ai-cinematic-haze-ofx)
[![Primary Language](https://img.shields.io/badge/Language-C++%20%2F%20Metal%20%2F%20CUDA-blue?style=for-the-badge)](https://github.com/hrlpavan/ai-cinematic-haze-ofx)
[![Created](https://img.shields.io/badge/Created-2026--09--18-informational?style=for-the-badge)](https://github.com/hrlpavan/ai-cinematic-haze-ofx)

> **Back to Index**: [Master Project Showcase](../README.md) | [Projects Catalog](README.md)

---

## Executive Summary
A studio-grade volumetric depth haze and optical halation plugin for DaVinci Resolve, executing locally on Apple Silicon and NVIDIA RTX GPUs with zero cloud latency.

## Repository Metadata
| Attribute | Specification |
| :--- | :--- |
| **Repository Name** | [`ai-cinematic-haze-ofx`](https://github.com/hrlpavan/ai-cinematic-haze-ofx) |
| **GitHub URL** | [https://github.com/hrlpavan/ai-cinematic-haze-ofx](https://github.com/hrlpavan/ai-cinematic-haze-ofx) |
| **GitLab Mirror URL** | [https://gitlab.com/hrlpavan/ai-cinematic-haze-ofx](https://gitlab.com/hrlpavan/ai-cinematic-haze-ofx) |
| **Architectural Domain** | `Creative Tools & GPU Shaders` |
| **Primary Language** | `C++ / Metal / CUDA` |
| **Ecosystem Stack** | `C++20`, `OpenFX API`, `Apple Metal`, `NVIDIA CUDA`, `DaVinci Resolve Fusion` |
| **Access Level** | `Public` |
| **Date Initiated** | `2026-09-18` |

---

## Core Capabilities & Engineering Highlights
- **Physically**: Physically based Beer-Lambert atmospheric scattering and lens-centric depth estimation
- **Hardware-accelerated**: Hardware-accelerated Apple Metal (MSL) and NVIDIA CUDA kernels for real-time 4K60 playback
- **ACEScc**: ACEScc and DaVinci Wide Gamut color-space preserving optical halation
- **Includes**: Includes both native C++ OpenFX bundle and cross-platform Fusion .fuse shader

---

## Architectural & System Design
The **AI Cinematic Haze — OpenFX & Fusion Plugin for DaVinci Resolve** initiative is engineered with high fidelity and strict performance constraints, forming an integral tier of the **HRL Ecosystem**. Key engineering vectors include:

1. **Modular Decoupling**: Interfaces designed to operate autonomously while exposing standardized RPC, CLI, or API contracts.
2. **Reliability & Validation**: Incorporates strict validation invariants to avoid state corruption or non-deterministic behavior.
3. **Dual-Platform Synchronization**: Maintained in lockstep across both GitHub and GitLab via HRL's automated dual-sync infrastructure.

---

## Tech Stack & Tooling
- **Primary Languages**: C++, Metal, CUDA, Lua, CMake
- **Core Technologies**: `C++20`, `OpenFX API`, `Apple Metal`, `NVIDIA CUDA`, `DaVinci Resolve Fusion`
- **Target Platforms**: macOS / Linux / Windows / Distributed Cloud

---

## Ecosystem Integration
This repository integrates seamlessly with the overarching **HRL Technology Suite**, providing robust infrastructure for autonomous intelligence, media automation, and enterprise computing.

For complete source code, documentation, and releases, visit:
- **GitHub**: **[https://github.com/hrlpavan/ai-cinematic-haze-ofx](https://github.com/hrlpavan/ai-cinematic-haze-ofx)**
- **GitLab**: **[https://gitlab.com/hrlpavan/ai-cinematic-haze-ofx](https://gitlab.com/hrlpavan/ai-cinematic-haze-ofx)**
