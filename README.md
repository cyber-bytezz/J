# Cody Frontend Developer Guide
**April 12, 2025**

## Table of Contents

1. [Introduction](#1-introduction)
2. [Project Overview](#2-project-overview)
3. [Getting Started](#3-getting-started)
4. [Codebase Structure](#4-codebase-structure)
5. [Architecture](#5-architecture)
6. [Key Frontend Components](#6-key-frontend-components)
7. [UI/UX Architecture](#7-uiux-architecture)
8. [AI Integration Points](#8-ai-integration-points)
9. [Memory System](#9-memory-system)
10. [Quantum-Enhanced Features](#10-quantum-enhanced-features)
11. [Development Workflow](#11-development-workflow)
12. [Testing](#12-testing)
13. [Common Development Tasks](#13-common-development-tasks)
14. [Troubleshooting](#14-troubleshooting)
15. [Glossary](#15-glossary)
16. [API Reference](#16-api-reference)

## 1. Introduction

This documentation serves as a comprehensive guide for frontend developers working on the Cody project. Cody is an AI-powered development assistant that combines deep IDE integration, multi-model AI, persistent memory, and enterprise security.

As a frontend developer, you'll be working on a custom VS Code fork with integrated AI capabilities that aims to compete with and surpass tools like Windsurf and GitHub Copilot. This guide will help you understand the codebase structure, development workflow, and key components.

### 1.1 Why Cody?

Cody differentiates itself from other AI coding assistants through:

- **Custom VS Code Fork**: Complete control over the editor experience rather than being limited to extension APIs
- **Multi-Model AI Support**: Integration with Anthropic, OpenAI, Google, DeepSeek, and custom models
- **Memory Persistence**: AI retains context across sessions and projects
- **Quantum-Enhanced Features**: Advanced semantic search and reasoning using quantum computing techniques
- **Self-Hosting & Privacy**: Fully on-premise deployment option for enterprise security

### 1.2 Target Audience

This guide is primarily for frontend developers working on:
- VS Code UI modifications
- Custom editor features
- AI-integrated UI components
- WebView panels and extensions
- Frontend API integrations

## 2. Project Overview

### 2.1 Product Vision

Cody is an **AI-powered development assistant** designed to compete with **Codeium and Windsurf**, providing deep IDE integration, multi-modal AI assistance, self-hosted enterprise capabilities, and persistent AI context memory. Built on a **custom VS Code fork**, Cody enables seamless AI workflows, offline capabilities, and repo-wide intelligence.

### 2.2 Core Capabilities

| Feature | Description | Implementation Status |
|---------|-------------|----------------------|
| Autocomplete | Multi-line, intent-aware, FIM completions | Complete |
| AI Chat | Multi-turn agentic chat with memory | Complete |
| Command-Based Edits | Natural language-driven code edits | Complete |
| Code Search | AI-assisted semantic search | In Progress (15%) |
| Unit Test Generation | Auto unit test generation | Complete |
| AI-Based Debugging | AI-assisted error fixing | Complete |
| Multi-File Context | Repo-wide AI indexing | In Progress (15%) |
| Memory Persistence | AI context across sessions | In Progress (70%) |
| Quantum Features | Enhanced semantic search | Early Stages (5%) |

### 2.3 Current Development Status

As of April 12, 2025, Cody is in Sprint 3-4 of a 10-sprint development plan:

- **Completed**: Core editor integration, AI model orchestration, basic memory APIs
- **In Progress**: Memory UI, refactoring service, repo indexing
- **Upcoming**: GitHub integration, semantic search, quantum features

## 3. Getting Started

### 3.1 Prerequisites

- Node.js v20.x (VS Code build requirement)
- Python 3.11 (for backend services)
- Git
- Docker and Docker Compose

### 3.2 Installation

```bash
# Clone the repository
git clone https://github.com/urbantech/cody.git
cd cody

# Install dependencies
npm install

# Set up VS Code development environment
cd src/vscode
npm install

# Start backend services
docker-compose up -d postgres redis rabbitmq

# Initialize database schema
cd src/backend
python -m app.utils.initialize_db

# Build VS Code fork
cd src/vscode
npm run compile

# Start the application
npm run start
```

### 3.3 Environment Setup

Copy the example environment file:

```bash
cp .env.example .env
```

Configure the environment variables in `.env`:

```
# Database Configuration for Local Development
DB_USER=cody
DB_PASSWORD=cody
DB_NAME=cody
DB_HOST=localhost
DB_PORT=5432

# Redis Configuration
REDIS_HOST=localhost
REDIS_PORT=6380

# API Configuration
API_BASE_URL=http://localhost:8000
API_HEALTH_ENDPOINT=/api/v1/health
API_USE_AUTH=false
```

## 4. Codebase Structure

The Cody codebase is organized into several key directories:

```
cody/
├── src/                           # Main source code
│   ├── vscode/                    # VS Code fork (main frontend)
│   │   ├── src/                   # Core VS Code source
│   │   │   ├── vs/                # VS Code modules
│   │   │   ├── main.ts            # Main Electron entry
│   │   │   └── bootstrap-*.ts     # Initialization files
│   │   ├── extensions/            # VS Code extensions
│   │   │   ├── cody/              # Cody-specific extension
│   │   │   │   ├── src/           # Extension source
│   │   │   │   │   ├── api/       # Backend API clients
│   │   │   │   │   ├── commands/  # Command handlers
│   │   │   │   │   ├── models/    # Data models
│   │   │   │   │   ├── views/     # UI components
│   │   │   │   │   └── extension.ts # Main extension entry
│   │   ├── resources/             # UI assets
│   │   └── product.json           # Product config
│   ├── backend/                   # Python backend services
│   │   ├── app/                   # Main application
│   │   │   ├── api/               # API endpoints
│   │   │   ├── services/          # Business logic
│   │   │   └── tests/             # BDD tests
│   └── ai_core/                   # AI model orchestration
├── docs/                          # Documentation
├── tests/                         # Integration tests
└── scripts/                       # Utility scripts
```

## 5. Architecture

### 5.1 Frontend Architecture

Cody's frontend architecture consists of:

1. **Electron Application**
   - VS Code shell customized for Cody
   - Main process manages lifecycle and services
   - Renderer process handles UI

2. **VS Code Core**
   - Monaco Editor for text editing
   - Command system for extensions
   - UI components and layouts

3. **Cody Extension**
   - Integrates with VS Code API
   - Communicates with backend services
   - Provides custom UI webviews

4. **WebViews**
   - Chat interface
   - Memory management
   - Refactoring suggestions
   - Custom panels

### 5.2 Backend Architecture

The backend consists of Python microservices:

1. **API Gateway**
   - FastAPI-based HTTP/WebSocket server
   - Authentication and routing
   - Request/response handling

2. **AI Model Orchestration**
   - Model registry and capability routing
   - Request transformation and caching
   - Async model communication

3. **Memory Service**
   - Persistent AI context
   - Search and retrieval
   - Priority management

4. **Other Services**
   - Error analysis
   - Refactoring
   - Repository indexing
   - Quantum bridge

### 5.3 Data Flow

```
┌─────────────┐     ┌───────────────┐     ┌─────────────────┐
│ VS Code UI  │────▶│ Cody Extension│────▶│ API Gateway     │
└─────────────┘     └───────────────┘     └─────────────────┘
      ▲                                             │
      │                                             ▼
┌─────────────┐     ┌───────────────┐     ┌─────────────────┐
│ WebViews    │◀───▶│ Frontend API  │◀───▶│ Microservices   │
└─────────────┘     └───────────────┘     └─────────────────┘
                                                   │
                                                   ▼
                                           ┌─────────────────┐
                                           │ AI Models       │
                                           └─────────────────┘
```

## 6. Key Frontend Components

### 6.1 Editor Integration

The core of Cody is its deep integration with the Monaco Editor, the same editor that powers VS Code. Key integration points include:

#### 6.1.1 Decorations and Inlay Hints
Decorations are visual elements added to the editor, like highlighting, squiggly lines, or gutter icons. Cody uses them to:

- Highlight code that could be refactored
- Mark lines with potential errors
- Indicate areas where AI has suggestions
- Show quantum analysis results

Example usage:
```typescript
const decoration = vscode.window.createTextEditorDecorationType({
  backgroundColor: 'rgba(100, 100, 200, 0.2)',
  after: {
    contentText: '// AI suggests refactoring',
    color: '#999999'
  }
});

editor.setDecorations(decoration, [
  new vscode.Range(new vscode.Position(lineNumber, 0), 
                   new vscode.Position(lineNumber, 80))
]);
```

#### 6.1.2 Completion Providers
Cody enhances the standard code completion with AI-powered suggestions:

```typescript
vscode.languages.registerCompletionItemProvider(
  { scheme: 'file', language: '*' },
  {
    provideCompletionItems(document, position) {
      // Get AI suggestions from backend
      return getAISuggestions(document, position)
        .then(suggestions => {
          return suggestions.map(s => {
            const item = new vscode.CompletionItem(s.label);
            item.insertText = s.code;
            item.documentation = s.explanation;
            item.kind = vscode.CompletionItemKind.Snippet;
            return item;
          });
        });
    }
  }
);
```

#### 6.1.3 Code Actions
Cody provides code actions for AI-powered fixes and refactoring:

```typescript
vscode.languages.registerCodeActionsProvider(
  { scheme: 'file', language: '*' },
  {
    provideCodeActions(document, range, context) {
      const actions = [];
      
      if (context.diagnostics.length > 0) {
        actions.push({
          title: 'Fix with Cody AI',
          command: 'cody.fixWithAI',
          arguments: [document, range, context.diagnostics]
        });
      }
      
      return actions;
    }
  }
);
```

### 6.2 Webview Panels

Webview panels provide rich UI experiences beyond what the VS Code API directly supports:

#### 6.2.1 Chat Interface
The AI chat interface is implemented as a webview panel:

```typescript
class ChatPanel {
  private static readonly viewType = 'cody.chat';
  private readonly _panel: vscode.WebviewPanel;
  
  constructor(extensionUri: vscode.Uri) {
    this._panel = vscode.window.createWebviewPanel(
      ChatPanel.viewType,
      'Cody AI Chat',
      vscode.ViewColumn.Beside,
      {
        enableScripts: true,
        localResourceRoots: [vscode.Uri.joinPath(extensionUri, 'media')]
      }
    );
    
    this._panel.webview.html = this._getHtmlForWebview(extensionUri);
    this._panel.webview.onDidReceiveMessage(this._handleMessage.bind(this));
  }
  
  private _getHtmlForWebview(extensionUri: vscode.Uri): string {
    // HTML for chat interface
  }
  
  private _handleMessage(message: any) {
    // Handle messages from webview
  }
}
```

#### 6.2.2 Memory Management UI
The memory panel allows users to view and manage Cody's memories:

```typescript
class MemoryPanel {
  // Similar structure to ChatPanel
  // Displays and manages memory entries
}
```

#### 6.2.3 Refactoring Panel
Shows code improvement suggestions:

```typescript
class RefactoringPanel {
  // Presents refactoring options
  // Allows application of changes
}
```

### 6.3 Command Registration

Cody registers custom commands in VS Code:

```typescript
// In extension.ts
export function activate(context: vscode.ExtensionContext) {
  // Register commands
  context.subscriptions.push(
    vscode.commands.registerCommand('cody.openChat', () => {
      new ChatPanel(context.extensionUri);
    }),
    
    vscode.commands.registerCommand('cody.analyzeCode', () => {
      const editor = vscode.window.activeTextEditor;
      if (editor) {
        const code = editor.document.getText();
        analyzeCode(code);
      }
    }),
    
    vscode.commands.registerCommand('cody.explainSelection', () => {
      const editor = vscode.window.activeTextEditor;
      if (editor && !editor.selection.isEmpty) {
        const text = editor.document.getText(editor.selection);
        explainCode(text);
      }
    })
  );
}
```

## 7. UI/UX Architecture

### 7.1 Design System

Cody follows VS Code's design patterns while extending them for AI-specific features:

#### 7.1.1 Color Scheme
```css
:root {
  --cody-primary: #0078D4;          /* Primary brand color */
  --cody-secondary: #2C974B;        /* Secondary color for success states */
  --cody-tertiary: #9B4F96;         /* Tertiary color for quantum features */
  --cody-error: #F85149;            /* Error states */
  --cody-warning: #D29922;          /* Warning states */
  --cody-info: #58A6FF;             /* Information states */
  
  /* Dark theme adjustments */
  --cody-panel-bg: #1E1E1E;         /* Panel backgrounds */
  --cody-hover-bg: #2A2A2A;         /* Hover states */
  --cody-selection-bg: #264F78;     /* Selection backgrounds */
  
  /* Light theme adjustments */
  --cody-panel-bg-light: #F5F5F5;   /* Panel backgrounds */
  --cody-hover-bg-light: #E8E8E8;   /* Hover states */
  --cody-selection-bg-light: #ADD6FF; /* Selection backgrounds */
}
```

#### 7.1.2 Component Library
Cody uses a custom component library built on top of VS Code's styling:

```typescript
// Button component example
const Button = ({ text, onClick, type = 'default' }) => {
  return `
    <button class="cody-button cody-button-${type}" id="button-${Math.random().toString(36).substring(7)}">
      ${text}
    </button>
  `;
};

// Usage in panel HTML
this._panel.webview.html = `
  <!DOCTYPE html>
  <html>
  <head>
    <style>
      ${getCodyStyles()}  /* Import our design system */
    </style>
  </head>
  <body>
    <div class="cody-container">
      <h2>Cody Refactoring Suggestions</h2>
      ${Button({ text: 'Apply All', type: 'primary', onClick: 'applyAll()' })}
      ${Button({ text: 'Dismiss', type: 'secondary', onClick: 'dismiss()' })}
    </div>
    <script>
      const vscode = acquireVsCodeApi();
      
      function applyAll() {
        vscode.postMessage({ command: 'applyAll' });
      }
      
      function dismiss() {
        vscode.postMessage({ command: 'dismiss' });
      }
    </script>
  </body>
  </html>
`;
```

### 7.2 UI Components

#### 7.2.1 Chat UI
The chat interface resembles modern AI chat applications:

- Message bubbles (user and AI)
- Code blocks with syntax highlighting
- Inline suggestions
- Action buttons for applying code
- File references and links

#### 7.2.2 Memory UI
The memory panel displays:

- Memory categories (code, user preferences, project)
- Priority levels
- Search and filter capabilities
- Memory editing and deletion

#### 7.2.3 Refactoring UI
The refactoring interface shows:

- Code before/after comparisons
- Explanation of suggested changes
- Confidence levels (with quantum enhancement)
- Apply/ignore action buttons

### 7.3 Interaction Patterns

Cody follows these key interaction patterns:

1. **Command Palette**: Access all Cody features via VS Code's command palette (Ctrl+Shift+P)
2. **Context Menus**: Right-click options for code-specific actions
3. **Quick Actions**: Lightbulb menu for inline suggestions
4. **Side Panels**: Dedicated views for chat, memory, and refactoring
5. **Inline Annotations**: Decorations and hover information in the editor
6. **Status Bar**: Indicators for active AI models and quantum features

## 8. AI Integration Points

### 8.1 AI Model Orchestration

Cody supports multiple AI models through an orchestration layer:

```typescript
// AI model client
class AIModelClient {
  private apiBaseUrl: string;
  private modelType: string;
  
  constructor(modelType: string) {
    this.modelType = modelType;
    this.apiBaseUrl = getApiBaseUrl();
  }
  
  async generateCompletion(prompt: string, options: CompletionOptions = {}): Promise<string> {
    const response = await fetch(`${this.apiBaseUrl}/ai/generate`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        model: this.modelType,
        prompt,
        options
      })
    });
    
    const data = await response.json();
    return data.completion;
  }
  
  async analyzeCode(code: string): Promise<CodeAnalysisResult> {
    const response = await fetch(`${this.apiBaseUrl}/ai/analyze`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        model: this.modelType,
        code
      })
    });
    
    return await response.json();
  }
}
```

### 8.2 Model Switching

Users can switch between different AI models:

```typescript
class ModelManager {
  private static instance: ModelManager;
  private currentModel: string = 'claude-3-opus';
  private availableModels = [
    { id: 'claude-3-opus', name: 'Claude 3 Opus', provider: 'anthropic' },
    { id: 'gpt-4-turbo', name: 'GPT-4 Turbo', provider: 'openai' },
    { id: 'gemini-2', name: 'Gemini 2.0', provider: 'google' },
    { id: 'deepseek-v3', name: 'DeepSeek V3', provider: 'deepseek' }
  ];
  
  private constructor() {}
  
  static getInstance(): ModelManager {
    if (!ModelManager.instance) {
      ModelManager.instance = new ModelManager();
    }
    return ModelManager.instance;
  }
  
  setCurrentModel(modelId: string) {
    if (this.availableModels.find(m => m.id === modelId)) {
      this.currentModel = modelId;
      // Update status bar and settings
    }
  }
  
  getCurrentModel(): string {
    return this.currentModel;
  }
  
  getAvailableModels() {
    return this.availableModels;
  }
}
```

### 8.3 AI Capability Routing

Different features require different AI capabilities:

```typescript
enum AICapability {
  CodeCompletion,
  CodeGeneration,
  Refactoring,
  Debugging,
  Documentation,
  Testing,
  QuantumEnhanced
}

class CapabilityRouter {
  getModelForCapability(capability: AICapability): string {
    const settings = vscode.workspace.getConfiguration('cody');
    
    switch (capability) {
      case AICapability.CodeCompletion:
        return settings.get('preferredModelForCompletion', 'claude-3-opus');
      case AICapability.Refactoring:
        return settings.get('preferredModelForRefactoring', 'gpt-4-turbo');
      case AICapability.Debugging:
        return settings.get('preferredModelForDebugging', 'claude-3-opus');
      case AICapability.QuantumEnhanced:
        return 'quantum-bridge-service';
      default:
        return ModelManager.getInstance().getCurrentModel();
    }
  }
}
```

## 9. Memory System

Cody's memory system allows the AI to maintain context across sessions:

### 9.1 Memory Types

```typescript
enum MemoryType {
  Code = 'code',
  User = 'user',
  Project = 'project',
  Session = 'session',
  Global = 'global'
}

interface Memory {
  id: string;
  type: MemoryType;
  content: string;
  priority: number; // 1-15, higher is more important
  tags: string[];
  created: Date;
  updated: Date;
}
```

### 9.2 Memory API Client

```typescript
class MemoryAPIClient {
  private apiBaseUrl: string;
  
  constructor() {
    this.apiBaseUrl = getApiBaseUrl();
  }
  
  async createMemory(memory: Omit<Memory, 'id' | 'created' | 'updated'>): Promise<Memory> {
    const response = await fetch(`${this.apiBaseUrl}/memories`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(memory)
    });
    
    return await response.json();
  }
  
  async getMemories(filters: {
    type?: MemoryType,
    tags?: string[],
    minPriority?: number
  } = {}): Promise<Memory[]> {
    const queryParams = new URLSearchParams();
    if (filters.type) queryParams.append('type', filters.type);
    if (filters.minPriority) queryParams.append('min_priority', filters.minPriority.toString());
    if (filters.tags) filters.tags.forEach(tag => queryParams.append('tag', tag));
    
    const response = await fetch(`${this.apiBaseUrl}/memories?${queryParams}`);
    return await response.json();
  }
  
  async updateMemory(id: string, updates: Partial<Memory>): Promise<Memory> {
    const response = await fetch(`${this.apiBaseUrl}/memories/${id}`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(updates)
    });
    
    return await response.json();
  }
  
  async deleteMemory(id: string): Promise<void> {
    await fetch(`${this.apiBaseUrl}/memories/${id}`, {
      method: 'DELETE'
    });
  }
}
```

### 9.3 Memory Management UI

The Memory Panel allows users to:

1. **View memories** by type, priority, and tags
2. **Create new memories** manually
3. **Edit existing memories** to correct or enhance them
4. **Delete obsolete memories**
5. **Search across memories** with natural language queries

## 10. Quantum-Enhanced Features

Cody integrates quantum computing for enhanced code analysis:

### 10.1 Quantum Bridge Service

```typescript
class QuantumBridgeClient {
  private apiBaseUrl: string;
  
  constructor() {
    this.apiBaseUrl = getApiBaseUrl();
  }
  
  async enhancedSearch(query: string, codebase: string[]): Promise<SearchResult[]> {
    const response = await fetch(`${this.apiBaseUrl}/quantum/search`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        query,
        codebase
      })
    });
    
    return await response.json();
  }
  
  async quantumCodeAnalysis(code: string): Promise<QuantumAnalysisResult> {
    const response = await fetch(`${this.apiBaseUrl}/quantum/analyze`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ code })
    });
    
    return await response.json();
  }
  
  async getQuantumJobStatus(jobId: string): Promise<QuantumJobStatus> {
    const response = await fetch(`${this.apiBaseUrl}/quantum/jobs/${jobId}`);
    return await response.json();
  }
}
```

### 10.2 Quantum Feature UI

Quantum-enhanced features have special UI indicators:

```typescript
class QuantumIndicator {
  private statusBarItem: vscode.StatusBarItem;
  
  constructor() {
    this.statusBarItem = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Right, 100);
    this.statusBarItem.text = "$(atom) Quantum: Off";
    this.statusBarItem.command = 'cody.toggleQuantumFeatures';
    this.statusBarItem.tooltip = "Toggle Quantum-Enhanced Features";
    this.statusBarItem.show();
  }
  
  setEnabled(enabled: boolean) {
    if (enabled) {
      this.statusBarItem.text = "$(atom) Quantum: On";
      this.statusBarItem.backgroundColor = new vscode.ThemeColor('statusBarItem.warningBackground');
    } else {
      this.statusBarItem.text = "$(atom) Quantum: Off";
      this.statusBarItem.backgroundColor = undefined;
    }
  }
}
```

### 10.3 Quantum Analysis Results

Quantum analysis provides probabilistic code insights:

```typescript
interface QuantumAnalysisResult {
  scores: {
    quality: number;       // 0-1 code quality score
    complexity: number;    // 0-1 complexity score
    maintenance: number;   // 0-1 maintainability score
  };
  suggestions: {
    text: string;          // Suggestion text
    confidence: number;    // 0-1 confidence score
    position: {            // Where to apply
      line: number;
      character: number;
    };
    replacement?: string;  // Suggested replacement code
  }[];
  quantumMetrics: {
    qubits: number;        // Number of qubits used
    depth: number;         // Circuit depth
    executionTime: number; // Execution time in ms
  };
}
```

## 11. Development Workflow

Following Semantic Seed Coding Standards V2.0, all development follows a structured workflow:

### 11.1 Backlog Management

We use Shortcut to manage the backlog with the following story types:
- **Features**: New functionality (feature/{id} branches)
- **Bugs**: Issue fixes (bug/{id} branches)
- **Chores**: Maintenance tasks (chore/{id} branches)

### 11.2 Standard Workflow

1. **Start a Story**
   - Choose the top unstarted story in the backlog
   - Create a branch with the proper naming convention
   - Create your working environment

2. **TDD Workflow**
   ```
   # 1. Write failing tests first
   git commit -m "WIP: Red Tests for feature X"
   
   # 2. Implement code to make tests pass
   git commit -m "WIP: Green Tests for feature X"
   
   # 3. Refactor your implementation
   git commit -m "Refactor complete for feature X"
   ```

3. **Pull Request Process**
   - Mark story as Finished
   - Create a PR and trigger a build
   - Request reviews
   - Address feedback

4. **Delivery**
   - Merge to main branch
   - Mark story as Delivered
   - Product Manager reviews and accepts/rejects

### 11.3 Coding Style Guidelines

According to Semantic Seed Coding Standards:

1. **Naming Conventions**
   - Use camelCase for variables and functions (JavaScript/TypeScript)
   - Use PascalCase for classes and React components
   - Use snake_case for filenames and directories

2. **Code Formatting**
   - 4-space indentation
   - Maximum line length of 80 characters
   - End files with a newline

3. **Comments**
   - Use JSDoc style for function documentation
   - Add comments for complex logic
   - Remove commented-out code

### 11.4 Git Workflow

1. **End-of-Day Commits**
   - All work should be committed daily with WIP tags
   - Push to remote to ensure continuity

2. **Descriptive Commit Messages**
   ```
   [type]: Brief description (max 50 chars)
   
   More detailed explanation of what changed and why.
   Include any important details about the change.
   ```

3. **Pull Request Guidelines**
   - Include a clear description
   - Reference the story ID
   - Add relevant reviewers
   - Ensure all tests pass

## 12. Testing

Testing follows BDD principles, ensuring all code has appropriate test coverage.

### 12.1 BDD Style Tests

Following Semantic Seed Coding Standards, tests are written in a BDD style:

```typescript
describe('Memory Panel', () => {
  describe('when user creates a new memory', () => {
    it('should send the memory to the API and update the UI', async () => {
      // Given: A memory panel with initial state
      const panel = new MemoryPanel();
      const api = new MockMemoryAPI();
      panel.setMemoryAPI(api);
      
      // When: User creates a new memory
      await panel.createMemory({
        type: MemoryType.Code,
        content: 'Remember to use camelCase for variables',
        priority: 5,
        tags: ['style', 'convention']
      });
      
      // Then: The memory is sent to API and UI is updated
      expect(api.createMemory).toHaveBeenCalled();
      expect(panel.getMemoriesCount()).toBe(1);
    });
  });
});
```

### 12.2 Test Structure

1. **Unit Tests**
   - Test individual components in isolation
   - Use Jest for frontend testing
   - Follow the Given/When/Then pattern

2. **Integration Tests**
   - Test component interactions
   - Test API integrations with real endpoints

3. **UI Tests**
   - Test webview interactions
   - Test command execution flows

### 12.3 Testing Commands

Test custom VS Code commands:

```typescript
import * as vscode from 'vscode';

describe('Commands', () => {
  it('should register and execute the openChat command', async () => {
    // Given: The extension is activated
    // When: The openChat command is executed
    await vscode.commands.executeCommand('cody.openChat');
    
    // Then: A chat panel should be created and visible
    const panels = vscode.window.webviewPanels.filter(
      p => p.viewType === 'cody.chat'
    );
    expect(panels.length).toBe(1);
  });
});
```

### 12.4 Testing Web Views

Test webview functionality:

```typescript
describe('Chat Panel WebView', () => {
  it('should properly handle messages from the webview', async () => {
    // Given: A chat panel with a webview
    const panel = new ChatPanel();
    
    // When: A message is received from the webview
    await panel.handleWebviewMessage({
      command: 'sendMessage',
      text: 'How do I implement a React component?'
    });
    
    // Then: The message should be processed
    expect(panel.messages.length).toBe(2); // User message + AI response
  });
});
```

## 13. Common Development Tasks

### 13.1 Adding a New Command

```typescript
// 1. In extension.ts, register the command
export function activate(context: vscode.ExtensionContext) {
  context.subscriptions.push(
    vscode.commands.registerCommand('cody.myNewCommand', () => {
      // Implement command logic
      vscode.window.showInformationMessage('My new command executed!');
    })
  );
}

// 2. In package.json, add the command to contributes.commands
{
  "contributes": {
    "commands": [
      {
        "command": "cody.myNewCommand",
        "title": "Cody: My New Command",
        "category": "Cody"
      }
    ]
  }
}
```

### 13.2 Adding a New WebView Panel

1. Create a new class extending the base panel:

```typescript
// src/vscode/extensions/cody/src/views/MyNewPanel.ts
import * as vscode from 'vscode';
import { BasePanel } from './BasePanel';

export class MyNewPanel extends BasePanel {
  public static readonly viewType = 'cody.myNewPanel';
  
  public static createOrShow(extensionUri: vscode.Uri) {
    const column = vscode.window.activeTextEditor
      ? vscode.window.activeTextEditor.viewColumn
      : undefined;
      
    // Check if panel already exists
    if (BasePanel.currentPanels[MyNewPanel.viewType]) {
      BasePanel.currentPanels[MyNewPanel.viewType].panel.reveal(column);
      return;
    }
    
    // Create new panel
    const panel = vscode.window.createWebviewPanel(
      MyNewPanel.viewType,
      'My New Panel',
      column || vscode.ViewColumn.One,
      {
        enableScripts: true,
        retainContextWhenHidden: true,
        localResourceRoots: [vscode.Uri.joinPath(extensionUri, 'media')]
      }
    );
    
    const myPanel = new MyNewPanel(panel, extensionUri);
    BasePanel.currentPanels[MyNewPanel.viewType] = myPanel;
  }
  
  constructor(panel: vscode.WebviewPanel, extensionUri: vscode.Uri) {
    super(panel, extensionUri);
    this._update();
    
    // Handle messages from webview
    this._panel.webview.onDidReceiveMessage(
      message => this._handleMessage(message),
      null,
      this._disposables
    );
  }
  
  private _update() {
    if (!this._panel.visible) {
      return;
    }
    
    this._panel.webview.html = this._getHtmlForWebview();
  }
  
  private _getHtmlForWebview(): string {
    // Return HTML for webview
    return `
      <!DOCTYPE html>
      <html lang="en">
      <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My New Panel</title>
        <style>
          body { font-family: var(--vscode-font-family); }
          .container { padding: 15px; }
        </style>
      </head>
      <body>
        <div class="container">
          <h1>My New Panel</h1>
          <button id="actionButton">Perform Action</button>
        </div>
        <script>
          const vscode = acquireVsCodeApi();
          document.getElementById('actionButton').addEventListener('click', () => {
            vscode.postMessage({ command: 'action', value: 'clicked' });
          });
        </script>
      </body>
      </html>
    `;
  }
  
  private _handleMessage(message: any) {
    switch (message.command) {
      case 'action':
        vscode.window.showInformationMessage('Action performed!');
        break;
    }
  }
}
```

2. Register a command to show the panel:

```typescript
// In extension.ts
import { MyNewPanel } from './views/MyNewPanel';

export function activate(context: vscode.ExtensionContext) {
  context.subscriptions.push(
    vscode.commands.registerCommand('cody.showMyNewPanel', () => {
      MyNewPanel.createOrShow(context.extensionUri);
    })
  );
}
```

### 13.3 Calling Backend APIs

Use the APIClient to make REST calls to the backend:

```typescript
import { APIClient } from '../api/APIClient';

class MyService {
  private client: APIClient;
  
  constructor() {
    this.client = new APIClient();
  }
  
  async fetchData() {
    try {
      const response = await this.client.get('/api/v1/my-endpoint');
      return response.data;
    } catch (error) {
      console.error('Error fetching data:', error);
      vscode.window.showErrorMessage('Failed to fetch data from the server');
      throw error;
    }
  }
  
  async sendData(data: any) {
    try {
      const response = await this.client.post('/api/v1/my-endpoint', data);
      return response.data;
    } catch (error) {
      console.error('Error sending data:', error);
      vscode.window.showErrorMessage('Failed to send data to the server');
      throw error;
    }
  }
}
```

### 13.4 Adding a Status Bar Item

Create and manage a status bar item:

```typescript
class MyStatusBarItem {
  private statusBarItem: vscode.StatusBarItem;
  
  constructor() {
    this.statusBarItem = vscode.window.createStatusBarItem(
      vscode.StatusBarAlignment.Right,
      100
    );
    this.statusBarItem.text = "$(rocket) Cody";
    this.statusBarItem.tooltip = "Cody AI Assistant";
    this.statusBarItem.command = 'cody.openChat';
    this.statusBarItem.show();
  }
  
  updateStatus(text: string, icon: string = 'rocket') {
    this.statusBarItem.text = `$(${icon}) ${text}`;
  }
  
  dispose() {
    this.statusBarItem.dispose();
  }
}
```

## 14. Troubleshooting

### 14.1 Common Issues

#### VS Code Build Problems
- **Issue**: Build fails with TypeScript errors
- **Solution**: 
  ```bash
  # Clean the build artifacts
  rm -rf out
  # Delete node_modules and reinstall
  rm -rf node_modules
  npm install
  # Rebuild
  npm run compile
  ```

#### Backend Connection Issues
- **Issue**: Cannot connect to backend services
- **Solution**:
  1. Check if backend services are running: `docker ps`
  2. Verify `.env` configuration is correct
  3. Check logs: `docker logs cody-backend`

#### Extension Not Loading
- **Issue**: Extension doesn't activate in VS Code
- **Solution**:
  1. Check activation events in `package.json`
  2. Look for errors in the Output panel (View > Output > Cody Extension)
  3. Try running with `--verbose` flag: `code --verbose`

#### WebView Not Rendering
- **Issue**: WebView panel shows blank content
- **Solution**:
  1. Check for console errors in the Developer Tools (Help > Toggle Developer Tools)
  2. Verify your HTML is valid
  3. Check if `localResourceRoots` is configured correctly

### 14.2 Debugging Tools

#### VS Code Extension Debugging
1. Use the "Extension Development Host" launch configuration
2. Set breakpoints in your extension code
3. Use console.log for debugging (appears in Debug Console)

#### Webview Debugging
1. Access the webview's dev tools with `this._panel.webview.html`
2. Log messages with `console.log` (appears in webview's console)
3. Use the VS Code Developer Tools to inspect elements

#### Backend API Debugging
1. Use the Network tab in Developer Tools to monitor API calls
2. Enable verbose logging in your API client
3. Use tools like Postman to test API endpoints directly

## 15. Glossary

| Term | Description |
|------|-------------|
| **AI Orchestration** | System for routing requests to different AI models based on capabilities |
| **Capability Routing** | Directing specific tasks to the AI model best suited for that task |
| **Memory API** | Backend service for storing and retrieving AI context |
| **Monaco Editor** | The code editor component that powers VS Code |
| **Quantum Bridge** | Service connecting to quantum computing resources for enhanced code analysis |
| **SCSS V2.0** | Semantic Seed Coding Standards Version 2.0, our development standard |
| **WebView** | Custom UI component within VS Code that uses HTML/CSS/JS |
| **Decoration** | Visual element added to the editor (highlighting, etc.) |
| **Inlay Hint** | Inline text added to the editor for additional information |
| **Code Action** | Quick fix or refactoring option shown in the editor |
| **Extension Host** | The process that runs VS Code extensions |
| **Command** | Named action that can be triggered by users or code |
| **FIM** | Fill-in-the-middle, an AI completion technique |
| **API Gateway** | Entry point for all backend API requests |
| **BDD** | Behavior-Driven Development, our testing methodology |

## 16. API Reference

### 16.1 Frontend APIs

#### VS Code Extension API
- [VS Code API Documentation](https://code.visualstudio.com/api/references/vscode-api)
- Key namespaces: `vscode.window`, `vscode.workspace`, `vscode.languages`

#### Cody Extension API
- `CodyAPI`: Main entry point for interacting with Cody services
- `MemoryAPI`: Interface for the memory system
- `AIModelAPI`: Interface for AI model orchestration
- `QuantumAPI`: Interface for quantum-enhanced features

### 16.2 Backend APIs

#### REST API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/health` | GET | Health check endpoint |
| `/api/v1/memories` | GET | Get memories with optional filters |
| `/api/v1/memories` | POST | Create a new memory |
| `/api/v1/memories/:id` | GET | Get a specific memory |
| `/api/v1/memories/:id` | PATCH | Update a memory |
| `/api/v1/memories/:id` | DELETE | Delete a memory |
| `/api/v1/ai/generate` | POST | Generate AI completions |
| `/api/v1/ai/analyze` | POST | Analyze code with AI |
| `/api/v1/ai/models` | GET | List available AI models |
| `/api/v1/quantum/search` | POST | Perform quantum-enhanced search |
| `/api/v1/quantum/analyze` | POST | Analyze code with quantum algorithms |
| `/api/v1/quantum/jobs/:id` | GET | Get quantum job status |

#### WebSocket Endpoints

| Endpoint | Description |
|----------|-------------|
| `/ws/chat` | Real-time chat with AI |
| `/ws/notifications` | Real-time notifications |
| `/ws/status` | Real-time status updates |

### 16.3 Configuration Options

Cody's settings are stored in VS Code's configuration system:

```json
{
  "cody.ai.preferredModel": "claude-3-opus",
  "cody.ai.quantumEnhanced": true,
  "cody.memory.autoSave": true,
  "cody.memory.minPriority": 3,
  "cody.ui.showInlineCompletions": true,
  "cody.ui.showStatusBarItem": true
}
```

These settings can be accessed and modified in your code:

```typescript
const config = vscode.workspace.getConfiguration('cody');
const preferredModel = config.get('ai.preferredModel');
config.update('ai.preferredModel', 'gpt-4-turbo', vscode.ConfigurationTarget.Global);
