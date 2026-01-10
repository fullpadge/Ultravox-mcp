# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-01-10

### Added
- ✨ **Initial Release** - Complete Ultravox MCP Server
- 🔧 **29 Ultravox Tools** - Full API coverage
  - 10 Call management tools
  - 5 Agent management tools
  - 2 Voice selection tools
  - 1 Model listing tool
  - 4 Webhook management tools
  - 3 Deleted calls tools
  - 3 Resource tools
- 📦 **Dual Mode Support**
  - FastMCP implementation (auto-installs)
  - Stdlib fallback (always available)
- 🖥️ **Multi-Platform Support**
  - Windows (Claude Desktop)
  - macOS (Claude Desktop)
  - Linux (systemd, Docker, Kubernetes)
  - n8n Integration
- 🐳 **Docker & Container Support**
  - Dockerfile (multi-stage, optimized)
  - Docker Compose configuration
  - Kubernetes manifests
- 📚 **Comprehensive Documentation**
  - English & French guides
  - Installation for all platforms
  - API reference
  - Troubleshooting guides
- 🔒 **Security Features**
  - Environment variable protection
  - .gitignore configured
  - No hardcoded secrets
- 🧪 **Testing & CI/CD**
  - GitHub Actions workflows
  - Test coverage reporting
  - Security scanning
- 📋 **Examples**
  - Python usage examples
  - Claude Desktop examples
  - n8n workflow examples

### Fixed
- 🔧 Fixed `get_call_recording` 302 redirect handling
- 🔧 Fixed `get_call_tools` list format structure
- 🔧 Improved error handling for missing endpoints

### Known Issues
- ⚠️ 2 Endpoints not available in Ultravox API
  - `get_open_api_schema` (404)
  - `get_call_usage` (404)
- ⚠️ Some features require recent Ultravox API versions

### Tested
- ✅ 27/29 tools validated (93.1%)
- ✅ All core functionality tested
- ✅ Multi-platform compatibility verified
- ✅ Security best practices implemented

### Credits
- Developed by **Mak3it.org**
- Unofficial implementation of Ultravox API
- Not affiliated with Ultravox/Fixie AI

---

## [0.9.0] - 2026-01-09

### Added
- 🚧 Beta release with 25 tools working
- Initial GitHub repository setup
- Basic documentation
- Docker support

### Changed
- Improved API error handling
- Better logging for debugging

---

## Unreleased

### Planned Features
- [ ] Web UI dashboard for managing agents/calls
- [ ] CLI tool for command-line usage
- [ ] WebSocket support for real-time updates
- [ ] Advanced caching layer
- [ ] Rate limiting management
- [ ] Call analytics and reporting
- [ ] Multi-language support expansion
- [ ] Integration with more platforms (Slack, Teams, etc.)

### Under Investigation
- Real-time voice streaming
- Custom model fine-tuning
- Advanced webhook filtering
- Backup/restore functionality

---

## How to Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Security

If you discover a security vulnerability, please email security@mak3it.org instead of using the issue tracker.

## License

MIT License - See [LICENSE](LICENSE) for details.
