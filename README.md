# Food-Delivery-Routing-Optimization (Fall 2023)

Introduction

In today's fast-paced world, food delivery has become an essential service, seamlessly blending technology with logistics to bring convenience right to our doorsteps. One of the key challenges in optimizing these services lies in designing the most efficient routing strategies—from the restaurant to the customer's location. This is where algorithms like Shortest Path First (SPF) can make a significant impact. By finding the most efficient routes through complex city layouts and traffic conditions, we can enhance both delivery speed and reliability.

For this project, I'm diving deep into graph theory to model a city's street network, focusing on optimizing routes for food delivery services. The streets in the city are represented as weighted edges in a graph, where each vertex is an intersection or significant landmark. The weight of each edge is the time it takes to travel that street segment, which becomes a crucial factor in determining the most effective routes.

By leveraging this graph-based approach, I aim to develop algorithms that can efficiently compute the shortest and fastest delivery paths, ultimately reducing delivery times and boosting customer satisfaction.
Project Objectives

    Construct a city street network using graph theory principles.
    Implement algorithms, such as Shortest Path First, to find optimal delivery routes.
    Minimize the time it takes for food deliveries, enhancing overall service efficiency.
    Improve customer experience by ensuring quicker, more reliable deliveries.

Resources

    City Map Data: For this project, I am using a specially curated fake city map dataset to simulate and analyze various delivery routes. The dataset is designed to mimic a complex network of streets and intersections, offering a realistic environment for testing and optimizing routing algorithms. You can find the dataset in the starter code included in this repository.

    Data Format: The dataset is organized into several text files, each containing records that represent the streets in the city. Every line in these files follows this format:
    NODE1|NODE2|COST
        NODE1 and NODE2 are nodes that denote key points, such as intersections or landmarks.
        COST indicates the time cost to travel between NODE1 and NODE2.
        This format allows each edge to be viewed as a bi-directional path between two significant locations within the city, modeled as vertices in a graph.
