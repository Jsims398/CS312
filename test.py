def find_upper_tangent(left, right, right_index, left_index):
    xlm, ylm = right[left_index]
    xrm, yrm = left[right_index]

    if xlm == xrm:
        start_slope = float('inf')  # Avoid division by zero (vertical line)
    else:
        start_slope = (yrm - ylm) / (xrm - xlm)

    changed = True

    while changed:
        changed = False
        while left_index - 1 >= 0:
            rx, ry = right[left_index - 1]
            new_slope = (ry - yrm) / (rx - xrm)
            if new_slope < start_slope:
                start_slope = new_slope
                xlm, ylm = rx, ry
                left_index -= 1
                changed = True
            else:
                break

        while right_index + 1 < len(left):
            rlx, rly = left[right_index + 1]
            new_slope = (ylm - rly) / (xlm - rlx)
            if new_slope > start_slope:
                start_slope = new_slope
                xrm, yrm = rlx, rly
                right_index += 1
                changed = True
            else:
                break
    return right_index, left_index


def find_lower_tangent(left, right, right_index, left_index):
    xlm, ylm = right[left_index]
    xrm, yrm = left[right_index]

    if xlm == xrm:
        start_slope = float('-inf')  # Avoid division by zero (vertical line)
    else:
        start_slope = (yrm - ylm) / (xrm - xlm)

    changed = True

    while changed:
        changed = False
        while left_index - 1 >= 0:
            rx, ry = right[left_index - 1]
            new_slope = (ry - yrm) / (rx - xrm)
            if new_slope < start_slope:
                start_slope = new_slope
                xlm, ylm = rx, ry
                left_index -= 1
                changed = True
            else:
                break

        while right_index + 1 < len(left):
            rlx, rly = left[right_index + 1]
            new_slope = (ylm - rly) / (xlm - rlx)
            if new_slope > start_slope:
                start_slope = new_slope
                xrm, yrm = rlx, rly
                right_index += 1
                changed = True
            else:
                break

    return right_index, left_index


def find_extreme_x_indices(left_list, right_list):
    rightmost_left_index = max(range(len(left_list)), key=lambda i: left_list[i][0]) if left_list else None
    leftmost_right_index = min(range(len(right_list)), key=lambda i: right_list[i][0]) if right_list else None
    return rightmost_left_index, leftmost_right_index


# Example usage
left_coords = [(1, 2), (2, 3)]
right_coords = [(4, 5), (5, 2)]

left_idx, right_idx = find_extreme_x_indices(left_coords, right_coords)

if left_idx is not None and right_idx is not None:
    x1, y1 = left_coords[left_idx]
    x2, y2 = right_coords[right_idx]

    if x1 == x2:
        print("None")  # Avoid division by zero (vertical line)
    else:
        print(f"Slope: {(y2 - y1) / (x2 - x1)}")

    print(f"Rightmost left index: {left_idx}, Coordinate: {left_coords[left_idx]}")
    print(f"Leftmost right index: {right_idx}, Coordinate: {right_coords[right_idx]}")
else:
    print("Invalid input: One of the lists is empty.")

# Fixing the argument order when calling the tangent functions
upper_tangent = find_upper_tangent(left_coords, right_coords, left_idx, right_idx)
lower_tangent = find_lower_tangent(left_coords, right_coords, left_idx, right_idx)

print(f"Upper tangent: {upper_tangent}")
print(f"Lower tangent: {lower_tangent}")

combined_hull = []
upper_right = upper_tangent[1]
lower_right = lower_tangent[1]
upper_left = upper_tangent[0]
lower_left = lower_tangent[0]

print(f"Upper right: {upper_right}, Lower right: {lower_right}, Upper left: {upper_left}, Lower left: {lower_left}")
