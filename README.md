# Food Delivery Routing Optimization

## What's This About?

Food delivery is everywhere now, and getting orders to customers fast is what separates good services from great ones. This project tackles that challenge head-on using graph theory and pathfinding algorithms.

The idea is simple: model a city as a graph where intersections are nodes and streets are edges, then find the fastest routes between restaurants and customers. I'm using Shortest Path First (SPF) algorithms to compute optimal delivery paths based on travel time.

## Project Goals

- Build a graph representation of a city street network
- Implement pathfinding algorithms (like Dijkstra's) to find optimal routes
- Minimize delivery times by calculating the fastest paths
- Create a foundation that could scale to real-world delivery optimization

## The Dataset

I'm using a simulated city map to test the routing algorithms. It's fake, but it mimics the complexity of real urban street networks with multiple intersections and varying travel times.

### Data Format

The city data lives in text files where each line represents a street:

```
NODE1|NODE2|COST
```

- **NODE1** and **NODE2** are intersections or landmarks
- **COST** is the travel time between them

Each edge is bidirectional, so you can travel both ways on any street.

### Example

```
MainSt_1st|MainSt_2nd|3
MainSt_2nd|Oak_2nd|5
Oak_2nd|Oak_3rd|2
```

This would represent three street segments with travel times of 3, 5, and 2 minutes respectively.

## How It Works

1. **Parse the data** - Read in the city map and build a graph structure
2. **Build the graph** - Create adjacency lists with weighted edges
3. **Run SPF algorithm** - Given a start (restaurant) and end (customer), find the shortest path
4. **Output the route** - Return the optimal path and total delivery time

## Why This Matters

In the real world, shaving even a few minutes off each delivery adds up. For a service doing hundreds of deliveries a day, efficient routing can mean:

- Happier customers (nobody likes cold food)
- Lower fuel costs
- More deliveries per driver
- Better driver satisfaction

This project is a simplified version of what companies like DoorDash and Uber Eats deal with, minus the real-time traffic updates and multiple simultaneous deliveries.

## Future Improvements

Some things I'd like to add:

- Real-time traffic weighting
- Multiple delivery optimization (traveling salesman style)
- Visual map output
- API integration for real city data

## Running the Code

Check the starter code in the repository. The main algorithm takes a start node and end node and returns the optimal path with total cost.

---

*This project was built to explore graph algorithms and their practical applications in logistics optimization.*
