```mermaid
sequenceDiagram
    participant Entwickler
    participant GitHub
    participant CI/CD-Pipeline
    participant Testsystem
    participant Server

    Entwickler->>GitHub: Code pushen
    GitHub->>CI/CD-Pipeline: Workflow starten
    CI/CD-Pipeline->>CI/CD-Pipeline: Code clonen & Abhängigkeiten installieren
    CI/CD-Pipeline->>Testsystem: Unit-Tests ausführen
    Testsystem-->>CI/CD-Pipeline: Testergebnisse senden
    CI/CD-Pipeline-->>GitHub: Erfolgreich / Fehlgeschlagen
    CI/CD-Pipeline->>Server: Deployment starten (falls erfolgreich)
    Server-->>Entwickler: Monitoring aktiv
