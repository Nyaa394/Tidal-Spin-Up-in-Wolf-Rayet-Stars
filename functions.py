# find separation a
# timescale in years, functions turns it to s, a is in m, m1 and m2 in kg
def max_separation(timescale, m1, m2):
    G = 6.674e-11  # N*m^2/Kg^2
    c = 299792458.0  # m/s
    return ((256/5)*(timescale*365.25*24*3600)*(G**3)*(m1*m2*(m1+m2))/(c**5))**(1/4)

# find orbital period


def orbital_period(a, m1, m2):
    import numpy as np
    G = 6.674e-11  # N*m^2/Kg^2
    return 2*np.pi*((a**3)/(G*(m1+m2)))**(1/2)

# find mass from radius


def mass_from_radius(R):
    return (R/0.2276)**(1/0.57)  # R in solar radii, m in solar masses

# find radius from mass


def radius_from_mass(m):
    return 0.2276*(m**0.57)  # R in solar radii, m in solar masses

# find minimum separation for stars to be detached


def min_separation(q, R):
    from numpy import log
    # in solar radii (both R and a_min)
    return (((0.49*q**(2/3))/((0.6*q**(2/3))+log(1+q**(1/3))))**(-1))*R

# gravitational wave frequency (twice the orbital frequency) (forb is half of this)


def gw_frequency(a, m1, m2):
    import numpy as np
    G = 6.674e-11  # N*m^2/Kg^2
    return (1/np.pi)*((G*(m1+m2))/(a**3))**(1/2)  # in Hz

# separation from gravitational wave frequency


def separation_from_gw_frequency(f, m1, m2):
    import numpy as np
    G = 6.674e-11  # N*m^2/Kg^2
    return ((G*(m1+m2))/(np.pi**2*f**2))**(1/3)  # in m

# tidal friction timescale + integrable version for quad


def tidal_friction_timescale(m1, m2, Q, k, a, R, f):
    Rsolar = 6.957e8  # in m
    import numpy as np
    return (1/6)*(m1/m2)*(Q/k)*((a/(R*Rsolar))**5)*(np.pi*f)**(-1)


def tidal_friction_timescale_integrable(x, m1, m2, a, R, f):
    Rsolar = 6.957e8  # in m
    import numpy as np
    return (1/6)*(m1/m2)*(1/x)*((a/(R*Rsolar))**5)*(np.pi*f)**(-1)

# mean and median of a function f between x1 and x2


def mean(f, x1, x2, *args):
    from scipy.integrate import quad
    return (1/(x2-x1))*quad(f, x1, x2, args=args)[0]


def median(f, x1, x2, *args):
    from scipy.integrate import quad
    from scipy.optimize import root_scalar
    return root_scalar(lambda m: 0.5*quad(f, x1, x2, args=args)[0]-quad(f, x1, m, args=args)[0], bracket=[x1, x2]).root

# effective spin vs q=mWR/mBH, q<1, using spin parameters a2 of the initial BH (a1 on worksheet), and a1 of BH from WR star (a2 on worksheet)


def effective_spin(q, a1, a2):
    return (a2 + q*a1)/(1+q)

def pca(file_paths, target_col, feature_cols=None, n_components=2):

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
   
    if isinstance(file_paths, list):
        df = pd.concat([pd.read_csv(f) for f in file_paths], ignore_index=True)
    else:
        df = pd.read_csv(file_paths)

    # Select the data we actually want
    # If feature_cols isn't provided, default to all numeric columns minus target
    if feature_cols is None:
        features_df = df.select_dtypes(include=[np.number]).drop(columns=[target_col], errors='ignore')
        feature_cols = features_df.columns.tolist()
    else:
        features_df = df[feature_cols]

    # drop rows with NaNs
    clean_df = features_df.join(df[target_col]).dropna()
    features_final = clean_df[features_df.columns]
    target_final = clean_df[target_col].values

    # Scaling & PCA
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(features_final)
    
    pca = PCA(n_components=n_components)
    pca_results = pca.fit_transform(scaled_data) 

    # plots

    # Scree Plot (Explained Variance)
    # Shows the "elbow" to decide how many PCs are enough (how many get 90% is goal)

    plt.figure()
    components = np.arange(1, len(pca.explained_variance_ratio_) + 1)

    plt.bar(components, pca.explained_variance_ratio_)
    plt.xlabel("Principal Component")
    plt.ylabel("Explained Variance Ratio")
    plt.title("Scree Plot")
    plt.xticks(components)
    plt.grid(axis='y')
    plt.show()

    # PCA Contour Plot (PC1 vs PC2 vs Target)
    plt.figure()
    scatter = plt.scatter(
        pca_results[:, 0],
        pca_results[:, 1],
        c=target_final,
        cmap='plasma'
    )

    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.title(f"PCA Scatter (Target: {target_col})")
    plt.colorbar(scatter, label=target_col)
    plt.grid(True)
    plt.show()

    # Loadings Plot
    # Shows which original variables "pull" the data in certain directions
    loadings = pca.components_.T
    plt.figure()

    # Draw axes crossing at origin
    plt.axhline(0)
    plt.axvline(0)

    plt.scatter(loadings[:, 0], loadings[:, 1])

    # Label each feature
    for i, feature in enumerate(feature_cols):
        plt.text(loadings[i, 0], loadings[i, 1], feature)

    plt.xlabel("PC1 Loadings")
    plt.ylabel("PC2 Loadings")
    plt.title("Feature Loadings Plot")
    plt.grid(True)
    plt.show()

    # Print loadings numerically too
    print("\n--- Feature Loadings Key ---")
    for i, feature in enumerate(feature_cols):
        print(f"{feature}: PC1={loadings[i, 0]:.3f}, PC2={loadings[i, 1]:.3f}")
