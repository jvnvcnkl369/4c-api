from sqlalchemy.orm import joinedload


def apply_includes(query, model, includes):

    if includes:
        for include in includes.split(","):
            if hasattr(model, include):
                query = query.options(joinedload(getattr(model, include)))
    return query
