interface Observer {
    update(message: string): void;
}



interface Subject {
    registerObserver(observer: Observer): void;
    removeObserver(observer: Observer): void;
    notifyObservers(): void;
}


class NewsPublisher implements Subject {
    private observers: Observer[] = [];
    private latestNews: string = "";

    registerObserver(observer: Observer): void {
        this.observers.push(observer);
    }

    removeObserver(observer: Observer): void {
        const index = this.observers.indexOf(observer);
        if (index === -1) {
            this.observers.splice(index, 1);
        }
        // this.observers = this.observers.filter(o => o !== observer);
    }

    notifyObservers(): void {
        for (const observer of this.observers) {
            observer.udpate(this.latestNews);
        }
        // this.observers.forEach(observer => observer.update("Hello"));
    }

    setLatestNews(news: string): void {
        this.latestNews = news;
        this.notifyObservers();
    }
}


class NewsSubscriber implements Observer {

    constructor(private name: string) { }

    update(message: string): void {
        console.log(`${this.name} received the news: ${message}`);
    }
}
