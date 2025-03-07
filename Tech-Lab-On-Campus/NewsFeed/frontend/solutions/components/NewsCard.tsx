import Link from "next/link";
import { Article } from "@/utils/types";

interface NewsCardProps {
    article: Article;
}


function NewsCard({ article }: NewsCardProps) {
    return (
        <div className="news-card">
            <div className="news-info">
                <img src={article.image_url} alt={article.title} className="news-img" />
                <h2 className="story-title">{article.title}</h2>
                <p className="story-summary">{article.body.slice(0, 150)}...</p>
            </div>
        </div>
    );
}

export default NewsCard;
