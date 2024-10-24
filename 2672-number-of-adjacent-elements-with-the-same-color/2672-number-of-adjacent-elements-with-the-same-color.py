class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        colors = [0] * n  # Initialize the colors array with all zeros (uncolored)
        adjacent_pairs = 0  # This will track the number of adjacent pairs with the same color
        result = []  # To store the answer after each query

        for index, new_color in queries:
            # Before changing the color, check if the current color forms adjacent pairs
            if index > 0 and colors[index] == colors[index - 1] and colors[index] != 0:
                adjacent_pairs -= 1  # Remove the adjacent pair before the update
            if index < n - 1 and colors[index] == colors[index + 1] and colors[index] != 0:
                adjacent_pairs -= 1  # Remove the adjacent pair before the update

            # Update the color at the given index
            colors[index] = new_color

            # After changing the color, check if the new color forms adjacent pairs
            if index > 0 and colors[index] == colors[index - 1]:
                adjacent_pairs += 1  # Add the adjacent pair after the update
            if index < n - 1 and colors[index] == colors[index + 1]:
                adjacent_pairs += 1  # Add the adjacent pair after the update

            # Append the current count of adjacent pairs to the result
            result.append(adjacent_pairs)

        return result