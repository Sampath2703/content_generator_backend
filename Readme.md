# 🚀 AI Content Generator (Full Stack AI SaaS Project)

An AI-powered content generation platform built using **Streamlit, FastAPI, and Groq LLaMA 3.3 70B**.  
This project generates high-quality, structured, and contextual content for multiple platforms like LinkedIn, Instagram, Blogs, Emails, and more.

---

# 📌 Project Overview

The AI Content Generator is a full-stack application that allows users to generate professional content instantly using AI.

It takes user inputs such as:

- Topic
- Technology
- Content Type
- Tone

and returns **well-structured AI-generated content** using Groq's LLaMA 3 model.

---

# 🎯 Key Features

## 🧠 AI-Powered Generation
- Uses **Groq LLaMA 3.3 70B model**
- Produces human-like, structured content
- Context-aware generation

## 🎨 Multi-Format Content Support
- LinkedIn Posts
- Blog Articles
- Instagram Captions
- Twitter/X Posts
- Email Drafts
- YouTube Descriptions

## ⚙️ Customization Options
- Select Technology (AI, Python, React, etc.)
- Choose Tone (Professional, Casual, Marketing, Friendly)
- Choose Content Type

## ⚡ Fast & Lightweight
- FastAPI backend for high performance
- Minimal latency AI responses

## 🖥️ Interactive UI
- Built using Streamlit
- Simple and user-friendly interface
- Real-time generation with loading spinner

---

# 🏗️ System Architecture

```text
                    ┌──────────────────────┐
                    │   Streamlit UI       │
                    │  (Frontend Layer)    │
                    └─────────┬────────────┘
                              │ HTTP Request
                              ▼
                    ┌──────────────────────┐
                    │   FastAPI Backend    │
                    │  (API Layer)         │
                    └─────────┬────────────┘
                              │ Prompt
                              ▼
                    ┌──────────────────────┐
                    │  Groq LLM (LLaMA 3)  │
                    │  AI Model Layer      │
                    └─────────┬────────────┘
                              │ Response
                              ▼
                    ┌──────────────────────┐
                    │   JSON Output        │
                    └──────────────────────┘