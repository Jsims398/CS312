import argparse
from time import time
import matplotlib.pyplot as plt

from generate import generate_random_points
from convex_hull import compute_hull
from plotting import plot_points, draw_hull, title, show_plot


def main(n: int, distribution: str, seed: int | None):
    points = generate_random_points(distribution, n, seed)
    plot_points(points)

    start = time()
    hull_points = compute_hull(points)
    end = time()

    draw_hull(hull_points)
    title(f'{n} {distribution} points: {round(end - start, 4)} seconds')
    # show_plot()
    return round(end - start, 6)

if __name__ == '__main__':

    # To debug or run in your IDE
    # you can uncomment the lines below and modify the arguments as needed
    # import sys
    # sys.argv = ['main.py', '-n', '10', '--seed', '312', '--debug']

    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int, help='The number of points to generate', default=10)
    parser.add_argument('-d', '--dist', '--distribution',
                        help='The distribution from which to generate points',
                        default='uniform'
                        )
    parser.add_argument('--seed', type=int, default=None, help="Random seed")
    parser.add_argument('--debug', action='store_true', help='Turn on debug plotting')
    args = parser.parse_args()

    if args.debug:
        # To debug your algorithm with incremental plotting:
        # - run this script with --debug (e.g. add '--debug' to the sys.argv above)
        # - set breakpoints
        # As you step through your code, you will see the plot update as you go
        import matplotlib.pyplot as plt
        plt.switch_backend('QtAgg')
        plt.ion()
    
    times= []
    ns = [10,100, 1000]
    for n in ns:
        c = main(n, args.dist, args.seed)
        times.append(c)
        # plt.clf()
        # plt.plot(ns, times, 'o')
        # plt.show()
    print(times)  

    # ns = [100, 1000]

    # for n in ns:
    #     # Generate random points
    #     points = generate_random_points("uniform", n, None)
        
    #     # Compute the convex hull
    #     hull_points = compute_hull(points)
        
    #     # Create a new figure
    #     plt.figure(figsize=(8, 6))
        
    #     # Plot the points and the convex hull
    #     plot_points(points, c='blue', alpha=0.5)
    #     draw_hull(hull_points, color='red', linewidth=2)
        
    #     # Title and display
    #     title(f'Convex Hull for {n} Points')
    #     plt.show()
      
    # main(args.n, args.dist, args.seed)
