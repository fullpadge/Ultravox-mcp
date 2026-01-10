# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-01-10

### Added

- **Initial Release** - Unofficial Ultravox MCP Server
- **29 Ultravox API Tools** fully implemented:
  - Call management (list, get, delete, recording)
  - Agent management (list, get, update, delete)
  - Voice & model selection
  - Webhook management
  - Deleted calls recovery
  - Account information

- **Multi-Platform Support:**
  - Claude Desktop (macOS, Linux, Windows)
  - Docker & Docker Compose
  - Linux systemd service
  - n8n integration

- **Comprehensive Documentation:**
  - README in English and French
  - Quick start guide (5 minutes)
  - Platform-specific installation guides
  - API reference documentation
  - Configuration guide
  - Troubleshooting guide

- **Code Quality:**
  - Full error handling
  - Type hints throughout
  - Comprehensive logging
  - Security best practices

- **Developer Tools:**
  - Python examples
  - n8n workflow template
  - Docker configuration (multi-stage build)
  - GitHub Actions CI/CD workflow
  - Contributing guidelines

- **Security:**
  - .env file protection (git ignored)
  - API key validation
  - Input sanitization
  - Error message safety

### Initial Features

- ✅ Full Ultravox API access
- ✅ MCP protocol implementation
- ✅ Production-ready code
- ✅ Tested on Python 3.8, 3.9, 3.10, 3.11
- ✅ Cross-platform compatibility
- ✅ Comprehensive test suite

## Development Timeline

### Planning Phase
- Research Ultravox API
- Design MCP integration
- Plan architecture

### Implementation Phase
- Implement 29 API tools
- Create documentation
- Build examples
- Set up CI/CD

### Testing Phase
- Unit tests for all tools
- Integration tests
- Cross-platform testing
- Performance optimization

### Release Phase
- Documentation finalization
- README & guides
- Contributing guidelines
- Initial release

---

## Future Roadmap

### Version 1.1.0 (Planned)

- [ ] Advanced caching for performance
- [ ] Batch operations support
- [ ] Custom tool extensions
- [ ] Web UI dashboard
- [ ] CLI tool (pip installable)
- [ ] Enhanced error recovery

### Version 1.2.0 (Planned)

- [ ] Database support for call history
- [ ] Analytics dashboard
- [ ] Advanced filtering options
- [ ] Event streaming
- [ ] Rate limiting configuration

### Version 2.0.0 (Planned)

- [ ] Full Ultravox REST API integration
- [ ] Real-time call monitoring
- [ ] Advanced webhook features
- [ ] Multi-user support
- [ ] Enterprise features

---

## How to Contribute

We follow Semantic Versioning:
- **MAJOR** version for incompatible API changes
- **MINOR** version for new functionality (backward compatible)
- **PATCH** version for bug fixes

To contribute:
1. Read [CONTRIBUTING.md](./CONTRIBUTING.md)
2. Fork the repository
3. Create a feature branch
4. Submit a pull request

---

## Version History

### v1.0.0 (Current)
- Initial public release
- 29 Ultravox API tools
- Full documentation
- Multi-platform support
- CI/CD pipeline

---

## Support

For issues or questions:
- Create an issue: [Issues](https://github.com/fullpadge/Ultravox-mcp/issues)
- Start a discussion: [Discussions](https://github.com/fullpadge/Ultravox-mcp/discussions)
- Email: hello@mak3it.org

---

## Maintained by Mak3it

This project is maintained as part of [Mak3it.org](https://mak3it.org)'s commitment to innovation in AI-powered legal technology.

**Website:** https://mak3it.org  
**Email:** hello@mak3it.org

---

## Acknowledgments

- Ultravox team for the amazing API
- MCP community for the protocol
- Contributors and testers
- All users providing feedback

---

**Keep this changelog updated when making releases!**
