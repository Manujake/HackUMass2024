def exclude_large_distances(distances):
    # List to store filtered distances
    filtered_distances = []

    # Process the distances in batches of 5
    for i in range(0, len(distances), 5):
        batch = distances[i:i + 5]
        
        # If batch has fewer than 5 distances, process remaining values
        if len(batch) < 5:
            break

        # Calculate the average of the batch
        batch_average = sum(batch) / len(batch)

        # Exclude values greater than 50% above the batch average
        threshold = 1.5 * batch_average
        batch_filtered = [d for d in batch if d <= threshold]

        # Add filtered batch to final result
        filtered_distances.extend(batch_filtered)

    return filtered_distances
