def common(request): return {'cart_count': request.session.get('cart', {}).get('count', 0)}
