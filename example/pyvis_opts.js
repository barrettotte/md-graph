var options = {
  "nodes": {
    "font": {
      "size": 32,
      "align": "middle"
    },
    "scaling": {
      "min": 70,
      "max": 100
    },
    "color": {
      "border": "rgba(151,153,153,1)",
      "background": "rgba(240,241,252,1)",
      "highlight": {
        "border": "rgba(94,212,103,1)",
        "background": "rgba(94,212,103,1)"
      }
    },
    "size": 100
  },
  "edges": {
    "color": {
      "inherit": true
    },
    "smooth": false
  },
  "physics": {
    "forceAtlas2Based": {
      "gravitationalConstant": -450,
      "springLength": 100,
      "avoidOverlap": 1
    },
    "minVelocity": 0.75,
    "solver": "forceAtlas2Based",
    "timestep": 0.50
  }
}