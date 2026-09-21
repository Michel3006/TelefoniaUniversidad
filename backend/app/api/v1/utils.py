def like_seguro(q: str) -> str:
    """Escapa comodines SQL para usar de forma segura en clausulas LIKE/ilike."""
    q = q.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")
    return f"%{q}%"