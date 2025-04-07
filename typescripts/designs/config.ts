class ConfigManager {
    private static instance: ConfigManager | null = null;
    private config: { [key: string]: string; } = {};



    private constructor() {
        this.config = {
            "apiKey": "123456",
            "api": "http://localhost:3000",
            "version": "1.0.0",
            "maxConnections": "10"
        };
    }
}
