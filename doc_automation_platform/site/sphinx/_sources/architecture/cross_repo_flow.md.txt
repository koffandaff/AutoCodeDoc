# Cross-Repository Data Flow

> **Auto-generated** pipeline visualization showing how the three neural-lam
> ecosystem repositories interact.
> Last updated: 2026-03-11 17:21:58

## The Three-Repo Pipeline

The neural-lam ecosystem consists of three interconnected repositories that form
a complete weather prediction pipeline:

| Repository | Purpose | Output |
|------------|---------|--------|
| [mllam-data-prep](https://github.com/mllam/mllam-data-prep) | Data preprocessing | `.zarr` datasets |
| [weather-model-graphs](https://github.com/mllam/weather-model-graphs) | Graph topology | `.pt` graph files |
| [neural-lam](https://github.com/mllam/neural-lam) | Model training & eval | Trained weights |

## Data Flow Diagram

```{mermaid}
graph LR
    subgraph mllam_data_prep ["📦 mllam-data-prep"]
        MDP_CONFIG["config.yaml\n(data sources, variables)"]
        MDP_PROCESS["Data Processing\n(xarray/dask)"]
        MDP_OUTPUT[".zarr Dataset\n(standardized weather data)"]
        MDP_CONFIG --> MDP_PROCESS --> MDP_OUTPUT
    end

    subgraph weather_model_graphs ["🌐 weather-model-graphs"]
        WMG_CONFIG["graph_config.yaml\n(mesh topology)"]
        WMG_BUILD["Graph Builder\n(networkx)"]
        WMG_OUTPUT[".pt Graph Files\n(mesh, g2m, m2g edges)"]
        WMG_CONFIG --> WMG_BUILD --> WMG_OUTPUT
    end

    subgraph neural_lam ["🧠 neural-lam"]
        NL_DATASTORE["MDPDatastore\n(reads .zarr)"]
        NL_GRAPH["Graph Loading\n(reads .pt files)"]
        NL_MODEL["GNN Model\n(Hi-LAM / GraphLAM)"]
        NL_TRAIN["Training Loop\n(PyTorch Lightning)"]
        NL_EVAL["Evaluation\n(RMSE, MAE, ACC)"]

        NL_DATASTORE --> NL_MODEL
        NL_GRAPH --> NL_MODEL
        NL_MODEL --> NL_TRAIN
        NL_TRAIN --> NL_EVAL
    end

    MDP_OUTPUT -->|".zarr via\nMDPDatastore"| NL_DATASTORE
    WMG_OUTPUT -->|".pt graph\nfiles"| NL_GRAPH

    style mllam_data_prep fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    style weather_model_graphs fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style neural_lam fill:#fff3e0,stroke:#ef6c00,stroke-width:2px
    style MDP_OUTPUT fill:#bbdefb,stroke:#1565c0
    style WMG_OUTPUT fill:#c8e6c9,stroke:#2e7d32
    style NL_MODEL fill:#ffe0b2,stroke:#ef6c00
    style NL_EVAL fill:#ffccbc,stroke:#bf360c
```

## Pipeline Details

### 1. mllam-data-prep → `.zarr` Datasets

The `mllam-data-prep` repository processes raw weather data (e.g., ERA5, DANRA)
into standardized `.zarr` datasets. It:

- Reads configuration from `config.yaml` defining data sources and variables
- Uses `xarray` and `dask` for parallel data processing
- Outputs `.zarr` stores with consistent coordinate systems and variable naming

### 2. weather-model-graphs → `.pt` Graph Files

The `weather-model-graphs` repository generates the graph structures used by
the neural-lam GNN models:

- **Mesh graphs**: Define the internal model resolution hierarchy
- **Grid-to-Mesh (g2m)**: Map input grid points to mesh nodes
- **Mesh-to-Grid (m2g)**: Map mesh predictions back to output grid

### 3. neural-lam — Core Training Engine

The `neural-lam` repository is the core training engine that:

- Loads `.zarr` data via `MDPDatastore` (from mllam-data-prep output)
- Loads `.pt` graph files (from weather-model-graphs output)
- Trains Graph Neural Network models (Hi-LAM, GraphLAM)
- Evaluates predictions using RMSE, MAE, and ACC metrics

## Integration Points

```{mermaid}
graph TD
    A["mllam-data-prep\nconfig.yaml"] -->|"creates"| B[".zarr store"]
    C["weather-model-graphs\ngraph_config.yaml"] -->|"creates"| D[".pt files"]
    B -->|"imported via"| E["neural_lam.weather_dataset\nMDPDatastore"]
    D -->|"loaded in"| F["neural_lam.models\ngraph loading"]
    E --> G["Training Pipeline"]
    F --> G
    G --> H["Evaluation Metrics"]
    H --> I["Trained Model Weights"]

    style A fill:#e3f2fd
    style C fill:#e8f5e9
    style G fill:#fff3e0
    style I fill:#ffccbc
```

## See Also

- [System Architecture](system_diagram.md) — Internal module architecture
- [ER Diagram](er_diagram.md) — Data model relationships
