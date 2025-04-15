if time.time() - last_growth_time >= growth_interval:
        snake.body.append(Point(snake.body[-1].x, snake.body[-1].y))  # Add new segment to snake's body
        last_growth_time = time.time()